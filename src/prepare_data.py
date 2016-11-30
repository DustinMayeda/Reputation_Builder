from __future__ import division

import copy
import pandas as pd

def reputation_change(x):
    if x != None:
        if x > 0:
            return 10 * x
        else:
            return 2 * x

def reputation(data):
    '''
    Converts the dataframe with an id and reputation points column.
    '''

    data['score'] = data['score'].apply(reputation_change)
    data['reputation'] = data['score']
    del data['score']
    del data['_id']
    del data['Unnamed: 0']
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
    topics = ['ViewCount', 'Body', 'Score', 'CommentCount', 'FavoriteCount', 'Reputation', 'UpVotes', 'DownVotes']
    modified_df['Body'] = modified_df['Body'].apply(lambda x: len(x.split()))
    modified_df['FavoriteCount'] = modified_df['FavoriteCount'].fillna(0)
    return modified_df[topics]

def score_real(x):
    if x >= 200:
        return 0
    elif x < 0:
        return 0
    else:
        return x

def score(x):
    if x >= 200:
        return 0
    elif x <= 0:
        return 0
    else:
        return 1

def convert_html(html):
    word = ''
    for sentence in html.select('p'):
        word += ' ' + sentence.text
    return word.strip()

def convert_documents(X):
    result = []
    for document in X:
        soup = BeautifulSoup(document, 'html.parser')
        result.append(convert_html(soup))
    return np.array(result)

# Building the classification dataset
data = pd.read_csv('data/answer.csv')
df = reputation(data)
df1 = pd.read_csv('data/QueryResults.csv')
modified_df = relevant_data(df1)
master = copy.deepcopy(modified_df)

def classification_data(modified_df):

    vectorizer = TfidfVectorizer()

    Z_class = modified_df['Body']
    Z_class = convert_documents(Z_class)
    Z_class = vectorizer.fit_transform(Z_class, y_0)

    Z = clean_data(modified_df)

    X_class = np.concatenate((Z, Z_class.todense()), axis=1)

    y_0 = df['reputation'].apply(score)
    y_0 = np.array(y_0)

    return X_class, y_0

# Building the regression dataset

def regression_data():

    vector = TfidfVectorizer()

    Z_reg = positive['Body']
    Z_reg = convert_documents(Z_reg)
    Z_reg = vector.fit_transform(Z_reg, y)

    Y = clean_data(positive)

    X_reg = np.concatenate((Y, Z_reg.todense()), axis=1)

    ids = df[df['reputation'] > 0]['id']
    positive = master[np.in1d(modified_df['Id'], ids)]
    y = df[df['reputation'] > 0]['reputation'].values

    return X_reg, y
