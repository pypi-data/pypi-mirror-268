import os
import pathlib
import unittest

from aghplctools.data.sample import HPLCSampleInfo, DADSpectrum, DADSignal, HPLCSample, DADSignalInfo, strptime_agilent_dt
from aghplctools.data.batch import pull_hplc_data_from_folder_timepoint, batch_convert_signals_to_csv, batch_report_text_to_xlsx

conditional_path = pathlib.Path(
    'tests/' if os.getcwd().endswith('tests') is False else ''
) / 'test_data/data folder 1'


class TestSignalInfo(unittest.TestCase):
    def test_unreferenced(self):
        """tests basic creation of the class"""
        basic_signal = DADSignalInfo(
            wavelength=210.,
            bandwidth=2.,
            name='DAD1 A'
        )
        self.assertEqual(
            basic_signal.name,
            'DAD1 A'
        )
        self.assertEqual(
            basic_signal.wavelength,
            210.,
        )
        self.assertIs(basic_signal.reference, None)
        self.assertEqual(
            basic_signal.agilent_specification_string,
            'DAD1 A, Sig=210,2 Ref=off',
        )

    def test_referenced(self):
        refd_signal = DADSignalInfo(
            wavelength=220,
            bandwidth=4.,
            reference='280,2',
            name='DAD1 B'
        )
        self.assertEqual(
            refd_signal.agilent_specification_string,
            'DAD1 B, Sig=220,4 Ref=280,2'
        )
        self.assertEqual(
            refd_signal.reference.wavelength,
            280.,
        )
        self.assertEqual(
            refd_signal.reference.bandwidth,
            2.,
        )

    def test_from_string(self):
        """tests creation from an input string which doesn't have a reference"""
        input_string = 'DAD1 C, Sig=240,6 Ref=off'
        string_signal = DADSignalInfo.create_from_agilent_string(input_string)
        self.assertEqual(
            string_signal.name,
            'DAD1 C'
        )
        self.assertEqual(
            string_signal.wavelength,
            240.
        )
        self.assertEqual(
            string_signal.bandwidth,
            6.
        )
        self.assertEqual(
            string_signal.agilent_specification_string,
            input_string
        )

    def test_from_string_refd(self):
        """tests creation from an input string that implies the signal is referenced"""
        input_string = 'DAD1 D, Sig=250,2 Ref=280,2'
        string_signal = DADSignalInfo.create_from_agilent_string(
            input_string
        )
        self.assertEqual(
            string_signal.name,
            'DAD1 D'
        )
        self.assertEqual(
            string_signal.wavelength,
            250.
        )
        self.assertEqual(
            string_signal.bandwidth,
            2.
        )
        self.assertEqual(
            string_signal.reference.wavelength,
            280.
        )
        self.assertEqual(
            string_signal.reference.bandwidth,
            2.
        )
        self.assertEqual(
            string_signal.agilent_specification_string,
            input_string
        )

    def test_from_ch(self):
        """tests creation from a channel file"""
        target = conditional_path / '2020-01-01' / '001.D'
        from_signal = HPLCSampleInfo.create_from_acaml(target / 'sequence.acam_')
        for ch_file, signal in zip(sorted(target.glob('*.ch')), from_signal.signals):
            from_channel = DADSignalInfo.create_from_CH_file(ch_file)
            msg_prefix = f'signal {signal.name}'
            self.assertEqual(
                from_channel.wavelength,
                signal.wavelength,
                f'{msg_prefix} wavelength equality'
            )
            self.assertEqual(
                from_channel.bandwidth,
                signal.bandwidth,
                f'{msg_prefix} bandwidth equality',
            )
            # channel names can differ in spaces between acaml and ch spec (yay!)
            self.assertEqual(
                from_channel.name.replace(' ', ''),
                signal.name.replace(' ', ''),
                f'{msg_prefix} name equality',
            )
            # self.assertEqual(  # fails in every case because of the above comment
            #     from_channel.agilent_specification_string,
            #     signal.agilent_specification_string,
            # )
            if any([from_channel.reference, signal.reference]):
                self.assertEqual(
                    from_channel.reference.wavelength,
                    signal.reference.wavelength,
                    f'{msg_prefix} reference wavelength equality'
                )
                self.assertEqual(
                    from_channel.reference.bandwidth,
                    signal.reference.bandwidth,
                    f'{msg_prefix} reference bandwidth equality'
                )


