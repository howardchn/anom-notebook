import numpy as np
from scipy.stats import norm
from pandas import DataFrame
from sample_data import iter_data

def __iqa(data_flow, threshold = 98):
    ratio = (100.0 - threshold) * .5
    [min, max] = np.percentile(data_flow['y'].values, [ratio, 100 - ratio])
    raw = data_flow['y'].values[-1]
    mean = np.mean(data_flow['y'].values)
    return [min, max, raw, mean]
    

def run_with_iqr(raw_data, threshold = 95, flow_count = 60):
    data_result = []
    for data_flow in iter_data(raw_data, flow_count):
        data_result.append(__iqa(data_flow, threshold))

    df = DataFrame(data_result, columns = ['min', 'max', 'raw', 'mean'])
    return df

def __mad(data_flow, threshold = 3.5, flow_count = 60):
    if type(data_flow) is list:
            data_flow = np.asarray(data_flow)
    if len(data_flow.shape) == 1:
        data_flow = data_flow[:, None]
    med = np.median(data_flow['y'].values, axis=0)
    abs_dev = np.absolute(data_flow['y'].values - med)

    med_abs_dev = np.median(abs_dev)

    abs_dev_bounds = threshold * med_abs_dev / norm.ppf(0.75)
    abs_upper = med + abs_dev_bounds
    abs_lower = med - abs_dev_bounds

    raw = data_flow['y'].values[-1]
    return [abs_lower, abs_upper, raw, med]

def run_with_mad(raw_data, threshold = 3.5, flow_count = 60):
    data_result = []
    for data_flow in iter_data(raw_data, flow_count):
        data_result.append(__mad(data_flow, threshold))

    df = DataFrame(data_result, columns = ['min', 'max', 'raw', 'mean'])
    return df
    
