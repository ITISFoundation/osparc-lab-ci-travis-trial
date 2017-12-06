''' Testing Package3 '''

import sys

def main():
    '''Main test function'''
    print "Hello world from Test 3"

    exit_code = 0
    if exit_code != 0:
        print "Test 3 shall fail now with exit code ", exit_code
    else:
        print "I think, test 3 was a success :)"
    return exit_code

if __name__ == '__main__':
    sys.exit(main())
