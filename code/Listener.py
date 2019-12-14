import time
import io
from tweepy.streaming import StreamListener

#Listener Class Override
class Listener(StreamListener):

    def __init__(self, start_time, time_limit=60):

        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []

    def on_data(self, data):

        while (time.time() - self.time) < self.limit:
            print(time.time() - self.time)
            try:
                self.tweet_data.append(data)
                return True
            except BaseException as e:
                print('failed ondata,', str(e))
                time.sleep(5)
                pass
        print(self.tweet_data[0:5])
        saveFile = io.open('../data/raw_tweets.json', 'w', encoding='utf-8')
        saveFile.write(u'[\n')
        saveFile.write(','.join(self.tweet_data))
        saveFile.write(u'\n]')
        saveFile.close()
        exit()

    def on_error(self, status):
        print(status)