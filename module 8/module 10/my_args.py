"""
Practice program arguments
"""
import sys


def main(name, age):
    """
    Main Driver
    """
    print(f'Hello {name}')
    print(f'You are {age} years old')


if __name__ == '__main__':
    print(type(sys.argv), len(sys.argv))
    if len(sys.argv) != 3:
        print(f'Missing required parameters')
        print('Usage: python {sys.argv[0]} <name> <age>')
        sys.exit(1)  # exit program with error # 1
    
    # main()
    sys.exit(0)