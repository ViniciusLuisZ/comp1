class Lexico:
    def __init__(self, arq):
        with open(arq, 'r') as f:
            self.texto = f.read()
        self.indice = 0

    def retorna_token(self):
        token = ''
        for pos, c in enumerate(self.texto[self.indice:]):

            if c == 'e':
                if self.texto[self.indice + 1] == 'x' and self.texto[self.indice + 2] == 'p':
                    self.indice += pos + 3
                    return 'exp'

            if c in '0123456789':
                while True:
                    prox = self.texto[self.indice + len(token) + pos]
                    if prox in '0123456789' or prox == '.' and token.count('.') <= 1:
                        token += prox
                    else:
                        break

            if c in '*-+/[]()^':
                self.indice += pos + 1
                return c

            if c not in ['', '\n', '\t', ' ']:
                self.indice += pos + len(token)
                return (token)


a = Lexico('exemplo.txt')

file = open("exemplo.txt", "r")
data = file.read()
number_of_characters = len(data)

print('Número de caracteres :', number_of_characters)

# achar uma forma de não ficar hard coded aqui
for i in range(number_of_characters):
    print (a.retorna_token())
