import pandas as pd
from matplotlib import pyplot as plt
import os
import json
import glob
import sys
import time
import datetime


sys.path.append('./utils/')
from set_config import SetConfiguration

SC = SetConfiguration()
data_dir = SC.get_path_data()
save_dir = SC.get_path_save()
json_dir = SC.get_path_json()
csv_dir = glob.glob(data_dir + '*.csv')

def check_dirs():
    ##DATA DIRECTORY
    if not os.path.isdir(data_dir):
        raise FileNotFoundError("Path to CSV file storage is wrong?")

    ##SAVE DIRECTORY
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    print("Plots storage: " + save_dir)
    time.sleep(1)

    ##JSON DIRECTORY
    if not os.path.isdir(json_dir):
        os.makedirs(json_dir)
    print("JSON file storage: " + json_dir)
    time.sleep(1)


def csv2png():
    for csv_file in csv_dir:
        df = pd.read_csv(csv_file, index_col=0)
        file_name = os.path.splitext(os.path.basename(csv_file))[0]
        save_path = os.path.join(save_dir, file_name)
        for i, dat in df.iteritems():
            plt.scatter(df.index, dat, label=i)
        plt.title(file_name)
        plt.legend()
        plt.savefig(save_path + ".png")
        plt.close()
        print(save_path + ".png is created from " + csv_file)


def get_json_info():
    json_str = {
        'test_name' : SC.get_test_name('angular_profile'),
        'test_type' : SC.get_test_type('verification'),
        'test_site' : SC.get_test_site('chiba'),
        'test_date' : str(datetime.date.today()),
        'test_result' : {
            'result_type' : SC.get_result_type('graph'),
            'x-vals' : getVals(0),
            'y-vals' : getVals(1),
            'x-label' : SC.get_result_xlabel('angle'),
            'y-label' : SC.get_result_ylabel('intensity')
        }
    }
    return json_str


def getVals(axis):
    xval = []
    yval = []
    for i in range(len(csv_dir)):
        cw_data = pd.read_csv(csv_dir[i])
        x_data = pd.Series(cw_data['deg'])
        y_data = pd.Series(cw_data['cw'])
                
        for x, y in zip(x_data, y_data):
            xval.append(x)
            yval.append(y)
    if axis == 0:
        return xval
    elif axis == 1:
        return yval
    else:
        raise ValueError("Error!")


def str_json_info():
    json_str = get_json_info()
    for i in range(len(csv_dir)):
        data_json = os.path.splitext(os.path.basename(csv_dir[i]))[0]
        json_path = os.path.join(json_dir, data_json)
        with open(os.path.join(json_path + '.json'), 'w') as f:
            json.dump(json_str, f, indent=4)
            print(json_path + ".json is created.")


if __name__ == "__main__":
    print("This is the script for storing data of LED measurements!")
    time.sleep(1)
    
    ##CHECK DIRECTORY PATH
    print("--- DIRECTORY CHECK ---")
    check_dirs()
    print()

    ##CSV to PNG
    print("--- CONVERTING CSV TO PNG ---")
    csv2png()
    print("Done!\n")
    time.sleep(1)
    
    ##CREATE JSON FILE
    print("--- CREATE JSON FILE ---")
    str_json_info()
    print("Done!")
