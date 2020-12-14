import random


#variables
CardDeck = [{"index": 1, "value": 1, "suit": "coins", "gameValue": 1, "hidden": False}, {"index": 2, "value": 2, "suit": "coins", "gameValue": 2, "hidden": False}, {"index": 3, "value": 3, "suit": "coins", "gameValue": 3, "hidden": False}, {"index": 4, "value": 4, "suit": "coins", "gameValue": 4, "hidden": False}, {"index": 5, "value": 5, "suit": "coins", "gameValue": 5, "hidden": False}, {"index": 6, "value": 6, "suit": "coins", "gameValue": 6, "hidden": False}, {"index": 7, "value": 7, "suit": "coins", "gameValue": 7, "hidden": False}, {"index": 8, "value": 10, "suit": "coins", "gameValue": 0.5, "hidden": False}, {"index": 9, "value": 11, "suit": "coins", "gameValue": 0.5, "hidden": False}, {"index": 10, "value": 12, "suit": "coins", "gameValue": 0.5, "hidden": False},
            {"index": 11, "value": 1, "suit": "cups", "gameValue": 1, "hidden": False}, {"index": 12, "value": 2, "suit": "cups", "gameValue": 2, "hidden": False}, {"index": 13, "value": 3, "suit": "cups", "gameValue": 3, "hidden": False}, {"index": 14, "value": 4, "suit": "cups", "gameValue": 4, "hidden": False}, {"index": 15, "value": 5, "suit": "cups", "gameValue": 5, "hidden": False}, {"index": 16, "value": 6, "suit": "cups", "gameValue": 6, "hidden": False}, {"index": 17, "value": 7, "suit": "cups", "gameValue": 7, "hidden": False}, {"index": 18, "value": 10, "suit": "cups", "gameValue": 0.5, "hidden": False}, {"index": 19, "value": 11, "suit": "cups", "gameValue": 0.5, "hidden": False}, {"index": 20, "value": 12, "suit": "cups", "gameValue": 0.5, "hidden": False},
            {"index": 21, "value": 1, "suit": "swords", "gameValue": 1, "hidden": False}, {"index": 22, "value": 2, "suit": "swords", "gameValue": 2, "hidden": False}, {"index": 23, "value": 3, "suit": "swords", "gameValue": 3, "hidden": False}, {"index": 24, "value": 4, "suit": "swords", "gameValue": 4, "hidden": False}, {"index": 25, "value": 5, "suit": "swords", "gameValue": 5, "hidden": False}, {"index": 26, "value": 6, "suit": "swords", "gameValue": 6, "hidden": False}, {"index": 27, "value": 7, "suit": "swords", "gameValue": 7, "hidden": False}, {"index": 28, "value": 10, "suit": "swords", "gameValue": 0.5, "hidden": False}, {"index": 29, "value": 11, "suit": "swords", "gameValue": 0.5, "hidden": False}, {"index": 30, "value": 12, "suit": "swords", "gameValue": 0.5, "hidden": False},
            {"index": 31, "value": 1, "suit": "clubs", "gameValue": 1, "hidden": False}, {"index": 32, "value": 2, "suit": "clubs", "gameValue": 2, "hidden": False}, {"index": 33, "value": 3, "suit": "clubs", "gameValue": 3, "hidden": False}, {"index": 34, "value": 4, "suit": "clubs", "gameValue": 4, "hidden": False}, {"index": 35, "value": 5, "suit": "clubs", "gameValue": 5, "hidden": False}, {"index": 36, "value": 6, "suit": "clubs", "gameValue": 6, "hidden": False}, {"index": 37, "value": 7, "suit": "clubs", "gameValue": 7, "hidden": False}, {"index": 38, "value": 10, "suit": "clubs", "gameValue": 0.5, "hidden": False}, {"index": 39, "value": 11, "suit": "clubs", "gameValue": 0.5, "hidden": False}, {"index": 40, "value": 12, "suit": "clubs", "gameValue": 0.5, "hidden": False}]
currentPlayers = []

gameOn = True
gameStart = True
gameRound = 0
choosingPlayers = True
numOfPlayers = 0
botNum = 0

# Player selection
print("This game is for 2-8 players")
while choosingPlayers:
    if numOfPlayers == 8:
        choosingPlayers = False
        print("Maximum number of players reached")
        break
    newPlayer = input("Enter a name to enter a new player, or the word 'bot' to enter one\nEnter 'stop' to stop adding players\n")
    # Check if player exists in database
    """Enter code here"""
    if newPlayer == "bot":
        if numOfPlayers == 0:
            print("Enter a human first!")
        else:
            botNum += 1
            currentPlayers.append(
                {"id": f"bot{botNum}", "name": f"bot{botNum}", "cards": {}, "isDealer": False, "gameStatus": "playing",
                 "points": 20, "handPoints": 0, "isBot": True})
            numOfPlayers += 1
    elif newPlayer == "stop":
        if numOfPlayers < 2:
            print("Need more players before stopping")
        else:
            print("Selection finished")
            break
    else:
        numOfPlayers += 1
        currentPlayers.append({"id": numOfPlayers, "name": newPlayer, "cards": {}, "isDealer": False,
                               "gameStatus": "playing", "points": 20, "handPoints": 0, "isBot": False})


