# before running this code, you have to install the modules snscrape and pandas in your cmd:
    # pip install snscrape
    # pip install pandas

import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
# you will have to use different search querys and times, e.g.: "drone since:2021-08-07 until:2021-10-20"
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Drones Pakistan  (#FATA OR #WARCRIME OR #Taliban OR #CounterTerrorism OR #burraq OR #survivor OR #strike OR #TerrorMonitor OR #ISIS OR #US OR  #JihadWithoutBorders OR #NorthWaziristan OR #Kurram OR #GilgitBaltistan OR #terrorists OR #Peshawar OR #PAKISTAN OR #IS OR #terrorism OR #USA OR #usa OR #Genocide OR #war OR #PakPoint OR #humanrights OR #drones OR #drone OR #civilians OR #pakistan OR #dronewar OR #obamafail OR #IHaveADrone OR #CollateralDamage OR #terror) until:2009-10-31 since:2009-10-24').get_items()):
    if i>30000:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# prints list in cmd, not necessary    
print(tweets_list)

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# safes df to csv
tweets_df.to_csv("snscrape_tweets_october_terrorists_2009.csv")