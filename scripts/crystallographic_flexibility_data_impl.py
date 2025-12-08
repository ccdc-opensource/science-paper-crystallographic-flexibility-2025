from ccdc import io

from crystallographic_flexibility import CrystallographicFlexibility

REFCODE = 'refcode'
GCD = 'gcd'
MOL = 'mol'

class CrystallographicFlexibilityBaseData:
    
    def process(self, input_data):
        raise NotImplementedError("Subclasses must implement the `process` method")

    def header(self):
        print(f"{'id':<15} {'baseline':<8} {'unif':<15} {'rel':<15}")

    def print_flex_values(self, id):
        print(f'{id:<15} {self.cf_.baseline:<8d} {self.cf_.uniform_wtd:<15.2f} {self.cf_.rel_wtd:<15.2f}')

    def finish(self):
        print(f"See {self.cf_.output_dir()} for output files.")
                
        
class FileData(CrystallographicFlexibilityBaseData):

    def __init__(self, outdir):
        
        self.cf_ = CrystallographicFlexibility(outdir)
        
    def process(self, args):
        
        if args.verbose:
            self.header()

        molfile = args.input

        rdr = io.MoleculeReader(molfile)
        for mol in rdr:
            self.cf_.process(mol.identifier, mol)
            if args.verbose:
                self.print_flex_values(mol.identifier)

        self.finish()
                
        
class RefcodeData(CrystallographicFlexibilityBaseData):

    def __init__(self, outdir):
        
        self.cf_ = CrystallographicFlexibility(outdir)
        
    def process(self, args):
        
        if args.verbose:
            self.header()
    
        refcode = args.input.upper()

        with io.EntryReader('CSD') as rdr:
            entry = rdr.entry(refcode)
            self.cf_.process(refcode, entry.molecule)
            if args.verbose:
                self.print_flex_values(refcode)

        self.finish()


class GCDData(CrystallographicFlexibilityBaseData):

    def __init__(self, outdir):
        
        self.cf_ = CrystallographicFlexibility(outdir)
        
    def process(self, args):
    
        gcdfile = args.input

        try:
            with open(gcdfile, 'r') as file, io.EntryReader('CSD') as rdr:
                if args.verbose:
                    self.header()
                for line in file:
                    refcode = line.strip()
                    self.cf_.process(refcode, rdr.entry(refcode).molecule)
                    if args.verbose:
                        self.print_flex_values(refcode)
        except FileNotFoundError:
            print(f'The gcd file {gcdfile} was not found.')

        self.finish()


class DataFactory:

    @staticmethod
    def create(input_data, outdir):
        data_map = {
            REFCODE: RefcodeData,
            MOL: FileData,
            GCD: GCDData
        }
        data_class = data_map.get(input_data)
        if not data_class:
            raise ValueError(f"Unknown input data type {input_data}")
        
        return data_class(outdir)