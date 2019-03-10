
import torch
import numpy as np

data_file = '../data/js_to_os_traj.csv'
# data_file = '../data/push_traj.csv'

def load_demo():
    
    data = []

    ee_pos_data = np.loadtxt(open(data_file, "rb"), delimiter=",", skiprows=0)[100:1100]

    x_data = np.flip(ee_pos_data[:,0])
    y_data = -np.flip(ee_pos_data[:,1])
    y_data = y_data + 2*ee_pos_data[-1,1]
    # print(x_data.shape)
    new_data = np.vstack([x_data,y_data,np.zeros([x_data.shape[0]])]).T
    # print (new_data.shape)
    # ee_pos_data = np.vstack([ee_pos_data,new_data])
    # ee_pos_data = new_data

    bias = np.mean(ee_pos_data, 0)
    std  = np.std(ee_pos_data, 0)

    for k in range(ee_pos_data.shape[0]):
        datum = ee_pos_data[k,:]
        data.append(torch.tensor([ [ (datum[0]-bias[0])/std[0], (datum[1]-bias[1])/std[1] ] ]))

    return torch.stack(data)