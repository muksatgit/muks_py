class Club:
    def __init__(self, name):
        self.players = []
        self.name = name


    def __len__(self):
        return len(self.players)


    def __getItemAt__(self, i):
        return self.players[i]

    def __str__(self):
        return f"This is a club with name '{self.name}'"



myclub = Club("BMD Cricket Club")

myclub.players.append("Player 1")
myclub.players.append("Player 2")
myclub.players.append("Player 3")
myclub.players.append("Player 4")

print(myclub.players[0])
print(myclub)