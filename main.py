from fastapi import FastAPI
from pydantic import BaseModel
from model import load_model, infer_model
import os

MODEL_PATH = os.environ.get("MODEL_PATH", "./tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf")
N_CTX = int(os.environ.get("N_CTX", 2048))
N_THREADS = int(os.environ.get("N_THREADS", 8))

app = FastAPI()
model = load_model(
  model_path=MODEL_PATH, 
  n_ctx=N_CTX,
  n_threads=N_THREADS,
)

class InferenceInput(BaseModel):
  system_message: str
  prompt: str
  max_tokens: int

@app.get("/")
async def read_root():
  return {
    "message": "Welcome to my app!",
  }

@app.get("/health")
async def health_check():
  return {
    "status": "OK",
  }

@app.post("/infer")
async def infer(input:InferenceInput):
  print(f"Received request:\n{input}")
  output = infer_model(
    model=model,
    system_message=input.system_message,
    prompt=input.prompt,
    max_tokens=input.max_tokens,
  )
  return {
    "output": output
  }
