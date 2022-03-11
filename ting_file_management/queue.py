# pegando ideia de queue feita na aula ao vivo:
# https://github.com/tryber/sd-011-live-lectures/blob/lecture-37.2/queue.py
# estudando tbm um pouco de fila (queue) em:
# https://www.youtube.com/watch?v=tiee9D54tE0
class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    # metodo para saber se a lista está vazia
    def is_empty(self):
        return self._data == []

    def enqueue(self, value):
        # adiciona valor a fila/lista
        self._data.append(value)

    def dequeue(self):
        # removendo dado que está mais tempo na fila
        if not self.is_empty():
            return self._data.pop(0)
        return None

    def search(self, index):
        # buscando um indice valido
        # troquei a sequencia da logica, pois imagino que seja mais correto
        # deixar o else com retorno de uma busca valida
        # principalmente pq o IndexError funciona qdo tentamos acessar uma
        # posição que está fora do seu range
        # https://pythonhelp.wordpress.com/2012/12/31/deu-erro-e-agora-o-que-eu-faco/#:~:text=O%20IndexError%20significa%20que%20estamos,receber%20um%20IndexError%20na%20cabe%C3%A7a.
        if index < 0 or index > len(self._data):
            raise IndexError
        return self._data[index]   
