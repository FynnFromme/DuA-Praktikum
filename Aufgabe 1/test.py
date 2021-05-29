import os, sys
from timeit import timeit

#? Usage: python test.py < -check / -time > (optional filename)

if len(sys.argv) <= 1:
    # No arguments
    print('\033[31mPlease provide either -check or -time as first argument.\033[0m')
    exit()

if sys.argv[1] == '-time':  # Time of algorithm
    if len(sys.argv) <= 2:
        # No filename
        print('\033[31mPlease provide filename as second argument.\033[0m')
        exit()
        
    # Get time of specific input file
    heap_time = timeit(lambda: os.system(
        f'python3 chronological_sort.py -heap {sys.argv[2]}'), number=1)
    quick_time = timeit(lambda: os.system(
        f'python3 chronological_sort.py -quick {sys.argv[2]}'), number=1)

    # Output time
    print(chr(27) + "[2J")
    print('\033[92mHeap sort:', heap_time)
    print('Quick sort:', quick_time, '\033[0m')

elif sys.argv[1] == '-check':  # Check whether the algorithm is correct
    # Check every test instance
    for filename in os.listdir('pubInst/'):
        if not filename.endswith('.txt'):
            continue
        
        # Get the result of quick sort
        os.system(f'python3 chronological_sort.py -quick --test pubInst/{filename}')
        with open('./tmp.txt', 'r') as q:
            res_quick = q.read()
            
        # Get the result of heap sort
        os.system(
            f'python3 chronological_sort.py -heap --test pubInst/{filename}')
        with open('./tmp.txt', 'r') as h:
            res_heap = h.read()
        
        # Get the solution of the algorithm
        with open(f'pubInst/{filename}.sol', 'r') as s:
            sol = s.read()
            if sol.endswith('\n'):
                sol = sol[:-1]

        
        # Output result of test
        error = False
        if res_heap != sol:
            error = True
            print(f'\033[31mCheck failed for {filename} with heap sort\033[0m')
        if res_quick != sol:
            error = True
            print(f'\033[31mCheck failed for {filename} with quick sort\033[0m')
        if not error:
            print(f'\033[92m {filename} finished without any errors\033[0m')

    # Delete tmp file
    os.remove('tmp.txt')
else:
    # Arguments didn't match
    print('\033[31mPlease provide either -check or -time as first argument.\033[0m')
