import unittest
from robo import *


class TesteInformacoes(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_media(self):
        mensagens = [ "como calcular as médias?", "como se calcula as médias?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Para calcular a média aritimetica simples", resposta.text)

    def testar_desvio(self):
        mensagens = [ "como calcular o desvio padrão?", "como se calcula o desvio padrão?", "como calcular o desvio?", "como se calcula o desvio?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("A fórmula diz que o desvio-padrão", resposta.text)
    
    def testar_variancia(self):
        mensagens = [ "como calcular a variância?", "como se calcula a variância?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Primeiramente, devemos calcular a média aritmética do conjunto", resposta.text)
    
    def testar_moda(self):
        mensagens = [ "como calcular a moda?", "como se calcula a moda?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A Moda representa o valor mais frequente de um conjunto de dados", resposta.text)

    def testar_mediana(self):
        mensagens = [ "como calcular a mediana?", "como se calcula a mediana?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A Mediana representa o valor central de um conjunto de dados", resposta.text)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)