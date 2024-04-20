import torch
from torch.utils.data import DataLoader
from torcheval.metrics.functional import r2_score, mean_squared_error
from pytorch_lightning.callbacks import EarlyStopping
from sklearn.metrics import r2_score 
import pytorch_lightning as pl
import wandb
import math
from time import time
import src.coolML.models as models


class mlp_cool_pp:

    def __init__(self, config = None, num_epochs = 1500, num_workers = 10, verbosity=False, wandb_project = None, min_delta = 5e-4, patience = 100):
        self.config = config
        self.num_epochs = num_epochs
        self.verbosity = verbosity
        self.num_workers = num_workers
        self.wandb_project = wandb_project
        self.min_delta = min_delta 
        self.patience = patience

    def train(self, X_train, X_val, Y_train, Y_val):
        '''Train and test process to calibrate the neural network and predict the I-V curves
        -----------
        Input:
        ------
        X_train: torch.tensor
            Input train subsets
        X_val: torch.tensor
            Input validation subsets
        X_test: torch.tensor
            Input test subsets   
        config: dictionary
            Contains the key:value pairs for the neural network hyperparameters
        num_epochs: int
            Number of epochs, 1500 by default as it is implemented the early stopping method
        
        Output:
        -------
        - model: pytorch lightning object
            Calibrated neural network model'''
        if self.config is None:
            # Neural Network 1 hyperparameters
            self.config = {
                "input_layer": len(X_train[0]),
                "layer_1": int(len(X_train[0])*2.35),
                "layer_2": int(len(X_train[0])*1.9),
                "lr": 1e-1,
                "momentum": 0.9,
                "batch_size": 64,
                "output": len(Y_train[0]),
            }
        if self.wandb_project:
            wandb.init(project=self.wandb_project, config = self.config)
        train_dataset = models.CustomDataset(data_in = X_train, data_out = Y_train)
        train_loader = DataLoader(dataset = train_dataset, batch_size = self.config["batch_size"], num_workers = self.num_workers)
        val_dataset = models.CustomDataset(data_in = X_val, data_out = Y_val)
        val_loader = DataLoader(dataset=val_dataset, batch_size = self.config["batch_size"], num_workers = self.num_workers)
        if self.verbosity == True:
            print("Dimension train dataset:", len(train_dataset))
            print("Dimension validation dataset:", len(val_dataset))
        early_stopping = EarlyStopping('val/loss',mode='min', min_delta = self.min_delta, patience = self.patience)
        start_time = time()
        self.model = models.mlp_cool_pp_model(self.config) # Automates loops, hardware calls, model.train, model.eval and zero grad
        trainer = pl.Trainer(accelerator="cpu",max_epochs=self.num_epochs, log_every_n_steps = math.floor(len(X_train)/self.config["batch_size"]), callbacks=[early_stopping]) # Init Lightning trainer callbacks=[early_stopping]
        trainer.fit(self.model, train_loader, val_loader)
        if wandb.run is not None:
            wandb.finish()
        elapsed_time = round(time() - start_time,2)
        if self.verbosity == True:
            print('Trainer time:', elapsed_time)
            print(self.config)

    def test(self, X_test, Y_test, scaler_pp_ppo, pca_diff_pp_ppo):
        with torch.no_grad():
            y_hat1 = self.model(X_test)
        pred_test = pca_diff_pp_ppo.inverse_transform(y_hat1)
        pred_test = scaler_pp_ppo.inverse_transform(pred_test)
        sim = Y_test
        sim = pca_diff_pp_ppo.inverse_transform(sim)
        sim = scaler_pp_ppo.inverse_transform(sim)
        r2_test = r2_score(sim, pred_test)
        if self.verbosity == True:
            print('The R2 for the test subset is:', r2_score)
        return pred_test, sim, r2_test


class mlp_cool_thermal:

    def __init__(self, config = None, num_epochs = 1500, num_workers = 10, verbosity=False, wandb_project = None, min_delta = 5e-4, patience = 100):
        self.config = config
        self.num_epochs = num_epochs
        self.verbosity = verbosity
        self.num_workers = num_workers
        self.wandb_project = wandb_project
        self.min_delta = min_delta 
        self.patience = patience

    def train(self, X_train, X_val, Y_train, Y_val):
        '''Train and test process to calibrate the neural network and predict the I-V curves
        -----------
        Input:
        ------
        X_train: torch.tensor
            Input train subsets
        X_val: torch.tensor
            Input validation subsets
        X_test: torch.tensor
            Input test subsets   
        config: dictionary
            Contains the key:value pairs for the neural network hyperparameters
        num_epochs: int
            Number of epochs, 1500 by default as it is implemented the early stopping method
        
        Output:
        -------
        - model: pytorch lightning object
            Calibrated neural network model'''
        if self.config is None:
            self.config = {
                "input_layer": len(X_train[0]),
                "layer_1": int(len(X_train[0])/1.2),
                "layer_2": int(len(X_train[0])/1.2),
                "output":int(len(Y_train[0])),
                "lr": 1e-1,
                "momentum": 0.9,
                "batch_size": 64
            }
        if self.wandb_project:
            wandb.init(project=self.wandb_project, config = self.config)
        train_dataset = models.CustomDataset(data_in = X_train, data_out = Y_train)
        train_loader = DataLoader(dataset = train_dataset, batch_size = self.config["batch_size"], num_workers = self.num_workers)
        val_dataset = models.CustomDataset(data_in = X_val, data_out = Y_val)
        val_loader = DataLoader(dataset=val_dataset, batch_size = self.config["batch_size"], num_workers = self.num_workers)
        if self.verbosity == True:
            print("Dimension train dataset:", len(train_dataset))
            print("Dimension validation dataset:", len(val_dataset))
        early_stopping = EarlyStopping('val/loss',mode='min', min_delta = self.min_delta, patience = self.patience)
        start_time = time()
        self.model = models.mlp_cool_thermal_model(self.config) # Automates loops, hardware calls, model.train, model.eval and zero grad
        trainer = pl.Trainer(accelerator="cpu",max_epochs=self.num_epochs, log_every_n_steps = math.floor(len(X_train)/self.config["batch_size"]), callbacks=[early_stopping]) # Init Lightning trainer callbacks=[early_stopping]
        trainer.fit(self.model, train_loader, val_loader)
        if wandb.run is not None:
            wandb.finish()
        elapsed_time = round(time() - start_time,2)
        if self.verbosity == True:
            print('Trainer time:', elapsed_time)
            print(self.config)

    def test(self, X_test, Y_test, scaler_thermal):
        with torch.no_grad():
            y_hat = self.model(X_test)
        pred = scaler_thermal.inverse_transform(y_hat)
        sim = scaler_thermal.inverse_transform(Y_test)
        r2_CP = r2_score(sim[:,0], pred[:,0])
        r2_Te = r2_score(sim[:,1], pred[:,1])
        r2_W1 = r2_score(sim[:,2], pred[:,2])
        # loss_CP = mean_squared_error(sim[:,0], pred[:,0])**0.5
        # loss_Te = mean_squared_error(sim[:,1], pred[:,1])**0.5
        # loss_W1 = mean_squared_error(sim[:,2], pred[:,2])**0.5
        r2_test = r2_score(sim, pred)
        if self.verbosity == True:
            print('The R2 for the CP:', r2_CP)
            print('The R2 for the Te:', r2_Te)
            print('The R2 for the W1:', r2_W1)
            print('The R2 for the entire set:', r2_test)
        return pred, sim
