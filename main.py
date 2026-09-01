from core.prediction import PredictionEngine
from core.learning import LearningEngine
from memory.long_term import LongTermMemory
from core.world_model import WorldModel


class SudhaAI:

    def __init__(self):
        self.prediction = PredictionEngine()
        self.learning = LearningEngine()
        self.memory = LongTermMemory()
        self.world_model = WorldModel()

    def learn_from_experience(self, situation, result):

        self.prediction.learn(situation, result)

        self.world_model.update(
            situation,
            result
        )

    def observe(self, situation, actual_result):

        predicted = self.prediction.predict(situation)

        if predicted is None:
            difference = "unknown"
        else:
            difference = predicted != actual_result

        experience = self.learning.learn(
            situation,
            predicted,
            actual_result
        )

        self.memory.store(experience)

        self.world_model.update(
            situation,
            actual_result
        )

        print("\n--- SUDHA AI ---")
        print("Situation :", situation)
        print("Prediction:", predicted)
        print("Reality   :", actual_result)
        print("Difference:", difference)
        print("World Model:", self.world_model.show())

    def remember(self, situation):

        memories = self.memory.recall(situation)

        print("\n--- MEMORY ---")

        for memory in memories:
            print(memory)


if __name__ == "__main__":

    sudha = SudhaAI()

    # Previous experience
    sudha.learn_from_experience(
        "traffic_light",
        "green"
    )

    # New observation
    sudha.observe(
        "traffic_light",
        "red"
    )

    # Recall
    sudha.remember(
        "traffic_light"
    )
