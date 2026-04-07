import json

from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes


# Load salary data
with open("data/sample_salaries.json") as f:

    salaries = json.load(f)


engine = StatEngine(salaries)


print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())

print(
    "Sample Variance:",
    engine.get_variance(True)
)

print(
    "Population Variance:",
    engine.get_variance(False)
)

print(
    "Standard Deviation:",
    engine.get_standard_deviation()
)

print(
    "Outliers:",
    engine.get_outliers()
)


# Monte Carlo Simulation
crashes, prob = simulate_crashes(365)

print("\nMonte Carlo Simulation")
print("Crashes:", crashes)
print("Probability:", prob)
