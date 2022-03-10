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
        # se indice for >= que 0 ou indice <= que tamanho dessa lista
        if 0 <= index <= len(self._data):
            return self._data[index]
        raise IndexError
