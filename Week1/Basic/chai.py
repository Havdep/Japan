# from basic01 import chai

# chai(5)
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()


response = client.responses.create(
    model="gpt-4.1-nano-2025-04-14",
    input="Write a one-sentence story about tokyo."
)

print(response.output_text)