import csv
import time
import numpy as np
import sys

args = sys.argv
print(args)

file = open("data/test.csv", "w", newline = None)

csvwriter = csv.writer(file, delimeter = ",")

meta = ["time", "data"]
csvwriter.writerow(meta)

for i in range(10):
  now = time.time()
  value = np.random.random()
  csvwriter.writerow([now, value])
