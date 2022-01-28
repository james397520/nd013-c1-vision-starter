import argparse
import glob
import os
import random
import re
import numpy as np
import shutil

from utils import get_module_logger

def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # TODO: Implement function

    train_path = os.path.join(destination,"train")
    val_path = os.path.join(destination,"test")
    test_path = os.path.join(destination,"val")
    if os.path.exists(train_path): # remove folder and contents if exists
        shutil.rmtree(train_path)
    if os.path.exists(val_path):
        shutil.rmtree(val_path)
    if os.path.exists(test_path):
        shutil.rmtree(test_path)
        
    # create new directories
    os.mkdir(train_path)
    os.mkdir(val_path)
    os.mkdir(test_path)
    
    #get list of records to use
    record_files = glob.glob(source+"*.tfrecord")
    print(len(record_files))

    np.random.shuffle(record_files)
    # spliting files
    train_files, val_file, test_file = np.split(record_files, [int(.75*len(record_files)), int(.9*len(record_files))])
    print(train_path)
    print(val_file)
    print(test_file)
    
    for file in train_files:
        print(file)
        shutil.move(file, train_path)
    
    for file in val_file:
        print(file)
        shutil.move(file, val_path)

    for file in test_file:
        print(file)
        shutil.move(file, test_path) 




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)