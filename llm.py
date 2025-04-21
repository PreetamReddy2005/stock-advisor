from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "google/gemma-7b-it"  # or 2b, or whatever size you're using

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Generate a response
input_text = "What's the forecast for AAPL stock?"
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=100)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
