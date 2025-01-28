
import requests as re
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from bs4 import BeautifulSoup
os.environ["GOOGLE_API_KEY"] = "SUACHAVEAPIDOGEMINI"
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)
prompt = [
    ("system","voce resume conceitos")
]
resposta = re.get('https://pt.wikipedia.org/wiki/Aprendizado_de_máquina')

soup = BeautifulSoup(resposta.content, 'html.parser')

title = str(soup.find(id="firstHeading"))
prompt.append(("human", title))
ai_msg = llm.invoke(prompt)
response_text = ai_msg.content
print(response_text)
