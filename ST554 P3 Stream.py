## Bing Chen 
## Purpose: This script is written for streaming data part, to produce data, for ST 554 Project 3. 
## Date: 4/18/2026

import pandas as pd
import time

power = pd.read_csv("https://www4.stat.ncsu.edu/~online/datasets/power_streaming_data.csv")

for i in range(20):
    sample = power.sample(n=5)
    sample.to_csv(f"csv_files/power_{i}.csv", index=False)
    time.sleep(10) 

