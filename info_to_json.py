import os
import json

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

if __name__ == "__main__":
    directory = 'infos'  # Substitua pelo caminho para os seus arquivos TXT
    process_directory(directory)
