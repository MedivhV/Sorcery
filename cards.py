## Cards are the basic objects in Sorcery, making up players’ decks, hands, and graveyards
from player import all
class Minion:
    ## _init_: int str Player -> None
    def _init_(self, cost, name, owner):
        self._type = "minion"
        self._name = name
        self._cost = cost
        self._owner = owner