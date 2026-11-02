import random
import math

N = 8

def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def simulated_annealing():

    current = [random.randint(0, 7) for _ in range(N)]

    T = 100
    alpha = 0.95
    iteration = 0

    print("Initial State:", current)
    print("Initial Cost:", cost(current))
    print("-" * 100)

    while T > 0.01:

        iteration += 1

        current_cost = cost(current)

        if current_cost == 0:
            print("\nSolution Found!")
            break

        new = current.copy()

        col = random.randint(0, 7)
        row = random.randint(0, 7)

        new[col] = row

        new_cost = cost(new)

        delta = current_cost - new_cost

        probability = 1.0

        if delta > 0:
            current = new
            status = "Accepted (Better)"

        else:
            probability = math.exp(delta / T)
            r = random.random()

            if r < probability:
                current = new
                status = "Accepted (Probability)"
            else:
                status = "Rejected"

        print("Iteration:", iteration)
        print("Current Cost:", current_cost)
        print("New Cost:", new_cost)
        print("Temperature:", round(T, 4))
        print("Probability:", round(probability, 4))
        print("Status:", status)
        print("-" * 100)

        T = T * alpha

    return current


solution = simulated_annealing()

print("\nFinal Solution:", solution)
print("Final Cost:", cost(solution))

print("\nChessboard:")

for row in range(N):
    for col in range(N):
        if solution[col] == row:
            print("Q", end=" ")
        else:
            print("-", end=" ")
    print()