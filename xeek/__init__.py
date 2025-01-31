import os
from os.path import join

# Establish directories
root_dir = os.path.abspath(join(os.path.dirname(__file__), ".."))
data_dir = join(root_dir, "data")
raw_data_dir = join(data_dir, "raw")
external_data_dir = join(data_dir, "external")
processed_data_dir = join(data_dir, "processed")

# Establish input files
raw_train_filepath = join(external_data_dir, "train.csv")
raw_test_filepath = join(external_data_dir, "test.csv")
penalty_matrix_filepath = join(external_data_dir, "penalty_matrix.npy")
