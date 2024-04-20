import pandas as pd 
import torch
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import  StandardScaler, MinMaxScaler
from pickle import dump

def import_cooling_data(path):
    '''
    Import cooling data from csv to pandas dataframes
    Input:
    -----
    - path: path
        path where the csv input data is stored
    Output:
    -------
    - data: pandas.DataFrame
        DataFrame with all information needed to process
    '''
    raw_data = pd.read_csv(path, delimiter=',',header=None)
    data = pd.DataFrame()
    data['Lb1'] = raw_data.iloc[:, 0]
    data['Lqw'] = raw_data.iloc[:, 1]
    data['Lb2'] = raw_data.iloc[:, 2]
    data['Alb2'] = raw_data.iloc[:, 3]
    data['V'] = raw_data.iloc[:, 4]
    data['CP'] = raw_data.iloc[:, 5]
    data['Te'] = raw_data.iloc[:, 6]
    data['W1'] = raw_data.iloc[:, 7]
    data['W2'] = raw_data.iloc[:, 8]
    # Merging the potential profile in one column as a string
    data['PP'] = raw_data[raw_data.columns[9:]].apply(
        lambda x: ','.join(x.dropna().astype(str)),
        axis=1
    )
    # Potential profile as a list of floats
    data["PP"] = data["PP"].str.split(",").map(
        lambda x: list(map(float, x))
        ).tolist()
    return data


def compute_ppo(data,max_len=None):
    '''
    Calculates PPo from design parameters and extend the profile to max_len.
    -------
    Inputs:
    - data: data to calculate the PPo
    - max_len: length to fit all the PPo to the desired length. By default to the maximun PPo length  
    -------
    Outputs:
    - data['PP']: pandas DF
        Potential profile recortado to the same points as the PPo
    - data['PPo']: pandas DF
        List of the calculated PPo
    - data['PP-PPo']: panda DF
        Curve PP-PPo to avoid discontinuities and ensure derivability 
    '''
    ppo_list = []
    diff_pp_ppo = []
    for i in range(len(data['Lqw'])):
        ppo = PPo_Structure(data['Lqw'][i], data['Lb2'][i], data['Alb2'][i])
        ppo_list.append(ppo.PPo())
    # Pad lists to uniform length
    if max_len == None:
        max_len = max(len(x) for x in ppo_list)
    data['PPo'] = [x + [0]*(max_len - len(x)) for x in ppo_list]
    data['PP'] = data['PP'].apply(lambda x: x[:1514]) #1110
    for i in range(len(data['PP'])):
        diff_list = [a-b for a, b in zip(data['PP'][i], data['PPo'][i])]
        diff_pp_ppo.append(diff_list)
    data['PP-PPo'] = diff_pp_ppo
    return data['PP-PPo'], data['PPo'], data['PP']


class PPo_Structure():
    '''
    Class to obtain the solution of the potential profile (PPo) from design parameter
    '''
    def __init__(self,LQW,LB2,ALB2):
        self.LQW = LQW
        self.LB2 = LB2
        self.ALB2 = ALB2

    def Eg_AlGaAs(self, AlPercent):
        Eg_GaAs = 1.424
        if AlPercent != 1:
            BandGap = Eg_GaAs + 0.8*AlPercent + 0.53*AlPercent
        else:
            BandGap = Eg_GaAs + 1*AlPercent + 0.53*AlPercent
        return BandGap

    def DEGAM(self,AL1, AL2):
        y = self.Eg_AlGaAs(AL2) + (-((-0.53*AL1)-(-0.53*AL2))) - self.Eg_AlGaAs(AL1)
        return y

    def PPo(self):
        L = [200, 1.2, self.LQW, self.LB2, 200]
        a = 0.4
        Al = [0, 1, 0, self.ALB2, 0]
        PPo = []
        avant = 0
        for nb in range(0,5):
            for i in range(avant+1,avant+round(L[nb]/a)+1):
                if nb == 0:
                    PPo.append(float(0))
                else:
                    PPo.append(
                        float(PPo[avant-2]+self.DEGAM(Al[nb-1],Al[nb]))
                    )
            avant = avant+round(L[nb]/a)
            if nb<4:
                PPo.append(
                    float(PPo[avant-1]+(self.DEGAM(Al[nb], Al[nb+1])/2))
                )
            avant = avant+1
        return PPo


