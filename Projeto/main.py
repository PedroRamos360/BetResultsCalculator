from random import randint
from chances_wins import data


def average(list):
    total = 0
    for amount in range(len(list)):
        total += list[amount]

    average = total / len(list)
    return average


def calculate_bet(total_amount, amount, bets, chance, win):
    for black in range(bets):
        # Realização da aposta
        total_amount -= amount
        roll = randint(0, 10_000)

        # Verificação do resultado da aposta
        if roll <= chance:
            total_amount += amount * win

    return total_amount


def program():
    amount = int(input('Valor por aposta: '))
    bets = int(input('Número de apostas: '))
    precision = int(input('Precisão do cálculo: '))

    total_amount = amount * bets

    black_results = []
    red_results = []
    blue_results = []
    yellow_results = []

    for i in range(precision):
        black_results.append(calculate_bet(total_amount, amount, bets, data.black_chance, data.black_win))
        red_results.append(calculate_bet(total_amount, amount, bets, data.red_chance, data.red_win))
        blue_results.append(calculate_bet(total_amount, amount, bets, data.red_chance, data.red_win))
        yellow_results.append(calculate_bet(total_amount, amount, bets, data.yellow_chance, data.yellow_win))
    print("Total antes:", total_amount)
    print("Se apostar no preto:", average(black_results))
    print("Se apostar no vermelho:", average(red_results))
    print("Se apostar no azul:", average(blue_results))
    print("Se apostar no amarelo:", average(yellow_results))


program()

