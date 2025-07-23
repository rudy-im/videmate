
import sys, os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from database import DB
import data_filter

db = DB("../data.db")

print(db.select('rWrist', ['x', 'y']))
