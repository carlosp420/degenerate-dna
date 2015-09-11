import re
import warnings

from . import tables
from ._warnings import DegenerateWarning
from .exceptions import MissingParameterError
from .exceptions import WrongParameterError


class Degenera(object):
    """Performs Zwick et al method for returning degenerated DNA sequences.

    :param dna: DNA sequence as Python string.
    :param table: Genbank notation for Translation Tables http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
    :param method: Zwick's method for degeneration: normal, S, Z, or SZ.
    :return: degenerated DNA sequence as Python string.
    """
    def __init__(self, dna=None, table=None, method=None):
        self.dna = dna
        self.table = table
        self.method = method
        self.degenerated = None

    def degenerate(self):
        self._check_arguments()
        this_table = self._choose_genetic_table()

        # got "inspiration" from Biopython
        # https://github.com/biopython/biopython/blob/master/Bio/Seq.py#L2035
        dna = str(self.dna)
        n = len(dna)

        partial_codon_remainder = n % 3
        if partial_codon_remainder != 0:
            warnings.warn("Partial codon, len(sequence) not a multiple of three. "
                          "Explicitly trim the sequence or add trailing N before "
                          "translation. This may become an error in future.",
                          DegenerateWarning)

        out = []
        append = out.append
        for i in range(0, n - n % 3, 3):
            tmp_codon = dna[i:i + 3]
            codon = self._convert_to_nnn_if_ambiguous_nt1_nt2(tmp_codon)
            if '-' in codon:
                append(codon)
            else:
                try:
                    degen_codon = this_table[codon]
                    append(degen_codon)
                except KeyError:
                    warnings.warn('Codon {} cannot be degenerated'.format(codon), DegenerateWarning)
                    append(codon)

        # A few bases might have not been degenerated
        if partial_codon_remainder == 1:
            append(self.dna[-1:])
        if partial_codon_remainder == 2:
            append(self.dna[-2:])
        self.degenerated = ''.join(out)

    def _check_arguments(self):
        method_choices = ['normal', 'S', 'Z', 'SZ']

        if self.dna is None:
            raise MissingParameterError('Please enter a DNA string as input:'
                                        '\n>>> Degenera.dna = "ACT"')
        if self.table is None:
            raise MissingParameterError('Please enter a NCBI table code as input:'
                                        '\n>>> Degenera.table = 1')
        if self.table == 1 and self.method is None:
            raise MissingParameterError('Please enter a method of Degenerate code:'
                                        '\n>>> Degenera.method = "normal"'
                                        '\n>>> Degenera.method = "S"'
                                        '\n>>> Degenera.method = "Z"'
                                        '\n>>> Degenera.method = "SZ"')
        if self.table == 1 and self.method not in method_choices:
            raise WrongParameterError('Please use one of the following choices for'
                                      ' the Degenerate.method parameter:'
                                      '\n"normal", "S", "Z", or "SZ"')

        if self.method in ['S', 'Z', 'SZ'] and self.table != 1:
            raise WrongParameterError('The method parameter "normal", "S", "Z",'
                                      ' and "SZ" are only compatible with'
                                      ' table = 1 (Standard Genetic code)')

    def _choose_genetic_table(self):
        methods = {
            'normal': tables.degen_table_1,
            'S': tables.degen_S,
            'Z': tables.degen_Z,
            'SZ': tables.degen_SZ,
        }
        if self.table == 5:
            return tables.degen_table_5
        elif self.table == 1:
            return methods[self.method]
        else:
            raise WrongParameterError('Only table 1 and 5 are implemented so far.')

    def _convert_to_nnn_if_ambiguous_nt1_nt2(self, tmp_codon):
        value = self._clean_string(tmp_codon)
        pattern = '^[MWRYSKHVDBN]|^[ACTG][MWRYSKHVDBN]'
        if re.search(pattern, value) is not None:
            return 'NNN'
        else:
            return value

    def _clean_string(self, tmp_codon):
        out = tmp_codon.upper()
        out = out.replace('?', 'N')
        return out
