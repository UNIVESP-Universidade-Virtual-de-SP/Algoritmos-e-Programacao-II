"""
Reimplemente o método dequeue() da classe Queue de modo que seja levantada uma exceção KeyboardInterrupt (um tipo de exceção impróprio, nesse caso) com a mensagem 'remoção de uma fila vazia ' (uma mensagem de erro realmente apropriada) se for feita uma tentativa de remover algum elemento de uma fila vazia.

>>> queue = Queue()

>>> queue.dequeue()

Traceback (most recent call last):

  File "<pyshell#30>", line 1, in <module>

    queue.dequeue()

  File "/Users/me/ch8.py", line 183, in dequeue

    raise KeyboardInterrupt('remoção de uma fila vazia')

KeyboardInterrupt: remoção de uma fila vazia
"""
    

class Queue:
    'uma classe de fila clássica'
    def __init__(self):
        'instancia uma lista vazia'
        self.q = []
    def isEmpty(self):
        'retorna True se a fila estiver vazia, False caso contrário'
        return (len(self.q) == 0)
    def enqueue (self, item):
        'Insere item no final da fila'
        return self.q.append(item)
    def dequeue(self):
        if (len(self.q) == 0):
            raise KeyboardInterrupt("Remoção de uma fila vazia")
        return self.q.pop(0)

v1 = Queue()
v1.dequeue()
