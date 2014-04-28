import os, sys
from scripts.mail import run

def main():
	if sys.argv[1]=='mail':
		run()

if __name__ == "__main__":
    main()
