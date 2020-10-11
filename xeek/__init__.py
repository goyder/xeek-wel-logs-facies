import os
from os.path import join

root_dir = os.path.abspath(join(os.path.dirname(__file__), ".."))
data_dir = join(root_dir, "data")
raw_data_dir = join(data_dir, "raw")
external_data_dir = join(data_dir, "external")
processed_data_dir = join(data_dir, "processed")
