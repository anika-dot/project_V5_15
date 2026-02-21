''' P05_pics2csv.py
generates CSV File from posterized image
map: https://maps.zh.ch/?topic=CMS3ZH&scale=4990&x=683344&y=248027&markers=none,683459,248055,30,-1
pics: http://posterizer.online/rasterbator/
'''

import os
import re
import numpy as np
import colorama # https://pypi.python.org/pypi/colorama
from colorthief import ColorThief
from math import sqrt

CSV = r'Winterthur_neu' # csv file name
PICS_DIR_PATH = r'C:/Users/anika/Desktop/ZHAW/01_Informatik Programmieren/P05/pics/' # rel. path to pic dir

# read pic files and create array
files = [f for f in os.listdir(PICS_DIR_PATH) if os.path.isfile(os.path.join(PICS_DIR_PATH, f))]
# create list with all pic coordinates, e.g. [(1,1),(1,2), ... ] 
pics = [tuple((int(i) for i in re.split('_|.jpg',f) if i.isdigit())) for f in files]
# create array from pic coordinates
a = np.arange(len(files), dtype=object).reshape(max(pics)[0], max(pics)[1])
a.fill('S') # default Street

mapper = {} # mapper with color trained pics to csv char: mapper{pic:char} 
def train(pic, cell):
    mapper[ColorThief(PICS_DIR_PATH + pic).get_color(quality = 1)] = cell

# train cell colors
'''
find matching pics in PICS_DIR_PATH and assign char to be stored in CSV
'''
train('tile_row_6_col_24.jpg', 'R') # Residence
train('tile_row_1_col_4.jpg', 'G') # Green
train('tile_row_4_col_18.jpg', 'S') # Street
train('tile_row_15_col_1.jpg', 'T') # Garden


trainee_keys = list(mapper.keys()) # keys of reference colors 

# use closest color distance to define cell color
color_distance = lambda x, y: int(sqrt(abs((y[0]**2 - x[0]**2) + \
                                           (y[1]**2 - x[1]**2) + \
                                           (y[2]**2 - x[2]**2))))

os.system('cls' if os.name == 'nt' else 'clear') # clear console
if os.name == 'nt': # init Colorama (Windows only)
    colorama.init() 

# map pics to char 
l = len(files)
print('\033[1;1Hmapping %i pics:'%(l))
for i in range(l):
    print('\033[1;20H%.1f %% completed - %i pics left ' %(i * 100 / l, l - i))
    color_thief = ColorThief(PICS_DIR_PATH + files[i])
    try:
        c = color_thief.get_color(quality = 1) # find dominant pic color
    except Exception:
        continue
    distances = [color_distance(c, k)  for k in trainee_keys] # calculate color distances 
    key = mapper[trainee_keys[distances.index(min(distances))]] # find closest color
    row, col = tuple(int(j) for j in re.split('_|.jpg',files[i]) if j.isdigit()) # get pic row, col
    a[row - 1, col - 1] = key # save mapped char in array

np.savetxt(CSV + '.txt', a, fmt = '%1s', delimiter = ',') # save csv 
print(CSV, '.txt file is ready', sep='')



