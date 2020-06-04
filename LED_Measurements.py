import pandas as pd
from matplotlib import pyplot as plt
import os
import json
import glob

data_dir = '../data'
save_dir = '../graph'
json_dir = '../json'

def main():
    os.chdir(data_dir)
    filelists = glob.glob('*.csv')
    for file in filelists:
        if not os.path.isdir(file) and file[-4:]==".csv":
            csv2png(file)

def csv2png(file):
    df = pd.read_csv(file, index_col=0)
    for i, dat in df.iteritems():
            plt.scatter(df.index, dat, label = i)
    plt.title(file)
    plt.legend()
    plt.savefig(os.path.join(save_dir, file+"."))
    plt.close()

if __name__ == '__main__':
    main()

def get_json_info():
    json_str = {
        'test_name' : 'angular_profile',
        'test_type' : 'verification',
        'test_type' : 'Chiba',
        'test_data' : '2020/01/01',
        'test_result' : {
            'result_type' : 'graph',
            'x-vals' : getVals('xaxis'),
            'y-vals' : getVals('yaxis'),
            'x-label' : 'angle[deg]',
            'y-label' : 'intensity[mV]'
        }
    }
    return json_str


def getVals(axis):
    os.chdir('/mnt/c/Users/yuya9/mylab/LED_Measurements/data/')
    data_dir = glob.glob('*.csv')
    NumF = len(data_dir)
    xval = []
    yval = []
    for i in range(0, NumF):
        cw_data = pd.read_csv(data_dir[i])
        x_data = pd.Series(cw_data['deg'])
        y_data = pd.Series(cw_data['cw'])
                
        for x, y in zip(x_data, y_data):
            xval.append(x)
            yval.append(y)
    #string = f'{axis}'
    if axis == 'xaxis':
        return xval
    elif axis == 'yaxis':
        return yval
    else:
        raise ValueError("Argument should be 'xaxis' or 'yaxis'")

def str_json_info():
    json_str = get_json_info()
    os.chdir('/mnt/c/Users/yuya9/mylab/LED_Measurements/data/')
    data_dir = glob.glob('*.csv')
    NumF = len(data_dir)
    for i in range(0, NumF):
        data_json = os.path.splitext(os.path.basename(data_dir[i]))[0]
        with open(os.path.join(json_dir,data_json+'.json'), 'w') as f:
            json.dump(json_str, f, indent=4)
            print("JSON file is created.")
            print(json_str)

    
if __name__ == "__main__":
    str_json_info()

