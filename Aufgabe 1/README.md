# Chronological Sort
Data structures & algorithms - Summer 2021

_Python Version 3.9+_

## Input & Output of Algorithm
- Sorts a list of dates and text first in ascending order by date and then by text

**Input:**
```
31.12.1970    aaa
31.12.1970    a
31.12.1970    ab
01.01.1970    Unix-Null
```
**Output:**
```
01.01.1970    Unix-Null
31.12.1970    a
31.12.1970    aaa
31.12.1970    ab
```

## Using Heapsort
**Run command:**
```
python3 chronological_sort.py -heap <filename>
```

## Using Quicksort
**Run command:**
```
python3 chronological_sort.py -quick <filename>
```

## Test Running Time
**Run command:**
```
python3 test.py -time <filename>
```

## Test Correctness
**Run command:**
```
python3 test.py -check
```
