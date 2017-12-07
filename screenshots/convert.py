import sys

def main():
    for s in sys.argv[1:]:
        print '![{}](screenshots/{})'.format(s, s)

# Boiler plate invokes the main function
if __name__ == "__main__":
    main()
