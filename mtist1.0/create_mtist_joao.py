import os

from mtist import master_dataset_generation as mdg
from mtist import assemble_mtist as am

import numpy as np

###############################
# GENERATE MTIST              #
###############################

mu.MASTER_DATASET_DIR = "master_datasets_joao"
mu.GT_DIR = "ground_truths_joao"
mu.MTIST_DATASET_DIR = "mtist_datasets_joao"

am.N_TIMESERIES_PARAMS = np.arange(1, 21)
am.SAMPLING_FREQ_PARAMS = [10, 20, 30]
am.SAMPLING_SCHEME_PARAMS = ["even"]

mdg.generate_mtist_master_datasets()

plt.close("all")

am.assemble_mtist()
