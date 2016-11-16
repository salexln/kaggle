import csv as csv


test_file_object = csv.reader(open('../data/test.csv', 'rb'))
header = test_file_object.next()



prediction_file_object = csv.writer(open('../results/gender_based_model.csv', 'wb'))

prediction_file_object.writerow(['PassengerId', 'Survived'])


for row in test_file_object:
    survived = 0
    if row[3] == 'female':
        survived = 1

    prediction_file_object.writerow([row[0], survived])
