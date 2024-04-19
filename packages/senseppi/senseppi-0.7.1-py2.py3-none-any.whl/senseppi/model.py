import argparse
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
import pytorch_lightning as pl
import torch.utils.data as data
from torch.utils.data import Subset
from torchmetrics import AUROC, Accuracy, Precision, Recall, F1Score, MatthewsCorrCoef, AveragePrecision
from torchmetrics.collections import MetricCollection
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
import torch.optim as optim
import numpy as np


class DynamicGRU(pl.LightningModule):
    """
    Dynamic GRU module, which can handle variable length input sequence.

    Parameters
    ----------
    input_size : input size
    hidden_size : hidden size
    num_layers : number of hidden layers. Default: 1
    dropout : dropout rate. Default: 0
    bidirectional : If True, becomes a bidirectional RNN. Default: False.

    Inputs
    ------
    input: tensor, shaped [batch, max_step, input_size]
    seq_lens: tensor, shaped [batch], sequence lengths of batch

    Outputs
    -------
    output: tensor, shaped [batch, max_step, num_directions * hidden_size],
         tensor containing the output features (h_t) from the last layer
         of the GRU, for each t.
    """

    def __init__(self, input_size, hidden_size=100,
                 num_layers=1, dropout=0., bidirectional=False, return_sequences=False):
        super(DynamicGRU, self).__init__()

        self.lstm = torch.nn.GRU(
            input_size, hidden_size, num_layers, bias=True,
            batch_first=True, dropout=dropout, bidirectional=bidirectional)

        self.return_sequences = return_sequences

    def forward(self, x, seq_lens):
        # sort input by descending length
        _, idx_sort = torch.sort(seq_lens, dim=0, descending=True)
        _, idx_unsort = torch.sort(idx_sort, dim=0)
        x_sort = torch.index_select(x, dim=0, index=idx_sort)
        seq_lens_sort = torch.index_select(seq_lens, dim=0, index=idx_sort).to('cpu')

        # pack input
        x_packed = pack_padded_sequence(
            x_sort, seq_lens_sort, batch_first=True)

        # pass through rnn
        y_packed, _ = self.lstm(x_packed)

        # unpack output
        y_sort, length = pad_packed_sequence(y_packed, batch_first=True)

        # unsort output to original order
        y = torch.index_select(y_sort, dim=0, index=idx_unsort)

        if self.return_sequences:
            return y

        y_new = torch.unsqueeze(y[0, seq_lens[0] - 1, :].squeeze(), 0)

        for i in range(1, len(seq_lens)):
            y_i = torch.unsqueeze(y[i, seq_lens[i] - 1].squeeze(), 0)
            y_new = torch.cat((y_new, y_i), dim=0)

        return y_new


class CosineWarmupScheduler(optim.lr_scheduler._LRScheduler):

    def __init__(self, optimizer, warmup, max_iters):
        self.warmup = warmup
        self.max_num_iters = max_iters
        super().__init__(optimizer)

    def get_lr(self):
        lr_factor = self.get_lr_factor(epoch=self.last_epoch)
        # print('Current lr: ', [base_lr * lr_factor for base_lr in self.base_lrs])
        return [base_lr * lr_factor for base_lr in self.base_lrs]

    def get_lr_factor(self, epoch):
        lr_factor = 0.5 * (1 + np.cos(np.pi * epoch / self.max_num_iters))
        if epoch <= self.warmup:
            lr_factor *= (epoch + 1) * 1.0 / self.warmup
        return lr_factor


