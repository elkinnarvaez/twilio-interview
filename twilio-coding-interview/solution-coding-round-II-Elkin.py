#!/bin/python3


import math
import os
import random
import re
import sys

from collections import deque

# There exist six airports identified by codes { SFO, YYZ, ORD, DFW, JFK, PVR }.
# There exist a number of flights between airports as follows:
# SFO -> PVR
# SFO -> ORD
# SFO -> YYZ
# ORD -> DFW
# DFW -> JFK
# YYZ -> JFK

# The above flights are uni-directional (one-way).
# Given two airports, for example (SFO, JFK), can one fly from one to the other given available flights?
# Try the following inputs:
# 1) SFO to JFK ? (answer = Yes)   In fact there are two possible routes: (SFO - YYZ - JFK) or (SFO - ORD - DFW - JFK)

# 2) JFK to PVR ? (answer = No)

airports = { 'SFO', 'YYZ', 'ORD', 'DFW', 'JFK', 'PVR'}
paths = [
    ('SFO', 'PVR'),
    ('SFO', 'ORD'),
    ('SFO', 'YYZ'),
    ('ORD', 'DFW'),
    ('DFW', 'JFK'),
    ('YYZ', 'JFK'),
    ('JFK', 'ORD'),
    ('ORD', 'SJC'),
    ('SJC', 'SFO')
]

def pathBetweenAirports(startingAirport, destinationAirport):
    graph = {}
    for u, v in paths:
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
    
    visited = set()
    previous = {startingAirport: None}
    stack = deque()
    stack.append(startingAirport)
    found = False
    while (len(stack) != 0 and not found):
        u = stack.pop()
        if u == destinationAirport:
            found = True
        else:
            if u in graph:
                for v in graph[u]:
                    if v not in visited:
                        stack.append(v)
                        visited.add(v)
                        previous[v] = u
    
    if (found):
        currentAirport = destinationAirport
        while(currentAirport != None):
            print(currentAirport, end = " ")
            currentAirport = previous[currentAirport]
    return found

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = pathBetweenAirports('JFK', 'SFO')
    print(result)
