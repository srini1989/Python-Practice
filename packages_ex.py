import random
print(random.randint(1, 100))
print(random.randrange(100))

import math
print(math.sin(45))

import time
print(time.asctime())

import requests
response = requests.get("https://api.github.com/events")
print(response.content)
print("===================================="*100)
response = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
print(response.content)

import os
print(os.getcwd())
dir(os)

import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move("/Users/Test", "TestDir")

import statistics as stc
data = [2, 3, 4, 5, 6]
print(stc.mean(data))
print(stc.median(data))

from datetime import date
print(date.today())
