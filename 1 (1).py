import pulp


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
        self._room_occupation_times = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0}

    def solve(self):
        # Adapt this function to create your LP solver for the specified problem.
        # You are free to add your own 'helper' functions as you see fit.
        self._problem = pulp.LpProblem() # Adapt this line.
        return [] # Adapt this line.










##########################
##### SOLUTION CHECK #####
##########################

print("\n\nDISCLAIMER\nNote that if you pass the solution check that does not mean that you will get full points. " +
      "We will test more and different things. Also note that you should see DONE at the end of the tests. " +
      "If you do not see DONE, this means that the program got stuck somewhere and consequently does not work properly. " +
      "Finally, note that you must use all attributes and functions that are defined in the template and give them correct values according to the assignment description. " +
      "You must not change names or signatures of predefined classes, attributes or functions. Doing so may lead to severe deduction of points. " +
      "\n\nSOLUTION CHECK\n" +
      "All of the following should be True:")

problem = HospitalProcedureScheduling()
solution = problem.solve()
print("- An optimal solution was found:", problem._problem.status == 1)
print("- The solution contains an assignment:", len(solution) > 0)
print("- The assignment is a list of tuples:", type(solution) == list and len(solution) > 0 and type(solution[0]) == tuple)
print("- All procedures in the assignment are part of the problem description:", all([j in problem._procedures for (j, m) in solution]))
print("- All operating_rooms in the assignment are part of the problem description:", all([m in problem._operating_rooms for (j, m) in solution]))

problem = HospitalProcedureScheduling()
problem._procedures = ['P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P110', 'P111', 'P112', 'P113', 'P114', 'P115',
                       'P116', 'P117', 'P118', 'P119', 'P120']
problem._operating_rooms = ['R11', 'R12', 'R13', 'R14']
problem._procedure_type = {'P11': 'B', 'P12': 'A', 'P13': 'D', 'P14': 'D', 'P15': 'D', 'P16': 'B', 'P17': 'A', 'P18': 'D',
                           'P19': 'B', 'P110': 'C', 'P111': 'C', 'P112': 'B', 'P113': 'C', 'P114': 'D', 'P115': 'A',
                           'P116': 'C', 'P117': 'B', 'P118': 'D', 'P119': 'A', 'P120': 'B'}
problem._procedure_severity = {'P11': 1, 'P12': 3, 'P13': 3, 'P14': 1, 'P15': 2, 'P16': 2, 'P17': 1, 'P18': 2, 'P19': 2,
                               'P110': 1, 'P111': 3, 'P112': 3, 'P113': 1, 'P114': 3, 'P115': 3, 'P116': 3, 'P117': 1, 'P118': 3,
                               'P119': 3, 'P120': 1}
problem._operating_room_factors = {('R11', 'A'): 1.4, ('R11', 'B'): 0.0, ('R11', 'C'): 0.9, ('R11', 'D'): 1.5,
                                   ('R12', 'A'): 1.5, ('R12', 'B'): 0.8, ('R12', 'C'): 1.1, ('R12', 'D'): 1.2,
                                   ('R13', 'A'): 0.0, ('R13', 'B'): 1.3, ('R13', 'C'): 0.6, ('R13', 'D'): 1.0,
                                   ('R14', 'A'): 0.6, ('R14', 'B'): 1.0, ('R14', 'C'): 1.3, ('R14', 'D'): 1.3}
problem._room_occupation_times = {'R11': 0, 'R12': 0, 'R13': 0, 'R14': 0}
solution = problem.solve()
print("- the solution properly uses the procedures from the constructor and does not change the constructor:", all([p in problem._procedures for (p, r) in solution]))
print("- the solution properly uses the operating_rooms from the constructor and does not change the constructor:", all([r in problem._operating_rooms for (p, r) in solution]))
print("DONE\n")


###################################################################################################################
#### DO NOT TOUCH THE CODE BELOW
#### IT IS USED FOR GRADING
###################################################################################################################

