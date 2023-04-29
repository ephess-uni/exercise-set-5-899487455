import argparse
import numpy as np
import pandas as pd

def scale(infile, outfile):
    data = pd.read_csv(infile)
    data_scaled = (data - np.mean(data)) / np.std(data)
    data_scaled.to_csv(outfile, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This program applies a standard scale transform to the data in infile and writes it to outfile.')
    parser.add_argument('infile', help='input filename for the data file that needs to be processed')
    parser.add_argument('outfile', help='output filename')
    args = parser.parse_args()

    scale(args.infile, args.outfile)

