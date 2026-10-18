class SubstMatrix:
    def __init__(self):
        self.mat = {}

    def create_match_mismatch(self, alphabet, match, mismatch):
        for c1 in alphabet:
            for c2 in alphabet:
                if c1 == c2:
                    self.mat[(c1, c2)] = match
                else:
                    self.mat[(c1, c2)] = mismatch

    def score(self, c1, c2):
        return self.mat[(c1, c2)]