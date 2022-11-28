from flask import Blueprint, request, render_template
from functions import *
from placas import *
from flask import redirect, url_for

auth = Blueprint('auth', __name__)

potTotal = None #teste1
areaTelhado = None
areaPlaca = None
voltagem = None
amperagem = None
potZerarLuz = None
valortotal = None
alturatelhado = None
comprimentotelhado = None
consumomensal = None
valortotal = None
qtddias = None
qtdPlacasNec = None
voltagemNec = None
amperagemNec = None
potTotalNec = None
geracaoMensalNec = None
valortotalNec = None
potInv = None


@auth.route('send_data', methods=['POST'])
def send_data():
    global alturatelhado
    global comprimentotelhado
    global consumomensal
    global valortotal
    global qtddias
    global potTotal
    global areaTelhado
    global areaPlaca
    global qtdPlacas
    global potTotal
    global voltagem
    global amperagem
    global potZerarLuz
    global geracaoMensal
    global valortotal
    global qtdPlacasNec
    global voltagemNec
    global amperagemNec
    global potTotalNec
    global geracaoMensalNec
    global valortotalNec

    #2)Agora deve-se solicitar ao usuário os dados de sua instalação para que o sistema possa sugerir algumas possibilidades ao usuário
    #INPUTS
    alturatelhado = float(request.form['altura-telhado'])
    comprimentotelhado = float(request.form['comprimento-telhado'])
    consumomensal = float(request.form['consumo-mensal'])
    valortotal = float(request.form['valor-total'])
    qtddias = int(request.form['qtd-dias'])
    
    #calculos
    areaTelhado = calcularArea(alturatelhado, comprimentotelhado)
    areaPlaca = calcularAreaPlaca(CANADIANSOLAR.alturaPlaca, CANADIANSOLAR.larguraPlaca)
    qtdPlacas = divisaoAtAp(areaTelhado, areaPlaca)
    potTotal = multiplicacaoQtdPlacaPotPlaca(qtdPlacas, CANADIANSOLAR.potenciaPainel)
    voltagem = multiplicacaoQtdPlacaVoltagem(qtdPlacas, CANADIANSOLAR.voltagemPainel)
    amperagem = multiplicacaoQtdPlacaAmperagem(qtdPlacas, CANADIANSOLAR.correntePainel)
    potZerarLuz = divisaoConsumomensalQtddias(consumomensal, qtddias)
    geracaoMensal = calculoGeracaoMensal(potTotal, qtddias)
    valortotal = calculoValortotal(geracaoMensal)
    
    #cálculos do 2º quadro
    qtdPlacasNec = divisaoAtApNec(consumomensal, geracaoMensal)
    voltagemNec = multiplicacaoQtdPlacaVoltagemNec(qtdPlacasNec, CANADIANSOLAR.voltagemPainel)
    amperagemNec = multiplicacaoQtdPlacaAmperagemNec(qtdPlacasNec, CANADIANSOLAR.correntePainel)
    potTotalNec = multiplicacaoQtdPlacaPotPlacaNec(qtdPlacasNec, CANADIANSOLAR.potenciaPainel)
    geracaoMensalNec = calculoGeracaoMensalNec(potTotalNec, qtddias)
    valortotalNec = calculoValortotalNec(geracaoMensalNec)

    alturaPlaca=CANADIANSOLAR.alturaPlaca
    larguraPlaca=CANADIANSOLAR.larguraPlaca
    qtdPlacas=qtdPlacas

    return render_template ('base.html', areaTelhado=areaTelhado, areaPlaca=areaPlaca, alturaPlaca=CANADIANSOLAR.alturaPlaca, 
    larguraPlaca=CANADIANSOLAR.larguraPlaca, qtdPlacas=qtdPlacas, potTotal=multiplicacaoQtdPlacaPotPlaca(qtdPlacas, CANADIANSOLAR.potenciaPainel), 
    voltagem=voltagem, amperagem=amperagem, potZerarLuz=potZerarLuz, geracaoMensal=calculoGeracaoMensal(potTotal, qtddias), valortotal=valortotal, 
    voltagemNec=voltagemNec, amperagemNec=amperagemNec, potTotalNec=potTotalNec, qtdPlacasNec=qtdPlacasNec, geracaoMensalNec=calculoGeracaoMensalNec(potTotalNec, qtddias), 
    valortotalNec = calculoValortotalNec(geracaoMensalNec))


