class WorldModel:
    def __init__(self):
        self.world = {}

    def update(self, situation, result):
        self.world[situation] = result

    def predict(self, situation):
        return self.world.get(situation)

    def show(self):
        return self.world
