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
![image](https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA/assets/103287884/a47ef6ac-41e9-4587-810d-134b251755bc)


#### **_api_**: Está toda a lógica para fazer a extração, treinamento e o uso do ChatBot.
#### **_extraction_**: Onde a extração das informações dos PDFs está acontecendo.
#### **_robot_**: Onde o treinamento do bot está sendo feito.
#### **_utils_**: Onde está funções auxiliadores dentro de todo o projeto.
#### **_interface_**: Onde está a intarface de integração do sistema.

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

## Execução do Projeto

#### Após as configurações de ambiente, você irá rodar o projeto na "main.py" e irá aparecer uma tela inicial para a conversa do ChatBot.
![image](https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA/assets/103287884/44b4f237-b32d-48b6-9266-bfcccb5197f5)

**_OBS_**: O botão "Treinar" é para executar todo o processo de extração/tratamento dos pdf e o treinamento para o Bot. <br> <br>
**_Caso queira treinar o bot: Apagar o arquivo "output.csv" e limpar o conteúdo do arquivo "pdfs_registered"_**



