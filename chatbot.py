import os
import dotenv
import openai

# Set up the OpenAI API client
dotenv.load_dotenv()
openai.api_key = os.getenv("API_KEY")

# Set up the model to use
model_engine = "text-davinci-002"

def generate_response(prompt):
  # Use the OpenAI API to generate a response
  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  # Get the first response from the list of completions
  message = completions.choices[0].text
  return message

# Test out the chatbot
prompt = "Hello, how are you today?"
response = generate_response(prompt)
print(response)