@auth.route('send_data2', methods=['post'])
def send_data2():
   global quadro
   quadro = request.form.get('quadro')
   return render_template('base.html', quadro=quadro, areaTelhado=areaTelhado, areaPlaca=areaPlaca, alturaPlaca=CANADIANSOLAR.alturaPlaca, 
    larguraPlaca=CANADIANSOLAR.larguraPlaca, qtdPlacas=qtdPlacas, potTotal=multiplicacaoQtdPlacaPotPlaca(qtdPlacas, CANADIANSOLAR.potenciaPainel), 
    voltagem=voltagem, amperagem=amperagem, potZerarLuz=potZerarLuz, geracaoMensal=calculoGeracaoMensal(potTotal, qtddias), valortotal=valortotal, 
    voltagemNec=voltagemNec, amperagemNec=amperagemNec, potTotalNec=potTotalNec, qtdPlacasNec=qtdPlacasNec, geracaoMensalNec=calculoGeracaoMensalNec(potTotalNec, qtddias), 
    valortotalNec = calculoValortotalNec(geracaoMensalNec))



@auth.route('send_data3', methods=['POST'])
def send_data3():    
    global alturatelhado
    global comprimentotelhado
    global consumomensal
    global valortotal
    global qtddias
    global potTotal
    global areaTelhado
    global areaPlaca
    global qtdPlacas
    global potTotal
    global voltagem
    global amperagem
    global potZerarLuz
    global geracaoMensal
    global valortotal
    global qtdPlacasNec
    global voltagemNec
    global amperagemNec
    global potTotalNec
    global geracaoMensalNec
    global valortotalNec
    global potInv
    global quadro
    global prodEletrica
    global payback
    global producao
    global potencia
    
    potTotal = multiplicacaoQtdPlacaPotPlaca(qtdPlacas, CANADIANSOLAR.potenciaPainel)
    potInv = float(request.form['potInv'])
    voltagemInv = float(request.form['voltagemInv'])
    amperagemInv = float(request.form['amperagemInv'])

    critW = potTotal / potInv
    critV = voltagem / voltagemInv
    critA = amperagem / amperagemInv
    Inversores(potTotal, voltagem, amperagem, potInv, voltagemInv, amperagemInv)
    InversoresNec(potTotalNec, voltagemNec, amperagemNec, potInv, voltagemInv, amperagemInv)
    CalculoProdEletrica(potTotal)
    CalculoProdEletrica(potTotalNec)

    if quadro == '1':
       nmenor = Inversores(potTotal, voltagem, amperagem, potInv, voltagemInv, amperagemInv)
       prodEletrica = CalculoProdEletrica(potTotal)
       producao = prodEletrica * 12 * 0.70
       payback = valortotal / producao
    elif quadro == '2':
       nmenor = InversoresNec(potTotalNec, voltagemNec, amperagemNec, potInv, voltagemInv, amperagemInv)
       prodEletrica = CalculoProdEletrica(potTotalNec)
       producao = prodEletrica * 12 * 0.70
       payback = valortotalNec / producao

    if prodEletrica <= 30:
         taxa = '20,40'
    elif prodEletrica > 30 and prodEletrica <= 50:
         taxa = '34,00'
    elif prodEletrica > 50:
         taxa = '68,00'

    return render_template('base.html', nmenor=round(nmenor), prodEletrica=prodEletrica, taxa=taxa, payback=round(payback, 1), areaTelhado=areaTelhado, areaPlaca=areaPlaca, alturaPlaca=CANADIANSOLAR.alturaPlaca, 
    larguraPlaca=CANADIANSOLAR.larguraPlaca, qtdPlacas=qtdPlacas, potTotal=multiplicacaoQtdPlacaPotPlaca(qtdPlacas, CANADIANSOLAR.potenciaPainel), 
    voltagem=voltagem, amperagem=amperagem, potZerarLuz=potZerarLuz, geracaoMensal=calculoGeracaoMensal(potTotal, qtddias), valortotal=valortotal, 
    voltagemNec=voltagemNec, amperagemNec=amperagemNec, potTotalNec=potTotalNec, qtdPlacasNec=qtdPlacasNec, geracaoMensalNec=calculoGeracaoMensalNec(potTotalNec, qtddias), 
    valortotalNec = calculoValortotalNec(geracaoMensalNec))

