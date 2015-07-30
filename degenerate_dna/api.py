import warnings

from ._warnings import DegenerateWarning
from .tables import degen_table_1
from .exceptions import MissingParameterError
from .exceptions import WrongParameterError


class Degenera(object):
    """Performs Zwick et al method for returning degenerated DNA sequences.

    :param dna: DNA sequence as Python string.
    :param table: Genbank notation for Translation Tables http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
    :param type: Zwick's method for degeneration: normal, S, Z, or SZ.
    :return: degenerated DNA sequence as Python string.
    """
    def __init__(self, dna=None, table=None, type=None):
        self.dna = dna
        self.table = table
        self.type = type
        self.degenerated = None

    def degenerate(self):
        self._check_arguments()

        # proceed
        # getting "inspiration" from Biopython
        # https://github.com/biopython/biopython/blob/master/Bio/Seq.py#L2035
        dna = str(self.dna)
        n = len(dna)

        if n % 3 != 0:
            warnings.warn("Partial codon, len(sequence) not a multiple of three. "
                          "Explicitly trim the sequence or add trailing N before "
                          "translation. This may become an error in future.",
                          DegenerateWarning)

        out = []
        append = out.append
        for i in range(0, n - n % 3, 3):
            codon = dna[i:i + 3]
            degen_codon = degen_table_1[codon]
            append(degen_codon)
        self.degenerated = ''.join(out)

    def _check_arguments(self):
        if self.dna is None:
            raise MissingParameterError('Please enter a DNA string as input:'
                                        '\n>>> Degenera.dna = "ACT"')
        if self.table is None:
            raise MissingParameterError('Please enter a NCBI table code as input:'
                                        '\n>>> Degenera.table = 1')
        if self.type is None:
            raise MissingParameterError('Please enter a type of Degenerate code:'
                                        '\n>>> Degenera.type = "normal"'
                                        '\n>>> Degenera.type = "S"'
                                        '\n>>> Degenera.type = "Z"'
                                        '\n>>> Degenera.type = "SZ"')
        type_choices = ['normal', 'S', 'Z', 'SZ']
        if self.type not in type_choices:
            raise WrongParameterError('Please use one of the following choices for'
                                      ' the Degenerate.type parameter:'
                                      '\n"normal", "S", "Z", or "SZ"')