class BaselineModel(pl.LightningModule):
    def __init__(self, params):
        super(BaselineModel, self).__init__()

        self.save_hyperparameters(params)

        # Transfer to hyperparameters
        self.train_set = None
        self.val_set = None
        self.test_set = None

        # Defining whether to sync the logs or not depending on the number of gpus
        if hasattr(self.hparams, 'devices') and int(self.hparams.devices) > 1:
            self.hparams.sync_dist = True
        else:
            self.hparams.sync_dist = False

        self.valid_metrics = MetricCollection([
            Accuracy(task="binary"),
            Precision(task="binary"),
            Recall(task="binary"),
            F1Score(task="binary"),
            MatthewsCorrCoef(task="binary", num_classes=2),
            AUROC(task="binary"),
            AveragePrecision(task="binary")
        ], prefix='val_')

        self.train_metrics = self.valid_metrics.clone(prefix="train_")
        self.test_metrics = self.valid_metrics.clone(prefix="test_")

    def _single_step(self, batch):
        preds = self.forward(batch)
        preds = preds.view(-1)
        loss = F.binary_cross_entropy(preds, batch["label"].to(torch.float32))
        return batch["label"], preds, loss

    def training_step(self, batch, batch_idx):
        trues, preds, loss = self._single_step(batch)
        self.train_metrics.update(preds, trues)
        return loss

    def test_step(self, batch, batch_idx):
        trues, preds, test_loss = self._single_step(batch)
        self.test_metrics.update(preds, trues)
        self.log("test_loss", test_loss, batch_size=self.hparams.batch_size, sync_dist=self.hparams.sync_dist)

    def validation_step(self, batch, batch_idx):
        trues, preds, val_loss = self._single_step(batch)
        self.valid_metrics.update(preds, trues)
        self.log("val_loss", val_loss, batch_size=self.hparams.batch_size, sync_dist=self.hparams.sync_dist)

    def training_epoch_end(self, outputs) -> None:
        result = self.train_metrics.compute()
        self.train_metrics.reset()
        self.log_dict(result, on_epoch=True, sync_dist=self.hparams.sync_dist)

    def test_epoch_end(self, outputs) -> None:
        result = self.test_metrics.compute()
        self.test_metrics.reset()
        self.log_dict(result, on_epoch=True, sync_dist=self.hparams.sync_dist)

    def validation_epoch_end(self, outputs) -> None:
        result = self.valid_metrics.compute()
        self.valid_metrics.reset()
        self.log_dict(result, on_epoch=True, sync_dist=self.hparams.sync_dist)

    def load_data(self, dataset, valid_size=0.1, indices=None):
        if indices is None:
            dataset_length = len(dataset)
            valid_length = int(valid_size * dataset_length)
            train_length = dataset_length - valid_length
            self.train_set, self.val_set = data.random_split(dataset, [train_length, valid_length])
            print('Data has been randomly divided into train/val sets with sizes {} and {}'.format(len(self.train_set),
                                                                                                   len(self.val_set)))
        else:
            train_indices, val_indices = indices
            self.train_set = Subset(dataset, train_indices)
            self.val_set = Subset(dataset, val_indices)
            print('Data has been divided into train/val sets with sizes {} and {} based on selected indices'.format(
                len(self.train_set), len(self.val_set)))

    def train_dataloader(self, train_set=None, num_workers=8):
        if train_set is not None:
            self.train_set = train_set
        return DataLoader(dataset=self.train_set,
                          batch_size=self.hparams.batch_size,
                          num_workers=num_workers,
                          shuffle=True)

    def test_dataloader(self, test_set=None, num_workers=8):
        if test_set is not None:
            self.test_set = test_set
        return DataLoader(dataset=self.test_set,
                          batch_size=self.hparams.batch_size,
                          num_workers=num_workers)

    def val_dataloader(self, val_set=None, num_workers=8):
        if val_set is not None:
            self.val_set = val_set
        return DataLoader(dataset=self.val_set,
                          batch_size=self.hparams.batch_size,
                          num_workers=num_workers)

    @staticmethod
    def add_model_specific_args(parent_parser):
        parser = parent_parser.add_argument_group("Args_model")
        parser.add_argument("--lr", type=float, default=1e-4, help="Learning rate for training. "
                                                                   "Cosine warmup will be applied.")
        parser.add_argument("--batch_size", type=int, default=32, help="Batch size for training/testing.")
        parser.add_argument("--encoder_features", type=int, default=2560,
                            # help="Number of features in the encoder "
                            #      "(Corresponds to the dimentionality of per-token embedding of ESM2 model.) "
                            #      "If not a 3B version of ESM2 is chosen, this parameter needs to be set accordingly."
                            help=argparse.SUPPRESS)
        return parent_parser


