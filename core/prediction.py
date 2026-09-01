class PredictionEngine:
    def __init__(self):
        self.predictions = {}

    def predict(self, situation):
        if situation in self.predictions:
            return self.predictions[situation]

        return None

    def learn(self, situation, actual_result):
        self.predictions[situation] = actual_result

    def compare(self, situation, actual_result):
        predicted = self.predict(situation)

        if predicted is None:
            return {
                "predicted": None,
                "actual": actual_result,
                "difference": "No previous prediction"
            }

        difference = predicted != actual_result

        return {
            "predicted": predicted,
            "actual": actual_result,
            "difference": difference
        }
