import os as os

arquivo = open('arquivo.txt', 'w')
print(os.path.abspath(arquivo.name))
arquivo.write('Ola Mundo sdfgsdf')
print(os.path.abspath(arquivo.name))

print(arquivo)