def data_to_input_output_tensors(data):
    '''
    Separates data in the different input and output tensors for the two neural networks
    --------
    Inputs:
    - data: data to import in required format
    --------
    Outputs:
    - X1: input for the first (mlp_cool_pp) neural network
    - Y1: output for the first (mlp_cool_pp) neural network
    - X2: input for the second (mlp_cool_thermal) neural network
    - Y1: output for the second (mlp_cool_thermal) neural network
    '''
    v_list = data['V'].to_numpy()
    # Función para concatenar el valor correspondiente de 'V' a cada lista en la columna 'PPo'
    data['PPo+V'] = data.apply(lambda row: row['PPo'] + [v_list[row.name]], axis=1)
    # Convertir las listas concatenadas a arrays de NumPy y luego a tensores de PyTorch
    data['PPo+V'] = data['PPo+V'].apply(np.array)
    diff_ppo_v_tensor = torch.stack([torch.from_numpy(x) for x in data['PPo+V']])
    # Diff PP-PPo tensor
    data['PP-PPo'] = data['PP-PPo'].apply(np.array)
    diff_ppo_pp_tensor = torch.stack([torch.from_numpy(x) for x in data['PP-PPo']])
    # PP tensor
    pp_tensor= torch.tensor(np.array([np.array(lst) for lst in data['PP'].tolist()]), dtype=torch.float32)
    # Output properties
    output_properties =  torch.tensor(data[['CP','Te','W1']].to_numpy(), dtype=torch.float32)
    X1, X2, Y1, Y2 = diff_ppo_v_tensor, pp_tensor, diff_ppo_pp_tensor, output_properties
    return X1, X2, Y1, Y2

def split_data(X1, X2, Y1, Y2, test_split = 0.2, verbosity = False):
    '''Split data into train, validation and test subsets
    ---------
    Input:
    ------
    X: torch.tensor
        Scaled input tensor
    Y: torch.tensor
        Scaled output tensor
    test_split: float
        Percentage of subsets distribution, 20% test by default
    verbosity: boolean
        default=False, information about the final datasets
    Output:
    -------
    X_train, Y_train: torch.tensor
        Input, Output train subsets
    X_val, Y_val: torch.tensor
        Input, Output validation subsets
    X_test, Y_test: torch.tensor
        Input, Output test subsets
    '''
    ramdom_state = 10
    X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X1, Y1, test_size=test_split, random_state=ramdom_state)
    X_train1, X_val1, Y_train1, Y_val1 = train_test_split(X_train1,  Y_train1, test_size=test_split, random_state=ramdom_state)
    X_train2, X_test2, Y_train2, Y_test2 = train_test_split(X2, Y2, test_size=test_split, random_state=ramdom_state)
    X_train2,  X_val2, Y_train2,  Y_val2 = train_test_split(X_train2,  Y_train2, test_size=test_split, random_state=ramdom_state)
    if verbosity == True:      
        print("FIRST MLP:\tTrain size\n","\tInput:", X_train1.shape,"\tOutput:",Y_train1.shape)
        print("\tTest size\n","\tInput:", X_test1.shape,"\tOutput:",Y_test1.shape)
        print("\tValidation size\n","\tInput:", X_val1.shape,"\tOutput:",Y_val1.shape)
        print("SECOND MLP:\tTrain size\n","\tInput:", X_train2.shape,"\tOutput:",Y_train2.shape)
        print("\tTest size\n","\tInput:", X_test2.shape,"\tOutput:",Y_test2.shape)
        print("\tValidation size\n","\tInput:", X_val2.shape,"\tOutput:",Y_val2.shape)
    return X_train1, X_val1, X_test1, Y_train1, Y_val1, Y_test1, X_train2, X_val2, X_test2, Y_train2, Y_val2, Y_test2 

