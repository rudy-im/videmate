import numpy as np
import pandas as pd
from scipy.ndimage import median_filter
from scipy.signal import butter, filtfilt

# 이동 평균 필터 (Moving Average)

data = [10, 12, 11, 50, 13, 12, 11, 10]
df = pd.Series(data)

smoothed = df.rolling(window=3, center=True).mean()
print(smoothed)



# 중앙값 필터 (Median Filter)

data = [1, 100, 2, 3, 2, 1, 100, 2, 3]
filtered = median_filter(data, size=3)
print(filtered)



# 저역통과 필터 (Low-pass filter)

def lowpass_filter(data, cutoff=0.1, fs=1.0, order=2):
    b, a = butter(order, cutoff / (0.5 * fs), btype='low')
    return filtfilt(b, a, data)

t = np.linspace(0, 1, 100)
data = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(100)

filtered = lowpass_filter(data)
