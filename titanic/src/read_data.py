import numpy as np
import csv as csv






csv_file_object = csv.reader(open('../data/train.csv', 'rb'))

header = csv_file_object.next()
data=[]

for row in csv_file_object:
    data.append(row)

data = np.array(data)

number_passenger = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
propotion_survival = number_survived / number_passenger

# print number_passenger
# print number_survived
# print propotion_survival


women_only_stats = data[0::, 4] == 'female'
men_only_stats = data[0::, 4] != 'female'

women_on_board =  data[women_only_stats, 1].astype(np.float)
men_on_board =  data[men_only_stats, 1].astype(np.float)

proprtion_women_survived = np.sum(women_on_board) / np.size(women_on_board)
proprtion_men_survived = np.sum(men_on_board) / np.size(men_on_board)

# print 'proprtion women survived = ', proprtion_women_survived
# print 'proprtion men survived = ', proprtion_men_survived


fare_ceiling = 40
data[ data[0::,9].astype(np.float) >= fare_ceiling, 9 ] = fare_ceiling - 1.0

fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size

number_of_classes = 3
number_of_classes = len(np.unique(data[0::,2]))
survival_table = np.zeros((2, number_of_classes, number_of_price_brackets))



for i in xrange(number_of_classes):       #loop through each class
    for j in xrange(number_of_price_brackets):   #loop through each price bin

        women_only_stats = data[                          \
                         (data[0::,4] == "female")    \
                       &(data[0::,2].astype(np.float) \
                             == i+1) \
                       &(data[0:,9].astype(np.float)  \
                            >= j*fare_bracket_size)   \
                       &(data[0:,9].astype(np.float)  \
                            < (j+1)*fare_bracket_size)\
                          , 1]

        men_only_stats = data[                        \
                         (data[0::,4] != "female")    \
                       &(data[0::,2].astype(np.float) \
                             == i+1)                  \
                       &(data[0:,9].astype(np.float)  \
                            >= j*fare_bracket_size)   \
                       &(data[0:,9].astype(np.float)  \
                            < (j+1)*fare_bracket_size)\
                          , 1]


survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float))
survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float))
survival_table[ survival_table != survival_table ] = 0.


survival_table[ survival_table < 0.5 ] = 0
survival_table[ survival_table >= 0.5 ] = 1

print survival_table
