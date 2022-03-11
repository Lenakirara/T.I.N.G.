# importações usada para teste:
# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue


def exists_word(word, instance):
    occurrences = []
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
                line_occurrences = {'linha': i + 1}
                # adicionamos as ocorrencias de linha
                data['ocorrencias'].append(line_occurrences)
        # condicional para ver se a ocorrencia existe
        # adicioando info na condicional => > 0
        size_occurrences = len(data['ocorrencias'])
        if size_occurrences > 0:
            occurrences.append(data)
    return occurrences


def search_by_word(word, instance):
    occurrences = []
    for index in range(len(instance)):
        file = instance.search(index)
        data = {
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': []
        }
        for i, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                line_occurrences = {'linha': i + 1, "conteudo": line}
                # adicionamos as ocorrencias de linha e seu conteudo
                data['ocorrencias'].append(line_occurrences)
        # condicional para ver se a ocorrencia existe
        size_occurrences = len(data['ocorrencias'])
        if size_occurrences > 0:
            occurrences.append(data)
    return occurrences

# para rodar no terminal => python -m ting_word_searches.word_search
# if __name__ == "__main__":
#     test = Queue()
    # process('statics/nome_pedro.txt', test)
    # testando se a palavra existe
    # word1 = exists_word("Pedro", test)
    # print(word1)
    # testando para ver se vem uma lista vazia
    # word2 = exists_word("Ratinho", test)
    # print(word2)
    # word3 = exists_word("UM", test)
    # print(word3)

    # testando outro arquivo
    # process('statics/novo_paradigma_globalizado.txt', test)
    # word4 = exists_word("desafiador", test)
    # print('======>>>>>')
    # print(word4)

    # testando a parte de search
    # word5 = search_by_word('Pedro', test)
    # print(word5)
    # word6 = search_by_word('Ratinho', test)
    # print(word6)

    # testando outro arquivo
    # word7 = search_by_word('desafiador', test)
    # print('====>>>>====>>>>')
    # print(word7)
