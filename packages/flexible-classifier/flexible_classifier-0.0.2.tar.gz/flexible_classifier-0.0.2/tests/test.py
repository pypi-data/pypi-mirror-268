from flexible_classifier import classifier
import pandas as pd

salaries = pd.read_csv('./data/ds_salaries.csv')
model = classifier.process_data('./data/ds_salaries.csv', 'experience_level')

# customers1 = pd.read_csv('./data/Train.csv', index_col='ID')
# customers2 = pd.read_csv('./data/Test.csv', index_col='ID')
# customers = pd.concat([customers1, customers2])
# classifier.process_data(customers, 'Segmentation')

# to use in classifier file 
# salaries = pd.read_csv('../../tests/data/ds_salaries.csv')
# process_data('../../tests/data/ds_salaries.csv', 'experience_level')

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

salaries = pd.read_csv('../../tests/data/ds_salaries.csv')
train, test = train_test_split(salaries, test_size=0.2)
model = process_data(train, 'experience_level')
y_true = test['experience_level']
y_pred = model.predict(test.drop(['experience_level'], axis='columns'))
print(accuracy_score(y_true, y_pred))