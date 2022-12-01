        # self.scores1 = [100, 0, 90, 30, 20, 15, 60, 30, 88, 75, 100, 11]
        # self.scores2 = [50, 66]

def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse = True)
    return scores[0:3]

def sort_highest_to_lowest(scores):
    scores.sort(reverse = True)
    return scores