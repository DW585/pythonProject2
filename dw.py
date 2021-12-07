def valor_do_combustivel():##questao1
    valor_combustivel = float(input('qual valor do combustível?'))
    valor_dinheiro = float(input('valor a ser abastecido?'))
    litros_final = valor_dinheiro / valor_combustivel
    print('vai dar pra abastecer', litros_final, 'litros de combustivel')

def consumo():##questao2
    km_inicial = float(input('qual o km inicial?'))
    km_final = float(input('qual km final?'))
    litros = float(input('quantos litros de gasolina foram gastos?'))
    consumo_kml = float((km_final - km_inicial) / litros)
    print('a media de consumo é', consumo_kml, 'kml')

def valor_a_ser_pago():##questao3
    pg = float(input('qual valor a ser pago?'))
    dias  = float(input('dias de atraso?'))
    juros = float(input('valor do juros por dia?'))
    valor_rs = float((juros * dias) + pg)
    print('o valor final a ser pago é de', valor_rs, 'R$')

def area_total_casa():##questao4
    comodo1_l = float(input('qual a largura do 1° comodo?'))
    comodo1_c = float(input('qual o comprimento 1° comodo?'))
    comodo2_l = float(input('qual a largura do 2° comodo?'))
    comodo2_c = float(input('qual a comprimento do 2° comodo?'))
    comodo3_l = float(input('qual a largura do 3° comodo?'))
    comodo3_c = float(input('qual a comprimento do 3° comodo?'))
    comodo4_l = float(input('qual a largura do 4° comodo?'))
    comodo4_c = float(input('qual a comprimento do 4° comodo?'))
    area_t = float((comodo1_l * comodo1_c) + (comodo2_l * comodo2_c) + (comodo3_l * comodo3_c) + (comodo4_l * comodo4_c))
    print('A área total da casa é', area_t, 'm²')

def conversor():##questao5
    valor_dolar = float(input('Qual a cotção do dolar em relação ao real?'))
    valor_rs = float(input('Valor em R$ a ser convertido para dolar:'))
    conversao_rs = float(valor_dolar * valor_rs)
    print(conversao_rs,'dolars')

def valor_do_salario():##questao6
    valor_salario = float(input('valor do salário?'))
    reajuste = float(input('valoer do reajuste em %'))
    valor_f = float((reajuste / 100) * (valor_salario))
    print(valor_f)

def ate_o_milhao():##questao7
    salario_total = float(input("valor do salário mensal?"))
    despesas_totais = float(input('valor total das despesas?'))
    valor_f_d = float(salario_total - despesas_totais)
    vf = float((valor_f_d /  1000000) ) // 12
    print('vai demorar', vf, 'anos')

def valor_inteiro():##questao8
   n_ = int(input('Numero?'))
   print('n - 1, n - 2, n +1, n+2')

def nome_idade():##questao9
    nome = input('qual seu nome?')
    ano = int(input('qual o ano atual?'))
    ano_n = int(input('qual ano em que você nasceu?'))
    print(nome,'tem', ano - ano_n,'anos')

def capiroto():
    medida_sala_c = float(input('qual ocomprimento da sala?')) + (1.5)
    medida_sala_l = float(input('qual lagura da sala?'))
    medida_carteira_c = float(input('qualo comprimento da carteira?')) + (0.2)
    medida_carteira_l = float(input('qualo largura da carteira?')) + (0.5)
    qnt_cart  = float(medida_carteira_l * medida_sala_c) // (medida_carteira_l * medida_carteira_c)
    print('na sala cabem', qnt_cart, 'carteiras')

capiroto()