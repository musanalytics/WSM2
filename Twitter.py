#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 00:07:14 2022

@author: hunchoahmad
"""


import json
credentials = {}
credentials['CONSUMER_KEY']= '48s1nF1w7gB4YQCvQxHNhwflR'
credentials['CONSUMER_SECTOR']= 'aeXolaObf1mS9mXUapvD5I09cj3BtG6BF9XXd6aXr00WZz80KM'
credentials['ACCESS_TOKEN'] = '2569555417-LoUCPSyAOF6iA8Dr67RTbcwTalY1dKojiQZCRBm'
credentials['ACCESS_SECRET'] = 'Qx9jtxffFZdunze60TFqK2bzqePV533tM8IkvkYWZsb7e'

with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)

from twython import TwythonStreamer
import csv
import json
def process_tweet(tweet):
    d={}
    d['hashtag'] = [hashtag['text'] for  hashtag in tweet['entities']['hashtags']]
    d['text'] = tweet['text']
    d['user']= tweet['user']['screen_name']
    d['user_loc'] = tweet['user']['location']
    d['Time']=tweet["created_at"]
    d['source_device'] = tweet['source']
    d['verification'] = tweet['user']['verified']
    if "place" in tweet and tweet ["place"] != None:
        d['place'] = tweet["place"]["bounding_box"]["coordinates"][0][0]
    return d

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if data['lang'] =='en':
            tweet_data = process_tweet(data)
            self.save_to_csv(tweet_data)

    def on_error(self, status_code , data, x):
        print(status_code , data)
        self.disconnect()

    def save_to_csv(self, tweet):
        with open(r'/Users/ali/Desktop/Lessons/saved_tweets.csv' , 'a'  , encoding='utf_8') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))

import json
stream = MyStreamer('xxxx', 'xxxx' , 'xxxx' , 'xxxx')
stream.statuses.filter(track = 'Elon Musk')



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager
import itertools

fig, ax = plt.subplots()
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#909090'
plt.rcParams['axes.labelcolor']= '#909090'
plt.rcParams['xtick.color'] = '#909090'
plt.rcParams['ytick.color'] = '#909090'
plt.rcParams['font.size']=12


# labels = [w for w,k in itertools.groupby(twitter_client_system , lambda x : x)]
from pathlib import Path
import re
tweets_trending_file_path = Path() / "saved_tweets.csv"
trending_tweets = pd.read_csv(tweets_trending_file_path)


import re
client_system = trending_tweets["client_platform"].tolist()

#print(client_system)
twitter_client_system = []
for i in client_system:
    match = re.search(r'Android|iPhone|Web App|Tweetdeck|TweetDeck|Tweetbot',i)
    if match is not None:
      device = match.group()
      twitter_client_system.append(device)

# print(twitter_client_system) 


counts = dict()
for i in twitter_client_system:
  counts[i] = counts.get(i, 0) + 1


labels = list(counts.keys())
data = list(counts.values())
colors = sns.color_palette('pastel')[0:5]
plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
plt.show()

import folium
from folium.plugins import HeatMap

mapObj = folium.Map(location = [51.49799827422944, -0.13568476148837225], zoom_start=10)
mapObj.save("output.html")

data = [

        [51.605812007125, -0.06898898448285012, 0.50],
        [55.95618309089697, -3.1874873502969554, 0.50],
        [40.75984493852281, -73.98312138462074, 0.50], 
        [51.590670375376334, -0.016460603531450745, 0.50],
        [38.949103568734, -77.07233950096516, 0.50],
        [32.9004703057876, -97.03986422126415, 0.50],
        [30.152249737544775, -97.81452087661509, 0.50],
        [-16.406866360566553, -49.091628235126535, 0.50],
        [49.277428703352264, -123.13386193716576, 0.50],
        [19.31917616580943, -99.18580241072587, 0.50],
        [32.77960745053676, -96.80297152285584, 0.50],
        [40.30823071359626, -82.93462887155731, 0.50],
        [27.998506055292708, -82.4651056138908, 0.50],
        [32.667418087099406, -83.35615918369047, 0.60],
        [29.973458937412744, -90.29043892484235, 0.50],
        [29.94609384515217, -89.96908882961026, 0.50],
        [51.62199402874661, -86.80363737787188, 0.50],
        [27.775410730579033, -81.68329082683769, 0.50],
        [-37.68550552126533, 145.06414942679308, 0.50],
        [51.4492475782009, -0.9832574708937988, 0.50],
        [50.30288346233121, 8.775348412521778, 0.50],
        [41.411445830064274, 2.197522221379609, 0.50],
        [52.35149945781347, 4.932111375638867, 0.50],
        [33.64912919007266, -112.08723358635656, 0.50],
        [29.91565749952911, -90.05276126227567,0.50],
        [29.866930681056218, -89.86815194072324, 0.60],
        [29.820474914459233, -89.66696480845187, 0.60],
        [46.921962304593784, -118.97436815181968, 0.60],
        [40.561620190367336, -74.4412874330749, 0.60],
        [40.78739408657794, -73.11955149988688, 0.50],
        [-22.92746310750504, 143.52863721533842, 0.50],
        [12.959982472626876, 77.57187913446921, 0.45],
        [-31.36248205052039, 116.15070778508912, 0.20],
        [-28.564738306469685, 26.07985934015553, 0.50],
        [9.146033724346067, 7.403101659264552, 0.25],
        [38.48741585294798, 33.91867156176391, 0.50],
        [38.624876318803565, 38.4450387151185, 0.50], 
        [36.05148815910341, 128.5824890153749, 0.50], 


        ]

HeatMap(data).add_to(mapObj)    
mapObj.save('output.html')
mapObj




