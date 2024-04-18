import argparse
from .instruct import load_model, infer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, default="Mistral", help="Name of the model or path to the model file")
    parser.add_argument("--temperature", type=float, default=0.5, help="Temperature for sampling")
    parser.add_argument("--max_new_tokens", type=int, default=512, help="Maximum number of new tokens to generate")
    parser.add_argument("--model_kwargs", type=dict, default={"n_gpu_layers":0}, help="Arguments for the model")
    args = parser.parse_args()

    model_path = load_model(args.name)
    infer(model_path, args.temperature, args.max_new_tokens, args.model_kwargs)

if __name__ == "__main__":
    main()
