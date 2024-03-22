# Desafio para Desenvolvedor Inteligência Artificial

#### Esse projeto consiste em um ChatBot sobre ativos do mercado financeiro em base de informações extraídas de 20 PDFs, onde foi possível fazer com Python por meio ferramentas de Processamento de linguagem natural (NLP).

## Tecnologias Usadas
- Python
- PyTorch
- Keras
- Nltk
- Pandas / Numpy
- PyPDF2
- FastAPI
- Tkinter

## Arquitetura do Projeto
![image](https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA/assets/103287884/c32cc5c2-4280-47aa-bde1-00829c9efef9)

#### **_api_**: Está toda a lógica para fazer a extração, treinamento e o uso do ChatBot.
#### **_extraction_**: Onde a extração das informações dos PDFs está acontecendo.
#### **_robot_**: Onde o treinamento do bot está sendo feito.
#### **_utils_**: Onde está unções auxiliadores dentro de todo o projeto.

## Pré-requisitos
- python 
- python-venv
  
## Instalação e configuração
#### 1. Clone o repositório do GitHub: https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA.git

## Ambiente Windows
#### Crie e configure o ambiente virtual
```
python -m venv venv
```
```
. .\venv\Scripts\activate 
````
```
pip install -r requirements.txt
```

## Ambiente Linux
#### Crie e configure o ambiente virtual
```
python3 -m venv venv
```
```
source .\venv\Scripts\activate 
````
```
pip install -r requirements.txt
```