###################################################################################################################
####################################### SCALING SECTION ###########################################################
###################################################################################################################
def scale_mlp1_input(X_train, X_val, X_test):
    '''
    Fitting a scaler to the train subset and transforming the validation and test dataset
    --------
    Inputs:
    -------
    - X_train: torch.tensor
        tensor with the training subset
    - x_val: torch.tensor
        tensor with the validation subset
    - x_test: torch.tensor
        tensor with the test subset
    Outputs:
    -------
    - ppo_train_scaled: torch.tensor
        scaled training subset
    - ppo_val_scaled: torch.tensor
        scaled validation subset
    - ppo_test_scaled: torch.tensor
        scaled test subset
    - scaler_ppo: Scaler object
        fitted scaler object to train subset to apply the transformations
    '''
    # Train dataset
    ppo_train = [sublist[:-1].tolist() for sublist in X_train]
    ppo_train_scaled, scaler_ppo = norm_pp(ppo_train)
    bias_train = torch.tensor([sublist[-1] for sublist in X_train], dtype=torch.float32)
    # Validation dataset
    ppo_val = [sublist[:-1].tolist() for sublist in X_val]
    ppo_val_scaled = torch.tensor(scaler_ppo.transform(ppo_val),dtype = torch.float32)
    bias_val = torch.tensor([sublist[-1] for sublist in X_val], dtype=torch.float32)
    # Test dataset
    ppo_test = [sublist[:-1].tolist() for sublist in X_test]
    ppo_test_scaled = torch.tensor(scaler_ppo.transform(ppo_test),dtype = torch.float32)
    bias_test = torch.tensor([sublist[-1] for sublist in X_test], dtype=torch.float32)
    # Concatenate the PPo values with bias
    X_train_scaled = torch.cat((ppo_train_scaled, bias_train.unsqueeze(1)), dim=1)
    X_val_scaled = torch.cat((ppo_val_scaled, bias_val.unsqueeze(1)), dim=1)
    X_test_scaled = torch.cat((ppo_test_scaled, bias_test.unsqueeze(1)), dim=1)
    return X_train_scaled, X_val_scaled, X_test_scaled, scaler_ppo


def scale_mlp1_output(Y_train, Y_val, Y_test):
    '''
    Fitting a scaler to the train subset and transforming the validation and test dataset
    --------
    Inputs:
    -------
    - X_train: torch.tensor
        tensor with the training subset
    - x_val: torch.tensor
        tensor with the validation subset
    - x_test: torch.tensor
        tensor with the test subset
    Outputs:
    -------
    - Y_train_scaled: torch.tensor
        scaled training subset
    - Y_val_scaled: torch.tensor
        scaled validation subset
    - Y_test_scaled: torch.tensor
        scaled test subset
    - scaler_pp_ppo: Scaler object
        fitted scaler object to train subset to apply the transformations
    '''
    Y_train_scaled, scaler_pp_ppo = norm_diff_pp_ppo(Y_train)
    Y_val_scaled = torch.tensor(scaler_pp_ppo.transform(Y_val), dtype = torch.float32)
    Y_test_scaled = torch.tensor(scaler_pp_ppo.transform(Y_test), dtype = torch.float32)
    return Y_train_scaled, Y_val_scaled, Y_test_scaled, scaler_pp_ppo


def scale_mlp2_input(X_train, X_val, X_test):
    '''
    Fitting a scaler to the train subset and transforming the validation and test dataset
    --------
    Inputs:
    -------
    - X_train: torch.tensor
        tensor with the training subset
    - X_val: torch.tensor
        tensor with the validation subset
    - X_test: torch.tensor
        tensor with the test subset
    Outputs:
    -------
    - X_train_scaled: torch.tensor
        scaled training subset
    - X_val_scaled: torch.tensor
        scaled validation subset
    - X_test_scaled: torch.tensor
        scaled test subset
    - scaler_pp: Scaler object
        fitted scaler object to train subset to apply the transformations
    '''# SCALER TO PP
    X_train_scaled, scaler_pp = norm_pp(X_train)
    X_test_scaled = torch.tensor(scaler_pp.transform(X_test), dtype = torch.float32)
    X_val_scaled = torch.tensor(scaler_pp.transform(X_val), dtype = torch.float32)
    return X_train_scaled, X_val_scaled, X_test_scaled, scaler_pp


