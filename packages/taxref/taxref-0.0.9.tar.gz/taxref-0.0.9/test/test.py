"""test module for Taxref"""
import os
from pathlib import Path

import unittest

from dotenv import load_dotenv
import pandas as pd
from taxref.taxref_common import pdReadCts

from taxref.taxref11 import Taxref11, to_taxref11_tuple


class TestTaxref(unittest.TestCase):
    """test class for Simple Unit"""

    load_dotenv()

    def test_taxref11(self):
        """test metric prefixes units"""

        self.assertEqual(first=40, second=len(Taxref11))

        df_taxref11 = pd.read_csv(
            Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v11', 'TAXREFv11.txt'),
            sep=pdReadCts.sep,
            header=pdReadCts.header,
            index_col=pdReadCts.index_col,
            dtype=pdReadCts.dtype,
            na_filter=pdReadCts.na_filter)

        self.assertEqual(550843, len(df_taxref11))
        self.assertEqual(Taxref11.CD_NOM.name, df_taxref11.index.name)

        single = df_taxref11.loc['183718']
        self.assertEqual(40 - 1, len(single))  # 39 colonnes (40 champs moins celui mis en index)

        self.assertEqual('183718', single.name)

        single_tu = to_taxref11_tuple(single)

        self.assertEqual(len(Taxref11), len(single_tu))


if __name__ == '__main__':
    unittest.main()
