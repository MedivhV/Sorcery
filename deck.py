## The players’ deck is a collection of cards which they may draw from
class Deck:
    
    ## Deck(n) consumes an integer n as the number of cards in the deck,
    ## _init_: int -> None
    def _init_(self, n):
        self._data = [None]* 30
        self._top = 0
        
    ## cardsleft() returns the number of cards left in this deck
    def cardsleft(self):
        return self._count
    