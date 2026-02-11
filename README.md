# Quantifying Molecular Flexibility in Crystals

Supporting code for "Quantifying Molecular Flexibility Using Crystallographically Accessible Conformational Space" <https://doi.org/10.1021/acs.jcim.5c02976>.

## Overview

Minimal required inputs:

- Either a single CSD refcode, multiple CSD refcodes listed in a gcd file, or a molecule in a molecule file (e.g. mol2)
- Output directory specification

Optional:

- A verbose flag. This will write basic output to the screen.

Output:

- multiple files written to the specified output directory. flexibility.txt contains the main results.

## Dependencies & Requirements

- CSD Discovery, CSD Materials or CSD Enterprise license

## Installation

Ensure you have a working CSD Python API environment (see the CCDC online documentation <a href="https://downloads.ccdc.cam.ac.uk/documentation/API/">here</a> for more information.) No separate
package installation is required beyond dependencies already provided with the API.

## Usage

### Show all options

```
python main.py -h
```

### A Single CSD Refcode

Compute flexibility scores for CSD entry AABHTZ, writing output files to F:\tmp and specifying verbose output

```
python main.py refcode aabhtz F:\tmp -v 
```

### Multiple CSD Refcodes

Compute flexibility scores for all refcodes specified in the given GCD file writing output files to F:\tmp

```
python main.py gcd F:\gcd\test.gcd F:\tmp
```

### A Molecule in a mol2 File

Compute flexibility scores for the molecule specified in the given mol2 file writing output files to F:\tmp

```
python main.py mol2 F:\mol2\HXACAN.mol2 F:\tmp
```

## Output Files

- flexibility.txt containing the flexibility scores with and without topological weighting (wtd)
- flexibility_log.txt/flexibility_log_rotamers.txt meta data relating to the rotamer distributions, the name depending on the version of the CCDC software installed
- flexibility_log_rejects Any rejected entries with a reason
- flexibility_log_rings.txt meta data relating to the ring templates
- flexibility_log_ring_template_wts.txt weights associated with the ring templates, depending on the version of the CCDC software installed
- flexibility_meta_data Meta data about the process

## Citation

Please cite the associated scientific paper:
<https://doi.org/10.1021/acs.jcim.5c02976>

## License

Provided by the Cambridge Crystallographic Data Centre (CCDC).  See the license file for detailed terms and conditions.

## Support

This script is provided as-is and is not formally supported by CCDC at this time. For questions or issues, please refer to the CSD Python API documentation or contact the authors.

## Authors

- **Patrick McCabe** (<mccabe@ccdc.cam.ac.uk>) - Original implementation
