import os
import PyPDF2
import json

def extract_text_from_pdf(pdf_path, txt_path):
  """Extrai texto de um arquivo PDF e salva em um arquivo .txt"""
  with open(pdf_path, 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    
    text = ''
    for page in reader.pages:
      text += page.extract_text()
        
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
      txt_file.write(text)

def convert_pdfs_to_txts():
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

def read_file(file_name):
  """Lê o conteúdo de um arquivo .txt"""
  with open(file_name, "r", encoding="utf-8") as file:
    return file.read()

def extract_raw_info(lines):
  """Extrai informações brutas das linhas de texto"""
  raw_info = {}

  for line in lines:
    parts = line.split()
    if "Eritrócitos" in line:
      raw_info["Eritrócitos"] = parts[0]
    elif "Hemoglobina" in line:
      raw_info["Hemoglobina"] = parts[0]
    elif "Hematócrito" in line:
      raw_info["Hematócrito"] = parts[0]
    elif "RDW" in line:
      raw_info["RDW"] = parts[0]
    elif "Leucócitos" in line:
      raw_info["Leucócitos"] = parts[0]
    elif "Neutrófilos" in line:
      raw_info["Neutrófilos"] = parts[0]
    elif "Basófilos" in line:
      raw_info["Basófilos"] = parts[2]
    elif "Eosinófilos" in line:
      raw_info["Eosinófilos"] = parts[2]
    elif "Linfócitos" in line:
      raw_info["Linfócitos"] = parts[2]
    elif "Monócitos" in line:
      raw_info["Monócitos"] = parts[2]
    elif "Plaquetas" in line:
      raw_info["Plaquetas"] = parts[0]

  return raw_info

def extract_info_from_file(file_name):
  """Extrai informações de um arquivo e salva em um novo arquivo na pasta 'infos'"""
  content = read_file(file_name).replace(",", ".")
  raw_info = extract_raw_info(content.splitlines())

  base_file_name = os.path.splitext(os.path.basename(file_name))[0]
  output_file_name = os.path.join("infos", f"{base_file_name}_info.txt")

  if not os.path.exists("infos"):
    os.makedirs("infos")

  with open(output_file_name, "w", encoding="utf-8") as output_file:
    for key, value in raw_info.items():
      output_file.write(f"{key}: {value}\n")

def process_all_txt_files_in_directory(directory_name):
  """Processa todos os arquivos .txt em um diretório"""
  infos_directory = os.path.join(directory_name, "infos")
  if not os.path.exists(infos_directory):
    os.makedirs(infos_directory)

  for file in os.listdir(directory_name):
    if file.endswith(".txt"):
      file_path = os.path.join(directory_name, file)
      extract_info_from_file(file_path)

def convert_txts_to_info():
  directory_name = "texts"
  process_all_txt_files_in_directory(directory_name)

def extract_patient_name(filename):
  """
  Extrai o nome do paciente a partir do nome do arquivo.
  Exemplo: "0067191-LABRF-JOSE-SOUSA-DE-MELO_info.txt" -> "jose sousa de melo"
  """
  base_name = os.path.splitext(filename)[0]
  parts = base_name.split('-')
  patient_name = " ".join(parts[2:]).lower().split("_")[0]
  return patient_name

def convert_content_to_dict(content):
  """
  Converte o conteúdo de um arquivo txt para um dicionário.
  """
  data = {}
  for line in content.strip().split('\n'):
    key, value = line.split(': ')
    data[key] = value
  return data

def process_directory(directory):
  """
  Lê todos os arquivos txt no diretório dado e cria uma estrutura JSON.
  """
  result = {}

  for filename in os.listdir(directory):
    if filename.endswith("_info.txt"):
      filepath = os.path.join(directory, filename)
      with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

      patient_name = extract_patient_name(filename)
      patient_data = convert_content_to_dict(content)
      result[patient_name] = patient_data

  # Salvar o resultado em um arquivo JSON
  with open('result.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, ensure_ascii=False, indent=2)

def convert_infos_to_json():
  directory = 'infos'  # Substitua pelo caminho para os seus arquivos TXT
  process_directory(directory)

if __name__ == "__main__":
  convert_pdfs_to_txts()
  convert_txts_to_info()
  convert_infos_to_json()
  print("All conversions procedures was done.")
