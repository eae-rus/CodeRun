import numpy as np
import os
import json
import re
import pickle
# импортируем модуль
from gensim.models.fasttext import FastText
# для модели
import tensorflow as tf
from tensorflow.keras import layers

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

def extract_vowels(string):
    vowels = re.findall('[аеёиоуыэюя]', string, re.IGNORECASE)
    return ''.join(vowels)

def is_vowel(letter):
    vowels = re.findall('[аеёиоуыэюя]', letter, re.IGNORECASE)
    return len(vowels) > 0

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
        vowel_array = [0 for _ in range(6)] # определено, что максимум 6 глассных в исследуюмых текстах
        for word in target_string:
            if has_uppercase(word):
                vowels_word = extract_vowels(word)
                i = 0
                for vowel in vowels_word:
                    if has_uppercase(vowel):
                        vowel_array[i] = 1
                        train_output.append(vowel_array)
                        break
                    i += 1
        
    # сохарение в файл
    with open(train_input_path, 'wb') as file:
        pickle.dump(train_input, file)
    with open(train_output_path, 'wb') as file:
        pickle.dump(train_output, file)

def test_input_vectors(test_data, fastText_model, test_input_path):
    train_input = []
    # Сохранение обучающего датасета
    index_word = 0
    
    for data in test_data:
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
             
    # сохарение в файл
    with open(test_input_path, 'wb') as file:
        pickle.dump(train_input, file)

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

    # train_data_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train.json'
    # train_data = read_json_file(train_data_path)
    test_data_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\test.json'
    test_data = read_json_file(test_data_path)


    # model_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\model_fastText.bin'
    # создание и сохранение модели
    # train_and_save_fastText(train_data, model_path)

    # Загрузка модели
    # fastText_model = FastText.load(model_path)
  
    # тест выдачи похожих слов
    # word_vector = fastText_model.wv['августА']
    # topn = 100  # Количество наиболее похожих слов
    # similar_words = fastText_model.wv.most_similar([word_vector], topn=topn)
    # print(similar_words)    
    
    # Создание и сохранение массива в файл
    # train_input_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train_input.pickle'
    # train_output_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train_output.pickle'
    # test_input_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\test_input.pickle'
    # train_input_output_vectors(train_data, fastText_model, train_input_path, train_output_path)
    # test_input_vectors(test_data, fastText_model, test_input_path)
    
    # Загрузка массива из файла
    # with open(train_input_path, 'rb') as file:
    #     train_input = pickle.load(file)    
    # with open(train_output_path, 'rb') as file:
    #     train_output = pickle.load(file)
    # with open(test_input_path, 'rb') as file:
    #     test_input = pickle.load(file)
    
    train_input_path_np = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train_input_np.npy'
    train_output_path_np = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train_output_np.npy'
    test_input_path_np = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\test_input_np.npy'
    
    # train_input_np = np.array(train_input)
    # train_input_np = train_input_np.reshape(train_input_np.shape[0], -1)
    # np.save(train_input_path_np, train_input_np)
    train_input_np = np.load(train_input_path_np)
    
    # train_output_np = np.array(train_output)
    # train_output_np = train_output_np.reshape(train_output_np.shape[0], -1)
    # np.save(train_output_path_np, train_output_np)
    train_output_np = np.load(train_output_path_np)
    
    # test_input_np = np.array(test_input)
    # test_input_np = test_input_np.reshape(test_input_np.shape[0], -1)
    # np.save(test_input_path_np, test_input_np)
    test_input_np = np.load(test_input_path_np)
    
    #------------------------------------
    # обучение модели
    model = tf.keras.Sequential([
        layers.Conv1D(512, 100, strides=100, activation='relu', input_shape=(2100, 1)),
        layers.Dropout(0.2),
        layers.Conv1D(64, 3, activation='relu'),
        layers.Dropout(1/16),
        layers.Flatten(),
        layers.Dense(1024, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.1),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.1),
        layers.Dense(32, activation='relu'),
        layers.Dropout(0.1),
        layers.Dense(6, activation='softmax')
    ])
    # Компиляция модели
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Обучение модели
    model.fit(train_input_np, train_output_np, epochs=2, batch_size=256)
    
    answer = []
    for data, test_text in zip(test_input_np, test_data):
        data_test = data.reshape(-1, 1).T
        prediction = model.predict(data_test, verbose=0)
        word_answer = ''
        for word in test_text['source'].split():
            if has_uppercase(word):
                word_answer = word.lower()
                break
        
        index_vowels = np.argmax(prediction) # max_index 
        
        i = 0
        for i_char in range(len(word_answer)):
            if is_vowel(word_answer[i_char]):
                if index_vowels == i:
                    word_answer = word_answer[:i_char] + word_answer[i_char].upper() + word_answer[i_char+1:]
                    break
                else:
                    i += 1
        
        answer.append(word_answer) 
    
    # Сохранение массива в текстовый файл
    answer_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\answer.txt'
    # Открытие файла для записи
    with open(answer_path, "w", encoding="utf-8") as file:
        # Запись каждой строки в файл
        for string in answer:
            file.write(string + "\n")

    # neyro_model_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\neyro_model'


if __name__ == '__main__':
    main()