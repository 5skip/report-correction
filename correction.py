from dotenv import load_dotenv
import os
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


def correct_report(file, dialect: str, human) -> str:
  
    pdf_text = extract_text_from_pdf(file)
    
    if dialect:
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f'{pdf_text} "このレポートを添削して。返答は{dialect}でよろしく"'}
        ]
        )
        
    elif human:
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f'{pdf_text} "このレポートを添削して。添削者は{human}なひとでお願い"'}
        ]
        )
    
    return completion.choices[0].message.content.strip()