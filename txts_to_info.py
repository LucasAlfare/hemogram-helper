import os

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

if __name__ == "__main__":
    directory_name = "texts"
    process_all_txt_files_in_directory(directory_name)
