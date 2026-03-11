This project was developed for the course Intel·ligència Artificial in the Bachelor’s Degree in Artificial Intelligence at FIB (UPC). It implements a local search solution to solve the Azamon problem: an optimization challenge focused on assigning packages to transportation offers efficiently.

The goal of the project is to manage the logistics of a company that receives packages with specific deadlines and must assign them to various transport offers. Each assignment has an associated cost and a potential "unhappiness" factor (delay).

The system focuses on optimizing two main functions:
- Cost Minimization: Reducing the total price paid for transport and warehouse storage.
- Unhappiness Minimization: Prioritizing faster delivery to ensure customer satisfaction.

Key Features:
- State Representation: A mapping of packages to specific transport offers.
- Heuristic Functions: Mathematical functions that evaluate the "quality" of a solution based on economic and temporal criteria.
- Search Strategies:
   Hill Climbing: A greedy approach that always moves towards the best neighbor.
   Simulated Annealing: A probabilistic technique that allows "bad" moves to escape local optima, controlled by a temperature parameter.
- Operators: Defined moves like SWAP (exchanging transport for two packages) or MOVE (changing a package's transport).

