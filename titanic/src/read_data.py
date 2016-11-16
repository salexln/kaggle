import numpy as np
import csv as csv






csv_file_object = csv.reader(open('../data/train.csv', 'rb'))

header = csv_file_object.next()
data=[]

for row in csv_file_object:
    data.append(row)

data = np.array(data)

# print header
# print data[0]
# print data[1]
# print data[0::,2].astype(np.float)

number_passenger = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
propotion_survival = number_survived / number_passenger

# print number_passenger
# print number_survived
print propotion_survival


women_only_stats = data[0::, 4] == 'female'
men_only_stats = data[0::, 4] != 'female'

women_on_board =  data[women_only_stats, 1].astype(np.float)
men_on_board =  data[men_only_stats, 1].astype(np.float)

proprtion_women_survived = np.sum(women_on_board) / np.size(women_on_board)
proprtion_men_survived = np.sum(men_on_board) / np.size(men_on_board)

print 'proprtion women survived = ', proprtion_women_survived
print 'proprtion men survived = ', proprtion_men_survived
