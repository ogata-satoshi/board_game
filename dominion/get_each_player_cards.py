import re
from collections import defaultdict


class PlayersCards:
    def __init__(self):
        self.log_lines = self._set_log_lines()
        self.players = self._get_players_from_log()
        self.players_cards = self._init_players_cards()

    def _set_log_lines(self) -> list[str]:
        """ログの前処理をしながらログの行のリストを返す

        Returns:
            前処理済みのログの行のリスト
        """
        with open("log.text", "r") as f:
            lines = f.read().split('。')

        # 前処理する
        # 冒頭に空白文字列が含まれているだめ除去する
        lines = [line.lstrip() for line in lines]
        # 空白行が邪魔なため除去する
        lines = [line for line in lines if line]

        return lines

    def _get_players_from_log(self) -> list[str]:
        """ログのテキストからプレイヤー一覧を取得する

        Returns:
            プレイヤー名のリスト
        """
        players = []

        for line in self.log_lines:
            # 「屋敷を受け取った」というログは初回のみ吐き出され、各プレイヤー1度しか出現せず、
            #  このログの冒頭がプレイヤー名を表すため、そこからプレイヤー名を特定する
            if line.endswith("屋敷を受け取った"):
                players.append(line[0])

        return players

    def _init_players_cards(
        self,
    ) -> dict[str, dict[str, int]]:
        """各プレイヤーの初期手札を作成する

        Arguments:
            players: 各プレイヤーの名称のリスト

        Returns:
            各プレイヤーの初期手札の辞書
        """
        players_cards = {p: defaultdict(int) for p in self.players}
        for _, cards in players_cards.items():
            cards["屋敷"] = 3
            cards["銅貨"] = 7
        return players_cards

    def set_players_cards(self):
        """各プレイヤーの所持する各カードの枚数を記録する"""
        for line in self.log_lines:
            player_name = line[0]
            if player_name not in self.players:
                continue

            # カードを獲得した場合に追加する。
            got_card_match = re.match(f"{player_name}は(.*)を(購入・)?獲得した", line)
            if got_card_match:
                card_name = got_card_match.group(1)
                self.players_cards[player_name][card_name] += 1

            # カードを破棄した場合に減らす
            remove_card_match = re.match(f"{player_name}は(.*)を廃棄した", line)
            if remove_card_match:
                card_name = remove_card_match.group(1)
                self.players_cards[player_name][card_name] -= 1
