class PairwiseAlignment:

    def __init__(self, subst_matrix, gap):
        self.sm = subst_matrix
        self.gap = gap

    def create_matrix(self, rows, cols):
        return[
            [0 for j in range(cols)]
            for i in range(rows)
        ]

    def needleman_wunsch(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2

        rows = len(seq1) + 1
        cols = len(seq2) + 1

        self.S = self.create_matrix(rows, cols)

        self.T = self.create_matrix(rows, cols)
        for i in range(1, rows):
            self.T[i][0] = "U"
        for j in range(1, cols):
            self.T[0][j] = "L"

        for i in range(rows):
            self.S[i][0] = i * self.gap
        for j in range(cols):
            self.S[0][j] = j * self.gap

        for i in range(1, rows):
            for j in range(1, cols):

                diag = self.S[i-1][j-1] + self.sm.score(seq1[i-1], seq2[j-1])
                up = (self.S[i-1][j] + self.gap)
                left = (self.S[i][j-1] + self.gap)

                best = max(diag, up, left)
                self.S[i][j] = best

                if best == diag:
                    self.T[i][j] = "D"
                elif best == up:
                    self.T[i][j] = "U"
                else:
                    self.T[i][j] = "L"
                    
        return self.S[-1][-1]

    def recover_alignment(self):
        i = len(self.seq1)
        j = len(self.seq2)

        aln1 = ""
        aln2 = ""

        while i > 0 or j > 0:
            move = self.T[i][j]

            if move == "D":
                aln1 = self.seq1[i-1] + aln1
                aln2 = self.seq2[j-1] + aln2

                i -= 1
                j -= 1

            elif move == "U":
                aln1 = self.seq1[i-1] + aln1
                aln2 = "-" + aln2

                i -= 1

            elif move == "L":
                aln1 = "-" + aln1
                aln2 = self.seq2[j-1] + aln2

                j -= 1

        return aln1, aln2