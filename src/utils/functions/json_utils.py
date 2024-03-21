import pandas as pd
import json

class JsonUtils:
  def __init__(self):
    pass
  
  def fill_json(self, target_tag: str, list_responses: list):
    with open('intents.json', 'r', encoding='utf-8') as f:
      intents = json.load(f)

    for intent in intents["intents"]:
      if intent['tag'] == target_tag:
        intent['responses'].clear()
        intent['responses'] = list_responses
    
      
    with open('intents.json', 'w', encoding='utf-8') as outfile:
      json.dump(intents, outfile, indent=2, ensure_ascii=False)
  
  
  def append_json(self, object: str, target_tag: str):
    with open('intents.json', 'r', encoding='utf-8') as f:
      intents = json.load(f)

    for intent in intents["intents"]:

      if intent['tag'] == target_tag:
        intent['patterns'] = object['patterns']
        intent['responses'] = object['responses']
        with open('intents.json', 'w', encoding='utf-8') as outfile:
          json.dump(intents, outfile, indent=2, ensure_ascii=False)
        return

    intents['intents'].append({"tag": target_tag,
      "patterns": object['patterns'],
      "responses": object['responses']
    })
    
    with open('intents.json', 'w', encoding='utf-8') as outfile:
      json.dump(intents, outfile, indent=2, ensure_ascii=False)
  
