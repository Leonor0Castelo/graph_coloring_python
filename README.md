# Chromatic Number with Evolutionary Computation

A Python simulator that approximates the **chromatic number** of a graph using
evolutionary computation. Group project for the course *Elementos de Programação*
(Elements of Programming), Instituto Superior Técnico, October 2023. The report is
written in Portuguese.

## Overview

A proper coloring of an undirected graph gives different colors to vertices joined by
an edge. The chromatic number is the smallest number of colors for which this is
possible. Finding it is an NP-hard combinatorial optimisation problem, so this project
uses a stochastic, evolution-inspired heuristic to find a good approximation instead
of an exact solution.

A population of candidate colorings evolves over simulated time through three kinds of
random events, scheduled with exponentially distributed waiting times:

| Event | Effect |
|-------|--------|
| **Evaluation** (`av`) | An individual may die. The death probability depends on its fitness and age: `1 - (2/π) · arctan((1 + A)^(1 + 8/(1 + I)))`, where `A` is the fitness and `I` the age. |
| **Evolution** (`ev`) | An individual mutates with probability `1 / (1 + e^((K - T)/10))`, where `K` is the initial population size and `T` the current size. Otherwise it reproduces. A mutation changes the color of one node and is kept only if it improves fitness. |
| **Selection** (`sel`) | All individuals with an invalid coloring die. If all colorings are valid, the worst individuals die until the population is at most 3/2 of the initial size. |

**Fitness:** for a valid coloring, `number of nodes / number of colors used`. For an
invalid coloring, `1 / (1 + number of defective edges)`.

The simulation keeps an agenda of pending events (CAP), processes them in time order,
and at the end plots the population size over time and returns the number of colors of
the best individual.

## Modules

| Module | Contents |
|--------|----------|
| `grafos.py` | Graph type: create graphs, add and remove edges, list nodes, edge checks |
| `coloration.py` | Colorings: create a coloring, validity check, number of colors, number of defects |
| `individuals.py` | Individuals: birth time, id, fitness, mutation and reproduction |
| `pop.py` | Population: initial population, add and remove individuals, best individual, death and selection |
| `event.py` | Events: time, kind and individual |
| `cap.py` | Agenda of pending events, kept ordered by time |
| `exprandom.py` | Exponentially distributed random variable |
| `[simulator file]` | Main simulation loop, `sim(ht, tri, tlim, tfil, G, k)` |

## Requirements

- Python 3
- `matplotlib` (for the population plot)

## How to run

The simulator is the function `sim(ht, tri, tlim, tfil, G, k)`:

| Parameter | Meaning |
|-----------|---------|
| `ht` | Time limit of the simulation |
| `tri` | Mean time between evolution events |
| `tlim` | Mean time between evaluation events |
| `tfil` | Time between selection events |
| `G` | The graph |
| `k` | Size of the initial population |

```python
import grafos
from [simulator file] import sim

G = grafos.newgraph(10)
# add the edges of your graph with grafos.addedge(G, x, y)

print(sim(100, [tri], [tlim], [tfil], G, 100))
```

It plots the population size over time and returns the number of colors of the best
coloring found.

## Results

The simulator was tested on the **Petersen graph**, whose chromatic number is known to
be 3.

| Run | Change | Result |
|-----|--------|--------|
| 1 | Initial population 100, time limit 100 | **3 colors** (correct) |
| 2 | Same as run 1, with `tri`, `tlim` and `tfil` tripled | 4 colors, slower convergence |
| 3 | Same as run 2, initial population reduced to 20 | 5 colors, needs more time |
| 4 | Same as run 3, time limit raised to 200 | **3 colors** (correct) |

These runs show how the search depends on its settings: slower event rates and smaller
populations need more simulated time to reach the optimum, and a longer run recovers
the correct answer.
