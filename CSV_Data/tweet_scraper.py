import GetOldTweets3 as got
import re
# Need this to fix Http requests otherwise it wont work
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

known_Pollsters = {"MSR": 0, "Redfield":1, "RCP":2, "IBD/TIPP":3,\
                   "Research Co.":4}

class Scraper:
###########################################
# This is the Scraper object class.
# Basically an instance of this allows us to gather tweets of a specific
# user based on certain criteria.
# username: Tweets from a specific account
# start_date: collect a tweet from a specific starting time
# end_date: collect a tweet from a specific ending time
# specific_text: collect a tweet with specific text
###########################################
    def __init__(self, start_date, end_date, race_type, dict_format,\
                 candidate_names):
        ##################################
        # username: Tweets from a specific account
        # start_date: collect a tweet from a specific starting time
        # end_date: collect a tweet from a specific ending time
        # specific_text: collect a tweet with specific text
        ##################################
        self.username = 'Politics_Polls'
        self.start_date = start_date
        self.end_date = end_date
        self.race_type = race_type
        self.tweet_dictionary = dict_format
        self.candidate_names = candidate_names

    def scrape(self):
        # Creation of query object
        tweetCriteria = got.manager.TweetCriteria().setUsername(self.username)\
                                                .setSince(self.start_date)\
                                                .setUntil(self.end_date)\
                                                .setQuerySearch(self.race_type)
        # Creation of list that contains all tweets
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        # Creating dictionary of chosen tweet data
        tweet_size = len(tweets)
        for key in self.tweet_dictionary:
            self.tweet_dictionary[key] = [0]*tweet_size
        for tweet_index in range(0, len(tweets)):
            words = (tweets[tweet_index].text).split()
            for word_index in range(0, len(words)):
                if words[word_index] == "College":
                    break
                else:
                    for candidate_index in range(0, len(self.candidate_names)):
                        if  words[word_index] == self.candidate_names[candidate_index]:
                            if self.race_type == "National GE:":
                                try :
                                    data = int(words[word_index+1][0:2])
                                except:
                                    break
                                self.tweet_dictionary[\
                                self.candidate_names[candidate_index]][tweet_index] = data
                            else:
                                try :
                                    data = int(words[word_index+2][0:2])
                                except:
                                    break
                                self.tweet_dictionary[\
                                self.candidate_names[candidate_index]][tweet_index] = data

                    if re.match(".*?@.*?", words[word_index]) or \
                    words[word_index] in known_Pollsters:
                        self.tweet_dictionary["Pollster"][tweet_index] = \
                        words[word_index]
                    elif re.match("[(]?[0-9]/.*?", words[word_index]):
                        date = re.findall("[0-9][0-9]?/.*", words[word_index])
                        self.tweet_dictionary["Date"][tweet_index] = date[0]
