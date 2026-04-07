import random

def simulate_crashes(days):
    crash_prob = 0.045
    crashes = 0

    for i in range(days):
        r = random.random()

        if r < crash_prob:
            crashes += 1

    simulated_prob = crashes / days

    return crashes, simulated_prob

days_list = [20, 300, 1000]

for d in days_list:
    crashes, prob = simulate_crashes(d)
    print("Days: ",d)
    print("Total Crashes: ", crashes)
    print("Simulated Probability: ", prob)
    print()
