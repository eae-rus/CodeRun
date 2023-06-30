import os
import numpy as np
import pandas as pd

def main():
    '''
    Полезные ссылки
    https://www.kaggle.com/code/midouazerty/restaurant-recommendation-system-using-ml
    '''
    # Считываем данные из файлов
    file_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Инокентий с друзьями\\users.csv'
    users = pd.read_csv(file_path)
    file_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Инокентий с друзьями\\organisations.csv'
    orgs = pd.read_csv(file_path)
    file_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Инокентий с друзьями\\reviews.csv'
    reviews = pd.read_csv(file_path)
    file_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Инокентий с друзьями\\test_users.csv'
    test_users = pd.read_csv(file_path)

    # заполняем NaN
    orgs['average_bill'] = orgs['average_bill'].fillna(1000000)
    orgs['features_id'] = orgs['features_id'].fillna('-1')
    
    count_orgs = reviews['org_id'].value_counts()
    
    count_orgs = count_orgs.sort_values(ascending=False)
    file_path_out = os.path.abspath("") + '\\2023\\ml\\Сложные\\Инокентий с друзьями\\sort_count.csv'
    count_orgs.to_csv(file_path_out)
    
    count_orgs_more_100 = count_orgs[count_orgs.values > 100]
    array_index_more_100 = list(count_orgs_more_100.index)
    
    # разделям по городам
    orgs_more_100 = orgs[orgs['org_id'].isin(array_index_more_100)]
    orgs_more_100['count_reviews'] = [0] * orgs_more_100.shape[0]
    for index in array_index_more_100:
        orgs_more_100.loc[orgs_more_100['org_id'] == index, 'count_reviews'] = count_orgs_more_100[index]
    orgs_msk = orgs_more_100[orgs_more_100['city'] == 'msk']
    orgs_msk = orgs_msk[orgs_msk['rating']>4]
    orgs_msk = orgs_msk.sort_values(by='count_reviews', ascending=False)
    orgs_spb = orgs_more_100[orgs_more_100['city'] == 'spb']
    orgs_spb = orgs_spb[orgs_spb['rating']>4]
    orgs_spb = orgs_spb.sort_values(by='count_reviews', ascending=False)
    
    head = 10
    results = {}
    i = 0
    for user_id in test_users.user_id.values:
        i += 1
        #if i >= 20:
        #    break
        if i % 50:
            print(i)
        # находим город данного пользователя
        city_user = users.loc[users['user_id'] == user_id].iloc[0]['city']
        
        if city_user == 'msk':
            first_10_orgs = orgs_spb.head(head)
            results[user_id] = first_10_orgs.loc[:, 'org_id'].values
        else: # spb
            first_10_orgs = orgs_msk.head(head)
            results[user_id] = first_10_orgs.loc[:, 'org_id'].values
    
    # преобразуем словарь в список кортежей
    data_list = [[key, value] for key, value in results.items()]
    # df = pd.DataFrame(data_list, columns=['user_id', 'target'])
    
    # Сохраняем результаты в файл
    file_path_out = os.path.abspath("") + '\\2023\\ml\\Сложные\\Инокентий с друзьями\\results.txt'
    # df.to_csv(file_path_out)

    with open(file_path_out, "w") as f:
        # Выводим результаты
        i = 0
        print(',user_id,target', file=f)
        for key, value in data_list:
            stroke = str(i) + ',' + str(key) + ',"['
            for item in value:
                stroke += '\'' + str(item) + '\'' + ', '
            stroke = stroke[:-2]
            stroke += ']"'
            print(stroke, file=f)
            i += 1


if __name__ == '__main__':
	main()