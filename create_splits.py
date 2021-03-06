import argparse
import glob
import os
import shutil
import random

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.

    tf_records = glob.glob("{}waymo/training_and_validation/*".format(data_dir))
    val_list = random.sample(range(97), 10)
    for idx, tf_record in enumerate(tf_records):   
        if idx in val_list:
            # move data to val dir
            shutil.move(tf_record, "{}waymo/val/{}".format(data_dir, os.path.basename(tf_record)))
        else:
            # move data to train dir
            shutil.move(tf_record, "{}waymo/train/{}".format(data_dir, os.path.basename(tf_record)))
            
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)