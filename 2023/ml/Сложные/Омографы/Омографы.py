import numpy as np
import os
import json
import re
import pickle
# импортируем модуль
from gensim.models.fasttext import FastText

def train_and_save_fastText(train_data, model_path):
    # создание массива
    train_data_list = []
    # max_len = 0 # итоговое значение 291, будем брать +-10 слов
    for data in train_data:
        train_data_list.append(data['source'].split())
        # max_len = max(max_len, len(data['source'].split()))
        
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
    index_word = 0
    
    for data in train_data:
        index_word += 1
        if index_word % 10000 == 0:
            print(index_word)
        
        # Извлекаем строку из JSON
        source_string = data['source'].split()
        # предварительная обработка source
        i = 0
        for word in source_string:
            if has_uppercase(word):
                index_up_word = i
                break
            i += 1
        temp = []
        # до
        if index_up_word < 10:
            for _ in range(10 - index_up_word):
                temp.append(".")
            for sourse_word in source_string[:index_up_word]:
                temp.append(sourse_word)
        else:
            for sourse_word in source_string[index_up_word - 10 :index_up_word]:
                temp.append(sourse_word)
        # слово
        temp.append(source_string[index_up_word])
        # после
        if index_up_word == len(source_string)-1:
            for _ in range(10):
                temp.append(".")
        elif (index_up_word+10) - (len(source_string)-1) > 0:
            for sourse_word in source_string[index_up_word+1:]:
                temp.append(sourse_word)
            for _ in range((index_up_word+10) - (len(source_string)-1)):
                temp.append(".")
        else:
            for sourse_word in source_string[index_up_word + 1 : index_up_word + 11]:
                temp.append(sourse_word)
        
        source_string = temp
        vectorizer_array = []
        for word in source_string:
            vectorizer = fastText_model.wv[word]
            vectorizer_array.append(vectorizer)
        train_input.append(vectorizer_array)
        
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

def train_and_save_model(train_input, train_output, model_path):
    pass

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
  
    # тест выдачи похожих слов
    # word_vector = fastText_model.wv['августА']
    # topn = 100  # Количество наиболее похожих слов
    # similar_words = fastText_model.wv.most_similar([word_vector], topn=topn)
    # print(similar_words)    
    
    # Создание и сохранение массива в файл
    # train_input_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train_input.pickle'
    # train_output_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train_output.pickle'
    # train_input_output_vectors(train_data, fastText_model, train_input_path, train_output_path)
    
    # Загрузка массива из файла
    # with open(train_input_path, 'rb') as file:
    #     train_input = pickle.load(file)    
    # with open(train_output_path, 'rb') as file:
    #     train_output = pickle.load(file)
    
    train_input_path_np = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train_input_np'
    train_output_path_np = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train_output_np'
    
    # train_input_np = np.array(train_input)
    # train_input_np = train_input_np.reshape(train_input_np.shape[0], -1)
    # np.save(train_input_path_np, train_input_np)
    train_input_np = np.load(train_input_path_np)
    
    # train_output_np = np.array(train_output)
    # train_output_np = train_output_np.reshape(train_output_np.shape[0], -1)
    # np.save(train_output_path_np, train_output_np)
    train_output_np = np.load(train_output_path_np)
    
    model_SimpleRNN_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\model_SimpleRNN_path.h5'
    # В разработке
    # train_and_save_model(train_input, train_output, model_SimpleRNN_path)

    # Загрузка модели
    # model_SimpleRNN = load_model(model_SimpleRNN)
    
    for data in test_data:
        # Извлекаем строку из JSON
        source_string = data['source'].split()
        vectorizer_array = []
        for word in source_string:
            vectorizer = fastText_model.wv[word]
            vectorizer_array.append(vectorizer)
        input.append(vectorizer_array)
        
        target_string = data['target'].split()
        target_vector = ""
        for word in target_string:
            if has_uppercase(word):
                target_vector = fastText_model.wv[word]
                break
        
        similar_words = fastText_model.wv.most_similar([target_vector], topn=10)
        print(similar_words)
        
        output_vector = model_SimpleRNN.predict(input)

        
        
        
        # выводим результат для ручной оценки
        print(source_string)
    


if __name__ == '__main__':
    main()