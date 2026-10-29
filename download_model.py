from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Target the Laya model for download
model_name = "laya" 

print(f"Downloading {model_name} from Hugging Face...")
AutoTokenizer.from_pretrained(model_name)
AutoModelForSequenceClassification.from_pretrained(model_name)
print("Download complete. Model weights are now cached.")