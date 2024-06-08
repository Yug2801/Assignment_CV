from transformers import AutoModelForCausalLM, AutoTokenizer

# Decorator for caching the loaded model to improve performance
@st.cache(allow_output_mutation=True)
def load_llama_model(model_name="distilgpt2"):
    try:
        # Loading the tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        return tokenizer, model
    except EnvironmentError as e:
        # Handling errors
        print(f"Error loading model or tokenizer: {e}")
        return None, None

def query_llama(prompt, model_name="distilgpt2", max_length=200, max_new_tokens=50, do_sample=True, temperature=0.7, top_p=0.9):
    # Loading the tokenizer and model
    tokenizer, model = load_llama_model(model_name)
    if tokenizer is None or model is None:
        return "Model loading failed."

    # Tokenizing the prompt and preparing it for model input
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=True, temperature=temperature, top_p=top_p)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
