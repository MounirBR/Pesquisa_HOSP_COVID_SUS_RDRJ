# Pesquisa_HOSP_COVID_SUS_RDRJ
Pesquisa por CIDs de doenças respiratórias em arquivos de internações hospitalares pagas com extensão .DBF

Para usar este script é necessário usar a biblioteca simpleDBF, para mais informações de como instalar, usar e distribuir, consulte https://github.com/rnelsonchem/simpledbf

Para converter os arquivos .DBC em .DBF é necessário baixar o programa TABWIN do DATASUS em:
https://datasus.saude.gov.br/transferencia-de-arquivos/

Escolher as opções 
Fonte: TABWIN/TABNET
Modalidade: Programas
Tipo de Arquivo: TABWIN

Não é necessário usr o TABWIN para a conversão. Esta aplicação distruibui dois arquivos - dbf2dbc.exe e IMPBORL.DLL que devem permanecer juntos no mesmo diretório. Eles irão fazer a conversão, para saber como usar execute o arquivo DBF2dbc.exe sem parâmetros.

Seu output deverá ser assim:
DATASUS dbf2dbc 1.0: Comprime arquivos DBF e Expande arquivos DBC
Sintaxe:
dbf2dbc <Especificaçao de arquivos> [<Diretório de saída>]

No arquivo será necessário apontar a variável path para a respectiva pasta na máquina local.

Executação recomendada em um Jupyter Notebook.
