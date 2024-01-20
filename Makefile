model:
	huggingface-cli download TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False

dev:
	uvicorn main:app --reload

build:
	docker build . -f Dockerfile -t aip-project:1.0.0

run:
	docker compose up -d