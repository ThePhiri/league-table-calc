class TableGenerator(object):
    def readFile(self, file):
        self.results = {}
        self.file = file
        with open(self.file, 'r') as file:
            for line in file:
                self.splitLine = line.split()
                self.team1 = self.splitLine[0]
                self.team2 = self.splitLine[-2]
                if (int(self.splitLine[1][0]) > int(self.splitLine[-1])):

                    if self.team1 in self.results:
                        self.results[self.team1] += 3
                    else:
                        self.results.update({self.team1: 3})

                    if self.team2 in self.results:
                        self.results[self.team2] += 0
                    else:
                        self.results.update({self.team2: 0})

                if int(self.splitLine[1][0]) == int(self.splitLine[-1]):

                    if self.team1 in self.results:
                        self.results[self.team1] += 1
                    else:
                        self.results.update({self.team1: 1})

                    if self.team2 in self.results:
                        self.results[self.team2] += 1
                    else:
                        self.results.update({self.team2: 1})

                if int(self.splitLine[1][0]) < int(self.splitLine[-1]):

                    if self.team1 in self.results:
                        self.results[self.team1] += 0
                    else:
                        self.results.update({self.team1: 0})

                    if self.team2 in self.results:
                        self.results[self.team2] += 3
                    else:
                        self.results.update({self.team2: 3})

                allResults = self.results
            return allResults


class ShowRanking:
    soccer_results = TableGenerator()
    sorted_scores = []

    def sortResults(self):
        unsorted = self.soccer_results.readFile('input.txt')
        self.sorted_scores = sorted(
            unsorted.items(), key=lambda x: x[1], reverse=True)
        return self.sorted_scores

    def displayResults(self):
        sorted_results = self.sortResults()
        with open('output.txt', 'w') as f:
            for idx, team in enumerate(sorted_results):
                f.write('{0}. {1}, {2} pts\n'.format(
                    idx + 1, team[0], team[1]))


def main():
    finalTable = ShowRanking()
    finalTable.displayResults()


if __name__ == "__main__":
    main()
