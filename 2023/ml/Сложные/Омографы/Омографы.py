import os
import json
import re
import pickle
# импортируем модуль
from gensim.models.fasttext import FastText

def train_and_save_fastText(train_data, model_path):
    # создание массива
    train_data_list = []
    for data in train_data:
        train_data_list.append(data['source'].split())
        
    for data in train_data:
        train_data_list.append(data['target'].split())

    # Обучим модели fastText
    fastText_model = FastText(train_data_list)
    # Сохраним модель в файл
    fastText_model.save(model_path)
    
def train_input_output_vectors(train_data, fastText_model, train_input_path, train_output_path):
    train_input = []
    train_output = []
    # Сохранение обучающего датасета
    for data in train_data:
        # Извлекаем строку из JSON
        source_string = data['source'].split()
        for word in source_string:
            vectorizer = fastText_model.wv[word]
            train_input.append(vectorizer)
        
        target_string = data['target'].split()
        for word in target_string:
            if has_uppercase(word):
                vectorizer = fastText_model.wv[word]
                train_output.append(vectorizer)
                break
        
    # сохарение в файл
    with open(train_input_path, 'wb') as file:
        pickle.dump(train_input, file)
    with open(train_output_path, 'wb') as file:
        pickle.dump(train_output, file)
    
def has_uppercase(array):
    for element in array:
        if any(char.isupper() for char in element):
            return True
    return False

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
    # vectorizer = fastText_model.wv['АДОНИС']
    # print(vectorizer)
    
    # Создание и сохранение массива в файл
    train_input_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train_input.pickle'
    train_output_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train_output.pickle'
    # train_input_output_vectors(train_data, fastText_model, train_input_path, train_output_path)
    
    # Загрузка массива из файла
    with open(train_input_path, 'rb') as file:
        train_input = pickle.load(file)    
    with open(train_output_path, 'rb') as file:
        train_output = pickle.load(file)
    

    
    
    for data in test_data:
        # Извлекаем строку из JSON
        source_string = data['source']
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
    


if __name__ == '__main__':
    main()