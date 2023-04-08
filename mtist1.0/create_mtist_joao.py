import os

from mtist import master_dataset_generation as mdg
from mtist import assemble_mtist as am
from mtist import mtist_utils as mu

import numpy as np

###############################
# GENERATE MTIST              #
###############################

mu.GLOBALS.MASTER_DATASET_DIR = "master_datasets_joao"
mu.GLOBALS.GT_DIR = "ground_truths_joao"
mu.GLOBALS.MTIST_DATASET_DIR = "mtist_datasets_joao"

am.ASSEMBLE_MTIST_DEFAULTS.N_TIMESERIES_PARAMS = np.arange(1, 21, 4)
am.ASSEMBLE_MTIST_DEFAULTS.SAMPLING_FREQ_PARAMS = [10, 20, 30]
am.ASSEMBLE_MTIST_DEFAULTS.SAMPLING_SCHEME_PARAMS = ["even"]

mdg.MASTER_DATASET_DEFAULTS.NOISE_SCALES = [0.1]

mdg.generate_mtist_master_datasets()

plt.close("all")

am.assemble_mtist()
