wrongpoint=[]
from dotenv import load_dotenv
import os
load_dotenv()

import openai
from openai import OpenAI
client = OpenAI()

import fitz  # PyMuPDF
import openai

# OpenAI APIキーの設定
openai.api_key = 'your-api-key'

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # または最新のモデル
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

pdf_path = "C:\\Users\\kosuk\\OneDrive\\Desktop\\勉強関係\\課題\\物理化学\\1025368319MonExp1-坂倉光祐.pdf"
pdf_text = extract_text_from_pdf(pdf_path)





completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    
    {"role": "user", "content": f'{pdf_text} "このレポートを添削して。返答は関西弁でよろしく"'}
  ]
)

print(completion.choices[0].message.content.strip())
