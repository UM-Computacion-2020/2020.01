lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]


class Sort():
    def BubbleSort(self, lista):
        n = len(lista)
        i = 0
        for i in range(1, n):
            for j in range(n-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista
