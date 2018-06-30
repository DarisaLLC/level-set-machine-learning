import numpy as np

from stat_learn_level_set import stat_learn_level_set as SLLS
from stat_learn_level_set.feature_maps.dim2 import simple_feature_map as sfm
from stat_learn_level_set.init_funcs import random as rand_init

# Seed a random number generator.
rs = np.random.RandomState(1234)

# Set simple feature map function.
fmap = sfm.simple_feature_map(sigmas=[0,3])

# Set the level set init routine.
ifnc = rand_init.random(rs=rs)

# Initialize the model.
slls = SLLS(data_file="./dataset.h5", feature_map=fmap,
            init_func=ifnc, band=3.0, rs=rs)

# See documentation for complete list of fit options.
slls.set_fit_options(maxiters=50, remove_tmp=0,
                     logfile="./log.txt", logstamp=0, logstdout=1)

# See documentation for complete list of neural network fit options.
slls.set_net_options(nhidden=[8], maxepochs=100, ninits=1, step=0.1)
     
# Finally, start the fitting process.
slls.fit()