# importações usada para teste:
# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue


def exists_word(word, instance):
    occurrencies = []
    # percorrendo o tamanho do instance
    # Não esquecendo que o Queue() está instanciado no test
    for index in range(len(instance)):
        # buscando dentro de um indice valido
        file = instance.search(index)
        data = {
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': []
                }
        # buscando indice e a info da respectiva linha
        # usando enumerate()
        # https://pythonhelp.wordpress.com/2012/01/05/a-funcao-enumerate/
        # https://www.hashtagtreinamentos.com/enumerate-no-python
        for i, line in enumerate(file['linhas_do_arquivo']):
            # case insensitive -> lower()
            if word.lower() in line.lower():
                line_occurrencies = {'linha': i + 1}
                # adicionamos as ocorrencias de linha
                data['ocorrencias'].append(line_occurrencies)
            # condicional para ver se a ocorrencia existe
            if len(data['ocorrencias']):
                occurrencies.append(data)
    return occurrencies


def search_by_word(word, instance):
    ...


# para rodar no terminal => python -m ting_word_searches.word_search
# if __name__ == "__main__":
#     test = Queue()
#     process('statics/nome_pedro.txt', test)
#     # testando se a palavra existe
#     word1 = exists_word("Pedro", test)
#     print(word1)
#     # testando para ver se vem uma lista vazia
#     word2 = exists_word("Ratinho", test)
#     print(word2)
#     word3 = exists_word("UM", test)
#     print(word3)
#
#     # testando outro arquivo
#     process('statics/novo_paradigma_globalizado.txt', test)
#     word4 = exists_word("desafiador", test)
#     print(word4)
