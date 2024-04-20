from flask import Flask, request, jsonify
from .instruct import load_model
from llama_index.llms.llama_cpp import LlamaCPP
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, default="127.0.0.1", help="Host on which you wish to run the API server")
parser.add_argument("--port", type=str, default='5000', help="Host on which you wish to run the API server")

app = Flask(__name__)
app.config['DEBUG'] = False

model_files = [f for f in os.listdir('model') if f.endswith('.gguf')]
model_path = load_model(model_files[0])

def generate(model):
    prompt_template = "<s>[INST] {prompt} [/INST]"
    llm = LlamaCPP(
            model_path=model,
            temperature=0.5,
            max_new_tokens=512,
            context_window=3900,
            # model_kwargs=model_kwargs,
            verbose=False,
        )
    return llm

def infer(llm, prompt):
    prompt_template = "<s>[INST] {prompt} [/INST]"
    prompt = prompt_template.format(prompt=prompt)
    response = llm.complete(prompt)
    return str(response)


@app.route('/')
def index():
    return "Welcome to the allmdev API!"

@app.route('/v1/chat/completions', methods=['POST'])
def infer_text():
    data = request.json
    user_input = data.get('user_input')
    
    # Verify if the model is loaded and initialized
    # Assuming load_model() returns the model path if it's loaded and None otherwise
    if model_path is None:
        return jsonify({"error": "Model is not loaded or initialized. Kindly run 'allm-run --name model_name_or_path' to initialize the model"})

    # Perform inference
    llm=generate(model_path)
    response = infer(llm, user_input)
    return jsonify({"response": response})

def main():
    args = parser.parse_args()
    host = args.host
    port = args.port
    print(f"Inference is working on http://{host}:{port}/v1/chat/completions")
    app.run(host=host, port=port)
    


if __name__ == '__main__':
    main()
