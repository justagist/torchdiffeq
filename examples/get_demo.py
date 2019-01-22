
import torch
import numpy as np

data_file = '../data/demo_ts_spoon_sprial_setion.csv'

def load_demo():
    
    data = []

    ee_pos_data = np.loadtxt(open(data_file, "rb"), delimiter=",", skiprows=0)

    bias = np.mean(ee_pos_data, 0)
    std  = np.std(ee_pos_data, 0)

    for k in range(ee_pos_data.shape[0]):
        datum = ee_pos_data[k,:]
        data.append(torch.tensor([ [ (datum[0]-bias[0])/std[0], (datum[1]-bias[1])/std[1] ] ]))

    return torch.stack(data)