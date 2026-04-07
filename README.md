# Statistical Engine Project

## Project Overview
This project provides a Python-based statistical engine (StatEngine) capable of computing mean, median, mode, variance, standard deviation, and outliers for a given dataset. It also includes a Monte Carlo simulation (monte_carlo.py) to simulate crash probabilities over a period of days.

The goal is to demonstrate how statistical computations and simulations can be implemented in Python with proper handling of edge cases.

---

 Mathematical LogicMean**: Average of all numbers in the dataset. 

Median: Sort the list; if the number of elements is even, take the average of the two middle values; if odd, take the middle value. 


Mode: The most frequent value(s); if all values are unique, a message is returned. Variancece**:  
  - Population variance: σ² = Σ(x - μ)² / n  
  - Sample variance: s² = Σ(x - x̄)² / (n-1) 
  
  Standard Deviationon: Square root of the variance. 
  
  Outliersrs: Data points beyond a threshold number of standard deviations from the mean (default threshold = 2).

  Monte Carlo Simulationon: Repeated random trials simulate events (e.g., crashes) over a given number of days and estimate probabilities.

---

## Setup Instructions
Clone the repository:y:**
`bash
git clone https://github.com/fk-2code/statistical_engine.git
cd statistical_engine

## testing
python -m unittest tests/test_stat_engine.py
