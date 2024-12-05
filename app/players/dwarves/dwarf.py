from app.players import player
from abc import ABC


class Dwarf(player.Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

        # def get_rating(self) -> int:
        #     return 0
        #
        # def player_info(self) -> str:
        #     return f"player is {self.nickname}"

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
