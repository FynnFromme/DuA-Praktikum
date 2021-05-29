import sys


def prime_numbers(n):
    # Create list of bool values
    prim = [False, False] + [True]*(n-1)

    # Set indexes that are no prime number to False
    for i in range(2, n):
        for j in range(2*i, n+1, i):
            prim[j] = False

    return prim


def non_prime_numbers(n):
    # Create list of bool values
    no_prime = [False] * (n+2)

    # Set indexes that are no prime number to False
    for i in range(2, n):
        for j in range(2*i, n+1, i):
            no_prime[j] = True

    return no_prime


def print_true_index(l):
    # Output indexes to console that have the value True
    output = ''
    for i, v in enumerate(l):
        if v:
            output += str(i) + '\n'
    if output.endswith('\n'):
        output = output[:-1]
    
    print(output)

def write_true_index(l):
    # Write indexes to file that have the value True
    output = ''
    for i, v in enumerate(l):
        if v:
            output += str(i) + '\n'
    if output.endswith('\n'):
        output = output[:-1]
    
    with open('./tmp.txt', 'w') as f:
        f.write(output)

if __name__=='__main__':
    # Get number out of file
    filename = sys.argv[-1]
    output_prime = sys.argv[1] != '-np'
    with open(filename, 'r') as f:
        n = int(f.read())

    # Get list of numbers
    if output_prime:
        l = prime_numbers(n)
    else:
        l = non_prime_numbers(n)

    # Output numbers
    if output_prime and sys.argv[1] == '--test' or not output_prime and sys.argv[2] == '--test':
        write_true_index(l)
    else:
        print_true_index(l)
