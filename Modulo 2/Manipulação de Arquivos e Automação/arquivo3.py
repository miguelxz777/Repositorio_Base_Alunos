import os
print(os.getcwd())
#os.mkdir("d")
#os.mkdir("e")
#os.mkdir("f")
arquivo_path= "diretorio"
contador = 1
while contador <= 50:
    nome_pasta = f"pasta{contador}"
try:
    os.rmdir(arquivo_path)
    print(f"""\033[0;32m Pasta '{arquivo_path}'removida com sucesso! ;D""")
except FileNotFoundError:
    print(f"""\033[0;33m Pasta '{arquivo_path}'nao encontrada...@_@]""")
except OSError:
    print(f"""\033[0;34m '{arquivo_path}'é um arquivo,nao uma pasta!!! +_+""")
    contador = 1
while contador <= 50:
    nome_pasta = f"pasta{contador}"
for i in range(1,51):
    folder_name = "pasta(" + str(i)+ ")"
try:
    os.mkdir((folder_name))
    print(f"pasta '{folder_name}'criada com sucesso...")
except FileExistsError: 
    print(f"pasta '{folder_name}'ja existe")
except Exception as e:
     print(f"Erro ao criar a pasta '{folder_name}':{e}")    
contador = +1