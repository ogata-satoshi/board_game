from calculate_each_player_score import CalculateScore
from get_each_player_cards import PlayersCards


def main():
    players_cards = PlayersCards()
    players_cards.set_players_cards()
    for player, card in players_cards.players_cards.items():
        print(player, card)
    calculate = CalculateScore(players_cards.players_cards)
    calculate.set_players_score()

    for player, score in calculate.players_score.items():
        print(player, score)


if __name__ == "__main__":
    main()
