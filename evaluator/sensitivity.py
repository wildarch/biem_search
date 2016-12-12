from .base import AbstractEvaluator


class SensitivityEvaluator(AbstractEvaluator):
    def name(self):
        return "Sensitivity"

    def __init__(self, data, cutoff):
        super().__init__(data)
        self.total_matches = 0
        self.cutoff = cutoff
        for entry in data:
            if entry[-1] == '1':
                self.total_matches += 1

    def evaluate(self, subgroup):
        matches_in_group = 0
        for index in subgroup[1]:
            if self.is_match(index):
                matches_in_group += 1
        #Sensitivity quality evaluator: p/P
        return matches_in_group / self.total_matches