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


#### **_api_**: Contém a lógica para extração, treinamento e uso do ChatBot.
#### **_extraction_**: Responsável pela extração de informações dos PDFs.
#### **_robot_**: Onde ocorre o treinamento do bot.
#### **_utils_**: Funções auxiliares em todo o projeto.
#### **_interface_**: Interface de integração do sistema.

## Pré-requisitos
- python 
- python-venv (ambiente virtual)
  
## Instalação e configuração
#### 1. Clone o repositório do GitHub: https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA.git

## Ambiente Windows
```
python -m venv venv
. .\venv\Scripts\activate
pip install -r requirements.txt
```

## Ambiente Linux
```
python3 -m venv venv
source .\venv\Scripts\activate
pip install -r requirements.txt
```


## Execução do Projeto

#### Após as configurações de ambiente, você irá rodar o projeto na "main.py" e irá aparecer uma tela inicial para a conversa do ChatBot.
![image](https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA/assets/103287884/44b4f237-b32d-48b6-9266-bfcccb5197f5)

**_OBS_**: O botão "Treinar" realiza a extração, tratamento dos PDFs e treinamento do Bot. Caso deseje treinar o bot novamente, apague o arquivo "output.csv" e limpe o conteúdo de "pdfs_registered". <br> <br>

Após o processo de treinamento e preparação, o ChatBot financeiro está pronto para interagir de forma inteligente e útil. <br>

## Exemplos de entradas:

![image](https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA/assets/103287884/17122dbd-6e38-412f-afb8-188dbe0526bf)





