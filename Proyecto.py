import random

"""
variables
"""
CardDeck = [str(i) for i in range(1,41)]
currentPlayers = [{"id": "1", "name": "Lorenzo"}, {"id": "2", "name": "Jose"}, {"id": "3", "name": "Eric"}]

gameOn = True
gameStart = True


while gameOn:
    gameCardDeck = CardDeck
    random.shuffle(gameCardDeck)
    for player in currentPlayers:
        player["game order"] = gameCardDeck.pop(gameCardDeck.index(random.choice(gameCardDeck)))
    for i in range(len(currentPlayers) - 1):
        for j in range(len(currentPlayers) - i - 1):
            if currentPlayers[j]["game order"] < currentPlayers[j + 1]["game order"]:
                currentPlayers[j], currentPlayers[j + 1] = currentPlayers[j + 1], currentPlayers[j]
            elif currentPlayers[j]["game order"] == currentPlayers[j + 1]["game order"]:
                print("Comparación de palos")
    while gameStart:
        print("Game starts")
"""
La banca puede vender su posición
Comienza jugador a la izquierda de la banca
Repartir 1 carta boca abajo a cada jugador
Se apuesta
Puedes pedir una carta o plantarte
Si tu carta inicial es una figura y al pedir recibes una figura puedes hacer Split de la jugada
Puedes apostar en cada una de las jugadas por separado
Cuando terminan los jugadores, juega la banca sin cartas boca abajo
Ganan los que tienen mejor puntuación que la banca
La banca debe pagar a los ganadores
Los que ganan con 7 y medio, cobran el doble
Los empates los gana la banca
Si la banca gana con 7 y medio a otros jugadores por empate, estos pagan el cuádruple.

"""