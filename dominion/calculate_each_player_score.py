class CalculateScore:
    def __init__(self, players_cards):
        self.players_cards = players_cards
        self.normal_card_scores = {
            "呪い": -1,
            "屋敷": 1,
            "公領": 3,
            "属州": 6,
            "植民地": 10,
            "大広間": 1,
            "貴族": 2,
            "ハーレム": 2,
            "島": 2,
            "坑道": 2,
            "農地": 2,
            "騎士": 2,
            "風車": 1,
            "墓地": 2,
            "遠い海岸": 2,
            "要塞": 2,
        }
        self.special_cards = ["庭園", "遠隔地", "公爵"]
        self.players_score = {}

    def _calculate_score(self, each_player_cards: dict[str, int]) -> int:
        """あるプレイヤーの持つカードに対して、その得点の合計を計算する

        Args:
            each_player_cards : あるプレイヤーの持つカード

        Returns:
            そのプレイヤー得点の合計
        """
        total_score = 0

        # カードの点数がそのまま得点になるカードについて計算する
        for card, point in self.normal_card_scores.items():
            if card in each_player_cards:
                total_score += each_player_cards[card] * point

        # 手札枚数などによって得点が変動するカードについて計算する
        for card in self.special_cards:

            # 庭園は山札の枚数/10（切り捨て）の勝利点となる
            if card == "庭園":
                card_count = sum(each_player_cards.values())
                total_score += (card_count // 10) * each_player_cards["庭園"]

        return total_score

    def set_players_score(self):
        """各プレイヤーの得点を記録する"""
        for player, each_player_cards in self.players_cards.items():
            self.players_score[player] = self._calculate_score(each_player_cards)
