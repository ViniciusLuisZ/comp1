import os


def split_manual(linha, caracter):
    linha_splitada = []
    palavra = ''
    for letra in linha:
        if letra != caracter and letra != '\n':
            palavra += letra
        else:
            linha_splitada.append(palavra)
            palavra = ''
    if palavra != '':
        linha_splitada.append(palavra)
    return linha_splitada


def remove_caracter(linha, caracter):
    palavra_final = ''
    for letra in linha:
        if letra == caracter:
            pass
        else:
            palavra_final += letra
    return palavra_final


class Sintatico:
    def __init__(self):
        self.patch_gramatica = os.getcwd().replace('src', '') + 'texts\\gramatica.txt'
        self.patch_first_follow = os.getcwd().replace('src', '') + 'texts\\firstFollow.txt'
        self.linhas = []
        self.first_follow = []
        with open(self.patch_gramatica, 'r') as f:
            for line in f:
                self.linhas.append(split_manual(line, ' '))
            self.texto = f.read()
        with open(self.patch_first_follow, 'r') as f:
            for line in f:
                self.first_follow.append(split_manual(line, ' '))
        self.tabela = ''
        self.First = {}
        self.Follow = {}
        self.tabela = {'id': {'E': [], 'T': [], 'P': [], 'F': []},
                       '(': {'E': [], 'T': [], 'P': [], 'F': []},
                       ')': {'E': [], 'T': [], 'P': [], 'F': []},
                       '/': {'E': [], 'T': [], 'P': [], 'F': []},
                       '*': {'E': [], 'T': [], 'P': [], 'F': []},
                       '+': {'E': [], 'T': [], 'P': [], 'F': []},
                       '-': {'E': [], 'T': [], 'P': [], 'F': []},
                       '^': {'E': [], 'T': [], 'P': [], 'F': []},
                       'exp[': {'E': [], 'T': [], 'P': [], 'F': []},
                       ']': {'E': [], 'T': [], 'P': [], 'F': []},
                       '$': {'E': [], 'T': [], 'P': [], 'F': []},
                       }

    def retorna_texto(self):
        return self.texto

    def popula_tabela(self):
        self.configura_first_follow()
        for regra in self.linhas:
            if regra[2] == '&':
                for n_terminal in self.Follow[regra[0]]:
                    self.tabela[n_terminal][regra[0]].append(regra)

            elif regra[2] not in self.tabela.keys():
                for n_terminal in self.First[regra[2]]:
                    if n_terminal == '&':
                        for no_terminal in self.Follow[regra[0]]:
                            self.tabela[no_terminal][regra[0]].append(regra)
                    else:
                        self.tabela[n_terminal][regra[0]].append(regra)

            else:
                self.tabela[regra[2]][regra[0]].append(regra)

        print(self.tabela)

        return True

    def configura_first_follow(self):
        for linha in self.first_follow:
            linha[3] = (remove_caracter(linha[3], '{'))
            linha[3] = (remove_caracter(linha[3], '}'))
            linha[3] = (split_manual(linha[3], caracter=','))
            linha[1] = (remove_caracter(linha[1], '('))
            linha[1] = (remove_caracter(linha[1], ')'))
            if linha[0] == 'First':
                if linha[1] not in self.First.keys():
                    self.First[linha[1]] = linha[3]

            if linha[0] == 'Follow':
                if linha[1] not in self.Follow.keys():
                    self.Follow[linha[1]] = linha[3]

        return True