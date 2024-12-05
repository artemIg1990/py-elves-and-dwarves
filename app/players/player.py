from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        return 0

    @abstractmethod
    def player_info(self) -> str:
        return "info about player"
