from tweet_scraper import Scraper
import csv

general_election = {"Biden": [], "Trump": [], "Pollster": [], "Date": []}
general_election_scrape = Scraper("2020-05-01", "2020-06-27", "National GE:", general_election\
        , ["Biden", "Trump"])
general_election_scrape.scrape()
my_dict = general_election_scrape.tweet_dictionary
with open('general_election.csv', 'w') as file:
    writer = csv.writer(file)
    for key_index in range(-1, len(my_dict["Biden"])):
        if key_index == -1:
             writer.writerow([key_index+1, "Date","Biden", "Trump", "Pollster"])
        else:
            writer.writerow([key_index+1, my_dict["Date"][key_index],\
            my_dict["Biden"][key_index], my_dict["Trump"][key_index],\
            my_dict["Pollster"][key_index]])



##print(general_election_scrape.tweet_dictionary)

Az_Senate_Scrape = {"Kelly": [], "McSally": [], "Pollster": [], "Date": []}
Az_Senate_Scrape = Scraper("2020-06-25", "2020-06-27", "#AZsen", Az_Senate_Scrape\
        , ["Kelly", "McSally"])
Az_Senate_Scrape.scrape()
my_dict = Az_Senate_Scrape.tweet_dictionary
with open('AZ_Senate.csv', 'w') as file:
    writer = csv.writer(file)
    for key_index in range(-1, len(my_dict["Kelly"])):
        if key_index == -1:
             writer.writerow([key_index+1, "Date","Kelly", "McSally", "Pollster"])
        else:
            writer.writerow([key_index+1, my_dict["Date"][key_index],\
            my_dict["Kelly"][key_index], my_dict["McSally"][key_index],\
            my_dict["Pollster"][key_index]])
