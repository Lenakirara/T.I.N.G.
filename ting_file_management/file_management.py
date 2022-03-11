import sys


# https://docs.python.org/pt-br/3/library/sys.html#sys.stderr
# formas de imprimir com stderr:
# https://www.delftstack.com/pt/howto/python/python-print-to-stderr/
# https://www.programcreek.com/python/example/56344/sys.stderr.write
def txt_importer(path_file):
    if not path_file.endswith('txt'):
        return sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, 'r') as file_txt:
            # separamos a linha usando split()
            data_file = file_txt.read().split('\n')
            return data_file
    # tratamento erros:
    # https://www.hashtagtreinamentos.com/try-e-except-no-python?gclid=CjwKCAiAg6yRBhBNEiwAeVyL0BrU0Tuf2FS7koljKUhYWriFV14tOjsX2rO14Y_f6PSSUdqSHOZ29RoCzb4QAvD_BwE
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')


# if __name__ == "__main__":
#     print(txt_importer('statics/arquivo_teste.txt'))
#     print(txt_importer('statics/arquivo_teste1.txt'))
