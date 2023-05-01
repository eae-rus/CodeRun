import os
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression



def main():
    '''
    '''
    print(os.getcwd())
    train_colums_name = ['feature_' + str(i) for i in range(1, 101)] + ['target']
    test_colums_name = ['feature_' + str(i) for i in range(1, 101)]
    train_df = pd.read_csv('2023\\ml\\Средние\\Разминка\\train.tsv', sep='\t', names=train_colums_name)
    test_df = pd.read_csv('2023\\ml\\Средние\\Разминка\\test.tsv', sep='\t', names=test_colums_name)
    
    x_train = train_df.iloc[:, 0:100]
    y_train = train_df.iloc[:, 100]
    
    x_test = test_df.iloc[:, 0:100]
    x_test.columns = ['feature_' + str(i) for i in range(1, 101)]
    
    lr = LinearRegression().fit(x_train, y_train)
    
    print(lr.score(x_train, y_train))
    
    y_pred = lr.predict(x_test)
    y_pred = np.round(y_pred, decimals=8)
    write_to_submission_file(y_pred, '2023\\ml\\Средние\\Разминка\\answer.csv')
    

# Функция записи в файл
def write_to_submission_file(predicted_labels, out_file):
    predicted_df = pd.DataFrame(predicted_labels)
    predicted_df.to_csv(out_file, index=False, header=False)

if __name__ == '__main__':
	main()