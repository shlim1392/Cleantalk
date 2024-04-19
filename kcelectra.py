import json
import numpy as np
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch


tokenizer = AutoTokenizer.from_pretrained('beomi/KcELECTRA-base-v2022')
model = AutoModelForTokenClassification.from_pretrained('beomi/KcELECTRA-base-v2022', num_labels=2)
weight_path = 'static/model/model_tag3.pth'
model_weights = torch.load(weight_path)
model.load_state_dict(model_weights)
model.eval()


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def predict(texts):
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=128, return_tensors="pt")
    model.eval()
    inputs = {key: val.to(device) for key, val in encodings.items()}
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)
    return predictions.cpu().numpy()

def replace_sensitive_words(texts, predictions):
    replaced_texts = []
    for text, pred in zip(texts, predictions):
        tokens = tokenizer.tokenize(text)
        tokenized_text = tokenizer.convert_tokens_to_string(tokens)
        words = tokenized_text.split()
        new_words = [word if label != 1 else '*'*len(word) for word, label in zip(words, pred[:len(words)])]
        replaced_text = " ".join(new_words)
        replaced_texts.append(replaced_text)
    return replaced_texts

