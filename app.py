from fastapi import FastAPI
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from pydantic import BaseModel

app = FastAPI()
model_name = "laya"

# Load the model and tokenizer from the local cache 
# (These will be pre-downloaded by download_model.py during the Docker build)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

class RequestBody(BaseModel):
    text: str

@app.post("/predict")
def predict(payload: RequestBody):
    # Tokenize the input text
    inputs = tokenizer(payload.text, return_tensors="pt")
    
    # Run the model inference
    outputs = model(**inputs)
    
    # Return the classification logits
    return {
        "status": "success", 
        "logits": outputs.logits.tolist()
    }