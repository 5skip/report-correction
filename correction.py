from dotenv import load_dotenv
import os
from zundamon import textToVoice
load_dotenv()

import openai
client = openai.OpenAI()

import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text


def correct_report(file, dialect: str | None, human: str | None) -> str:
  
    pdf_text = extract_text_from_pdf(file)
    
    if not dialect and not human:
        return "添削する方言を指定してほしいのだ"
    
    if dialect:
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f'{pdf_text} "このレポートを添削して。返答は{dialect}でよろしく"'}
        ]
        )
        
        return completion.choices[0].message.content.strip()
    
    if human:
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f'{pdf_text} "このレポートを添削して。採点者は{human}でお願い"'}
        ]
        )
        
        return completion.choices[0].message.content.strip()
        

if __name__ == '__main__':
    textToVoice('もちろん、サンプルレポートを添削するのは楽しいわね！それじゃあ、早速見てみるわね。どんな内容なのか教えてくれる？')