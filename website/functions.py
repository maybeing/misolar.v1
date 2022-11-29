from scipy.optimize import root
from math import sqrt, log
import math
from placas import *

#3) Nesta parte o sistema fará alguns cálculos sem interação com o usuário.

#3.a) Calcula a área do telhado(AT)
def calcularArea(alturatelhado, comprimentotelhado):
    areaTelhado = alturatelhado * comprimentotelhado
    return round(areaTelhado, 2)

#3.b)Calcula a área de um placa solar(AP);
def calcularAreaPlaca(alturaPlaca, larguraPlaca):
    areaPlaca = alturaPlaca * larguraPlaca
    return round(areaPlaca, 2)

#3.c)Dividir AT/AP, para obter a quantidade de placas solares que podem ser instaladas no telhado;
def divisaoAtAp(areaTelhado, areaPlaca):
    qtdPlacas = areaTelhado / areaPlaca
    return int(qtdPlacas)
    #qtd de placas que podem ser instaladas

#3.d)Multiplicar a quantidade de placas solares pela potência de cada placa solar, para obter a potência total que pode ser instalada no telhado;
def multiplicacaoQtdPlacaPotPlaca(qtdPlacas, potenciaPainel):
    potTotal = qtdPlacas * float(potenciaPainel)
    return round(potTotal, 2)
    #potencia total que pode ser instalada no telhado

#3.e) fazer as multiplicações do item anterior para voltagem e corrente elétrica para saber a voltagem e Amperagem que está instalada no telhado.
def multiplicacaoQtdPlacaVoltagem(qtdPlacas, voltagemPainel):
    voltagem = qtdPlacas * float(voltagemPainel)
    return round(voltagem, 2)

def multiplicacaoQtdPlacaAmperagem(qtdPlacas, correntePainel):
    amperagem = qtdPlacas * float(correntePainel)
    return round(amperagem, 2)

#3. f)Dividir o consumo mensal da conta de luz pela quantidade de dias do período de leitura na conta de luz para obter o consumo por dia e
# depois dividir por 8, que seriam 8 horas de geração solar, este parâmetro pode mudar de acordo com a região,
# desta forma vai obter qual a potência watts de geração que precisa ser instalada no telhado para zerar a conta de luz.
def divisaoConsumomensalQtddias(consumomensal, qtddias):
    potZerarLuz = (consumomensal / qtddias) / 8 #consumo diario
    return round(potZerarLuz, 2)
    #potencia watts de geracação que precisa ser instalada no telhado para zerar a conta de luz

#4)
def calculoGeracaoMensal(potTotal, qtddias):
    geracaoMensal = potTotal * 8 * qtddias * 0.70
    return round(geracaoMensal, 2)

def calculoValortotal(geracaoMensal):
    geracaoMensalKW = geracaoMensal / 1000
    valortotal = geracaoMensalKW * 0.70
    return round(valortotal, 2)

#Cálculos com "Nec" se referem aos cálculos do 2º quadro, de acordo com o número de placas NECessárias

def divisaoAtApNec(consumomensal, geracaoMensal):
    geracaoMensalKW = geracaoMensal / 1000
    qtdPlacasNec = consumomensal / geracaoMensalKW
    return round(qtdPlacasNec, 1)

def multiplicacaoQtdPlacaPotPlacaNec(qtdPlacasNec, potenciaPainel):
    potTotalNec = float(qtdPlacasNec) * float(potenciaPainel)
    return round(potTotalNec, 2)

def multiplicacaoQtdPlacaVoltagemNec(qtdPlacasNec, voltagemPainel):
    voltagemNec = float(qtdPlacasNec) * float(voltagemPainel)
    return round(voltagemNec, 2)

def multiplicacaoQtdPlacaAmperagemNec(qtdPlacasNec, amperagemPainel):
    amperagemNec = float(qtdPlacasNec) * float(amperagemPainel)
    return round(amperagemNec, 2)

def calculoGeracaoMensalNec(potTotalNec, qtddias):
    geracaoMensalNec = potTotalNec * 8 * qtddias * 0.70
    return round(geracaoMensalNec, 2)


#concentar calculo de valor total
#aparentemente a proposta original era essa:

#def calculoValortotalNec(consumomensal):
#    valortotalNec = consumomensal * 0,70
#    return round(valortotalNec, 2)

#mas não faz muito sentido o valor total da produção ser
#o consumo do usuário vezes a tarifa (esse é o valor que
#ele já paga. então fiz a tarifa vezes a geração mensal
#de acordo com o quadro.

def calculoValortotalNec(geracaoMensalNec):
    geracaoMensalNecKW = geracaoMensalNec / 1000
    valortotalNec = geracaoMensalNecKW * 0.70
    return round(valortotalNec, 2)

#depois disso, modifiquei a função de valor total do primeiro
#quadro também, que estava de acordo com a proposta original.

#6)
#Cálculos do inversor

def menor(x,y,z):
    max = x
    if y < max:
        max = y
    if z < max:
        max = z
    return max

def Inversores(potTotal, voltagem, amperagem, potInv, voltagemInv, amperagemInv):
    critW = potTotal / potInv
    critV = voltagem / voltagemInv
    critA = amperagem / amperagemInv
    nmenor = menor(critW, critV, critA)
    return(nmenor)

def CalculoProdEletrica(potTotal):
    potEletrica = potTotal * 8
    prodEletrica = potEletrica / 1000
    return round(prodEletrica, 2)


def CalculoPayback(valorTotal, prodEletrica):
    producao = prodEletrica * 12 * 0.70
    payback = valorTotal / producao
    return round(payback, 1)
