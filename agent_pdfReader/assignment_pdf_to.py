import pymupdf
import os
import camelot
import pandas as pd

pdf_file_path = './agent_pdfReader/data/04-NTCIR18-HIDDEN-RAD-ChoJ.pdf'

docs = pymupdf.open(pdf_file_path)

full_text = ''

for page in docs:
    text = page.get_text()
    full_text += text

tables = camelot.read_pdf(pdf_file_path, pages='all', flavor='stream')

markdown_tables = []

for i, table in enumerate(tables):
    df = table.df
    markdown = df.to_markdown(index=False)
    markdown_with_title = f"---테이블 {i+1} ---\n" + markdown
    markdown_tables.append(markdown_with_title)

all_tables_text = "\n".join(markdown_tables)

full_text += all_tables_text

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0]

text_file_path = f"./agent_pdfReader/data/{pdf_file_name}.txt"
with open(text_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)
