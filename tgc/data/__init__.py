from .lorenz import lorenz_96
from .var import var_stable
from .var import custom_var_function
from .fMRI import fmri_net_sim
from .dream3 import dream3_trajectories
from .dream4 import dream4_trajectories

__all__ = ['lorenz_96', 'var_stable', "custom_var_function", 'fmri_net_sim', 'dream3_trajectories','dream4_trajectories']
