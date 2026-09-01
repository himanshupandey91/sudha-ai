from core.prediction import PredictionEngine
from core.learning import LearningEngine
from memory.long_term import LongTermMemory


class SudhaAI:

    def __init__(self):
        self.prediction = PredictionEngine()
        self.learning = LearningEngine()
        self.memory = LongTermMemory()

    def learn_from_experience(self, situation, result):
        self.prediction.learn(situation, result)

    def observe(self, situation, actual_result):

        comparison = self.prediction.compare(
            situation,
            actual_result
        )

        predicted = comparison["predicted"]

        experience = self.learning.learn(
            situation,
            predicted,
            actual_result
        )

        self.memory.store(experience)

        print("\n--- SUDHA AI ---")
        print("Situation :", situation)
        print("Prediction:", predicted)
        print("Reality   :", actual_result)
        print("Difference:", experience["difference"])
        print("Memory    : Experience stored")

        return experience

    def remember(self, situation):

        memories = self.memory.recall(situation)

        print("\n--- MEMORY ---")

        if not memories:
            print("No memory found.")
            return

        for memory in memories:
            print(memory)


if __name__ == "__main__":

    sudha = SudhaAI()

    # First experience
    sudha.learn_from_experience(
        "traffic_light",
        "green"
    )

    # Observe reality
    sudha.observe(
        "traffic_light",
        "red"
    )

    # Recall memory
    sudha.remember(
        "traffic_light"
    )
