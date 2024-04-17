#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   detect_oxygen_desaturation
@Time        :   2023/4/25 14:41
@Author      :   Xuesong Chen
@Description :
"""

import numpy as np
import pandas as pd


def detect_oxygen_desaturation(spo2_arr, duration_max=120, spo2_des_min_thre=3, ret_format='df'):
    '''

    :param spo2_arr:
    :param duration_max:
    :param spo2_des_min_thre: 血氧降低最低报警阈值
    :return:
    '''
    spo2_max = spo2_arr[0]  # 初始化最大值
    spo2_max_index = 1  # 初始化最大值下标
    spo2_min = 100  # 初始化血氧最低值
    des_onset_pred_set = np.array([], dtype=int)  # 算法预测氧降起始点总集
    des_duration_pred_set = np.array([], dtype=int)  # 算法预测氧降持续时间总集
    des_level_set = np.array([])  # 被记录的氧降事件合集 （下降百分比2%，3%，4%，5%....
    des_onset_pred_point = 0  # 预测事件起始点
    des_flag = 0  # 氧降事件发生标记
    ma_flag = 0  # motion artifact事件发生标记
    spo2_des_max_thre = 50  # 血氧motion artifact阈值,50%
    duration_min = 5  # 氧降事件至少持续duration_min s才会被记录在内
    prob_end = []

    for i, current_value in enumerate(spo2_arr):

        des_percent = spo2_max - current_value  # 氧降值

        # 检测Motion artifacts
        if ma_flag and (des_percent < spo2_des_max_thre):
            if des_flag and len(prob_end) != 0:
                des_onset_pred_set = np.append(des_onset_pred_set, des_onset_pred_point)
                des_duration_pred_set = np.append(des_duration_pred_set, prob_end[-1] - des_onset_pred_point)
                des_level_point = spo2_max - spo2_min
                des_level_set = np.append(des_level_set, des_level_point)
            # 重置
            spo2_max = current_value
            spo2_max_index = i
            ma_flag = 0
            des_flag = 0
            spo2_min = 100
            prob_end = []
            continue

        # 如果氧降值大于2%, 记录起始时间
        if des_percent >= spo2_des_min_thre:
            if des_percent > spo2_des_max_thre:
                ma_flag = 1
            else:
                des_onset_pred_point = spo2_max_index
                des_flag = 1
                if current_value < spo2_min:
                    spo2_min = current_value

        if current_value >= spo2_max and not des_flag:
            spo2_max = current_value
            spo2_max_index = i

        elif des_flag:

            if current_value > spo2_min:
                if current_value > spo2_arr[i - 1]:
                    prob_end.append(i)

                # 定位血氧连续下降点
                if current_value <= spo2_arr[i - 1] < spo2_arr[i - 2]:
                    spo2_des_duration = prob_end[-1] - spo2_max_index

                    # 下降时间不够的话，则不认为是氧降事件
                    if spo2_des_duration < duration_min:
                        spo2_max = spo2_arr[i - 2]
                        spo2_max_index = i - 2
                        spo2_min = 100
                        des_flag = 0
                        prob_end = []
                        continue

                    else:
                        # 下降时间满足条件，则记录该次氧降事件
                        if duration_min <= spo2_des_duration <= duration_max:
                            des_onset_pred_set = np.append(des_onset_pred_set, des_onset_pred_point)
                            des_duration_pred_set = np.append(des_duration_pred_set, spo2_des_duration)
                            des_level_point = spo2_max - spo2_min
                            des_level_set = np.append(des_level_set, des_level_point)

                        # 下降时间过长，说明存在多个氧降事件，需要分开记录
                        else:
                            # 记录第一个氧降事件
                            des_onset_pred_set = np.append(des_onset_pred_set, des_onset_pred_point)
                            des_duration_pred_set = np.append(des_duration_pred_set, prob_end[0] - des_onset_pred_point)
                            des_level_point = spo2_max - spo2_min
                            des_level_set = np.append(des_level_set, des_level_point)

                            # 重新查找可能的氧降事件
                            remain_spo2_arr = spo2_arr[prob_end[0]:i + 1]
                            _onset, _duration, _des_level = detect_oxygen_desaturation(remain_spo2_arr,
                                                                                       ret_format='tuple')
                            des_onset_pred_set = np.append(des_onset_pred_set, _onset + prob_end[0])
                            des_duration_pred_set = np.append(des_duration_pred_set, _duration)
                            des_level_set = np.append(des_level_set, _des_level)

                        spo2_max = spo2_arr[i - 2]
                        spo2_max_index = i - 2
                        spo2_min = 100
                        des_flag = 0
                        prob_end = []
    if ret_format == 'tuple':
        return des_onset_pred_set, des_duration_pred_set, des_level_set
    else:
        return pd.DataFrame({
            'Type': 'OD',
            'Start': des_onset_pred_set,
            'Duration': des_duration_pred_set,
            'OD_level': des_level_set
        })
