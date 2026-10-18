class MyAlign:

    def __init__(self, seqs, seq_type="dna"):
        self.listseqs = seqs
        self.seq_type = seq_type

    def num_seqs(self):
        return len(self.listseqs)

    def __len__(self):
        return len(self.listseqs[0])

    def __getitem__(self, n):
        return self.listseqs[n]

    def column(self, pos):

        res = []

        for seq in self.listseqs:
            res.append(seq[pos])

        return res

    def consensus(self):

        cons = ""

        for i in range(len(self)):

            col = self.column(i)

            counts = {}

            for c in col:

                if c == "-":
                    continue

                counts[c] = counts.get(c, 0) + 1

            best = max(counts, key=counts.get)

            cons += best

        return cons