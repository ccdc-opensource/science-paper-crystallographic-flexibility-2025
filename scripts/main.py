from argparse import ArgumentParser
import pathlib
import sys

from crystallographic_flexibility_data_impl import *


def parse_args():

    argparser = ArgumentParser(description='A utility to compute crystallographic flexibility scores.',
                               epilog='Check the output directory for files containing the results.')
    
    # Positional arguments
    argparser.add_argument('mode',
                           choices=[REFCODE, GCD, MOL],
                           help='Compute for a CSD refcode, a gcd file, or a molecule in a molecule file (mol2, mol)')
    argparser.add_argument('input', type=str,
                           help='The refcode or path to the gcd file, or file containing the molecule')
    argparser.add_argument('outdir', type=str, help='Path to the output directory')

    # Optional
    argparser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output. This writes output to the screen as well'
                            ' as to the output files.')

    args = argparser.parse_args()

    return args


def check_output_dir(args):

    output_path = pathlib.Path(args.outdir)

    if not output_path.is_dir():
        print(f"Fatal error. Output directory {output_path} does not exist.")
        sys.exit(1)
    

def main():

    args = parse_args()
    check_output_dir(args)
    crystflex = DataFactory.create(args.mode, args.outdir)
    crystflex.process(args)
    
    
if __name__ == '__main__':
    main()
