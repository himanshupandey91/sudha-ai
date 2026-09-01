from core.prediction import PredictionEngine
from core.learning import LearningEngine
from core.attention import AttentionEngine
from core.world_model import WorldModel
from memory.long_term import LongTermMemory


class SudhaAI:

    def __init__(self):
        self.prediction = PredictionEngine()
        self.learning = LearningEngine()
        self.attention = AttentionEngine()
        self.memory = LongTermMemory()
        self.world_model = WorldModel()

    def learn_from_experience(self, situation, result):
        self.prediction.learn(situation, result)
        self.world_model.update(situation, result)

    def observe(self, observations):

        # 1. Attention chooses what to focus on
        focus = self.attention.focus(observations)

        if focus is None:
            print("No observation.")
            return

        print("\n--- SUDHA AI ---")
        print("Observations:", observations)
        print("Attention:", focus)

        return focus


if __name__ == "__main__":

    sudha = SudhaAI()

    observations = [
        "sky is cloudy",
        "door is open",
        "alarm is ringing",
        "table is brown"
    ]

    sudha.observe(observations)
