import os
import json
import re
# импортируем модуль
from gensim.models.fasttext import FastText
import gensim.downloader as download_api

import transformers
#print(transformers.__version__)

def train_and_save_fastText(train_data, model_path):
    # создание массива
    train_data_list = []
    for data in train_data:
        train_data_list.append(data['target'].split())

    # Обучим модели fastText
    fastText_model = FastText(train_data_list)
    # Сохраним модель в файл
    fastText_model.save(model_path)
    


def main():
    '''
    '''
    def read_json_file(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    
    def save_json_as_txt(data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False, separators=(',', ': '))

    train_data_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train.json'
    train_data = read_json_file(train_data_path)
    test_data_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\test.json'
    test_data = read_json_file(test_data_path)


    model_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\model_fastText.bin'
    # создание и сохранение модели
    # train_and_save_fastText(train_data, model_path)

    # Загрузка модели
    fastText_model = FastText.load(model_path)
    vectorizer = fastText_model.wv['АДОНИС']
    print(vectorizer)
    
    for data in test_data:
        # Извлекаем строку из JSON
        source_string = data['source'].replace('%', '%%')
        # Используем регулярное выражение для поиска слова с заглавной буквой
        match = re.search(r'\b\w*[А-Я]\w*\b', source_string)
        # Извлекаем слово
        word_with_capital = match.group(0)
        # переводим слово и предложение в нижний регистр
        lowercase_word = word_with_capital.lower()
        # ставим ударения с контекстом
        source_string_lower = source_string.lower() 

        
        
        
        # выводим результат для ручной оценки
        print(source_string)
    
    pass

if __name__ == '__main__':
    main()