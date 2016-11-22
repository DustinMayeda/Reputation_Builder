from pymongo import MongoClient
from bs4 import BeautifulSoup

import pandas as pd
import selenium
from selenium import webdriver
from random import random as rnd
import time


'''
Initialize MongoDB
'''
client = MongoClient()
db = client['question_pred1']
question_html = db['question_html1']
question_score = db['question_score1']
answer_score = db['answer_score1']

'''
Loading in question ids
'''

df = pd.read_csv('~/stack_exchange_project/data/QueryResults.csv') #/home/ubuntu
browser = webdriver.Firefox()
question_ids = df['Id']
base_url = "http://stackoverflow.com/questions/"


for qid in question_ids:
    '''
    Scrape stackoverflow question for upvotes, downvotes, views, and number of comments.
    '''
    browser.get(base_url + str(qid))
    time.sleep(3 + rnd())
    html = browser.page_source
    question_html.insert_one({'id': qid, 'html': html})
    soup = BeautifulSoup(html, 'html.parser')
    if len(soup.select('span.vote-count-post')) > 0:
        question_score.insert_one({'id': qid, 'score': int(soup.select('span.vote-count-post')[0].text)})
        if len(soup.select('span.vote-count-post')) > 1:
            for i in xrange(1, len(soup.select('span.vote-count-post'))):
                answer_score.insert_one({'id': qid, 'score': int(soup.select('span.vote-count-post')[i].text)})
    if len(soup.select('span.vote-accepted-on')) > 0:
        answer_score.insert_one({'id': qid, 'accepted': soup.select('span.vote-accepted-on')[0].text})

client.close()
