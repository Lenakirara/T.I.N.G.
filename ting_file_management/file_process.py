from ting_file_management.file_management import txt_importer
# essa importação foi usada para testar:
# from ting_file_management.queue import Queue
import sys


def process(path_file, instance):
    # no teste o Queue() já está instanciado
    # na condicional => ver se arquivo possui mesmo nome
    for name in range(len(instance)):
        if instance.search(name)['nome_do_arquivo'] == path_file:
            return None

    data_file = txt_importer(path_file)
    qty_lines = len(data_file)  # buscando a quantidade de linhas
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': qty_lines,
        'linhas_do_arquivo': data_file,
    }
    # relembrando conceitos:
    # https://www.educative.io/edpresso/how-to-implement-a-queue-in-python
    # enqueue => estamos adicioando em data
    instance.enqueue(data)
    # https://acervolima.com/sys-stdout-write-em-python/
    # https://www.delftstack.com/pt/howto/python/python-print-without-newline/
    return sys.stdout.write(str(data))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# para rodar no terminal => python3 -m pytest tests/test_file_process.py
# if __name__ == "__main__":
#     test1 = Queue()
#     print(process('statics/arquivo_teste.txt', test1))
