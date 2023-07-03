import os
import json
import pymorphy2

def main():
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
    
    # Сохранение данных JSON в файл "txt"
    # save_train_data_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\train.txt'
    # save_json_as_txt(train_data, save_train_data_path)
    # save_test_data_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Омографы\\test.txt'
    # save_json_as_txt(test_data, save_test_data_path)
    pass

if __name__ == '__main__':
    main()