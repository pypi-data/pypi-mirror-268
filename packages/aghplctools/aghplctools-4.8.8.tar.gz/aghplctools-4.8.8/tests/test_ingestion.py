import os
import pathlib
import unittest
import json

from aghplctools.ingestion.text import pull_hplc_area_from_txt, report_text_to_xlsx

conditional_path = pathlib.Path(
    'tests/' if os.getcwd().endswith('tests') is False else ''
) / 'test_data/data folder 1'


def floatify_dictionary(dct):
    """converts a dumped dictionary to have float keys"""
    out = {}
    for wl in dct:
        wl_float = float(wl)
        out[wl_float] = {}
        for rt in dct[wl]:
            rt_float = float(rt)
            out[wl_float][rt_float] = dct[wl][rt]
    return out


class TestText(unittest.TestCase):
    """tests text ingestion"""
    def test_area_pulling(self):
        """tests area pulling functionality"""
        signals = pull_hplc_area_from_txt(conditional_path / '2020-01-01/020.D/Report.TXT')
        with open(conditional_path / '2020-01-01/020.D/expected_signals.json') as f:
            expected = floatify_dictionary(json.load(f))
        self.assertEqual(signals, expected)

    def test_to_xlsx(self):
        """tests report conversion to xlsx"""
        path = report_text_to_xlsx(conditional_path / '2020-01-01/020.D/Report.TXT')
        self.assertTrue(pathlib.Path(path).is_file())
