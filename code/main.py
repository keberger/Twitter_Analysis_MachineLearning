
#Load Libraries
import pandas
import sys
import subprocess
import numpy
import matplotlib.pyplot as plt

#Load Tweepy
try :
    from tweepy import Stream
    from tweepy import OAuthHandler
    from tweepy.streaming import StreamListener
except ImportError as e:
    subprocess.call([sys.executable, "-m", "pip", "install", 'tweepy'])
    pass

#Load Listener Library
import listener

#Load Various solutions
import time
import os
import io


#Function Definition

def Authentification()->OAuthHandler:
    """
    Allows the code to connect to twitter account
    The keys are stored in seperate file and should keep secrets
    """
    #Load information about consumer
    consumer_key = pandas.read_csv("../id_key/consumer_key.csv", header = None)
    consumer_key = consumer_key.loc[0].values[0]
    consumer_secret = pandas.read_csv("../id_key/consumer_secret.csv", header = None)
    consumer_secret = consumer_secret.loc[0].values[0]
    #Load Information about Tokens
    access_token = pandas.read_csv("../id_key/access_token.csv", header = None)
    access_token = access_token.loc[0].values[0]
    access_token_secret = pandas.read_csv("../id_key/access_token_secret.csv", header = None)
    access_token_secret = access_token_secret.loc[0].values[0]

    auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
    auth.set_access_token(access_token, access_token_secret)
    return auth


def main()->None:
    """
    Main Function calling all other functions
    """
    #Define key words
    keyword_list = ['#DataScience', '#MachineLearning', '#artificialintelligence', '#AI', '#ai', '#machinelearning',
                    '#deeplearning', 'DeepLearning', '#ML', '#ArtificialIntelligence', '#machinelearning',
                    'DigitalTransformation']  # track list

    #Initiate Time
    start_time = time.time()  # grabs the system time
    print("Launch! \n")

    #Listen to twitter
    twitterStream = Stream(Authentification(), listener.Listener(start_time, time_limit=3600))  # initialize Stream object with a time out limit
    twitterStream.filter(track=keyword_list, languages=['en'])  # call the filter method to run the Stream Object
    print('Exctraction from twitter succesful')

if __name__ == "__main__":
    main()

