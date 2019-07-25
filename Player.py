
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return "Player({}, {})".format(self.name, self.score)
  
    # def comparator(a, b):
    #     if a.score < b.score: return 1
    #     if a.score > b.score: return -1
    #     if a.name < b.name: return -1
    #     if a.name > b.name: return 1
    #     return 0

    def key(self):
        return (-self.score, self.name)

        
if __name__ == "__main__":
    a = Player("Amit", 6)
    b = Player("Vanessa", 18)
    c = Player("Apple", 18)

    list_players = [a, b, c]

    print(sorted([a, b, c], key=Player.key))

