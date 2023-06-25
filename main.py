from hangman_words import palavras
from hangman_art import estagios, logo
import random

class HangmanGame:
    def __init__(self):
        self.palavras = palavras
        self.logo = logo
        self.estagios = estagios
        self.palavra_escolhida = ""
        self.tamanho_palavra = 0
        self.mostrar = []
        self.vidas = 6  # quantidade vidas
        self.final_do_jogo = False

    def iniciar_jogo(self):
        self._escolher_palavra()
        self._mostrar_palavra_inicial()
        self._executar_jogo()

    def _executar_jogo(self):
        while not self.final_do_jogo:
            advinhe = self._obter_input()
            self._verificar_advinhe(advinhe)
            self._verificar_final_do_jogo()
            self._mostrar_progresso()
            self._mostrar_estagio()

    def _escolher_palavra(self):
        self.palavra_escolhida = random.choice(self.palavras).lower()
        self.tamanho_palavra = len(self.palavra_escolhida)
        print(self.logo)  # Print do logo HANGMAN para deixar o código mais bonito

    def _mostrar_palavra_inicial(self):
        self.mostrar = ['_' for _ in range(self.tamanho_palavra)]

    def _obter_input(self):
        advinhe = input('Advinhe a letra: ').lower().strip()[0]
        return advinhe

    def _verificar_advinhe(self, advinhe):
        if advinhe in self.mostrar:
            print(f'Você já advinhou {advinhe} e por isso perdeu uma vida')
            self.vidas -= 1

        acertou = False
        for posicao in range(self.tamanho_palavra):
            frase = self.palavra_escolhida[posicao]
            if frase == advinhe:
                self.mostrar[posicao] = frase
                acertou = True

        if not acertou:
            print(f'Você advinhou {advinhe}, essa letra não está na palavra. Você perdeu uma vida')
            self.vidas -= 1

    def _verificar_final_do_jogo(self):
        if self.vidas == 0:
            self.final_do_jogo = True
            print('Você perdeu')
        elif "_" not in self.mostrar:
            self.final_do_jogo = True
            print('Você ganhou')

    def _mostrar_progresso(self):
        print(' '.join(self.mostrar))

    def _mostrar_estagio(self):
        print(self.estagios[self.vidas])

hangman = HangmanGame()
hangman.iniciar_jogo()