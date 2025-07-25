
import sys, os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from database import DB
import data_filter

db = DB("../data.db")

rWrist = db.select('rWrist', ['x', 'y'])

rWristX = rWrist['x'].tolist()
rWristX = rWrist['y'].tolist()

rWristXMovingAvg = data_filter.movingavg(rWristX)
rWristXMedian = data_filter.median(rWristX)
rWristXLowPass = data_filter.lowpass(rWristX)

rWristXMovingAvgIP = data_filter.find_inflection_points(rWristXMovingAvg)
rWristXMedianIP = data_filter.find_inflection_points(rWristXMedian)
rWristXLowPassIP = data_filter.find_inflection_points(rWristXLowPass)


print(rWristXMovingAvg)
print(rWristXMovingAvgIP)
print('')

print(rWristXMedian)
print(rWristXMedianIP)
print('')

print(rWristXLowPass)
print(rWristXLowPassIP)
print('')

