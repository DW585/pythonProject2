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

def area_total_casa():##
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
