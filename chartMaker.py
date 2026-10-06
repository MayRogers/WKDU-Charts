import numpy as np
import pandas as pd
import datetime as dt
from pathlib import Path as pt

def currYear():
    return dt.datetime.now().year

def findFile(searchText):
    directory = pt.Path()
    for file in directory.glob("**/*.csv"):
        if searchText in file.name:
            return file
    return None

def searchData(data, artist, album):
    trimmedData = data[:, [2, 3, 6]]
    inds = np.where((artist in trimmedData[:, 0]) & (album in trimmedData[:, 1]))
    if len(inds[0]) == 0:
        return False, None
    promoters = trimmedData[inds[0], 2]
    return promoters[0] if len(promoters) > 0 else None

def parsePromoter(promoters):
    for promoter in promoters:
        promoter.tolower()
        if ("syndicate" in promoter) or ("pirate" in promoter) or ("sign" in promoter) or ("secretly" in promoter) or ("shine" in promoter) or ("planetary" in promoter) or ("terror" in promoter) or ("tiger" in promoter):
            return promoter
    return "n/a"

searchText = "charts"
chartsFile = findFile(searchText)
if chartsFile is None:
    raise FileNotFoundError(f"No csv file containing '{searchText}' found")
chartsDF = pd.read_csv(chartsFile)
chartsData = chartsDF.to_numpy()

searchText = "currAdds"
currAddsFile = findFile(searchText)
if currAddsFile is None:
    raise FileNotFoundError(f"No csv file containing '{searchText}' found")
currAddsDF = pd.read_csv(currAddsFile)
currAddsData = currAddsDF.to_numpy()

searchText = currYear()
yearAddsFile = findFile(searchText)
if yearAddsFile is None:
    raise FileNotFoundError(f"No csv file containing '{searchText}' found")
yearAddsDF = pd.read_csv(yearAddsFile)
yearAddsData = yearAddsDF.to_numpy()

searchText = currYear() - 1
prevYearAddsFile = findFile(searchText)
if prevYearAddsFile is None:
    raise FileNotFoundError(f"No csv file containing '{searchText}' found")
prevYearAddsDF = pd.read_csv(prevYearAddsFile)
prevYearAddsData = prevYearAddsDF.to_numpy()


while (plays > 0):