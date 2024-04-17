import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.utils.data import Dataset
from torcheval.metrics.functional import r2_score
import pytorch_lightning as pl
import wandb


class CustomDataset(Dataset):
    '''
    Dataset type class
    '''

    def __init__(self, data_in, data_out):
        self.data_in = data_in
        self.data_out = data_out

    def __len__(self):
        return len(self.data_in)

    def __getitem__(self, i):
        if torch.is_tensor(i):
            i = i.tolist()
        return self.data_in[i], self.data_out[i]


class mlp_cool_pp_model(pl.LightningModule): 
    # Definition of the neural network
    def __init__(self, config):
        super().__init__()
        self.input_layer = config["input_layer"]
        self.layer_1 = config["layer_1"]
        self.layer_2 = config["layer_2"]
        # self.layer_3 = config["layer_3"]
        self.lr = config["lr"]
        self.batch_size = config["batch_size"]
        self.momentum = config["momentum"]
        self.output =config["output"]
        # self.std = config["weight_std"]
        self.encoder = nn.Sequential(
            nn.Linear(self.input_layer, self.layer_1),
            nn.Tanh(),
            nn.Linear(self.layer_1, self.layer_2),
            nn.Tanh(),
            nn.Linear(self.layer_2, self.output)
        )
        self.save_hyperparameters()

        # self.apply(self.init_weights_normal)

    # Weights initialization
    def init_weights_normal(self, module):
        '''
        Initialization of the weights of neural network layers and nodes
        with a normal distribution with mean=0, with std as a hyperparameter
        '''
        if isinstance(module, nn.Linear):
            module.weight.data.normal_(mean=0.0, std=self.std)
            if module.bias is not None:
                module.bias.data.zero_()

    def init_weights_he(self, module):
        '''
        The current standard approach for initialization of the weights of neural
        network layers and nodes that use the rectified linear (ReLU) activation
        function is called “he” initialization.
        '''
        if isinstance(module, nn.Linear):
            torch.nn.init.kaiming_uniform_(module.weight)
            module.bias.data.fill_(0.0)

    # Prediction/inference actions
    def forward(self,x):
        y = self.encoder(x)
        return y
    
    # Optimization algorithm
    def configure_optimizers(self):
        # optimizer = torch.optim.Adam(self.parameters())
        optimizer = torch.optim.SGD(self.parameters(), momentum=self.momentum, lr=self.lr,nesterov=True)
        lr_scheduler = {
            'scheduler': torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min',factor=0.1),
            'name': 'learning_rate_scheduler',
            'monitor': 'val/loss'
        } 
        return [optimizer], [lr_scheduler]
    
    # Training loop with MSE as loss function, R2 metric to visualize
    def training_step(self, train_batch):
        x, y = train_batch
        x = x.view(x.size(0),-1)
        y = y.view(y.size(0),-1)
        y_hat = self.encoder(x)
        loss = F.mse_loss(y_hat, y)
        if len(y_hat)>2:
            r2 = r2_score(y_hat, y)
            if wandb.run is not None:
                wandb.log({"mlp1_r2_train": r2, "mlp1_loss_train": loss})
            self.log('train/r2', r2, on_step=True, on_epoch=True, logger=True)
        self.log('train/loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True) # sending metrics to TensorBoard, add on_epoch=True to calculate epoch-level metrics
        return loss
    
    # Validation with MSE as loss function, R2 metric to visualize
    def validation_step(self, val_batch, batch_idx):
        x, y = val_batch
        x = x.view(x.size(0),-1)
        y = y.view(y.size(0),-1)
        y_hat = self.encoder(x)
        loss = F.mse_loss(y_hat, y)
        if len(y_hat)>2:
            r2_val = r2_score(y_hat, y)
            if wandb.run is not None:
                wandb.log({"mlp1_r2_val": r2_val, "mlp1_loss_train": loss})
            self.log('val/r2', r2_val, on_step=True, on_epoch=True, logger=True)
        self.log('val/loss', loss, on_step=True, prog_bar=False,on_epoch=True, logger=True)

    # Test with MSE as loss function, R2 and RMSE metrics to visualize
    def test_step(self, test_batch, batch_idx):
        x, y = test_batch
        x = x.view(x.size(0),-1)
        y = y.view(y.size(0),-1)
        y_hat = self.encoder(x)
        print('Target:',y.shape)
        print('Prediction', y_hat.shape)
        loss = F.mse_loss(y_hat, y)
        if len(y_hat)>2:
            r2 = r2_score(y_hat, y)
            if wandb.run is not None:
                wandb.log({"mlp2_r2_test": r2, "mlp2_loss_test": loss})

class mlp_cool_thermal_model(pl.LightningModule): 
    '''
    Definition of the neural network model used to predict the thermal and energetic properties from the potential profile
    '''
    # Definition of the neural network structure
    def __init__(self, config):
        super().__init__()
        self.input_layer = config["input_layer"]
        self.layer_1 = config["layer_1"]
        self.layer_2 = config["layer_2"]
        self.lr = config["lr"]
        self.batch_size = config["batch_size"]
        self.momentum = config["momentum"]
        self.output =config["output"]
        self.encoder = nn.Sequential(
            nn.Linear(self.input_layer, self.layer_1),
            nn.Tanh(),
            nn.Linear(self.layer_1, self.layer_2),
            nn.Tanh(),
            nn.Linear(self.layer_2, self.output)
        )
        self.save_hyperparameters()
        # Initialization of weights with desired function as follows:
        # self.apply(self.init_weights_normal or self.init_weights_he)

    def init_weights_normal(self, module):
        '''
        Initialization of the weights of neural network layers and nodes
        with a normal distribution with mean=0, with std as a hyperparameter
        '''
        if isinstance(module, nn.Linear):
            module.weight.data.normal_(mean=0.0, std=self.std)
            if module.bias is not None:
                module.bias.data.zero_()

    def init_weights_he(self, module):
        '''
        The current standard approach for initialization of the weights of neural
        network layers and nodes that use the rectified linear (ReLU) activation
        function is called “he” initialization.
        '''
        if isinstance(module, nn.Linear):
            torch.nn.init.kaiming_uniform_(module.weight)
            module.bias.data.fill_(0.0)

    # Prediction/inference actions
    def forward(self,x):
        y = self.encoder(x)
        return y
    
    # Optimization algorithm and learning rate scheduler
    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.lr)
        lr_scheduler = {
            'scheduler': torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min',factor=0.1),
            'name': 'learning_rate_scheduler',
            'monitor': 'val/loss'
        } 
        return [optimizer] , [lr_scheduler]
    
    # Training neural network loop
    def training_step(self, train_batch, batch_idx):
        x, y = train_batch
        x = x.view(x.size(0),-1)
        x = x.view(x.size(0),-1)
        y = y.view(y.size(0),-1)
        y_hat = self.encoder(x)
        loss = F.mse_loss(y_hat, y)
        loss = F.mse_loss(y_hat, y)
        if len(y_hat)>2:
            r2 = r2_score(y_hat, y)
            wandb.log({"mlp2_r2_train": r2, "mlp2_loss_train": loss})
            self.log('train/r2', r2, on_step=True, on_epoch=True, logger=True )
        self.log('train/loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)  
        return loss
    
    # Validation neural network loop
    def validation_step(self, val_batch, batch_idx):
        x, y = val_batch
        x = x.view(x.size(0),-1)
        x = x.view(x.size(0),-1)
        y = y.view(y.size(0),-1)
        y_hat = self.encoder(x)
        loss = F.mse_loss(y_hat, y)
        loss = F.mse_loss(y_hat, y)
        if len(y_hat)>2:
            r2 = r2_score(y_hat, y)
            wandb.log({"mlp2_r2_validation": r2, "mlp2_loss_validation": loss})
            self.log('val/r2', r2, on_step=True, on_epoch=True, logger=True )
        self.log('val/loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)  