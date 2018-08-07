from collections import Counter
l = [1, 1, 2, 2, 2, 2, 2, 3, 4, 10, 10, 10, 10, 10]
c = Counter(l)
[(i, c[i] / len(l) * 100.0) for i in c]
