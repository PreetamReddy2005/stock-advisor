import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model + tokenizer once
model_name = "google/gemma-2b-it"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,  # CPU-friendly
    device_map="auto"
)

# LLM response function
def get_llm_response(stock_name: str, stock_price: float) -> str:
    prompt = f"The latest price for {stock_name.upper()} is ${stock_price:.2f}. What is your analysis or advice?"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
