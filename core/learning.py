class LearningEngine:
    def __init__(self):
        self.experiences = []

    def learn(self, situation, prediction, actual):
        difference = prediction != actual

        experience = {
            "situation": situation,
            "prediction": prediction,
            "actual": actual,
            "difference": difference
        }

        self.experiences.append(experience)

        return experience

    def get_experiences(self):
        return self.experiences