class TestHPLCSI(unittest.TestCase):
    """tests HPLCSampleInfo class"""
    # todo add tests for older-style data

    def test_loading(self):
        """tests acaml loading"""
        test_sample = HPLCSampleInfo.create_from_acaml(
            conditional_path / '2020-01-01/020.D/sequence.acam_'
        )
        # check value retrieval
        self.assertEqual(
            test_sample.date,
            '2020-06-19',
        )
        self.assertEqual(
            test_sample.method_name,
            'YS-Kinugasa.M'
        )
        self.assertEqual(
            test_sample.sample_file_name,
            '020.D'
        )
        self.assertEqual(
            len(test_sample.signals),
            7,
        )


class TestDADSpectrum(unittest.TestCase):
    def test_spectrum(self):
        """tests DADspectrum loading"""
        test_spectrum = DADSpectrum(
            conditional_path / '2020-01-01/020.D/DAD1.UV'
        )
        # check shape
        self.assertEqual(
            test_spectrum.data.shape,
            (9600, 100)
        )
        self.assertEqual(
            test_spectrum.total_absorbance_chromatogram.shape,
            (9600,)
        )
        # check retrieval of intensities
        intensities = test_spectrum.get_band_intensities(210, 4)
        self.assertEqual(
            intensities.shape,
            (9600, 3)
        )
        self.assertAlmostEqual(intensities.sum(), 149189388.661)
        mean_intensities = test_spectrum.get_band_mean_intensity(210, 4)
        self.assertAlmostEqual(mean_intensities.sum(), 49729796.22033334)


class TestDADSignal(unittest.TestCase):
    def test_signal(self):
        signal = DADSignal(
            210.,
            4.,
            '310,4',
            'TEST',
            spectrum=DADSpectrum(conditional_path / '2020-01-01/020.D/DAD1.UV')
        )
        # check signal naming
        self.assertEqual(
            signal.name,
            'TEST',
        )
        # check specification string
        self.assertEqual(
            signal.agilent_specification_string,
            'TEST, Sig=210,4 Ref=310,4'
        )
        # check bandwidth and wavelength assignment
        self.assertEqual(
            signal.bandwidth,
            4.
        )
        self.assertEqual(
            signal.wavelength,
            210.
        )
        # check reference passthrough
        self.assertEqual(
            signal.reference.agilent_specification_string,
            'Ref, Sig=310,4 Ref=off'
        )
        # check array retrieval by sum
        self.assertEqual(
            signal.mean_referenced_intensities.sum(),
            43695436.94333334
        )
        self.assertEqual(
            signal.mean_unreferenced_intensities.sum(),
            49729796.22033334
        )
        self.assertEqual(
            signal.reference.mean_unreferenced_intensities.sum(),
            6034359.277
        )
        # check referencing
        self.assertAlmostEqual(
            signal.mean_unreferenced_intensities.sum() - signal.reference.mean_referenced_intensities.sum(),
            signal.mean_referenced_intensities.sum(),
            places=3,
        )
        # check array shape
        self.assertEqual(
            signal.mean_referenced_intensities.shape,
            (9600,)
        )
        self.assertEqual(
            signal.unreferenced_intensities.shape,
            (9600, 3)
        )


