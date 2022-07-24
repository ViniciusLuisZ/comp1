from lexico import Lexico
from sintatico import Sintatico;

tokens = []
a = Lexico('exemplo.txt')
file = open("exemplo.txt", "r")
data = file.read()
number_of_characters = len(data)
print('Número de caracteres :', number_of_characters)
for i in range(number_of_characters-6):
    tokens.append(a.retorna_token())
    
print (tokens)    
Sintatico(tokens)
        
