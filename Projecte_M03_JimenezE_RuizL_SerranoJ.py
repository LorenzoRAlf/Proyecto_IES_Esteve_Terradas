import random

# variables
CardDeck = [{"index": 1, "value": 1, "suit": "coins", "gameValue": 1, "hidden": False},
            {"index": 2, "value": 2, "suit": "coins", "gameValue": 2, "hidden": False},
            {"index": 3, "value": 3, "suit": "coins", "gameValue": 3, "hidden": False},
            {"index": 4, "value": 4, "suit": "coins", "gameValue": 4, "hidden": False},
            {"index": 5, "value": 5, "suit": "coins", "gameValue": 5, "hidden": False},
            {"index": 6, "value": 6, "suit": "coins", "gameValue": 6, "hidden": False},
            {"index": 7, "value": 7, "suit": "coins", "gameValue": 7, "hidden": False},
            {"index": 8, "value": 10, "suit": "coins", "gameValue": 0.5, "hidden": False},
            {"index": 9, "value": 11, "suit": "coins", "gameValue": 0.5, "hidden": False},
            {"index": 10, "value": 12, "suit": "coins", "gameValue": 0.5, "hidden": False},
            {"index": 11, "value": 1, "suit": "cups", "gameValue": 1, "hidden": False},
            {"index": 12, "value": 2, "suit": "cups", "gameValue": 2, "hidden": False},
            {"index": 13, "value": 3, "suit": "cups", "gameValue": 3, "hidden": False},
            {"index": 14, "value": 4, "suit": "cups", "gameValue": 4, "hidden": False},
            {"index": 15, "value": 5, "suit": "cups", "gameValue": 5, "hidden": False},
            {"index": 16, "value": 6, "suit": "cups", "gameValue": 6, "hidden": False},
            {"index": 17, "value": 7, "suit": "cups", "gameValue": 7, "hidden": False},
            {"index": 18, "value": 10, "suit": "cups", "gameValue": 0.5, "hidden": False},
            {"index": 19, "value": 11, "suit": "cups", "gameValue": 0.5, "hidden": False},
            {"index": 20, "value": 12, "suit": "cups", "gameValue": 0.5, "hidden": False},
            {"index": 21, "value": 1, "suit": "swords", "gameValue": 1, "hidden": False},
            {"index": 22, "value": 2, "suit": "swords", "gameValue": 2, "hidden": False},
            {"index": 23, "value": 3, "suit": "swords", "gameValue": 3, "hidden": False},
            {"index": 24, "value": 4, "suit": "swords", "gameValue": 4, "hidden": False},
            {"index": 25, "value": 5, "suit": "swords", "gameValue": 5, "hidden": False},
            {"index": 26, "value": 6, "suit": "swords", "gameValue": 6, "hidden": False},
            {"index": 27, "value": 7, "suit": "swords", "gameValue": 7, "hidden": False},
            {"index": 28, "value": 10, "suit": "swords", "gameValue": 0.5, "hidden": False},
            {"index": 29, "value": 11, "suit": "swords", "gameValue": 0.5, "hidden": False},
            {"index": 30, "value": 12, "suit": "swords", "gameValue": 0.5, "hidden": False},
            {"index": 31, "value": 1, "suit": "clubs", "gameValue": 1, "hidden": False},
            {"index": 32, "value": 2, "suit": "clubs", "gameValue": 2, "hidden": False},
            {"index": 33, "value": 3, "suit": "clubs", "gameValue": 3, "hidden": False},
            {"index": 34, "value": 4, "suit": "clubs", "gameValue": 4, "hidden": False},
            {"index": 35, "value": 5, "suit": "clubs", "gameValue": 5, "hidden": False},
            {"index": 36, "value": 6, "suit": "clubs", "gameValue": 6, "hidden": False},
            {"index": 37, "value": 7, "suit": "clubs", "gameValue": 7, "hidden": False},
            {"index": 38, "value": 10, "suit": "clubs", "gameValue": 0.5, "hidden": False},
            {"index": 39, "value": 11, "suit": "clubs", "gameValue": 0.5, "hidden": False},
            {"index": 40, "value": 12, "suit": "clubs", "gameValue": 0.5, "hidden": False}]
currentPlayers = []

gameOn = True
gameStart = True
gameRound = 0
choosingPlayers = True
numOfPlayers = 0
botNum = 0

