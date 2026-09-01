from core.prediction import PredictionEngine
from core.learning import LearningEngine


class SudhaAI:

    def __init__(self):
        self.prediction = PredictionEngine()
        self.learning = LearningEngine()

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

        print("\n--- SUDHA AI ---")
        print("Situation :", situation)
        print("Prediction:", predicted)
        print("Reality   :", actual_result)
        print("Difference:", experience["difference"])
        print("Learning  : Experience stored")

        return experience


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
