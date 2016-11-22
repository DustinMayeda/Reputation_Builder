import numpy as np
import pymongo
import pandas as pd
from pymongo import MongoClient

'''
Imports the answer scores scraped from stack overflow
'''

client = MongoClient()
db = client.question_pred1
collection = db.answer_score1
data = pd.DataFrame(list(collection.find()))

def reputation(data):
    '''
    Converts the dataframe with an id and reputation points column.
    '''

    del data['_id']
    accept = data[data['accepted'] == 'accepted']
    accepted = list(accept['id'])
    df = data.groupby('id').aggregate(lambda x: x.iloc[0])#.reset_index
    del df['accepted']
    df.ix[accepted, 'score'] += 15
    df.reset_index(level=0, inplace=True)
    df = df.sort('id')

def relevant_data(df1):
    '''
    Takes in the feature data and only takes the rows with ids in the reputation
    table.
    '''

    df1 = pd.read_csv('data/QueryResults.csv')
    ids = list(df['id'])
    np.in1d(df1['Id'].values, ids)  #which ids are in the ids
    modified_df = df1[np.in1d(df1['Id'].values, ids)]
    modified_df = modified_df.sort('Id')

def clean_data(modified_df):
    modified_df['Body'] = modified_df['Body'].apply(lambda x: len(x.split()))
    del modified_df['CreationDate']
    del modified_df['Id']
    del modified_df['OwnerUserId']
    del modified_df['Location']
    del modified_df['WebsiteUrl']
    del modified_df['OwnerDisplayName']
    del modified_df['Title']
    del modified_df['Age']
    del modified_df['Tags']
    del modified_df['CreationDate.1']
    del modified_df['LastAccessDate']
    modified_df['FavoriteCount'] = modified_df['FavoriteCount'].fillna(0)
