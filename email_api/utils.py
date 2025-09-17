import torch
from torch import nn
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import Tuple



# load the model and tokenizer from huggingface
model_uri = "muyiiwaa/email-classifier"
model = AutoModelForSequenceClassification.from_pretrained(model_uri)
tokenizer = AutoTokenizer.from_pretrained(model_uri)
softmax = nn.Softmax(dim=1)
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# define a function for preprocessing and tokenizing the input_data

def tokenize_text(text: str) -> dict:
    output = tokenizer(
        text = text,
        padding = 'max_length',
        truncation = True,
        return_tensors = 'pt'
    )
    return output

def predict(email_text: str, model = model) -> Tuple[float,str]:
    output_text = tokenize_text(text=email_text)
    model = model.to(device)
    output = model(**output_text)
    logits = output.logits
    probs, preds = torch.max(softmax(logits), 1)
    probs = round(probs.item(), 4) * 100
    classes = ['real email', 'junk email']
    
    return probs, classes[preds]
    



if __name__ == "__main__":
    sample_email = input("enter email: ")
    print(predict(email_text=sample_email))
    
