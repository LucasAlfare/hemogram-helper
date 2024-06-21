# Auto-Hemogramas

Projeto para me ajudar.

A ideia é basicamente obter as informações relevantes de um arquivo PDF que contenha um laudo de hemograma em TEXTO para preencher os campos de texto automaticamente em uma página da internet do sistema de gerenciamento de laboratório de onde trabalho.

Esse procedimento é feito em algumas etapas, desde a extração do texto bruto do arquivo PDF até à interação com a página da internet do paciente em questão.

Para digitar os resultados de um paciente em sua sub página, basta apertar a tecla "F" do teclado. Se esse programa conseguir encontrar um registro para o paciente atual, ele digitará tudo. Se não encontrar, não digitará, mostrará apenas um alerta.

Por fim, foi escolhida a abordagem de criar uma "extensão" de navegador para esse trabalho. A extensão é ativada após serem feitos as etapas descritas logo mais a frente, o que ajuda muito.

# Inicialização

Para fazer o projeto funcionar, verifique os seguintes passos:

1. Caso seja a primeira vez executando, execute o comando `pip install -r requirements.txt` para instalar as dependências externas que este projeto precisa para funcionar;
2. Certifique-se de mover todos os PDFs desejados para uma pasta "`pdfs`";
3. Execute o script `main.py`;
4. Aguarde a finalização do procedimento;
5. Copie o conteúdo do arquivo resultante `result.json` para uma constante javascript `const data = {}` em um arquivo chamado `data.js`;
6. Certifique-se que o arquivo `data.js` esteja dentro da pasta `/my_ext`;
7. Adicione esse projeto como extensão do navegador Google Chrome;
   1. Navegue até o menu/página de extenções do navegador;
   2. Habilite o modo de desenvolvedor;
   3. Procure pelo botão de adicionar extensão descompactada;
   4. Navegue até a pasta `/my_ext` deste projeto e selecione.

Ao fazer cumprir esses passos você estará apto a digitar de forma semi-automatizada os resultados dos laudos de hemograma da página HTML que estiver em foco.