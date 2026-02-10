from transformers import AutoTokenizer, AutoModel
import torch

model_name = "google/embeddinggemma-300m"

# Токенизатор - превращает текст в вектор чисел чтобы модель могла его обработать
tokenizer = AutoTokenizer.from_pretrained(model_name) 
model = AutoModel.from_pretrained(model_name)

texts = [
    "Я изучаю Машинное обучение, FastAPI, и ИИ.",
    "Я люблю играть в футбол и слушать музыку.",
    "Мой любимый цвет - красный.",
]

inputs = tokenizer(
    texts,
    padding=True,
    truncation=True,
    return_tensors="pt"
)

with torch.no_grad():
    outputs = model(**inputs)

embeddings = outputs.last_hidden_state[:, 0, :]
print(embeddings)

#Вывод: 
#tensor([[ 3.5269, -0.8535, -2.9115,  ..., -0.9560, -0.3822,  0.3549],
#        [ 1.3885,  0.8870, -2.7590,  ..., -3.2523,  0.2522,  1.2952],
#        [ 3.0982,  1.4795, -3.2142,  ..., -3.2998, -0.5610,  1.8693]])


