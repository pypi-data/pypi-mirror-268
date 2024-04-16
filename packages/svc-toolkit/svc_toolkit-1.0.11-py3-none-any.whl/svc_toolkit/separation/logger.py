import os

import pandas as pd
import matplotlib.pyplot as plt
from lightning_fabric.utilities.logger import _convert_params
from pytorch_lightning.loggers.logger import Logger
from pytorch_lightning.loggers.csv_logs import ExperimentWriter
from pytorch_lightning.utilities import rank_zero_only

from svc_toolkit.separation.constants import LoggerDFColumns

class MyLogger(Logger):
    def __init__(self, save_dir: str, old_dir: str = '') -> None:
        super().__init__()
        if old_dir != '':
            self.df = pd.read_csv(os.path.join(old_dir, 'loss.csv'))
        else:
            self.df = pd.DataFrame(columns=LoggerDFColumns.all())
        self.dir = save_dir
        self.experiment = ExperimentWriter(save_dir)

    @property
    def name(self) -> str:
        return "MyLogger"

    @property
    def version(self) -> str:
        return "0.1"

    @rank_zero_only
    def log_hyperparams(self, params: dict) -> None:
        self.experiment.log_hparams(_convert_params(params))
        self.experiment.save()

    @rank_zero_only
    def log_metrics(self, metrics: dict, step: int) -> None:

        epoch = metrics[LoggerDFColumns.EPOCH]
        if epoch not in self.df[LoggerDFColumns.EPOCH].values:
            self.df.loc[len(self.df)] = [epoch, None, None]

        loss_name = LoggerDFColumns.TRAIN_LOSS if LoggerDFColumns.TRAIN_LOSS in metrics else LoggerDFColumns.VAL_LOSS
        loss = metrics[loss_name]
        
        self.df.loc[self.df[LoggerDFColumns.EPOCH] == epoch, loss_name] = loss

    @rank_zero_only
    def save(self) -> None:
        csv_path = os.path.join(self.dir, 'loss.csv')
        self.df.to_csv(csv_path, index=False)

        graph_path = os.path.join(self.dir, 'loss.png')
        plt.figure(figsize=(10, 5))
        plt.plot(self.df[LoggerDFColumns.EPOCH], self.df[LoggerDFColumns.TRAIN_LOSS], label='train loss')
        plt.plot(self.df[LoggerDFColumns.EPOCH], self.df[LoggerDFColumns.VAL_LOSS], label='validation loss')
        plt.axhline(y=self.df[LoggerDFColumns.VAL_LOSS].min(), color='grey', linestyle='--', label='lowest validation loss')
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.title('Loss')
        plt.legend()
        plt.savefig(graph_path)
        plt.close()
