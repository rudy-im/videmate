import numpy as np
import pandas as pd
from scipy.ndimage import median_filter as scipy_median
from scipy.signal import butter, filtfilt

# parameter 'data' is a list of dataset.


# 이동 평균 필터 (Moving Average)

def movingAvg_filter (data, size=5):
    df = pd.Series(data)
    result = df.rolling(window=size, center=True).mean()
    return result.tolist()


# 중앙값 필터 (Median Filter)

def median_filter (data, size=5):
    if size % 2 == 0:
        raise ValueError("Median filter size must be an odd integer.")
    return scipy_median(data, size=size)



# 저역통과 필터 (Low-pass filter)

def lowpass_filter (data, cutoff=0.1, fs=1.0, order=2):
    if cutoff >= 0.5 * fs:
        raise ValueError("cutoff frequency must be less than Nyquist frequency (fs/2)")
    if len(data) < (order * 3):
        raise ValueError(f"Data length must be at least {order * 3} for filter stability.")
        
    b, a = butter(order, cutoff / (0.5 * fs), btype='low')
    return filtfilt(b, a, data)



