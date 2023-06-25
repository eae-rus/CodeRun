import os

import torch
import numpy as np
from sklearn.decomposition import PCA
import clip

from PIL import Image
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def main():
    '''
    Установка https://github.com/openai/CLIP#usage
    Источник https://questu.ru/articles/18747/
    '''
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)
    
    # Предварительная обработка изображений
    image_folder = os.path.abspath("") + '\\2023\\ml\\Сложные\\Звёздные карты 2.0\\dataset'
    features = []

    for filename in os.listdir(image_folder):
        if filename.endswith('.png'):
            image = Image.open(os.path.join(image_folder, filename))
            image = preprocess(image).unsqueeze(0).to(device)
            with torch.no_grad():
                image_features = model.encode_image(image)
            features.append(image_features.detach().cpu().numpy())

    # Снижаем размерность данных
    pca = PCA(n_components=100)  # оставляем только 100 главных компонент
    images_pca = pca.fit_transform(np.array(features).squeeze())

    # Кластеризуем данные
    kmeans = KMeans(n_clusters=983, random_state=42)  # число кластеров равно числу классов
    labels = kmeans.fit_predict(images_pca)
    
    file_path_out = os.path.abspath("") + '\\2023\\ml\\Сложные\\Звёздные карты 2.0\\out.txt'
    with open(file_path_out, "w") as f:
        # Выводим результаты
        for label in labels:
            print(label, file=f)

if __name__ == '__main__':
	main()