import os
import time
import unittest
import pathlib

from aghplctools.local_paths import ChemStationConfig, AcquisitionSearch


conditional_path = pathlib.Path(
    'tests/' if os.getcwd().endswith('tests') is False else ''
) / 'test_data/data folder 1'


class TestCSC(unittest.TestCase):
    """tests ChemStationConfig class"""
    def setUp(self) -> None:
        instances = ChemStationConfig.construct_from_ini('./test_data/ChemStation.ini')

    def test_from_ini(self):
        """tests that instances were created from ini"""
        instances = ChemStationConfig.registered_chemstations
        self.assertNotEqual(
            len(instances),
            0,
        )

    def test_attributes(self):
        """ensures attibutes are set correctly"""
        instances = ChemStationConfig.registered_chemstations
        for inst in instances:
            self.assertTrue(
                inst.data_path.data_parent.is_dir()
            )
            if inst.number is not None:
                self.assertIsNotNone(inst.core_path)
                self.assertIsNotNone(inst.method_path)
                self.assertIsNotNone(inst.sequence_path)
                self.assertIsNotNone(inst.version)

    def test_environ(self):
        """tests creation from environ"""
        os.environ['TEST_HPLC_PATH'] = str(conditional_path)
        instance = ChemStationConfig.construct_from_env('TEST_HPLC_PATH')
        self.assertIsNotNone(instance)
        self.assertTrue(
            instance.data_path.data_parent.is_dir()
        )


class TestACQSearch(unittest.TestCase):
    """Tests acquisition monitoring"""
    def setUp(self) -> None:
        self.test_search = AcquisitionSearch.get_by_path(conditional_path)

    def test_search_start(self):
        """tests finding of acquiring.txt"""
        AcquisitionSearch.start_monitoring_all_paths()
        while self.test_search.current_file is None:
            time.sleep(0.01)
        self.assertTrue(self.test_search.acquiring_path.is_file())
        self.assertTrue(self.test_search.current_file.is_dir())
        self.assertGreater(self.test_search.current_number, 0)
        self.assertTrue(self.test_search.acquiring)
        self.assertTrue(self.test_search._located.isSet())  # check that flag is set

    def test_direct_retrieval(self):
        """tests direct retrieval of the acquisition search"""
        file = self.test_search.find_acquiring()
        self.assertTrue(file.is_file())
