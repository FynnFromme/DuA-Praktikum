import os
import sys
from timeit import timeit

#? Usage: python test.py < -check / -time > <filename>

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
    p_time = timeit(lambda: os.system(
        f'python3 primzahlen.py {sys.argv[2]}'), number=1)
    np_time = timeit(lambda: os.system(
        f'python3 primzahlen.py -np {sys.argv[2]}'), number=1)

    # Output time
    print(chr(27) + "[2J")
    print('\033[92mPrime numbers:', p_time)
    print('Non-prime numbers:', np_time, '\033[0m')
        

elif sys.argv[1] == '-check':  # Check whether the algorithm is correct
    # Check every test instance
    for filename in os.listdir('../pubInst/'):
        if not filename.endswith('.txt'):
            continue

        # Get the result of quick sort
        os.system(f'python3 primzahlen.py --test ../pubInst/{filename}')
        with open('./tmp.txt', 'r') as q:
            res_p = q.read()

        # Get the result of heap sort
        os.system(f'python3 primzahlen.py -np --test ../pubInst/{filename}')
        with open('./tmp.txt', 'r') as h:
            res_np = h.read()

        # Get the solution for primenumbers
        with open(f'../pubInst/{filename}.sol', 'r') as s:
            sol_p = s.read()
            if sol_p.endswith('\n'):
                sol_p = sol_p[:-1]
        
        # Get the solution for non-primenumbers
        with open(f'../pubInst/{filename}.-np.sol', 'r') as s:
            sol_np = s.read()
            if sol_np.endswith('\n'):
                sol_np = sol_np[:-1]

        # Output result of test
        error = False
        if res_np != sol_np:
            error = True
            print(f'\033[31mCheck failed for {filename} with prime numbers\033[0m')
        if res_p != sol_p:
            error = True
            print(f'\033[31mCheck failed for {filename} with non-prime numbers\033[0m')
        if not error:
            print(f'\033[92m {filename} finished without any errors\033[0m')

    # Delete tmp file
    os.remove('tmp.txt')
else:
    # Arguments didn't match
    print('\033[31mPlease provide either -check or -time as first argument.\033[0m')
