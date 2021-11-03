import numpy as np


def calculate(arr: list) -> dict:
    if len(arr) < 9:
        raise ValueError('List must contain nine numbers.')

    np_arr = np.array(arr).reshape(3, 3)
    results = {}

    datas = {
        'mean': np_arr.mean,
        'variance': np_arr.var,
        'standard deviation': np_arr.std,
        'max': np_arr.max,
        'min': np_arr.min,
        'sum': np_arr.sum,
    }

    for key, data in datas.items():
        results[key] = [i.tolist() for i in (data(axis=0), data(axis=1))] + [data()]

    return results
