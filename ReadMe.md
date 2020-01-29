# BudCare
This project comes in the context of the challenge of tunihack 5.0 , the challenge theme is Trust and social media. 
Our project idea is to use data on social media to help parents control and protect their young childrens from the different risks such as violence , cyberbullying , blackmailing ..

Our project is divided into 3 axes:
 -Scraping tweets from twitter using tweepy API

 -NLP To classify posts , comments and any other textual data 

 -Developing an app using Flask for the demonstration of the project

# Scraping tweets :
into the file of tweet scraper you will find tweet.py , run this file and indicates which the user id you want to scrape and you will get a csv file containing the id ,date and the full_text of the tweet.
# NLP to classify textual data :
Data used to train the model was downloaded from kaggle .
it can be downladed using this command : 
kaggle datasets download -d eray1yildiz/emotion-classification
data contains 6 labels : anger/fear/surprise/love/joy/sadness , we have trained our model on only four labels : fear / joy /sadness/anger
we have used LSTM  and embedded words to create a model with an accuracy of 97% on vaidation set.
# Web app for demo : 
creating a demo site presenting a single use case where the user can track tweets of his children and seeing the predictions of the model which is integrated in the web applicaton .

### Technologies 
* [Flask] - web framework written in python to develop web apps (chIldcAre repository)
* [tensorflow] an open source library for numerical computation and large-scale machine learning
* [tweepy] - Twitter API to get data from twitter 

# Team members
* **Mokhtar Mami** - *github* - [Mokhtar Mami](https://github.com/Mo5mami)

  **Ahmed Attia** - *github* - [Ahmed Attia](https://github.com/ahmedattia143)
  
  **Bochra Saffar** - *github* - [Bochra Saffar](https://github.com/bochrasaffar)






