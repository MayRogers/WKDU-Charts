import numpy as np
import pandas as pd
import datetime as dt
from pathlib import Path as pt


directory = pt()
for file in directory.glob("**/*.csv"):
    if "charts" in file.name:
        chartsFile = file
        break
if chartsFile is None:
    raise FileNotFoundError(f"No csv file containing charts found")
chartsDF = pd.read_csv(chartsFile)
shuffledCharts = chartsDF.sample(frac=1)
shuffledCharts.to_csv("outputPOC.csv", index=False)