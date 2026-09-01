from core.prediction import PredictionEngine


class SudhaAI:
    def __init__(self):
        self.prediction = PredictionEngine()

    def learn_from_experience(self, situation, result):
        self.prediction.learn(situation, result)

    def observe(self, situation, actual_result):
        comparison = self.prediction.compare(
            situation,
            actual_result
        )

        print("\n--- Sudha AI Observation ---")
        print("Situation:", situation)
        print("Prediction:", comparison["predicted"])
        print("Reality:", comparison["actual"])
        print("Difference:", comparison["difference"])

        return comparison


if __name__ == "__main__":
    sudha = SudhaAI()

    # First experience
    sudha.learn_from_experience(
        "traffic_light",
        "green"
    )

    # New observation
    sudha.observe(
        "traffic_light",
        "red"
    )