class SensePPIModel(BaselineModel):
    def __init__(self, params):
        super(SensePPIModel, self).__init__(params)

        self.encoder_features = self.hparams.encoder_features
        self.hidden_dim = 256

        self.lstm = DynamicGRU(self.encoder_features, hidden_size=128, num_layers=3, dropout=0.5, bidirectional=True)

        self.dense_head = torch.nn.Sequential(
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(self.hidden_dim, 32),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(32, 1),
            torch.nn.Sigmoid()
        )

    def forward(self, batch):
        x1 = batch["emb1"]
        x2 = batch["emb2"]

        len1 = batch["len1"]
        len2 = batch["len2"]

        x1 = self.lstm(x1, len1)
        x2 = self.lstm(x2, len2)

        return self.dense_head(x1 * x2)

    def configure_optimizers(self):
        optimizer = torch.optim.AdamW(self.parameters(), lr=self.hparams.lr)
        # optimizer = torch.optim.RAdam(self.parameters(), lr=self.hparams.lr)
        lr_dict = {
            "scheduler": CosineWarmupScheduler(optimizer=optimizer, warmup=5, max_iters=200),
            "name": 'CosineWarmupScheduler',
        }
        return [optimizer], [lr_dict]


if __name__ == '__main__':
    from utils import add_general_args
    from matplotlib import pyplot as plt
    import pandas as pd
    import seaborn as sns
    import os

    # from Bio import SeqIO
    # from copy import deepcopy
    # with open('../test.fasta', 'r') as f:
    #     records = list(SeqIO.parse(f, 'fasta'))
    #
    # reversed_records = []
    # for record in records:
    #     record_seq_reversed = record.seq[::-1]
    #     record_reversed = deepcopy(record)
    #     record_reversed.seq = record_seq_reversed
    #     record_reversed.id = record.id + '_reversed'
    #     record_reversed.description = ''
    #     reversed_records.append(record_reversed)
    # with open('../test_reversed.fasta', 'w') as f:
    #     SeqIO.write(records + reversed_records, f, 'fasta')
    # exit()
    def preprocess_emb(emb):
        tensor_emb = emb
        tensor_len = tensor_emb.size(0)
        if tensor_emb.shape[0] > params.max_len:
            tensor_emb = tensor_emb[:params.max_len]
            tensor_len = params.max_len
        if tensor_emb.shape[0] < params.max_len:
            tensor_emb = F.pad(tensor_emb, (0, 0, 0, params.max_len - tensor_emb.size(0)), "constant", 0)
        return tensor_emb, tensor_len


    parser = argparse.ArgumentParser()
    parser = add_general_args(parser)
    parser = SensePPIModel.add_model_specific_args(parser)
    params = parser.parse_args()

    model = SensePPIModel(params)

    checkpoint = torch.load('../pretrained_models/senseppi_reg&rev.ckpt', map_location=torch.device('cpu'))

    model.load_state_dict(checkpoint['state_dict'])

    l_gru = ['lstm.lstm.weight_ih_l0', 'lstm.lstm.weight_hh_l0', 'lstm.lstm.bias_ih_l0', 'lstm.lstm.bias_hh_l0',
             'lstm.lstm.weight_ih_l0_reverse', 'lstm.lstm.weight_hh_l0_reverse', 'lstm.lstm.bias_ih_l0_reverse',
             'lstm.lstm.bias_hh_l0_reverse']

    gru = model.lstm

    outputs = {}
    outputs_reversed = {}
    dir = '/Users/volzhenin/PycharmProjects/SENSE-PPI/esm2_embs_3B'
    for file in os.listdir(dir):
        tensor = torch.load(os.path.join(dir, file))['representations'][36]

        tensor_emb, tensor_len = preprocess_emb(tensor)
        if '_reversed' in file:
            # outputs_reversed.update({file: tensor_emb[:tensor_len].mean(dim=0)})
            outputs_reversed.update({file: gru(tensor_emb.unsqueeze(0), torch.tensor([tensor_len])).squeeze(0)})
        else:
            # outputs.update({file: tensor_emb[:tensor_len].mean(dim=0)})
            outputs.update({file: gru(tensor_emb.unsqueeze(0), torch.tensor([tensor_len])).squeeze(0)})

    #calculate t-SNE for each output
    from sklearn.manifold import TSNE
    from sklearn.decomposition import PCA
    from tqdm import tqdm
    tsne = TSNE(n_components=2, learning_rate='auto', perplexity=5)
    pca = PCA(n_components=2)

    outputs = dict(sorted(outputs.items()))
    outputs_reversed = dict(sorted(outputs_reversed.items()))

    tsne_all = tsne.fit_transform(torch.stack(list(outputs.values())+list(outputs_reversed.values())).detach().numpy())
    # tsne_all = pca.fit_transform(torch.cat([outout_tensor, outout_tensor_reversed]).detach().numpy())

    interactions = pd.read_csv('../protein.pairs_string.tsv', sep='\t', names=['seq1', 'seq2', 'label'])
    positive_pairs = []
    negative_pairs = []
    for i, row in interactions.iterrows():
        if row['label'] > 0.0:
            positive_pairs.append(outputs[row['seq1']+'.pt'] * outputs[row['seq2']+'.pt'])
        else:
            negative_pairs.append(outputs[row['seq1']+'.pt'] * outputs[row['seq2']+'.pt'])

    pairs_outputs = torch.stack(positive_pairs + negative_pairs)
    tsne_pairs = tsne.fit_transform(pairs_outputs.detach().numpy())

    plt.figure(figsize=(5, 5))
    sns.scatterplot(x=tsne_pairs[:len(positive_pairs), 0], y=tsne_pairs[:len(positive_pairs), 1], color='r', label='positive')
    sns.scatterplot(x=tsne_pairs[len(positive_pairs):, 0], y=tsne_pairs[len(positive_pairs):, 1], color='b', label='negative')

    plt.figure(figsize=(5, 5))
    #the first half of the points: c='r', the second half: c='b'
    sns.scatterplot(x=tsne_all[:len(outputs), 0], y=tsne_all[:len(outputs), 1], color='r', label='straight')
    sns.scatterplot(x=tsne_all[len(outputs):, 0], y=tsne_all[len(outputs):, 1], color='b', label='reversed')
    plt.legend()


    corr_matrix = pd.DataFrame(columns=list(outputs.keys()), index=list(outputs.keys()))
    for key1 in outputs.keys():
        for key2 in outputs.keys():
            corr_matrix.loc[key1, key2] = torch.nn.functional.pairwise_distance(outputs[key1], outputs[key2]).detach().numpy()
    corr_matrix_rev = pd.DataFrame(columns=list(outputs_reversed.keys()), index=list(outputs.keys()))
    for key in outputs.keys():
        for key_rev in outputs_reversed.keys():
            corr_matrix_rev.loc[key, key_rev] = torch.nn.functional.pairwise_distance(outputs[key], outputs_reversed[key_rev]).detach().numpy()

    corr_matrix_rev.index = [i[:-3] for i in corr_matrix_rev.index]
    corr_matrix_rev.columns = [i[:-10] for i in corr_matrix_rev.columns]

    corr_matrix = corr_matrix.sort_index()
    corr_matrix = corr_matrix[sorted(corr_matrix.columns)]

    corr_matrix_rev = corr_matrix_rev.sort_index()
    corr_matrix_rev = corr_matrix_rev[sorted(corr_matrix_rev.columns)]

    plt.figure(figsize=(10, 10))
    sns.heatmap(corr_matrix_rev.astype(float), cmap='coolwarm')

    plt.figure(figsize=(10, 10))
    sns.heatmap(corr_matrix.astype(float), cmap='coolwarm')
    # plt.show()


    # l_gru = [i.replace('l0', 'l2') for i in l_gru]

    #plot the weight distribution from l_gru[0]
    plt.figure()
    plt.plot(model.state_dict()[l_gru[0]].detach().numpy().mean(axis=1))
    plt.plot(model.state_dict()[l_gru[4]].detach().numpy().mean(axis=1))

    plt.figure()
    plt.plot(model.state_dict()[l_gru[1]].detach().numpy().mean(axis=1))
    plt.plot(model.state_dict()[l_gru[5]].detach().numpy().mean(axis=1))

    plt.figure()
    plt.plot(model.state_dict()[l_gru[2]].detach().numpy())
    plt.plot(model.state_dict()[l_gru[6]].detach().numpy())

    plt.figure()
    plt.plot(model.state_dict()[l_gru[3]].detach().numpy())
    plt.plot(model.state_dict()[l_gru[7]].detach().numpy())
    plt.show()