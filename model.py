from llama_cpp import Llama

def load_model(
  model_path: str = "./tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", 
  n_ctx: int = 2048, 
  n_threads: int = 8
) -> Llama:
  model = Llama(
    model_path=model_path, # Download the model file first
    n_ctx=n_ctx,           # The max sequence length to use - note that longer sequence lengths require much more resources
    n_threads=n_threads,   # The number of CPU threads to use, tailor to your system and the resulting performance
    n_gpu_layers=0         # The number of layers to offload to GPU, if you have GPU acceleration available
  )
  return model

def infer_model(
  model: Llama, 
  system_message: str, 
  prompt: str, 
  max_tokens: int = 512
):
  prompt = f"<|system|>\n{system_message}</s>\n<|user|>\n{prompt}</s>\n<|assistant|>"
  output = model(
    prompt=prompt,         # Prompt
    max_tokens=max_tokens, # Generate up to 512 tokens
    stop=["</s>"],         # Example stop token - not necessarily correct for this specific model! Please check before using.
    echo=True             # Whether to echo the prompt
  )
  print(output)
  return output

# Chat Completion API

# llm = Llama(model_path="./tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", chat_format="llama-2")  # Set chat_format according to the model you are using
# llm.create_chat_completion(
#     messages = [
#         {"role": "system", "content": "You are a story writing assistant."},
#         {
#             "role": "user",
#             "content": "Write a story about llamas."
#         }
#     ]
# )