class TestHPLCSample(unittest.TestCase):
    """tests HPLCSample class"""
    sample = None

    @classmethod
    def setUpClass(cls) -> None:
        if cls.sample is None:
            cls.sample = HPLCSample.create_from_D_file(conditional_path / '2020-01-01/020.D')

    def test_hplc_sample(self):
        self.assertEqual(
            self.sample.directory,
            conditional_path / '2020-01-01/020.D'
        )
        # ensure 7 signals were loaded
        self.assertEqual(len(self.sample.signals), 7)

    # def test_add_signal(self):
    #     """tests the addition of signals"""
    #     pass  # todo

    def test_csv_export(self):
        """tests csv exporting"""
        result = self.sample.write_signals_to_csv()
        # ensure 8 csvs were written
        self.assertEqual(
            len(result),
            8
        )
        paths = [pathlib.Path(path) for path in result]

        for path, signal in zip(paths[:-1], self.sample.signals):
            # check naming
            self.assertEqual(
                path.stem,
                str(signal)
            )
            # check file was created
            self.assertTrue(path.is_file())

        # check TAC written
        self.assertTrue(paths[0].is_file())

    def test_xlsx_export(self):
        """tests excel exporting"""
        result = self.sample.write_signals_to_xlsx()
        self.assertTrue(pathlib.Path(result).is_file())


class TestBatch(unittest.TestCase):
    """tests batch methods"""
    def test_timepoint(self):
        """tests pull_hplc_data_from_folder_timepoint"""
        filenames, targets = pull_hplc_data_from_folder_timepoint(
            conditional_path / '2020-01-01',
        )
        # check 20 files processed
        self.assertEqual(len(filenames), 20)
        # check 7 wavelengths processed
        self.assertEqual(len(targets), 7)
        expected = {
            210.0: [0.542, 1.098, 1.157, 1.356, 1.503, 1.617, 1.765, 2.087, 2.354, 2.691, 2.841, 3.317, 3.458],
            230.0: [0.542, 1.099, 1.371, 1.504, 1.617, 2.087, 2.692, 2.841, 3.317, 3.458],
            254.0: [1.356, 1.503, 2.087, 2.691, 2.841, 3.317, 3.458],
            310.0: [1.504, 2.714, 3.318],
            280.0: [1.366, 1.504, 2.087, 2.692, 2.842, 3.318, 3.458],
            270.0: [1.366, 1.504, 2.087, 2.692, 2.841, 3.318, 3.458],
            350.0: [1.504],
        }
        # check that filenames were retrieved in order
        self.assertEqual(sorted(filenames), filenames)
        # check that all expected targets were extracted
        for wl in targets:
            self.assertEqual(
                len(targets[wl]),
                len(expected[wl])
            )
            # check that retention times are approximately the same
            for ind, rt in enumerate(sorted(targets[wl].keys())):
                self.assertAlmostEqual(rt, expected[wl][ind], 1)

        # check processing of late-appearance target
        late_appearance = targets[210.][1.098]
        self.assertEqual(len(late_appearance.areas), 20)  # correct number of data points
        self.assertEqual(sum(late_appearance.areas[:10]), 0.)  # first 10 points are 0
        self.assertEqual(sum(late_appearance.areas), 287.24672)  # correct total area

    def test_csv_batch(self):
        """tests batch_convert_signals_to_csv"""
        batch_convert_signals_to_csv(conditional_path / '2020-01-01')

    def test_xlsx_batch(self):
        """tests batch_report_text_to_xlsx"""
        batch_report_text_to_xlsx(conditional_path / '2020-01-01')


class TestTimeParsing(unittest.TestCase):
    """tests time parsing functions for metatdata retrieval"""

    def test_ms(self):
        """tests stamp with millisecond parsing"""
        parsed = strptime_agilent_dt('2020-07-08T21:14:40.56-07:00')

    def test_workstation(self):
        """tests time stamp from a workstation export"""
        parsed = strptime_agilent_dt('2022-02-02T08:53:54.3493809Z')

    def test_non_ms(self):
        """tests stamp without millisecond parsing"""
        parsed = strptime_agilent_dt('2020-07-08T21:14:40-07:00')
