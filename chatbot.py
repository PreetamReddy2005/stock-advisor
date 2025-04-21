from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Replace with your model name or path if using a custom model
model_name = "google/gemma-7b-it"  # Example with GPT-2, change to your Gemma model if necessary

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Chatbot function
def chatbot():
    print("Chatbot is ready to chat! Type 'exit' to end the chat.")
    
    # Start the conversation loop
    while True:
        # Get user input
        user_input = input("You: ")
        
        # If user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Tokenize the input
        inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

        # Generate a response from the model
        with torch.no_grad():
            outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7)

        # Decode the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Display the chatbot's response
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