class Tester:

    def __init__(self):
        self._procedures = ['testP1', 'testP2', 'testP3', 'testP4', 'testP5', 'testP6', 'testP7', 'testP8', 'testP9',
                            'testP10']
        self._operating_rooms = ['testR1', 'testR2', 'testR3', 'testR4']
        self._procedure_type = {'testP1': 'B', 'testP2': 'C', 'testP3': 'B', 'testP4': 'D', 'testP5': 'D',
                                'testP6': 'A', 'testP7': 'D', 'testP8': 'C', 'testP9': 'C', 'testP10': 'B'}
        self._procedure_severity = {'testP1': 2, 'testP2': 1, 'testP3': 3, 'testP4': 1, 'testP5': 2, 'testP6': 2,
                                    'testP7': 2, 'testP8': 3, 'testP9': 2, 'testP10': 1}
        self._operating_room_factors = {('testR1', 'A'): 0.0, ('testR1', 'B'): 0.0, ('testR1', 'C'): 0.8,
                                        ('testR1', 'D'): 0.5, ('testR2', 'A'): 1.1, ('testR2', 'B'): 0.9,
                                        ('testR2', 'C'): 0.5, ('testR2', 'D'): 0.8, ('testR3', 'A'): 0.0,
                                        ('testR3', 'B'): 1.2, ('testR3', 'C'): 1.4, ('testR3', 'D'): 1.3,
                                        ('testR4', 'A'): 0.0, ('testR4', 'B'): 0.0, ('testR4', 'C'): 1.1,
                                        ('testR4', 'D'): 0.8}
        self._room_occupation_times = {'testR1': 0, 'testR2': 0, 'testR3': 0, 'testR4': 0}

        self._problem = HospitalProcedureScheduling()
        self._problem._procedures = self._procedures
        self._problem._operating_rooms = self._operating_rooms
        self._problem._procedure_type = self._procedure_type
        self._problem._procedure_severity = self._procedure_severity
        self._problem._operating_room_factors = self._operating_room_factors
        self._problem._room_occupation_times = self._room_occupation_times
        self._solution = self._problem.solve()
        self._performed_procedures = set([p for (p, r) in self._solution])
        self._all_scheduled = self._performed_procedures == set(self._procedures)

    def test_1(self):
        points = 3
        message = "an optimal solution was found"
        passed = self._problem._problem.status == 1
        return {'passed': passed, 'points': points if passed else 0, 'message': message}

    def test_2(self):
        points = 3
        message = "all procedures are scheduled and no additional procedures are scheduled"
        passed = self._all_scheduled
        return {'passed': passed, 'points': points if passed else 0, 'message': message}

    def test_3(self):
        points = 3
        message = "all operating_rooms are within capacity"
        passed = self._all_scheduled and all(
            [sum([(30 if self._procedure_type[p] == 'A' and self._procedure_severity == 1 else
                   40 if self._procedure_type[p] == 'B' and self._procedure_severity == 1 else
                   60 if self._procedure_type[p] == 'C' and self._procedure_severity == 1 else
                   50 if self._procedure_type[p] == 'D' and self._procedure_severity == 1 else
                   35 if self._procedure_type[p] == 'A' and self._procedure_severity == 2 else
                   45 if self._procedure_type[p] == 'B' and self._procedure_severity == 2 else
                   70 if self._procedure_type[p] == 'C' and self._procedure_severity == 2 else
                   60 if self._procedure_type[p] == 'D' and self._procedure_severity == 2 else
                   40 if self._procedure_type[p] == 'A' and self._procedure_severity == 3 else
                   50 if self._procedure_type[p] == 'B' and self._procedure_severity == 3 else
                   80 if self._procedure_type[p] == 'C' and self._procedure_severity == 3 else
                   70) * self._operating_room_factors[(r, self._procedure_type[p])] for (p, rp) in
                  self._solution if
                  rp == p]) <= 480
             for r in self._operating_rooms])
        return {'passed': passed, 'points': points if passed else 0, 'message': message}

    def test_4(self):
        points = 3
        message = "all operating rooms are within capacity when also considering cleaning times"
        passed = self._all_scheduled and all([sum([
            (30 if self._procedure_type[p] == 'A' and self._procedure_severity[p] == 1 else
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
             70) * self._operating_room_factors[(r, self._procedure_type[p])] + (
                10 if self._procedure_type[p] == 'A'
                else 15 if self._procedure_type[p] == 'B' else 20)
            for (p, rp) in self._solution if rp == r]) <= 480 for r in self._operating_rooms])
        return {'passed': passed, 'points': points if passed else 0, 'message': message}

    def test_5(self):
        points = 3
        message = "all procedures are scheduled on a operating_room that can perform it"
        passed = self._all_scheduled and all(
            [self._operating_room_factors[(r, self._procedure_type[p])] > 0 for (p, r) in
             self._solution])
        return {'passed': passed, 'points': points if passed else 0, 'message': message}

    def test_6(self):
        points = 5
        message = "all operating_rooms have correct procedure durations listed"
        passed = self._all_scheduled and all([sum([
            (30 if self._procedure_type[p] == 'A' and self._procedure_severity[p] == 1 else
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
            (10 if self._procedure_type[p] == 'A' else 15 if self._procedure_type[p] == 'B' else 20)
            for (p, rp) in self._solution if rp == r]) == self._problem._room_occupation_times[r] for r in
                                              self._operating_rooms])
        return {'passed': passed, 'points': points if passed else 0, 'message': message}

    def test_7(self):
        points = 5
        message = "optimization result is close to minimal time"
        passed = self._all_scheduled and sum(
            [(30 if self._procedure_type[p] == 'A' and self._procedure_severity == 1 else
              40 if self._procedure_type[p] == 'B' and self._procedure_severity == 1 else
              60 if self._procedure_type[p] == 'C' and self._procedure_severity == 1 else
              50 if self._procedure_type[p] == 'D' and self._procedure_severity == 1 else
              35 if self._procedure_type[p] == 'A' and self._procedure_severity == 2 else
              45 if self._procedure_type[p] == 'B' and self._procedure_severity == 2 else
              70 if self._procedure_type[p] == 'C' and self._procedure_severity == 2 else
              60 if self._procedure_type[p] == 'D' and self._procedure_severity == 2 else
              40 if self._procedure_type[p] == 'A' and self._procedure_severity == 3 else
              50 if self._procedure_type[p] == 'B' and self._procedure_severity == 3 else
              80 if self._procedure_type[p] == 'C' and self._procedure_severity == 3 else
              70) * self._operating_room_factors[(r, self._procedure_type[p])] + (
                 10 if self._procedure_type[p] == 'A' else 15 if self._procedure_type[
                                                                              p] == 'B' else 20)
             for (p, r) in self._solution]) <= 1600
        return {'passed': passed, 'points': points if passed else 0, 'message': message}

    def print_tests(self):
        print("TESTS")
        total_points = 0
        for m in dir(self):
            if (m.startswith('test_')):
                try:
                    test_result = getattr(self, m)()
                    if m == "test_0":
                        if test_result == False:
                            break
                    else:
                        print(test_result)
                        total_points += test_result['points']
                except BaseException as e:
                    print({'passed': False, 'points': 0, 'message': 'Exception in test ' + m + ':' + repr(e)})
        print("TOTAL: " + str(total_points))


if __name__ == '__main__':
    tt = Tester()
    tt.print_tests()
