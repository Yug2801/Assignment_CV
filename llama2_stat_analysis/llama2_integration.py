from transformers import AutoModelForCausalLM, AutoTokenizer

def load_llama_model(model_name="distilgpt2"):
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        return tokenizer, model
    except EnvironmentError as e:
        print(f"Error loading model or tokenizer: {e}")
        return None, None

def query_llama(prompt, model_name="distilgpt2", max_length=200, max_new_tokens=50,do_sample=True, temperature=0.7, top_p=0.9 ):
    tokenizer, model = load_llama_model(model_name)
    if tokenizer is None or model is None:
        return "Model loading failed. Please check the model name and your internet connection."

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=True, temperature=temperature, top_p=top_p)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Example usage:
# response = query_llama("Provide a detailed analysis of the data.")
# print(response)
