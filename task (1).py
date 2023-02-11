

import pulp
from pulp import *


class HospitalProcedureScheduling:
    def __init__(self):
        self._procedures = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14',
                            'P15', 'P16', 'P17', 'P18', 'P19', 'P20']
        self._operating_rooms = ['R1', 'R2', 'R3', 'R4']
        self._procedure_type = {'P1': 'C', 'P2': 'C', 'P3': 'D', 'P4': 'D', 'P5': 'B', 'P6': 'C', 'P7': 'A', 'P8': 'A',
                                'P9': 'D', 'P10': 'A', 'P11': 'D', 'P12': 'A', 'P13': 'D', 'P14': 'D', 'P15': 'B',
                                'P16': 'B', 'P17': 'A', 'P18': 'B', 'P19': 'C', 'P20': 'C'}
        self._procedure_severity = {'P1': 2, 'P2': 1, 'P3': 2, 'P4': 1, 'P5': 3, 'P6': 3, 'P7': 2, 'P8': 1, 'P9': 2,
                                    'P10': 1, 'P11': 1, 'P12': 1, 'P13': 1, 'P14': 2, 'P15': 1, 'P16': 2, 'P17': 3,
                                    'P18': 3, 'P19': 1, 'P20': 3}
        self._operating_room_factors = {('R1', 'A'): 0.8, ('R1', 'B'): 0.9, ('R1', 'C'): 1.3, ('R1', 'D'): 1.3,
                                        ('R2', 'A'): 1.3, ('R2', 'B'): 0.0, ('R2', 'C'): 0.0, ('R2', 'D'): 0.8,
                                        ('R3', 'A'): 0.0, ('R3', 'B'): 0.6, ('R3', 'C'): 0.0, ('R3', 'D'): 0.9,
                                        ('R4', 'A'): 0.0, ('R4', 'B'): 1.0, ('R4', 'C'): 1.4, ('R4', 'D'): 0.0}
        self._operating_room_time = {('A',1): 30, ('B', 1): 40, ('C', 1): 60, ('D', 1): 50,
                                        ('A', 2): 35, ('B', 2): 45, ('C', 2): 70, ('D', 2): 60,
                                        ('A', 3): 40, ('B', 3): 50, ('C', 3):80, ('D', 3): 70}
        self._room_occupation_times = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0}
        

    def solve(self):
        # Adapt this function to create your LP solver for the specified problem.
        # You are free to add your own 'helper' functions as you see fit.
        self._problem = pulp.LpProblem("operation minization",LpMinimize)
        
        #Define variables
        self.X = LpVariable.dicts(
            "Variable",
            [(r, p) for r in self._operating_rooms for p in self._procedures], 
            lowBound = 0, 
            cat = "Binary")
        # Add the constraints
        
        #1 
        for r in self._operating_rooms:
            self._room_occupation_times[r]=lpSum([ 
            ((30 if self._procedure_type[p] == 'A' and self._procedure_severity[p] == 1 else
             40 if self._procedure_type[p] == 'B' and self._procedure_severity[p] == 1 else
             60 if self._procedure_type[p] == 'C' and self._procedure_severity[p] == 1 else
             50 if self._procedure_type[p] == 'D' and self._procedure_severity[p] == 1 else
             35 if self._procedure_type[p] == 'A' and self._procedure_severity[p] == 2 else
             45 if self._procedure_type[p] == 'B' and self._procedure_severity[p] == 2 else
             70 if self._procedure_type[p] == 'C' and self._procedure_severity[p] == 2 else
             60 if self._procedure_type[p] == 'D' and self._procedure_severity[p] == 2 else
             40 if self._procedure_type[p] == 'A' and self._procedure_severity[p] == 3 else
             50 if self._procedure_type[p] == 'B' and self._procedure_severity[p] == 3 else
             80 if self._procedure_type[p] == 'C' and self._procedure_severity[p] == 3 else
             70) * self._operating_room_factors[(r, self._procedure_type[p])] +
            (10 if self._procedure_type[p] == 'A' else 15 if self._procedure_type[p] == 'B' else 20))*self.X[(r, p)] 
            for p in self._procedures ])
            self._problem += self._room_occupation_times[r] <= 480,r
        #2
        for p in self._procedures:
            self._problem += lpSum([self.X[(r, p)] for r in self._operating_rooms]) >=1,p
        
        #3
        for r in self._operating_rooms:
            for p in self._procedures:
                self._problem += self.X[(r, p)]<=100*self._operating_room_factors[r,self._procedure_type[p]],r+ " , "+p

            
        #Add the objective function
        self._problem += lpSum([ 
            ((30 if self._procedure_type[p] == 'A' and self._procedure_severity[p] == 1 else
             40 if self._procedure_type[p] == 'B' and self._procedure_severity[p] == 1 else
             60 if self._procedure_type[p] == 'C' and self._procedure_severity[p] == 1 else
             50 if self._procedure_type[p] == 'D' and self._procedure_severity[p] == 1 else
             35 if self._procedure_type[p] == 'A' and self._procedure_severity[p] == 2 else
             45 if self._procedure_type[p] == 'B' and self._procedure_severity[p] == 2 else
             70 if self._procedure_type[p] == 'C' and self._procedure_severity[p] == 2 else
             60 if self._procedure_type[p] == 'D' and self._procedure_severity[p] == 2 else
             40 if self._procedure_type[p] == 'A' and self._procedure_severity[p] == 3 else
             50 if self._procedure_type[p] == 'B' and self._procedure_severity[p] == 3 else
             80 if self._procedure_type[p] == 'C' and self._procedure_severity[p] == 3 else
             70) * self._operating_room_factors[(r, self._procedure_type[p])] +
            (10 if self._procedure_type[p] == 'A' else 15 if self._procedure_type[p] == 'B' else 20))*self.X[(r, p)] 
            for p in self._procedures for r in self._operating_rooms])
            
            
            
            
        self._problem.solve()
        # Adapt this line.
        solution=[]
        for p in self._procedures:
            for r in self._operating_rooms :
                if self.X[(r,p)].varValue >=0.1:
                    solution.append((p,r))
           
        return solution # Adapt this line.

 

##########################
##### SOLUTION CHECK #####
##########################



problem = HospitalProcedureScheduling()
solution = problem.solve()
print("- An optimal solution was found:", problem._problem.status == 1)
print("- The solution contains an assignment:", len(solution) > 0)
print("- The assignment is a list of tuples:", type(solution) == list and len(solution) > 0 and type(solution[0]) == tuple)
print("- All procedures in the assignment are part of the problem description:", all([j in problem._procedures for (j, m) in solution]))
print("- All operating_rooms in the assignment are part of the problem description:", all([m in problem._operating_rooms for (j, m) in solution]))







