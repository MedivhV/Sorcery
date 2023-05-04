## the player will either be at active or non-avtive status
## A player’s board is a collection of cards which they have 
## played and which have not been moved to another zone.
## The players’ hand is a collection of cards (to a maximum of 5) which they may play

class Player:
    ## the first slot in player's board is a placeholder for any spells
    ## the player's board can host up to 5 minions.
    ##Player(name) consumes a str name, and creates a player with the name
    ##_init_: str -> None
    def _init_(self, name):
        self._name = name
        self._hp = 20
        self._board = [None] * 6
        self._hand = [None, None, None, None, None]
        self._status = "deactived"

    ## player.statuschange() mutates the status of the player
    ## 
    def statuschange(self):
        if self._status == "deactived":
            self.status = "actived"
        else:
            self.status = "deactived"
        print("player"+ self._name + "is now" + self.status )

    ## health(num, action) consumes an int and a str, mutates the player's hp
    ## health: int, str -> None
    def health(self, num, action):
        if action == "+":
            self._hp = self._hp + num
        elif action == "-":
            self_hp = self._hp - num