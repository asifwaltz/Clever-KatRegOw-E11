import csv
import time
import numpy as np
import sys

args = sys.argv
print(args)

# if len(sys.argv) != 3:
#     print("Usage: python script.py <filename> <runtime>")
#     sys.exit(1)

# data_path = sys.argv[1]
# runtime = int(sys.argv[2])

data_path = "data/" + args[1]
runtime = int(args[2])

file = open(data_path, "w", newline = None)

csvwriter = csv.writer(file, delimiter = ",")

meta = ["time", "data"]
csvwriter.writerow(meta)

for i in range(runtime):
  now = time.time()
  value = np.random.random()
  csvwriter.writerow([now, value])