def scale_mlp2_output(Y_train, Y_val, Y_test,scaler=None):
    '''
    Fitting a scaler to the train subset and transforming the validation and test dataset
    --------
    Inputs:
    -------
    - Y_train: torch.tensor
        tensor with the training subset
    - Y_val: torch.tensor
        tensor with the validation subset
    - Y_test: torch.tensor
        tensor with the test subset
    Outputs:
    -------
    - Y_train_scaled: torch.tensor
        scaled training subset
    - Y_val_scaled: torch.tensor
        scaled validation subset
    - Y_test_scaled: torch.tensor
        scaled test subset
    - scaler_pp_ppo: Scaler object
        fitted scaler object to train subset to apply the transformations
    '''
    Y_train_scaled, scaler_thermal = norm_thermal(Y_train,scaler)
    Y_test_scaled = torch.tensor(scaler_thermal.transform(Y_test), dtype = torch.float32)
    Y_val_scaled = torch.tensor(scaler_thermal.transform(Y_val), dtype = torch.float32)
    return Y_train_scaled, Y_val_scaled, Y_test_scaled, scaler_thermal

##### SCALER AUXILIAR FUNCTIONS
def norm_ppo(data, scaler='MinMax'):
    '''
    Normalization of PP with desired Scaler
    -------
    Inputs:
    - data: dataframe with the different values
    -------
    Outputs:
    - list(ppo_scaled): pp list of lists
    - scaler_ppo: fitted object for the PPo normalization
    '''
    if scaler == 'MinMax':
        scaler_ppo = MinMaxScaler()
    else:
        scaler_ppo = StandardScaler()
    ppo_scaled = scaler_ppo.fit_transform(data)
    dump(scaler_ppo, open('scaler_ppo.pkl', 'wb'))
    return torch.tensor(ppo_scaled, dtype=torch.float32), scaler_ppo

def norm_pp(data, scaler='MinMax'):
    '''
    Normalization of PP with desired Scaler
    -------
    Inputs:
    - data: dataframe with the different values
    -------
    Outputs:
    - list(ppo_scaled): pp list of lists
    - scaler_ppo: fitted object for the PPo normalization
    '''
    if scaler == 'MinMax':
        scaler_pp = MinMaxScaler()
    else:
        scaler_pp = StandardScaler()
    pp_scaled = scaler_pp.fit_transform(data)
    dump(scaler_pp, open('scaler_objects/scaler_pp.pkl', 'wb'))
    return torch.tensor(pp_scaled, dtype=torch.float32), scaler_pp

def norm_diff_pp_ppo(data, scaler='MinMax'):
    '''
    Normalization of PP-ppo with MinMaxScaler
    -------
    Inputs:
    - data: dataframe with the different values
    - scaler: string
        - MinMax by default
        - If not MinMax the Standard Scaler is applied
    -------
    Outputs:
    - diff_pp_ppo_list_scaled: torch.tensor
        PP-PPo curves scaled
    - scaler_pp_ppo: Scaler object
        fitted object for the PP-PPo normalization
    '''
    if scaler == 'MinMax':
        scaler_pp_ppo = MinMaxScaler()
    else:
        scaler_pp_ppo = StandardScaler()
    diff_pp_ppo_list_scaled = scaler_pp_ppo.fit_transform(data)
    dump(scaler_pp_ppo, open('scaler_objects/scaler_pp_ppo.pkl', 'wb'))
    return torch.tensor(diff_pp_ppo_list_scaled, dtype=torch.float32), scaler_pp_ppo


def norm_thermal(data, scaler='MinMax'):
    '''
    Normalization of thermal properties CP, Te, W1 and W2 with MinMaxScaler
    -------
    Inputs:
    - data: dataframe with the different values
    -------
    Outputs:
    - temp_df['CP']: scaled cooling power
    - temp_df['Te']: scaled electron temperature
    - temp_df['W1']: scaled w2 between the emitter and the quantum well ground state
    - temp_df['W2']: scaled w2 between the quantum well ground state and the top of the second barrier
    - scaler_thermal: fitted object for the output normalization
    '''
    if scaler == 'MinMax':
        scaler_thermal = MinMaxScaler()
    else:
        scaler_thermal = StandardScaler()
    thermal = scaler_thermal.fit_transform(data)
    dump(scaler_thermal, open('scaler_objects/scaler_thermal.pkl', 'wb'))
    return torch.tensor(thermal, dtype=torch.float32), scaler_thermal

