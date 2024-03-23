import numpy as np
import json

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from src.robot.nltk_utils import bag_of_words, tokenize, stem
from src.robot.model import NeuralNet
from src.robot.data_set import ChatDataset


def train_bot():
    """
    De fato onde as libs de Treinamento do Bot estão sendo chamadas.
    -> Cria o arquivo "data.pth" com os dados do treinamento.
    """

    with open('intents.json', 'r', encoding='utf-8') as f:
        intents = json.load(f)

    all_words = []
    tags = []
    xy = []

    for intent in intents['intents']:
        tag = intent['tag']

        tags.append(tag)
        for pattern in intent['patterns']:
            w = tokenize(pattern.lower())
            all_words.extend(w)

            xy.append((w, tag))


    ignore_words = ['?', '.', '!', ',', ')', '(', 'eu', 'você', 'ele', 'ela', 'nós', 'eles', 'delas', 'deles', 'seu', 'sua', 'seus', 'suas', 'meu', 'minha', 'meus', 'minhas', 'seu', 'sua', 'seus', 'suas', 'este', 'esta', 'isto', 'isso','aquele', 'aquela', 'aquilo', 'lá', 'aqui', 'ali', 'lá', 'então', 'também', 'ainda', 'apenas', 'até', 'tanto', 'tudo', 'todos', 'todas', 'todo', 'toda','qualquer', 'nenhum', 'nenhuma', 'cada', 'outro', 'outra', 'outros', 'outras', 'certo', 'errado','fazer', 'fazerem', 'feito', 'fazer', 'fazendo', 'fez', 'faz', 'fazer', 'fazerem', 'fazia','feita', 'feitas', 'feitos', 'fez', 'faz', 'por', 'para', 'entre', 'além','após', 'antes', 'enquanto', 'durante', 'depois', 'então', 'depois', 'logo', 'agora', 'sempre', 'nunca', 'às vezes', 'muitas vezes', 'raramente', 'geralmente', 'frequentemente', 'porém', 'a','contudo', 'todavia', 'assim', 'por que', 'porque', 'porquê', 'porquanto', 'portanto','logo', 'ou', 'mas', 'nem', 'que', 'se', 'como', 'quando', 'onde', 'quem', 'o que', 'que', 'qual', 'quanto', 'quão', 'quando', 'onde', 'quanto', 'como', 'seja', 'seja', 'estou', 'está']

    all_words = [stem(w) for w in all_words if w not in ignore_words]

    all_words = sorted(set(all_words))
    tags = sorted(set(tags))

    print(len(xy), "patterns")
    print(len(tags), "tags:", tags)
    print(len(all_words), "unique stemmed words:", all_words)

    X_train = []
    y_train = []
    for (pattern_sentence, tag) in xy:
        
        bag = bag_of_words(pattern_sentence, all_words)
        X_train.append(bag)
        
        label = tags.index(tag)
        y_train.append(label)

    X_train = np.array(X_train)
    y_train = np.array(y_train)


    num_epochs = 1000
    batch_size = 8
    learning_rate = 0.001
    input_size = len(X_train[0])
    hidden_size = 8
    output_size = len(tags)
    print(input_size, output_size)
    

    dataset = ChatDataset(X_train, y_train)
    train_loader = DataLoader(dataset=dataset,
                                batch_size=batch_size,
                                shuffle=True,
                                num_workers=0)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model = NeuralNet(input_size, hidden_size, output_size).to(device)


    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


    for epoch in range(num_epochs):
        for (words, labels) in train_loader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)
            
            
            outputs = model(words)
            
            loss = criterion(outputs, labels)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
        if (epoch+1) % 100 == 0:
            print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


    print(f'final loss: {loss.item():.4f}')

    data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "hidden_size": hidden_size,
    "output_size": output_size,
    "all_words": all_words,
    "tags": tags
    }

    FILE = "data.pth"
    torch.save(data, FILE)

    print(f'training complete. file saved to {FILE}')