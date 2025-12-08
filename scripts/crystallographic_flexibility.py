"""
    molecule_flexibility.py - for computing crystallographic flexibility measures for molecules
"""
##########################################################################

from ccdc.utilities import _private_importer

with _private_importer() as pi:
    pi.import_ccdc_module('ConformerGeneratorLib')


##########################################################################

class CrystallographicFlexibility:
    '''
    Provide measure of how flexible a molecule is in the crystallographic state

    Make use of CSD Customised Version of the Mogul distributions
    '''

    def __init__(self, output_dir):

        self.output_dir_ = output_dir
        self.calculator = ConformerGeneratorLib.MoleculeFlexibility(output_dir)


    def process(self, id, mol):
        '''
        Set the molecule to assess
        '''
        self.calculator.process(id, mol._molecule)

    @property
    def uniform_wtd(self):
        '''
        Return the (topologically weighted) uniformly calibrated crystallographic flexibility
        '''
        return self.calculator.uniform_wtd()

    @property
    def rel_wtd(self):
        '''
        Return the (topologically weighted) relatively calibrated crystallographic flexibility
        '''
        return self.calculator.rel_wtd()

    @property
    def baseline(self):
        '''
        Return the number of acyclic rotatable bonds
        '''
        return self.calculator.baseline()

    @property
    def baseline_wtd(self):
        return self.calculator.baseline_wtd()
    
    def output_dir(self):
        return self.output_dir_