###################################################################################################################
########################################### PCA SECTION ###########################################################
###################################################################################################################
def pca_to_ppo(X_train, X_val, X_test, pc=0.9999, verbosity = False):
    '''
    Fits the PCA to the PPo of the train subset and transforming the validation and test dataset
    --------
    Inputs:
    -------
    - X_train: torch.tensor
        tensor with the training subset
    - X_val: torch.tensor
        tensor with the validation subset
    - X_test: torch.tensor
        tensor with the test subset
    Outputs:
    -------
    - X_train_pca: torch.tensor
        training subset after PCA
    - X_val_scaled: torch.tensor
        validation subset after PCA
    - X_test_scaled: torch.tensor
        test subset after PCA
    - pca_ppo: PCA object
        fitted PCA object to train subset to apply the transformations to the other subsets
    '''
    # 1. Fit the PCA to the train dataset and convert to a torch tensor
    X_train_pca, pca_ppo = PCA_ppo(X_train[:, 1:], pc)
    bias_train = torch.tensor([sublist[-1] for sublist in X_train], dtype=torch.float32)
    # Concatenate the PPo_pco values with bias
    X_train_pca = torch.cat((X_train_pca, bias_train.unsqueeze(1)), dim=1)
    # 2. Transform the validation dataset with the fitted PCA and convert to a torch tensor
    X_val_pca = torch.tensor(pca_ppo.transform(X_val[:, 1:]), dtype=torch.float32)
    bias_val = torch.tensor([sublist[-1] for sublist in X_val], dtype=torch.float32)
    # Concatenate the PPo_pco values with bias
    X_val_pca = torch.cat((X_val_pca, bias_val.unsqueeze(1)), dim=1)
    # 3. Transform the test dataset with the fitted PCA and convert to a torch tensor
    X_test_pca = torch.tensor(pca_ppo.transform(X_test[:, 1:]), dtype=torch.float32)
    bias_test = torch.tensor([sublist[-1] for sublist in X_test], dtype=torch.float32)
    # Concatenate the PPo_pco values with bias
    X_test_pca = torch.cat((X_test_pca, bias_test.unsqueeze(1)), dim=1)
    if verbosity == True:      
        print("PPo Train size after PCA\n", X_train_pca.shape)
        print("PPo Test size after PCA\n", X_test_pca.shape)
        print("PPo Validation size\n", X_val_pca.shape)
    return X_train_pca, X_val_pca, X_test_pca, pca_ppo


def pca_to_diff_pp_ppo(Y_train, Y_val, Y_test, pc=0.99999, verbosity = False):
    '''
    Fits the PCA to the PP-PPo of the train subset and transforming the validation and test dataset
    --------
    Inputs:
    -------
    - Y_train: torch.tensor
        tensor with the training subset
    - Y_val: torch.tensor
        tensor with the validation subset
    - Y_test: torch.tensor
        tensor with the test subset
    Outputs:
    -------
    - Y_train_pca: torch.tensor
        training subset after PCA
    - Y_val_pca: torch.tensor
        validation subset after PCA
    - Y_test_pca: torch.tensor
        test subset after PCA
    - pca_diff_pp_ppo: PCA object
        fitted PCA object to train subset to apply the transformations to the other subsets
    '''
    # 1. Fit the PCA to the train dataset and convert to a torch tensor
    Y_train1_pca, pca_diff_pp_ppo = PCA_diff_pp_ppo(Y_train, pc)
    Y_train1_pca = torch.tensor(Y_train1_pca, dtype=torch.float32)

    # 2. Transform the test dataset with the fitted PCA and convert to a torch tensor
    Y_test1_pca = pca_diff_pp_ppo.transform(Y_test)
    Y_test1_pca = torch.tensor(Y_test1_pca, dtype=torch.float32)

    # 3. Transform the validation dataset with the fitted PCA and convert to a torch tensor
    Y_val1_pca = pca_diff_pp_ppo.transform(Y_val)
    Y_val1_pca = torch.tensor(Y_val1_pca, dtype=torch.float32)
    if verbosity == True:      
        print("PP-PPo Train size after PCA\n", Y_train1_pca.shape)
        print("PP-PPo Test size after PCA\n", Y_test1_pca.shape)
        print("PP-PPo Validation size\n", Y_val1_pca.shape)
    return Y_train1_pca, Y_val1_pca, Y_test1_pca, pca_diff_pp_ppo


