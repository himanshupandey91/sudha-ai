class CuriosityEngine:

    def score(self, prediction, reality):
        """
        Prediction और reality के बीच difference
        curiosity signal बनाता है।
        """

        if prediction is None:
            return 1.0

        if prediction != reality:
            return 1.0

        return 0.0

    def should_explore(self, curiosity_score):
        return curiosity_score > 0.5
