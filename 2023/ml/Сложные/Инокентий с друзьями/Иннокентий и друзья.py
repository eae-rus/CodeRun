import os
import numpy as np
import pandas as pd

def main():
    '''
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

    # разделям по городам
    orgs_msk = orgs[orgs['city'] == 'msk']
    orgs_msk = orgs_msk[orgs_msk['rating']>4]
    orgs_spb = orgs[orgs['city'] == 'spb']
    orgs_spb = orgs_spb[orgs_spb['rating']>4]
    
    results = {}
    i = 0
    for user_id in test_users.user_id.values:
        i += 1
        #if i >= 20:
        #    break
        print(i)
        # находим город данного пользователя
        city_user = users.loc[users['user_id'] == user_id].iloc[0]['city']
        restor_user = reviews[reviews['user_id'] == user_id].iloc[:]
        restor_user_by_rating = restor_user[restor_user['rating']>3].iloc[:]['org_id']
        
        if restor_user_by_rating.shape[0] == 0:
            restor_user_by_rating =  restor_user_by_rating_previous
        
        restor_user_by_rating_previous = restor_user_by_rating
        
        rubrics = orgs[orgs['org_id'].isin(restor_user_by_rating)].iloc[:]['rubrics_id']
        
        if city_user == 'msk':
            orgs_spb_rubrics = pd.DataFrame()
            for rubric in rubrics.values:
                for rub in rubric.split(' '):
                    new_orgs = orgs_spb[orgs_spb['rubrics_id'].str.contains(rub)].iloc[:]
                    orgs_spb_rubrics = pd.concat([orgs_spb_rubrics, new_orgs])

            orgs_spb_bill_sorted = orgs_spb_rubrics.sort_values(by='average_bill')
            first_10_orgs = orgs_spb_bill_sorted.head(100)
            results[user_id] = first_10_orgs.loc[:, 'org_id'].values
        else: # spb
            orgs_msk_rubrics = pd.DataFrame()
            for rubric in rubrics.values:
                for rub in rubric.split(' '):
                    new_orgs = orgs_msk[orgs_msk['rubrics_id'].str.contains(rub)].iloc[:]
                    orgs_msk_rubrics = pd.concat([orgs_msk_rubrics, new_orgs])
            
            orgs_msk_bill_sorted = orgs_msk_rubrics.sort_values(by='average_bill')
            first_10_orgs = orgs_msk_bill_sorted.head(100)
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