def pca_to_pp(X_train, X_val, X_test, pc=0.99999, verbosity = False):
    '''
    Fits the PCA to PP of the train subset and transforming the validation and test dataset
    --------
    Inputs:
    -------
    - X_train: torch.tensor
        tensor with the training subset
    - X_val: torch.tensor
        tensor with the validation subset
    - X_test: torch.tensor
        tensor with the test subset
    Outputs:
    -------
    - X_train_pca: torch.tensor
        training subset after PCA
    - X_val_scaled: torch.tensor
        validation subset after PCA
    - X_test_scaled: torch.tensor
        test subset after PCA
    - pca_ppo: PCA object
        fitted PCA object to train subset to apply the transformations to the other subsets
    '''
    # 1. Fit the PCA to the train dataset and convert to a torch tensor
    X_train_pca, pca_pp = PCA_pp(X_train,pc)

    # 2. Transform the test dataset with the fitted PCA and convert to a torch tensor
    X_test_pca_list = pca_pp.transform(X_test)
    X_test_pca = torch.tensor(X_test_pca_list, dtype=torch.float32)

    # 3. Transform the validation dataset with the fitted PCA and convert to a torch tensor
    X_val_pca_list = pca_pp.transform(X_val)
    X_val_pca = torch.tensor(X_val_pca_list, dtype=torch.float32)
    if verbosity == True:      
        print("PP Train size after PCA\n", X_train_pca.shape)
        print("PP Test size after PCA\n", X_test_pca.shape)
        print("PP Validation size\n", X_val_pca.shape)
    return X_train_pca, X_val_pca, X_test_pca, pca_pp

def PCA_ppo(x,PC=None):
    '''
    Performing PCA to ppo with the desired PC
    -------
    Inputs:
    - x: data to apply the pca
    - PC: number of principal components, by default fixed to 0.95
    -------
    Outputs:
    - components_list_ppo:
    - ppo_pca: fitted object for the ppo PCA
    '''
    if PC == None:
        PC = 0.95
    ppo_pca = PCA(PC)
    matrix_ppo = np.array(x, dtype=float)
    matrix_ppo_pca = ppo_pca.fit_transform(matrix_ppo)
    components_list_ppo = matrix_ppo_pca.tolist()
    dump(ppo_pca, open('pca_objects/pca_ppo.joblib', 'wb'))
    return torch.tensor(components_list_ppo, dtype=torch.float32), ppo_pca

def PCA_pp(x,PC=None):
    '''
    Performing PCA to ppo with the desired PC
    -------
    Inputs:
    - x: data to apply the pca
    - PC: number of principal components, by default fixed to 0.95
    -------
    Outputs:
    - components_list_ppo:
    - ppo_pca: fitted object for the ppo PCA
    '''
    if PC == None:
        PC = 0.95
    pp_pca = PCA(PC)
    matrix_pp = np.array(x, dtype=float)
    matrix_pp_pca = pp_pca.fit_transform(matrix_pp)
    components_list_pp = matrix_pp_pca.tolist()
    dump(pp_pca, open('pca_objects/pca_pp.joblib', 'wb'))
    return torch.tensor(components_list_pp, dtype=torch.float32), pp_pca


def PCA_diff_pp_ppo(x,PC=None):
    '''
    Performing PCA to PP-ppo with the desired PC
    -------
    Inputs:
    - x: data to apply the pca
    - PC: number of principal components, by default fixed to 0.95
    -------
    Outputs:
    - components_list_diff_pp_ppo: list with PP-ppo principal components
    - diff_pp_ppo_pca: fitted object for the pp-ppo PCA
    '''
    if PC == None:
        PC = 0.95
    diff_pp_ppo_pca = PCA(PC)
    matrix_diff_pp_ppo = np.array(x, dtype=float)
    matrix_diff_pp_ppo_pca = diff_pp_ppo_pca.fit_transform(matrix_diff_pp_ppo)
    components_list_diff_pp_ppo = matrix_diff_pp_ppo_pca.tolist()
    dump(diff_pp_ppo_pca, open('pca_objects/pca_diff_pp_ppo.joblib', 'wb'))
    return components_list_diff_pp_ppo, diff_pp_ppo_pca