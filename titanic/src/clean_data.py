import numpy as np
import csv as csv
import pandas as pd
import pylab as pl


# df = pd.DataFrame.from_csv('../data/train.csv')
# print df['Age'][0:10]

# print df['Age'].mean()



# print df[['Sex', 'Pclass', 'Age']]

# print df[df['Age'] > 60][['Sex', 'Pclass', 'Age', 'Survived']]

# print df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]



# df['Age'].dropna().hist(bins=16, range=(0,80), alpha = .5)
# pl.show()




def clean_data(df):
    print '*'*23
    print '   Cleaning the data   '
    print '*'*23



    #add new column
    df['Gender'] = 4

    # male => 1, female => 0
    df['Gender'] = df['Sex'].map({'female':0, 'male':1}).astype(int)


    # fill missing ages with the median:
    median_ages = np.zeros((2,3))

    # calculate the median age according to the gender and cabin:
    for i in xrange(0, 2):
        for j in xrange(0, 3):
            median_ages[i,j] = df[(df['Gender'] == i) & (df['Pclass'] == j + 1)]['Age'].dropna().median()

    # print median_ages

    #add AgeFill not to loose any data:
    df['AgeFill'] = df['Age']


    #fill it with the median calculated before:
    for i in range(0, 2):
        for j in range(0, 3):
            df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),\
                'AgeFill'] = 1 #median_ages[i,j]


    # print df[ df['Age'].isnull() ][['Gender','Pclass','Age','AgeFill']].head(10)

    #add a column that will tell if the age was missing
    df['AgeMissing'] = pd.isnull(df.Age).astype(int)

    # add FamilySize
    df['FamilySize'] = df['SibSp'] + df['Parch']

    # we know Pclass had a large effect on survival, and it's possible Age will too.
    # Aartificial feature could incorporate whatever predictive power might be available from both Age and Pclass by multiplying them.
    df['Age*Class'] = df.AgeFill * df.Pclass


    #find avarage Fair:
    mean_fare = df['Fare'].mean()
    df['Fare']=df['Fare'].fillna(mean_fare)


    # print df.head()
    # print df.dtypes[df.dtypes.map(lambda x: x=='object')]

    #drop the columns we won't need in Machine Learning algos (string)
    df = df.drop(['Name', 'Sex','Ticket', 'Cabin', 'Embarked'], axis=1)
    df = df.drop(['Age'], axis=1)
    return df



if __name__ == "__main__":
    df = pd.DataFrame.from_csv('../data/train.csv')
    clean_data(df)
