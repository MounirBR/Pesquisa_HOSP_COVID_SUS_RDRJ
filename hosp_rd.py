## pesquisa a série de iternações pagas do SUS no Estado do RJ nos últimos 5 anos 
## para síndromes gripais, SARS, peneumonias e infecções pulmonares por vírus
## e exporta para um formato CSV, em verdade semi-coma
## run in a Jupyter notebook

## dados dos arquivos Reduzidos (RD) podem ser encontrados em
##ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/

import pandas as pd
# necessário usar o pacote para ler arqvuios .dbf
from simpledbf import Dbf5
import os

caminho = 'D:\\...\\Documentos\\Estudos\\DS_EMSAUDE\\dbf\\RD\\'

files = os.listdir(caminho)

lista_df = []

#caso arquivo já exista, é apagado para ser recriado em modo append
if os.path.exists('.\RDRJ15_20.CSV'):
    os.remove('.\RDRJ15_20.CSV')

header = True
tot_linha = 0

# loop para varrer todos os arquivos na pasta.
for f in files:
     
     #verifica se é um arquivo .DBF
     if f[-3:].lower() == 'dbf':
         
         # usar codec 850 - para idiomas europeus latino
         dbf = Dbf5(caminho + f, codec='cp850')
        
         # expoerta para um dataframe Pandas
         df = dbf.to_dataframe()
        
         #pesquisa os CIDs relacionados a problemas respiratórios, no Brasil o CID para COVID19 é B342.
         df_sars = df.query('DIAG_PRINC in ["B342","B972","J11","J110","J111","J118","J15","J150","J151","J152","J153","J154","J155","J156","J157","J158","J159","U04","U049","U071"]')
        
         # Salva no fim do arquivo os registros pesquisados para o mês
         df_sars.to_csv('RDRJ15_20.CSV', sep=';', header=header, mode='a')
        
         # nomes das colunas só será impresso para o primeiro aquivo lido
         if header:
                header = False
        
         # recupero a quantidade de linhas e colunas salvas pelo dataframe
         linha, coluna = df_sars.shape
        
         # total de linhas salvas no arquivo CSV
         tot_linha = tot_linha + linha
         
         # Um log simples em tela para monitorar o progresso na leitura e escrita dos aquivos 
         print('UF:' + f[2:4]+ ' Mês:' + f[6:8] + ' Ano:' + f[4:6] + " Qtd.:" + str(linha))

# +1 para o header 
tot_linha = tot_linha +1

# informa o fim do script com o total de linhas salvas no arquivo CSV resultante.
print("RDRJ15_20.csv fim com {}".format(tot_linha) )
