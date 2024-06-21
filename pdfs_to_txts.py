import os
import PyPDF2

def extract_text_from_pdf(pdf_path, txt_path):
    """Extrai texto de um arquivo PDF e salva em um arquivo .txt"""
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        text = ''
        for page in reader.pages:
            text += page.extract_text()
            
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

def main():
    pdf_directory = 'pdfs'
    txt_directory = 'texts'
    
    if not os.path.exists(txt_directory):
        os.makedirs(txt_directory)
    
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, filename)
            txt_path = os.path.join(txt_directory, os.path.splitext(filename)[0] + '.txt')
            
            extract_text_from_pdf(pdf_path, txt_path)
            print(f'Text extracted from {filename} and saved to {os.path.basename(txt_path)}')

if __name__ == "__main__":
    main()
