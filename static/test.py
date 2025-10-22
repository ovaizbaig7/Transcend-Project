from gpt4all import GPT4All

model = GPT4All(
    model_name="mistral-7b-instruct-v0.1.Q4_0.gguf",
    model_path="models",
    allow_download=False
)

with model.chat_session():
    response = model.generate("What's the capital of Germany?")
    print(response)
