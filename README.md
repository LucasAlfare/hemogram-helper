# Auto-Hemogramas

Projeto para me ajudar.

# Passos
1. Mover novos PDFs
- Certifique-se de que todos os novos laudos estão na pasta pdfs.
2. Excluir Pastas Antigas
- Delete as pastas antigas infos e texts.
3. Executar Script de Conversão de PDFs para Textos
- Execute o script `pdfs_to_txts.py`:
```sh
python pdfs_to_txts.py
```
4. Executar Script de Extração de Informações dos Textos
- Execute o script `txts_to_info.py`:
```sh
python txts_to_info.py
```
5. Executar Script de Conversão de Informações para JSON
- Execute o script `info_to_json.py`:
```sh
python info_to_json.py
```
6. Atualizar o Arquivo JavaScript com o Novo JSON
- Cole o JSON resultante na constante `data` do arquivo `/my_ext/data.js`.