from . import exceptions


class Degenera(object):
    def __init__(self, dna=None, table=None, type=None):
        self.dna = dna
        self.table = table
        self.type = type

    def _check_arguments(self):
        if self.dna is None:
            raise exceptions.MissingParameterError('Please enter a DNA string as input:'
                                                   '\n>>> Degenera.dna = "ACT"')
        if self.table is None:
            raise exceptions.MissingParameterError('Please enter a NCBI table code as input:'
                                                   '\n>>> Degenera.table = 1')
        if self.type is None:
            raise exceptions.MissingParameterError('Please enter a type of Degenerate code:'
                                                   '\n>>> Degenera.type = "normal"'
                                                   '\n>>> Degenera.type = "S"'
                                                   '\n>>> Degenera.type = "Z"'
                                                   '\n>>> Degenera.type = "SZ"')
