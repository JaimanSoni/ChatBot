import pathlib
import textwrap
import google.generativeai as genai
from backend.settings import GOOGLE_API_KEY

# Used to securely store your API key
# from google.colab import userdata

from IPython.display import display, display_markdown
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '\n')
  # return Markdown(textwrap.indent(text, '\n ', predicate=lambda _: True))
  return text

# GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

def response(message):
  model = genai.GenerativeModel('gemini-pro')

  response = model.generate_content(message)
  response = response.text
  response = response.replace("*", "")
  return response
  # return 