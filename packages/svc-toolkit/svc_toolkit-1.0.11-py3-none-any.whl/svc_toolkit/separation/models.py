import torch
import torch.nn as nn
import pytorch_lightning as pl
from torchmetrics.aggregation import MeanMetric

def _down_layer(
    in_channels: int,
    out_channels: int,
    kernel_size: int = 5,
    stride: int = 2,
    padding: int = 2
) -> nn.Sequential:
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding),
        nn.BatchNorm2d(out_channels),
        nn.LeakyReLU(0.2, inplace=True),
    )

def _up_layer(
    in_channels: int,
    out_channels: int,
    kernel_size: int = 5,
    stride: int = 2,
    padding: int = 1,
    dropout: bool = False,
    last: bool = False
) -> nn.Sequential:
    layers = nn.Sequential(
        nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride, padding),
        nn.BatchNorm2d(out_channels),
    )

    if dropout:
        layers.append(nn.Dropout(0.5))

    layers.append(nn.Sigmoid() if last else nn.ReLU(inplace=True))

    return layers

class UNet(nn.Module):
    def __init__(self, channels: int = 1) -> None:
        super(UNet, self).__init__()

        self.down1 = _down_layer(channels, 16)

        self.down2 = _down_layer(16, 32)

        self.down3 = _down_layer(32, 64)

        self.down4 = _down_layer(64, 128)

        self.down5 = _down_layer(128, 256)

        self.down6 = _down_layer(256, 512)

        self.up1 = _up_layer(512, 256, dropout=True)

        self.up2 = _up_layer(512, 128, dropout=True)

        self.up3 = _up_layer(256, 64, dropout=True)

        self.up4 = _up_layer(128, 32)

        self.up5 = _up_layer(64, 16)

        self.up6 = _up_layer(32, channels, last=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x_down1 = self.down1(x)

        x_down2 = self.down2(x_down1)

        x_down3 = self.down3(x_down2)

        x_down4 = self.down4(x_down3)

        x_down5 = self.down5(x_down4)

        x_down6 = self.down6(x_down5)

        x_up1 = self.up1(x_down6)
        x_up1 = x_up1[:, :, : -1, : -1]

        x_up2 = torch.cat((x_up1, x_down5), 1)
        x_up2 = self.up2(x_up2)
        x_up2 = x_up2[:, :, : -1, : -1]

        x_up3 = torch.cat((x_up2, x_down4), 1)
        x_up3 = self.up3(x_up3)
        x_up3 = x_up3[:, :, : -1, : -1]

        x_up4 = torch.cat((x_up3, x_down3), 1)
        x_up4 = self.up4(x_up4)
        x_up4 = x_up4[:, :, : -1, : -1]

        x_up5 = torch.cat((x_up4, x_down2), 1)
        x_up5 = self.up5(x_up5)
        x_up5 = x_up5[:, :, : -1, : -1]

        x_up6 = torch.cat((x_up5, x_down1), 1)
        x_up6 = self.up6(x_up6)
        x_up6 = x_up6[:, :, : -1, : -1]

        return x_up6

class DeeperUNet(nn.Module):
    def __init__(self, channels: int = 1) -> None:
        super(DeeperUNet, self).__init__()

        self.down1 = _down_layer(channels, 16)

        self.down2 = _down_layer(16, 32)

        self.down3 = _down_layer(32, 64)

        self.down4 = _down_layer(64, 128)

        self.down5 = _down_layer(128, 256)

        self.down6 = _down_layer(256, 512)

        self.down7 = _down_layer(512, 1024)

        self.down8 = _down_layer(1024, 2048)

        self.up1 = _up_layer(2048, 1024, dropout=True)

        self.up2 = _up_layer(2048, 512, dropout=True)

        self.up3 = _up_layer(1024, 256, dropout=True)

        self.up4 = _up_layer(512, 128, dropout=True)

        self.up5 = _up_layer(256, 64)

        self.up6 = _up_layer(128, 32)

        self.up7 = _up_layer(64, 16)

        self.up8 = _up_layer(32, channels, last=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x_down1 = self.down1(x)

        x_down2 = self.down2(x_down1)

        x_down3 = self.down3(x_down2)

        x_down4 = self.down4(x_down3)

        x_down5 = self.down5(x_down4)

        x_down6 = self.down6(x_down5)

        x_down7 = self.down7(x_down6)

        x_down8 = self.down8(x_down7)

        x_up1 = self.up1(x_down8)
        x_up1 = x_up1[:, :, : -1, : -1]

        x_up2 = torch.cat((x_up1, x_down7), 1)
        x_up2 = self.up2(x_up2)
        x_up2 = x_up2[:, :, : -1, : -1]

        x_up3 = torch.cat((x_up2, x_down6), 1)
        x_up3 = self.up3(x_up3)
        x_up3 = x_up3[:, :, : -1, : -1]

        x_up4 = torch.cat((x_up3, x_down5), 1)
        x_up4 = self.up4(x_up4)
        x_up4 = x_up4[:, :, : -1, : -1]

        x_up5 = torch.cat((x_up4, x_down4), 1)
        x_up5 = self.up5(x_up5)
        x_up5 = x_up5[:, :, : -1, : -1]

        x_up6 = torch.cat((x_up5, x_down3), 1)
        x_up6 = self.up6(x_up6)
        x_up6 = x_up6[:, :, : -1, : -1]

        x_up7 = torch.cat((x_up6, x_down2), 1)
        x_up7 = self.up7(x_up7)
        x_up7 = x_up7[:, :, : -1, : -1]

        x_up8 = torch.cat((x_up7, x_down1), 1)
        x_up8 = self.up8(x_up8)
        x_up8 = x_up8[:, :, : -1, : -1]

        return x_up8

class UNetLightning(pl.LightningModule):
    def __init__(
        self,
        in_channels: int = 1,
        lr: float = 0.0001,
        weight_decay: float = 0.00001,
        deeper: bool = False,
        optimizer: str = 'adam'
    ) -> None:
        super(UNetLightning, self).__init__()
        self.save_hyperparameters()

        self.lr = lr
        self.weight_decay = weight_decay
        self.optimizer = optimizer

        self.model = DeeperUNet(in_channels) if deeper else UNet(in_channels)
        self.loss = nn.L1Loss()
        self.train_loss = MeanMetric()
        self.val_loss = MeanMetric()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.model(x)

    def configure_optimizers(self) -> torch.optim.Optimizer:
        if self.optimizer == 'adam':
            return torch.optim.Adam(self.parameters(), lr=self.lr, weight_decay=self.weight_decay)
        elif self.optimizer == 'adamw':
            return torch.optim.AdamW(self.parameters(), lr=self.lr, weight_decay=self.weight_decay)
        else:
            raise ValueError(f'Invalid optimizer: {self.optimizer}')

    def get_loss(self, batch: tuple[torch.Tensor, torch.Tensor]) -> torch.Tensor:
        x, y = batch
        y_hat = self.forward(x) * x
        return self.loss(y_hat, y)

    def training_step(self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int) -> torch.Tensor:
        loss = self.get_loss(batch)
        self.train_loss.update(loss)
        return loss

    def on_train_epoch_end(self) -> None:
        train_loss = self.train_loss.compute()
        self.train_loss.reset()
        self.log('train_loss', train_loss)

    def validation_step(self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int) -> torch.Tensor:
        loss = self.get_loss(batch)
        self.val_loss.update(loss)
        return loss
    
    def on_validation_epoch_end(self) -> None:
        val_loss = self.val_loss.compute()
        self.val_loss.reset()
        self.log('val_loss', val_loss)

    def predict_step(self, batch, batch_idx: int, dataloader_idx: int = None) -> torch.Tensor:
        return self.forward(batch)