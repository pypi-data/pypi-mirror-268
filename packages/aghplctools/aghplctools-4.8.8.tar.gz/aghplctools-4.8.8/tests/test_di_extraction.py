"""tests DI data extraction script"""

import os
import pathlib
import unittest
from DI_data_extraction import perform_data_extraction

conditional_path = pathlib.Path(
    'tests/' if os.getcwd().endswith('tests') is False else ''
) / 'test_data/data folder 2'


def sanitize_folder(target: pathlib.Path):
    """removes csv and xlsx files in the target directory"""
    for extension in ['csv', 'xlsx']:
        for file in target.glob(f'**/*.{extension}'):
            os.remove(file)


class TestDIExtraction(unittest.TestCase):
    def test_di_extraction_script(self):
        """tests the DI Data Extraction script"""
        sanitize_folder(conditional_path)
        perform_data_extraction(
            conditional_path,
        )
        for sample in conditional_path.glob('**/*.D'):
            # check for correct number of files
            self.assertEqual(
                len([path for path in sample.glob('*.csv')]),
                8
            )
            self.assertEqual(
                len([path for path in sample.glob('*.xlsx')]),
                1
            )

            # check content of files
            with open(sample / 'DAD1 A 210 nm (4 nm).csv') as f:
                # check header of first file
                self.assertEqual(
                    f.readline(),
                    'Retention Time (min),210 nm intensity (mAU)\n'
                )
                for val in f.readline().strip().split(','):
                    float(val)  # ensure that all values in subsequent line are float

            with open(sample / 'Total Absorbance Chromatogram.csv') as f:
                # check header
                self.assertEqual(
                    f.readline(),
                    'Retention Time (min),Total Absorbance Chromatogram (mAU)\n'
                )
                for val in f.readline().strip().split(','):
                    float(val)  # ensure that all values in subsequent line are float
