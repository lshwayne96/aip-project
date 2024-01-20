from llama_cpp import Llama

def load_model(
  model_path: str,
  n_ctx: int = 512,
  n_threads: int = None,
) -> Llama:
  model = Llama(
    model_path=model_path,
    n_ctx=n_ctx,
    n_threads=n_threads,
  )
  return model

def infer_model(
  model: Llama, 
  system_message: str, 
  prompt: str, 
  max_tokens: int = 256
):
  prompt = f"<|system|>\n{system_message}</s>\n<|user|>\n{prompt}</s>\n<|assistant|>"
  output = model(
    prompt=prompt,
    max_tokens=max_tokens,
    stop=["</s>"],
    echo=True,
  )
  print(output)
  return output
