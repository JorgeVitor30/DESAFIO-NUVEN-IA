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

## Implementação do Projeto
### *Extração das informações*: Usei a biblioteca PyPDF2, muito conhecida para esse tipo de solução proposto no desafio e implementei a raspagem das informações com REGEX junto de outras técnicas auxiliadoras.
### *Treinamento do Bot*: Na parte do treinamento do modelo pro ChatBot usei bibliotecas como PyTorch (torch) , nltk e keras para que o treinamento seja feito de forma correta, implementei em base de documentações, artigos no medium e vídeos sobre o assunto.

### Referências: 
https://www.nltk.org <br> <br>
https://medium.com/luizalabs/como-criar-um-chatbot-usando-aprendizado-profundo-e-python-47821402367 <br> <br>
https://www.youtube.com/watch?v=1lwddP0KUEg&t=506s <br> <br>
https://www.youtube.com/watch?v=RpWeNzfSUHw&t=1106s 



## Arquitetura do Projeto
![image](https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA/assets/103287884/a47ef6ac-41e9-4587-810d-134b251755bc)


#### **_api_** : Contém a lógica para extração, treinamento e uso do ChatBot.
#### **_extraction_**: Responsável pela extração de informações dos PDFs.
#### **_robot_**: Onde ocorre o treinamento do bot.
#### **_utils_**: Funções e Arquivos auxiliares em todo o projeto.
#### **_interface_**: Interface de integração do sistema. <br> <br>

## Arquivos Importantes
#### **_output.csv_**: Arquivo csv com as informações extraídas dos PDFs.
#### **_talking_bot.txt_**: Arquivo txt do diálogo do Usuário com o Bot.
#### **_pdfs_registered.txt_**: Arquivo txt com o nome de todos os PDFs que foram extraídos. <br> <br>


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
source ./venv/bin/activate
pip install -r requirements.txt
```


## Execução do Projeto

#### Após as configurações de ambiente, você irá rodar o projeto na "main.py" e irá aparecer uma tela inicial para a conversa do ChatBot.
![image](https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA/assets/103287884/44b4f237-b32d-48b6-9266-bfcccb5197f5)

**_OBS_**: O botão "Treinar" realiza a extração, tratamento dos PDFs e treinamento do Bot. Caso deseje treinar o bot novamente, apague o arquivo "output.csv" e limpe o conteúdo de "pdfs_registered". <br> <br>

Após o processo de treinamento e preparação, o ChatBot financeiro está pronto para interagir de forma inteligente e útil. <br>

## Exemplos de entradas:

![image](https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA/assets/103287884/17122dbd-6e38-412f-afb8-188dbe0526bf)


## Exemplo de interação:
![image](https://github.com/JorgeVitor30/DESAFIO-NUVEN-IA/assets/103287884/d7829709-3539-47ac-b9d6-aec4380acedf)




