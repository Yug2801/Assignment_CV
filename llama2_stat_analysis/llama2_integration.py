from transformers import AutoModelForCausalLM, AutoTokenizer

def load_llama_model(model_name="EleutherAI/gpt-neo-2.7B"):
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        return tokenizer, model
    except EnvironmentError as e:
        print(f"Error loading model or tokenizer: {e}")
        return None, None

def query_llama(prompt, model_name="EleutherAI/gpt-neo-2.7B"):
    tokenizer, model = load_llama_model(model_name)
    if tokenizer is None or model is None:
        return "Model loading failed. Please check the model name and your internet connection."

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Example usage:
# response = query_llama("Provide a detailed analysis of the data.")
# print(response)