while gameOn:
    # Select number of rounds
    maxRound = 0
    while 30 > maxRound < 5:
        maxRound = int(input("How many rounds do you wish to play?\n(Enter an integer between 5 and 30)\n"))
    # Assign order of play
    gameCardDeck = CardDeck.copy()
    random.shuffle(gameCardDeck)
    for player in currentPlayers:
        player["cards"]["card1"] = gameCardDeck.pop(0)
    for i in range(len(currentPlayers) - 1):
        for j in range(len(currentPlayers) - i - 1):
            if currentPlayers[j]["cards"]["card1"]["value"] < currentPlayers[j+1]["cards"]["card1"]["value"]:
                currentPlayers[j], currentPlayers[j+1] = currentPlayers[j+1], currentPlayers[j]
            elif currentPlayers[j]["cards"]["card1"]["value"] == currentPlayers[j+1]["cards"]["card1"]["value"]:
                if currentPlayers[j]["cards"]["card1"]["index"] > currentPlayers[j+1]["cards"]["card1"]["index"]:
                    currentPlayers[j], currentPlayers[j+1] = currentPlayers[j+1], currentPlayers[j]
    currentPlayers[0]["isDealer"] = True
    playersToPrint = ""
    for player in currentPlayers:
        if player == currentPlayers[-1]:
            playersToPrint += f"and {player['name']}"
        else:
            playersToPrint += f"{player['name']}, "
    print(f"This game's players will be {playersToPrint}.")
    print(f"{currentPlayers[0]['name']} is going to be the dealer.")
    pressEnter = input()

    # Start game
    bustedPlayers = 0
    while gameStart:
        # End conditions
        if gameRound == maxRound:
            print("That was the last round!")
            gameStart = False
            break
        if bustedPlayers == len(currentPlayers) - 1:
            print("Too many busts!")
            gameStart = False
            break
        gameRound += 1
        print(f"Round {gameRound}")
        # Give the first card to every player
        gameCardDeck = CardDeck.copy()
        random.shuffle(gameCardDeck)
        for player in currentPlayers:
            if player["gameStatus"] == "playing":
                player["cards"]["card1"] = gameCardDeck.pop(0)
                player['handPoints'] += player["cards"]["card1"]["gameValue"]
                player["cards"]["card1"]["hidden"] = True
        currentPlayers[0]["cards"]["card1"]["hidden"] = False
        print(f"Dealer's card:\n{currentPlayers[0]['cards']['card1']['value']} of {currentPlayers[0]['cards']['card1']['suit']}")
        # Enter bets
        for player in currentPlayers:
            if player["isDealer"]:
                continue
            else:
                betReady = False
                while not betReady:
                    print(f"Current points: {player['points']}\nInitial card: {player['cards']['card1']['value']} of {player['cards']['card1']['suit']}")
                    player["bet"] = int(input(f"{player['name']}\nEnter a bet:\n(Max 7)\n"))
                    if 7 < player["bet"] or player["bet"] < 1:
                        print("Wrong input. Try again")
                    else:
                        print(f"You have bet {player['bet']} points")
                        betReady = True
        # Player rounds
        for player in currentPlayers:
            i = 2
            j = 0
            if player["isDealer"]:
                continue
            if player["gameStatus"] == "playing":
                player["roundStatus"] = "playing"
                # Show cards on table
                print("Table")
                for playerTable in currentPlayers:
                    print(playerTable["name"])
                    for card, content in playerTable["cards"].items():
                        if not content["hidden"]:
                            print(f"{content['value']} of {content['suit']}")
                print(f"{player['name']}'s turn")
                while player["roundStatus"] == "playing":
                    # Show player their cards
                    for card, content in player["cards"].items():
                        print(f"{content['value']} of {content['suit']}")
                    print(f"{player['handPoints']} points")
                    # Busted
                    if player["handPoints"] > 7.5:
                        print(f"{player['handPoints']} in hand.\nBusted...")
                        player["roundStatus"] = "busted"
                        break
                    else:
                        # Bot turn
                        if player["isBot"]:
                            if player["handPoints"] <= currentPlayers[0]["handPoints"]:
                                player["cards"][f"card{i}"] = gameCardDeck.pop(0)
                                player['handPoints'] += player["cards"][f"card{i}"]["gameValue"]
                            # Chances of hitting or settling if points are bigger than the dealer's
                            elif player["handPoints"] > currentPlayers[0]["handPoints"]:
                                safePoints = 7.5 - player["handPoints"]
                                safeCards = 0
                                for card in CardDeck:
                                    if card["gameValue"] <= safePoints:
                                        safeCards += 1
                                for playerTable in currentPlayers:
                                    for card, content in playerTable["cards"].items():
                                        if not content["hidden"]:
                                            if content["gameValue"] <= safePoints:
                                                safeCards -= 1
                                if safeCards > len(gameCardDeck) * 0.65:
                                    player["cards"][f"card{i}"] = gameCardDeck.pop(0)
                                    player['handPoints'] += player["cards"][f"card{i}"]["gameValue"]
                                elif safeCards >= len(gameCardDeck) * 0.5 or safeCards <= len(gameCardDeck) * 0.65:
                                    probabilities = safeCards * 0.5 / len(gameCardDeck) * 0.5
                                    chancesToHit = random.randint(0,100)

                        # Human turn
                        else:
                            # Hit or settle
                            hitMe = input("Hit or settle? (Enter 'hit' or anything else to settle)\n")
                            if hitMe.lower() == "hit":
                                player["cards"][f"card{i}"] = gameCardDeck.pop(0)
                                player['handPoints'] += player["cards"][f"card{i}"]["gameValue"]
                                faceUpOrDown = input("Face down or face up?\n (Enter 'down' or anything else)\n")
                                if faceUpOrDown == "down":
                                    for card, content in player["cards"].items():
                                        if content["hidden"]:
                                            player["cards"][card]["hidden"] = False
                                    player["cards"][f"card{i}"]["hidden"] = True
                                    i += 1
                                else:
                                    i += 1
                                if player["handPoints"] == 1.0:
                                    split = input("Split?")
                                    if split.lower() == "yes":
                                        j += 1
                                        currentPlayers.append({"id": f"{player['id']}.{j}", "name": f"{player['name']}.{j}",
                                                               "cards": {"card1": player["cards"].pop(f"card{i}")},
                                                               "isDealer": False, "gameStatus": "playing", "points": 0,
                                                               "handPoints": 0})
                                        player["handPoints"] -= 0.5
                                        print(currentPlayers[-1])
                                i += 1
                            else:
                                player["roundStatus"] = "settled"
                                print(f"{player['name']} has settled")
        # Dealer round
        currentPlayers[0]["cards"]["card1"]["hidden"] = False
        currentPlayers[0]["roundStatus"] = "playing"
        print("Dealer's turn")
        while currentPlayers[0]["roundStatus"] == "playing":
            # Show dealer their cards
            for card, content in currentPlayers[0]["cards"].items():
                print(f"{content['value']} of {content['suit']}")
            print(f"{currentPlayers[0]['handPoints']} points")
            # Busted
            if currentPlayers[0]["handPoints"] > 7.5:
                print(f"{currentPlayers[0]['handPoints']} in hand.\nBusted...")
                currentPlayers[0]["roundStatus"] = "busted"
                continue
            else:
                # Hit or settle
                hitMe = input("Hit or settle? (Enter 'hit' or anything else to settle)\n")
                if hitMe.lower() == "hit":
                    currentPlayers[0]["cards"][f"card{i}"] = gameCardDeck.pop(0)
                    currentPlayers[0]['handPoints'] += currentPlayers[0]["cards"][f"card{i}"]["gameValue"]
                    i += 1
                else:
                    currentPlayers[0]["roundStatus"] = "settled"
                    print(f"{currentPlayers[0]['name']} (dealer) has settled")
        # Redistribution of points
        losingPoints = 0
        winningPoints = 0
        for player in currentPlayers:
            if player["isDealer"]:
                continue
            else:
                points = player["bet"]
                # Busted
                if player["roundStatus"] == "busted":
                    if currentPlayers[0]["handPoints"] == 7.5:
                        points *= 2
                    player["points"] -= points
                    losingPoints += points
                # Win
                elif player["handPoints"] > currentPlayers[0]["handPoints"]:
                    if player["handPoints"] == 7.5:
                        points *= 2
                    player["points"] += points
                    winningPoints += points
                # Lower points
                elif player["handPoints"] < currentPlayers[0]["handPoints"]:
                    if currentPlayers[0]["roundStatus"] == "busted":
                        player["points"] += points
                        winningPoints += points
                    elif currentPlayers[0]["handPoints"] == 7.5:
                        points *= 2
                        player["points"] -= points
                        losingPoints += points
                    else:
                        player["points"] -= points
                        losingPoints += points
                # Tie
                elif player["handPoints"] == currentPlayers[0]["handPoints"]:
                    if player["handPoints"] == 7.5:
                        points *= 4
                    player["points"] -= points
                    losingPoints += points
                if player["points"] <= 0:
                    player["gameStatus"] = "out"
                if player["points"] < 0:
                    losingPoints += player["points"]

        currentPlayers[0]["points"] += losingPoints - winningPoints
        # Save state of round in database
        """Enter code here"""
        # Reset hand
        for player in currentPlayers:
            player["handPoints"] = 0
            player["cards"].clear()
        # End of round
    for player in currentPlayers:
        print(f"{player['name']}\nTotal points: {player['points']}")
    mostPointsPlayer = currentPlayers[0]
    for player in currentPlayers:
        if player["points"] > mostPointsPlayer["points"]:
            mostPointsPlayer = player
    print(f"The winner is {mostPointsPlayer['name']}")
    gameOn = False

"""
La banca puede vender su posición
Si tu carta inicial es una figura y al pedir recibes una figura puedes hacer Split de la jugada
Puedes apostar en cada una de las jugadas por separado
Cálculo de puntos
Mostrar carta de la banca al principio
"""