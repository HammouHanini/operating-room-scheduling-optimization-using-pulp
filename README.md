

## Problem Statement

A hospital has multiple operating rooms and a set of procedures that need to be performed. Not all operating rooms are suitable for each procedure and the time taken for a procedure may vary depending on the properties of the procedure and the operating room. The goal is to write a program that assigns procedures to operating rooms in such a way that the total time taken to perform the procedures is minimized.

## Properties of Procedures
- Unique identifier (str)
- Procedure type (str) - A, B, C, or D
- Severity (int) - 1, 2, or 3

## Properties of Operating Rooms
- Unique identifier (str)
- Speed factor for each procedure type (A, B, C, D) of type float. 0 indicates that the procedure cannot be performed in the room, while a value other than 0 represents the time taken to perform the procedure in the room.

## Constraints
- Every procedure must be assigned to an operating room in which it can be performed.
- Each operating room should only be used for a maximum of 8 hours per day.
- Total room occupation time in minutes must be tracked, including both the operating times and cleaning times.
- Cleaning time after a procedure must be added to the total duration of the procedure.
- Cleaning time depends on the type of procedure and is not influenced by the speed factor of the operating room.
- The standard duration of a procedure depends on the type and severity of the procedure.
- The actual duration of a procedure is influenced by the speed factor of the operating room.

## Cleaning Time
- 10 minutes for procedures of type A
- 15 minutes for procedures of type B
- 20 minutes for procedures of type C and D

| Procedure type | Severity 1 | Severity 2 | Severity 3 |
| --- | --- | --- | --- |
| A | 30 | 35 | 40 |
| B | 40 | 45 | 50 |
| C | 60 | 70 | 80 |
| D | 50 | 60 | 70 |

Table 1. Standard duration of a procedure as it depends on procedure type and severity.
