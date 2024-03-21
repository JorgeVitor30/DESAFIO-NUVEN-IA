import random
import json
from time import sleep

import torch

from src.robot.model import NeuralNet
from src.robot.nltk_utils import bag_of_words, tokenize
from src.utils.functions.open_txt import write_talking_txt


def chat_bot(sentence: str):

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open('intents.json', 'r', encoding='utf-8') as json_data:
        intents = json.load(json_data)

    FILE = "data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    bot_name = " Bot assistente"

    write_talking_txt("Usuário", sentence)

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() >= 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                sleep(0.5)
                answer = random.choice(intent['responses'])
                print(f"{bot_name}: {answer}")
                write_talking_txt("ChatBot", answer)
                return {"Chatbot": answer}
    else:
        write_talking_txt("ChatBot", "Não entendi a pergunta... pode reformular?")
        raise Exception("Não entendi a pergunta... pode reformular?")
           