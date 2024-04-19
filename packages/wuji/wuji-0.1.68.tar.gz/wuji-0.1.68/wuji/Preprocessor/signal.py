#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   signal 
@Time        :   2023/11/21 14:06
@Author      :   Xuesong Chen
@Description :   
"""

import numpy as np
from hrvanalysis import get_nn_intervals


def interp_signal(positions, values, fs, target_fs, n_samples):
    '''
    Interpolate RRI or JJI to target sampling frequency
    Parameters
    ----------
    positions: positions of RRI or JJI
    values: values of RRI or JJI
    fs: sampling frequency of RRI or JJI
    target_fs: target sampling frequency
    n_samples: number of samples of the raw signal

    Returns
    -------
    interp_value: interpolated RRI or JJI at target sampling frequency, in ms
    '''
    rri_in_ms = values / fs * 1000
    filtered_rri_in_ms = get_nn_intervals(rri_in_ms, verbose=False, ectopic_beats_removal_method='karlsson')
    interp_value = np.interp(
        np.arange(0, n_samples, fs / target_fs), positions,
        filtered_rri_in_ms).astype(np.float32)
    return interp_value
