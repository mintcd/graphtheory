from infer import similarity_infer, isomorphism_infer
from graph import generate
import time
import matplotlib.pyplot as plt


def check(G, H):
    rels = similarity_infer(G, H)
    if type(rels) is not bool:
        isomorphism_infer(rels, G, H)


def similar_test(r, dim, equidistant=False):
    if equidistant:
        times = []
        for i in range(r):
            data = generate(
                v=3 * (i + 2), dim=dim, shuffle=True, equidistant=equidistant
            )
            start = time.time()
            check(data.original, data.similar)
            end = time.time()
            times.append(end - start)
        plt.plot(range(6, 3 * r + 6, 3), times, marker="o", linestyle="-", color="b")
        plt.xlabel("Number of vertices")
        plt.ylabel("Time (seconds)")
        plt.grid(True)
        plt.show()
    else:
        times = []
        for i in range(r):
            data = generate(v=i + 10, dim=dim, shuffle=True, equidistant=equidistant)
            start = time.time()
            check(data.original, data.similar)
            end = time.time()
            times.append(
                end - start
            )  # Fix the time calculation, it should be end - start

        plt.plot(range(10, r + 10, 1), times, marker="o", linestyle="-", color="b")
        plt.xlabel("Number of vertices")
        plt.ylabel("Time (seconds)")
        plt.grid(True)
        plt.show()