while gameOn:
    # Player selection
    while choosingPlayers:
        print("This game is for 2-8 players")
        print(f"{numOfPlayers} player/s in the game")
        if numOfPlayers == 8:
            choosingPlayers = False
            print("Maximum number of players reached")
            break
        newPlayer = input(
            "Enter a name to enter a new player, or the word 'bot' to enter one\nEnter 'stop' to stop adding players\n")
        # Check if player exists in database
        """Enter code here"""
        if newPlayer == "bot":
            if numOfPlayers == 0:
                print("Enter a human first!")
            else:
                botNum += 1
                currentPlayers.append(
                    {"id": f"bot{botNum}", "name": f"bot{botNum}", "cards": {}, "isDealer": False,
                     "gameStatus": "playing",
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
    # Select number of rounds
    maxRound = 0
    while 30 < maxRound or maxRound < 5:
        maxRound = int(input("How many rounds do you wish to play?\n(Enter an integer between 5 and 30)\n"))
    # Assign order of play
    gameCardDeck = CardDeck.copy()
    random.shuffle(gameCardDeck)
    for player in currentPlayers:
        player["cards"]["card1"] = gameCardDeck.pop(0)
    for i in range(len(currentPlayers) - 1):
        for j in range(len(currentPlayers) - i - 1):
            if currentPlayers[j]["cards"]["card1"]["value"] < currentPlayers[j + 1]["cards"]["card1"]["value"]:
                currentPlayers[j], currentPlayers[j + 1] = currentPlayers[j + 1], currentPlayers[j]
            elif currentPlayers[j]["cards"]["card1"]["value"] == currentPlayers[j + 1]["cards"]["card1"]["value"]:
                if currentPlayers[j]["cards"]["card1"]["index"] > currentPlayers[j + 1]["cards"]["card1"]["index"]:
                    currentPlayers[j], currentPlayers[j + 1] = currentPlayers[j + 1], currentPlayers[j]
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
    eliminatedPlayers = 0
    while gameStart:
        # End conditions
        if gameRound == maxRound:
            print("That was the last round!")
            gameStart = False
            break
        if eliminatedPlayers == len(currentPlayers) - 1:
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
        # Enter bets
        print("**********" * 3)
        print("Betting phase\n")
        for player in currentPlayers:
            if player["isDealer"]:
                player["bet"] = 0
                continue
            elif player["gameStatus"] == "eliminated":
                player["bet"] = 0
                continue
            else:
                betReady = False
                while not betReady:
                    print(
                        f"Dealer's card:\n{currentPlayers[0]['cards']['card1']['value']} of {currentPlayers[0]['cards']['card1']['suit']}")
                    print(
                        f"Current points: {player['points']}\nInitial card: {player['cards']['card1']['value']} of {player['cards']['card1']['suit']}")
                    player["bet"] = int(input(f"{player['name']}\nEnter a bet:\n"))
                    if player["points"] < player["bet"] or player["bet"] < 1:
                        print("Wrong input. Try again")
                    else:
                        print(f"You have bet {player['bet']} points")
                        betReady = True
        # Player rounds
        print("**********" * 3)
        print("Playing phase\n")
        for player in currentPlayers:
            i = 2
            j = 0
            if player["isDealer"]:
                continue
            if player["gameStatus"] == "playing":
                player["roundStatus"] = "playing"
                print(f"{player['name']}'s turn")
                while player["roundStatus"] == "playing":
                    # Show cards on table
                    print("Table")
                    for playerTable in currentPlayers:
                        print(playerTable["name"])
                        for card, content in playerTable["cards"].items():
                            if not content["hidden"]:
                                print(f"{content['value']} of {content['suit']}")
                    # Show player their cards
                    print("Your cards:")
                    for card, content in player["cards"].items():
                        print(f"{content['value']} of {content['suit']}")
                    print(f"{player['handPoints']} points")
                    # Busted
                    if player["handPoints"] > 7.5:
                        print(f"{player['handPoints']} in hand.\nBusted...")
                        pressEnter = input()
                        player["roundStatus"] = "busted"
                        break
                    else:
                        # Bot turn
                        if player["isBot"]:
                            if player["handPoints"] <= currentPlayers[0]["handPoints"]:
                                print("Lower points than the dealer")
                                print(f"{player['name']} asks for another card")
                                print("**********" * 3)
                                player["cards"][f"card{i}"] = gameCardDeck.pop(0)
                                player['handPoints'] += player["cards"][f"card{i}"]["gameValue"]
                                i += 1
                            # Chances of hitting or settling if points are bigger than the dealer's
                            elif player["handPoints"] > currentPlayers[0]["handPoints"]:
                                safePoints = 7.5 - player["handPoints"]
                                print(f"Safe cards are cards below {safePoints}")
                                safeCards = 0
                                for card in CardDeck:
                                    if card["gameValue"] <= safePoints:
                                        safeCards += 1
                                for playerTable in currentPlayers:
                                    for card, content in playerTable["cards"].items():
                                        if not content["hidden"]:
                                            if content["gameValue"] <= safePoints:
                                                safeCards -= 1
                                print(f"There are {safeCards} safe cards in the deck")
                                probabilities = (safeCards / len(gameCardDeck)) * 100
                                print(f"{probabilities:.2f}% chances of getting a good card")
                                if probabilities > 65:
                                    print("Not that risky")
                                    print(f"{player['name']} asks for another card")
                                    print("**********" * 3)
                                    player["cards"][f"card{i}"] = gameCardDeck.pop(0)
                                    player['handPoints'] += player["cards"][f"card{i}"]["gameValue"]
                                    i += 1
                                elif probabilities < 1:
                                    player["roundStatus"] = "settled"
                                    pressEnter = input(f"{player['name']} has settled")
                                    break
                                elif probabilities < 50:
                                    chancesToHit = random.randint(1, 100)
                                    print(chancesToHit)
                                    if chancesToHit <= probabilities / 3:
                                        print("Very risky")
                                        print(f"{chancesToHit}")
                                        print(f"{player['name']} asks for another card")
                                        print("**********" * 3)
                                        player["cards"][f"card{i}"] = gameCardDeck.pop(0)
                                        player['handPoints'] += player["cards"][f"card{i}"]["gameValue"]
                                        i += 1
                                    else:
                                        player["roundStatus"] = "settled"
                                        pressEnter = input(f"{player['name']} has settled")
                                        break
                                else:
                                    chancesToHit = random.randint(1, 100)
                                    print(chancesToHit)
                                    if chancesToHit <= probabilities:
                                        print("Risky")
                                        print(f"{chancesToHit}")
                                        print(f"{player['name']} asks for another card")
                                        print("**********" * 3)
                                        player["cards"][f"card{i}"] = gameCardDeck.pop(0)
                                        player['handPoints'] += player["cards"][f"card{i}"]["gameValue"]
                                        i += 1
                                    else:
                                        player["roundStatus"] = "settled"
                                        pressEnter = input(f"{player['name']} has settled")
                                        break

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
                            else:
                                player["roundStatus"] = "settled"
                                print(f"{player['name']} has settled")
        # Dealer round
        if currentPlayers[0]["isBot"]:
            # Bot dealer
            currentPlayers[0]["roundStatus"] = "playing"
            print("Dealer's turn")
            while currentPlayers[0]["roundStatus"] == "playing":
                # Show cards on table
                print("Table")
                for playerTable in currentPlayers:
                    print(playerTable["name"])
                    for card, content in playerTable["cards"].items():
                        if not content["hidden"]:
                            print(f"{content['value']} of {content['suit']}")
                # Show dealer their cards
                print("Your cards")
                for card, content in currentPlayers[0]["cards"].items():
                    print(f"{content['value']} of {content['suit']}")
                print(f"{currentPlayers[0]['handPoints']} points")
                # Busted
                if currentPlayers[0]["handPoints"] > 7.5:
                    print(f"{currentPlayers[0]['handPoints']} in hand.\nBusted...")
                    pressEnter = input()
                    currentPlayers[0]["roundStatus"] = "busted"
                    continue
                else:
                    # Hit or settle
                    pointsToBeat = currentPlayers[0]["handPoints"]
                    for player in currentPlayers:
                        playerPoints = 0
                        if player["isDealer"] or player["roundStatus"] == "busted":
                            continue
                        else:
                            for card, content in player["cards"].items():
                                if content["hidden"]:
                                    continue
                                else:
                                    playerPoints += content["gameValue"]
                        if playerPoints > pointsToBeat:
                            pointsToBeat = player["handPoints"]

                    while pointsToBeat > currentPlayers[0]["handPoints"]:
                        print(f"{player['name']} asks for another card")
                        print("**********" * 3)
                        currentPlayers[0]["cards"][f"card{i}"] = gameCardDeck.pop(0)
                        currentPlayers[0]['handPoints'] += currentPlayers[0]["cards"][f"card{i}"]["gameValue"]
                    if currentPlayers[0]["handPoints"] <= 7.5:
                        print(f"{currentPlayers[0]['name']} has settled.")
                        currentPlayers[0]["status"] = "settled"
                        break
        else:
            # Human dealer
            currentPlayers[0]["roundStatus"] = "playing"
            print("Dealer's turn")
            while currentPlayers[0]["roundStatus"] == "playing":
                # Show cards on table
                print("Table")
                for playerTable in currentPlayers:
                    print(playerTable["name"])
                    for card, content in playerTable["cards"].items():
                        if not content["hidden"]:
                            print(f"{content['value']} of {content['suit']}")
                # Show dealer their cards
                print("Your cards")
                for card, content in currentPlayers[0]["cards"].items():
                    print(f"{content['value']} of {content['suit']}")
                print(f"{currentPlayers[0]['handPoints']} points")
                # Busted
                if currentPlayers[0]["handPoints"] > 7.5:
                    print(f"{currentPlayers[0]['handPoints']} in hand.\nBusted...")
                    pressEnter = input()
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
        print("**********" * 3)
        print("Total points for the round")
        losingPoints = 0
        winningPoints = 0
        for player in currentPlayers:
            if player["isDealer"]:
                continue
            elif player["roundStatus"] == "eliminated":
                continue
            else:
                points = player["bet"]
                # Busted
                if player["roundStatus"] == "busted":
                    if currentPlayers[0]["handPoints"] == 7.5:
                        points *= 2
                    if points > player["points"]:
                        losingPoints += player["points"]
                    else:
                        losingPoints += points
                    player["points"] -= points
                # Win
                elif player["handPoints"] > currentPlayers[0]["handPoints"]:
                    if player["handPoints"] == 7.5:
                        points *= 2
                    player["roundStatus"] = "winning"
                    player["payout"] = points
                    winningPoints += points
                # Lower points
                elif player["handPoints"] < currentPlayers[0]["handPoints"]:
                    if currentPlayers[0]["roundStatus"] == "busted":
                        player["roundStatus"] = "winning"
                        player["payout"] = points
                        winningPoints += points
                    elif currentPlayers[0]["handPoints"] == 7.5:
                        points *= 2
                        if points > player["points"]:
                            losingPoints += player["points"]
                        else:
                            losingPoints += points
                        player["points"] -= points
                    else:
                        if points > player["points"]:
                            losingPoints += player["points"]
                        else:
                            losingPoints += points
                        player["points"] -= points
                # Tie
                elif player["handPoints"] == currentPlayers[0]["handPoints"]:
                    if player["handPoints"] == 7.5:
                        points *= 4
                    if points > player["points"]:
                        losingPoints += player["points"]
                    else:
                        losingPoints += points
                    player["points"] -= points

        # Dealer's points

        currentPlayers[0]["points"] += losingPoints

        if winningPoints > currentPlayers[0]["points"]:
            for player in currentPlayers:
                if player["roundStatus"] == "winning":
                    if player["payout"] > currentPlayers[0]["points"]:
                        player["points"] += currentPlayers[0]["points"]
                        currentPlayers[0]["points"] = 0
                    else:
                        player["points"] += player["payout"]
                        currentPlayers[0]["points"] -= player["payout"]
                else:
                    continue
        else:
            currentPlayers[0]["points"] -= winningPoints
            for player in currentPlayers:
                if player == currentPlayers[0]:
                    continue
                elif player["roundStatus"] == "winning":
                    player["points"] += player["payout"]
        # Check for players without points
        for player in currentPlayers:
            if player["points"] <= 0 and player["gameStatus"] != "eliminated":
                player["gameStatus"] = "eliminated"
                print(f"{player['name']} has been eliminated")
                eliminatedPlayers += 1
                if player["points"] < 0:
                    player["points"] += player["points"] * -1
                # Change dealers
                if player["isDealer"]:
                    currentPlayers[0]["isDealer"] = False
                    currentPlayers.append(currentPlayers[0])
                    del currentPlayers[0]
                    currentPlayers[0]["isDealer"] = True
        # End of round points
        for player in currentPlayers:
            print(f"{player['name']}\nPoints: {player['points']}")
        print("**********" * 3)
        # Reset hand
        for player in currentPlayers:
            player["handPoints"] = 0
            player["cards"].clear()
        # End of round
    # End of game
    for player in currentPlayers:
        print(f"{player['name']}\nTotal points: {player['points']}")
    mostPointsPlayer = currentPlayers[0]
    for player in currentPlayers:
        if player["points"] > mostPointsPlayer["points"]:
            mostPointsPlayer = player
    print(f"The winner is {mostPointsPlayer['name']}")
    playAgain = input("Do you want to play again? (yes/no)")

    if playAgain.lower() == "no":
        print("Goodbye!")
        gameOn = False
    else:
        gameStart = True
        gameRound = 0
        samePlayers = input("Same players? (yes/no)")
        if samePlayers == "yes":
            choosingPlayers = False
            for player in currentPlayers:
                player["isDealer"] = False
                player["gameStatus"] = "playing"
                player["points"] = 20
        else:
            currentPlayers.clear()
            choosingPlayers = True
            numOfPlayers = 0
            botNum = 0
        continue
