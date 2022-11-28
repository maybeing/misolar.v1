#1) Na Primeira etapa selecione o modelo de placa solar a ser utilizado no projeto e quantidade, 
# o sistema deve armazenar os seguintes dados para realizar os cálculos posteriores:

class Placa:
    def __init__(self, modeloPlaca, alturaPlaca, larguraPlaca, voltagemPainel, potenciaPainel, correntePainel, valorPlaca):
        self.modeloPlaca = modeloPlaca
        self.alturaPlaca = alturaPlaca
        self.larguraPlaca = larguraPlaca
        self.voltagemPainel = voltagemPainel
        self.potenciaPainel = potenciaPainel
        self.correntePainel = correntePainel
        self.valorPlaca = valorPlaca

    def calcularAreaPlaca(self, alturaPlaca, larguraPlaca):
        areaPlaca = alturaPlaca * larguraPlaca
        return areaPlaca

CANADIANSOLAR = Placa('CANADIAN SOLAR - Modelo CS3W-455MS', 1.04, 2.10, 41.3, 455, 11.02, 1.069)
TRINASOLAR = Placa('TRINA SOLAR - Modelo TSM-DE17M(II)-455', 1.04, 2.10, '49.80', '455', '11.06', '552.37')
