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
        this_table = self._choose_genetic_table()

        # got "inspiration" from Biopython
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
        self.degenerated = ''.join(out)

    def _check_arguments(self):
        type_choices = ['normal', 'S', 'Z', 'SZ']

        if self.dna is None:
            raise MissingParameterError('Please enter a DNA string as input:'
                                        '\n>>> Degenera.dna = "ACT"')
        if self.table is None:
            raise MissingParameterError('Please enter a NCBI table code as input:'
                                        '\n>>> Degenera.table = 1')
        if self.table == 1:
            if self.type is None:
                raise MissingParameterError('Please enter a type of Degenerate code:'
                                            '\n>>> Degenera.type = "normal"'
                                            '\n>>> Degenera.type = "S"'
                                            '\n>>> Degenera.type = "Z"'
                                            '\n>>> Degenera.type = "SZ"')
            if self.type not in type_choices:
                raise WrongParameterError('Please use one of the following choices for'
                                          ' the Degenerate.type parameter:'
                                          '\n"normal", "S", "Z", or "SZ"')

        if self.type in type_choices and self.table != 1:
            raise WrongParameterError('The type parameter "normal", "S", "Z",'
                                      ' and "SZ" are only compatible with'
                                      ' table = 1 (Standard Genetic code)')

    def _choose_genetic_table(self):
        this_table = None
        if self.table == 1 and self.type == 'normal':
            this_table = tables.degen_table_1
        elif self.table == 1 and self.type == 'S':
            this_table = tables.degen_S
        elif self.table == 1 and self.type == 'Z':
            this_table = tables.degen_Z
        elif self.table == 1 and self.type == 'SZ':
            this_table = tables.degen_SZ
        if self.table == 5:
            this_table = tables.degen_table_5
        if this_table is None:
            raise WrongParameterError(
                'Only table 1 and 5 are implemented so far.')
        return this_table

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
