# program.py - Program to run as part of CS480 Bisecting exercise

import os
import os.path

def main():

    print("Running scenario...")

    # Get list of all .dat files in data/ directory
    SOURCE_PATH = os.path.dirname(__file__)

    if not os.path.isdir(os.path.join(SOURCE_PATH,"data")):
        print("ERROR: No data directory! Something is wrong...")
        exit(1)
    
    # Get list of all .dat files
    datfiles = sorted([f for f in os.listdir(os.path.join(SOURCE_PATH,"data")) if f.endswith(".dat")])
    if not len(datfiles):
        print("ERROR: No files in data directory! Something is wrong...")
        exit(1)

    running_total = 0

    print(f"There are {len(datfiles)} data files to process.")
    
    # Parse all dat files
    for datfile in datfiles:
        dat_lines = [x.strip() for x in open(os.path.join(SOURCE_PATH,"data",datfile),"r").readlines()]

        # This is where the bug will occur if there is a non-integer in the file.
        try:
            dat_total = sum([int(x) for x in dat_lines])
        except ValueError:
            print(f"ERROR: Something couldn't be parsed in the file {datfile}! Aborting program.")
            exit(2)
        
        print(f"  {datfile}: {len(dat_lines)} entries, total: {dat_total:,d}")
        running_total += dat_total
    
    # We made it!
    print(f"Scenario success! Total: {running_total:,d}")

    exit(0)

if __name__ == "__main__":
    main()