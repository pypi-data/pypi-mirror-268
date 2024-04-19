"""A module for testing the writecondastat.condastat module."""

import unittest
import unittest.mock
import filecmp
import os
import shutil
from pathlib import Path

import dask.dataframe as dd


from writecondastat.statdate import StatPeriod
from writecondastat.condastat import CondaStatDataSource, WriteCondaStat


PATH = Path(__file__).parent

STATS = dd.read_csv(
    f"{PATH}/assets/mock_input/2022-01-01-*.csv", dtype={"pkg_version": str}
)


class TestDownloadCondaStat(unittest.TestCase):
    """A class for testing WriteCondaStat.download_condastat() method."""

    # def test_download_without_mock(self) -> None:
    #     """A method for testing WriteCondaStat.download_condastat() without mock."""

    #     stat = WriteCondaStat.download_condastat(
    #         "conda-forge",
    #         year="2022",
    #         month="01",
    #         day="01",
    #         package="pandas",
    #     )
    #     self.assertEqual(
    #         len(stat.index),  # type: ignore
    #         265,
    #     )

    def test_if_date_is_available(self) -> None:
        """A method for testing WriteCondaStat.download_condastat() if date is available."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            stat = WriteCondaStat.download_condastat(
                "conda-forge",
                year="2022",
                month="01",
                day="01",
                package="pandas",
            )
            self.assertEqual(
                len(stat.index),  # type: ignore
                265,
            )

    def test_if_date_is_not_available(self) -> None:
        """A method for testing WriteCondaStat.download_condastat() if date is not available."""

        with unittest.mock.patch(
            "dask.dataframe.read_parquet", side_effect=FileNotFoundError
        ):
            self.assertEqual(
                WriteCondaStat.download_condastat(
                    "conda-forge",
                    year="2000",
                    month="01",
                    day="01",
                    package="pandas",
                ),
                None,
            )

    def test_if_package_is_not_available(self) -> None:
        """A method for testing WriteCondaStat.download_condastat() if package is not available."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            self.assertEqual(
                WriteCondaStat.download_condastat(
                    "conda-forge",
                    year="2022",
                    month="01",
                    day="01",
                    package="not-existing-conda-package",
                ),
                None,
            )

    def test_if_data_source_is_not_available(self) -> None:
        """
        A method for testing WriteCondaStat.download_condastat() if data source is not available.
        """

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            with self.assertRaises(ValueError):
                WriteCondaStat.download_condastat(
                    "not-existing-data-source",
                    year="2022",
                    month="01",
                    day="01",
                    package="not-existing-conda-package",
                )


class TestGetCondaStat(unittest.TestCase):
    """A class for testing WriteCondaStat.get_condastat() method."""

    def test_if_write_package_name_is_true(self) -> None:
        """A method for testing WriteCondaStat.get_condastat() if write_package_name is true."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            write_conda_stat = WriteCondaStat("pandas")
            write_conda_stat.write_package_name = True
            stats = write_conda_stat.get_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2022-01-01",
                end_date="2022-01-03",
            )
            self.assertEqual(
                len(stats.columns),  # type: ignore
                7,
            )

    def test_if_write_package_name_is_false(self) -> None:
        """A method for testing WriteCondaStat.get_condastat() if write_package_name is false."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            write_conda_stat = WriteCondaStat("pandas")
            write_conda_stat.write_package_name = False
            stats = write_conda_stat.get_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2022-01-01",
                end_date="2022-01-03",
            )
            self.assertEqual(
                len(stats.columns),  # type: ignore
                6,
            )

    def test_if_data_source_is_anaconda(self) -> None:
        """
        A method for testing WriteCondaStat.get_condastat()
        if data_source is CondaStatDataSource.ANACONDA.
        """

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            write_conda_stat = WriteCondaStat("pandas")
            stats = write_conda_stat.get_condastat(
                CondaStatDataSource.ANACONDA,
                start_date="2022-01-01",
                end_date="2022-01-03",
            )
            self.assertEqual(
                len(stats.index),  # type: ignore
                611 * 3,
            )

    def test_if_data_source_is_conda_forge(self) -> None:
        """
        A method for testing WriteCondaStat.get_condastat()
        if data_source is CondaStatDataSource.CONDAFORGE.
        """

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            write_conda_stat = WriteCondaStat("pandas")
            stats = write_conda_stat.get_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2022-01-01",
                end_date="2022-01-03",
            )
            self.assertEqual(
                len(stats.index),  # type: ignore
                265 * 3,
            )

    def test_if_data_source_is_bioconda(self) -> None:
        """
        A method for testing WriteCondaStat.get_condastat()
        if data_source is CondaStatDataSource.BIOCONDA.
        """

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            write_conda_stat = WriteCondaStat("pandas")
            stats = write_conda_stat.get_condastat(
                CondaStatDataSource.BIOCONDA,
                start_date="2022-01-01",
                end_date="2022-01-03",
            )
            self.assertEqual(
                stats,
                None,
            )

    def test_if_data_source_is_valid_string(self) -> None:
        """A method for testing WriteCondaStat.get_condastat() if data_source is valid string."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            write_conda_stat = WriteCondaStat("pandas")
            stats = write_conda_stat.get_condastat(
                "conda-forge", start_date="2022-01-01", end_date="2022-01-03"
            )
            self.assertEqual(
                len(stats.index),  # type: ignore
                265 * 3,
            )

    def test_if_data_source_is_not_valid_string(self) -> None:
        """
        A method for testing WriteCondaStat.get_condastat() if data_source is not valid string.
        """

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            write_conda_stat = WriteCondaStat("pandas")
            with self.assertRaises(ValueError):
                write_conda_stat.get_condastat(
                    "conda", start_date="2022-01-01", end_date="2022-01-03"
                )

    def test_if_using_more_data_source(self) -> None:
        """A method for testing WriteCondaStat.get_condastat() if using more data_source."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            write_conda_stat = WriteCondaStat("pandas")
            stats = write_conda_stat.get_condastat(
                CondaStatDataSource.ANACONDA,
                CondaStatDataSource.CONDAFORGE,
                CondaStatDataSource.BIOCONDA,
                start_date="2022-01-01",
                end_date="2022-01-03",
            )
            self.assertEqual(
                len(stats.index),  # type: ignore
                (611 + 265) * 3,
            )


class TestWriteCondaStat(unittest.TestCase):
    """A class for testing WriteCondaStat.write_condastat() method."""

    def test_if_outdir_is_none(self) -> None:
        """A method for testing WriteCondaStat.write_condastat() if outdir is none."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            write_conda_stat = WriteCondaStat("pandas")
            write_conda_stat.fill_no_data = False
            write_conda_stat.merge_stored_data = True
            with unittest.mock.patch(
                "writecondastat.condastat.WriteCondaStat._filter_data_frame_rows"
            ) as filter_data_frame_rows:
                write_conda_stat.write_condastat(
                    CondaStatDataSource.CONDAFORGE,
                    start_date="2022-01-01",
                    end_date="2022-01-03",
                )
                self.assertEqual(filter_data_frame_rows.call_count, 0)

    def test_outdir(self) -> None:
        """A method for testing WriteCondaStat.outdir."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            write_conda_stat = WriteCondaStat("pandas")
            write_conda_stat.fill_no_data = False
            write_conda_stat.merge_stored_data = False
            write_conda_stat.outdir = (
                f"{PATH}/.unittest/test_condastat/test_outdir_setter"
            )
            with unittest.mock.patch(
                "writecondastat.condastat.WriteCondaStat._filter_data_frame_rows"
            ) as filter_data_frame_rows:
                write_conda_stat.write_condastat(
                    CondaStatDataSource.CONDAFORGE,
                    start_date="2022-01-01",
                    end_date="2022-01-03",
                )
                self.assertEqual(filter_data_frame_rows.call_count, 1)

    def test_if_stats_are_not_available(self) -> None:
        """A method for testing WriteCondaStat.write_condastat() if stats are not available."""

        with unittest.mock.patch(
            "dask.dataframe.read_parquet", side_effect=FileNotFoundError
        ):
            outdir = f"{PATH}/.unittest/test_condastat/test_stats_are_not_available"
            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = False
            write_conda_stat.merge_stored_data = False
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2022-01-01",
                end_date="2022-01-03",
            )
            csv = f"{outdir}/2022_condastat.csv"
            self.assertEqual((csv, Path(csv).is_file()), (csv, False))

    def test_if_outdir_and_stats_are_none(self) -> None:
        """A method for testing WriteCondaStat.write_condastat() if outdir and stats are none."""

        with unittest.mock.patch(
            "dask.dataframe.read_parquet", side_effect=FileNotFoundError
        ):
            write_conda_stat = WriteCondaStat("pandas")
            write_conda_stat.fill_no_data = False
            write_conda_stat.merge_stored_data = False
            with unittest.mock.patch(
                "writecondastat.condastat.WriteCondaStat._filter_data_frame_rows"
            ) as filter_data_frame_rows:
                write_conda_stat.write_condastat(
                    CondaStatDataSource.CONDAFORGE,
                    start_date="2022-01-01",
                    end_date="2022-01-03",
                )
                self.assertEqual(filter_data_frame_rows.call_count, 0)

    def test_stats_fill_no_data_and_write_package_name(self) -> None:
        """
        A method for testing WriteCondaStat.write_condastat()
        if fill no data and write package name.
        """

        with unittest.mock.patch(
            "dask.dataframe.read_parquet", side_effect=FileNotFoundError
        ):
            outdir = f"{PATH}/.unittest/test_condastat/test_fill_no_data_and_write_package_name"
            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.write_package_name = True
            write_conda_stat.fill_no_data = True
            write_conda_stat.merge_stored_data = False
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2022-01-01",
                end_date="2022-01-03",
            )
            csv = f"{outdir}/2022_condastat.csv"
            self.assertTrue(
                filecmp.cmp(csv, f"{PATH}/assets/tests_ref/nan_with_packagename.csv"),
                "Csv files are different",
            )

    def test_stats_fill_no_data_and_not_write_package_name(self) -> None:
        """
        A method for testing WriteCondaStat.write_condastat()
        if fill no data and not write package name.
        """

        with unittest.mock.patch(
            "dask.dataframe.read_parquet", side_effect=FileNotFoundError
        ):
            outdir = f"{PATH}/.unittest/test_condastat/test_fill_no_data"
            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = True
            write_conda_stat.merge_stored_data = False
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2022-01-01",
                end_date="2022-01-03",
            )
            csv = f"{outdir}/2022_condastat.csv"
            self.assertTrue(
                filecmp.cmp(csv, f"{PATH}/assets/tests_ref/nan.csv"),
                "Csv files are different",
            )

    def test_date_period_with_year(self) -> None:
        """A method for testing WriteCondaStat.date_period with year."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            outdir = f"{PATH}/.unittest/test_condastat/test_date_period_year"
            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = False
            write_conda_stat.merge_stored_data = False
            write_conda_stat.date_period = StatPeriod.YEAR
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2020-12-31",
                end_date="2021-01-01",
            )
            csv1 = f"{outdir}/2020_condastat.csv"
            csv2 = f"{outdir}/2021_condastat.csv"
            csv3 = f"{outdir}/2022_condastat.csv"
            self.assertEqual(
                (
                    csv1,
                    Path(csv1).is_file(),
                    csv2,
                    Path(csv2).is_file(),
                    csv3,
                    Path(csv3).is_file(),
                ),
                (csv1, True, csv2, True, csv3, False),
            )

    def test_date_period_with_month(self) -> None:
        """A method for testing WriteCondaStat.date_period with month."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            outdir = f"{PATH}/.unittest/test_condastat/test_date_period_month"
            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = False
            write_conda_stat.merge_stored_data = False
            write_conda_stat.date_period = StatPeriod.MONTH
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2022-01-31",
                end_date="2022-02-01",
            )
            csv1 = f"{outdir}/2022-01_condastat.csv"
            csv2 = f"{outdir}/2022-02_condastat.csv"
            csv3 = f"{outdir}/2022-03_condastat.csv"
            self.assertEqual(
                (
                    csv1,
                    Path(csv1).is_file(),
                    csv2,
                    Path(csv2).is_file(),
                    csv3,
                    Path(csv3).is_file(),
                ),
                (csv1, True, csv2, True, csv3, False),
            )

    def test_date_period_with_day(self) -> None:
        """A method for testing WriteCondaStat.date_period with day."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            outdir = f"{PATH}/.unittest/test_condastat/test_date_period_day"
            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = False
            write_conda_stat.merge_stored_data = False
            write_conda_stat.date_period = StatPeriod.DAY
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2022-01-01",
                end_date="2022-01-02",
            )
            csv1 = f"{outdir}/2022-01-01_condastat.csv"
            csv2 = f"{outdir}/2022-01-02_condastat.csv"
            csv3 = f"{outdir}/2022-01-03_condastat.csv"
            self.assertEqual(
                (
                    csv1,
                    Path(csv1).is_file(),
                    csv2,
                    Path(csv2).is_file(),
                    csv3,
                    Path(csv3).is_file(),
                ),
                (csv1, True, csv2, True, csv3, False),
            )

    def test_date_period_with_none(self) -> None:
        """A method for testing WriteCondaStat.date_period with none."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            outdir = f"{PATH}/.unittest/test_condastat/test_date_period_none"
            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = False
            write_conda_stat.merge_stored_data = False
            write_conda_stat.date_period = StatPeriod.NONE
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2022-01-01",
                end_date="2022-01-02",
            )
            csv = f"{outdir}/condastat.csv"
            self.assertEqual(
                (
                    csv,
                    Path(csv).is_file(),
                ),
                (csv, True),
            )

    def test_merge_stored_data_with_year(self) -> None:
        """A method for testing WriteCondaStat.merge_stored_data with year."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            outdir = f"{PATH}/.unittest/test_condastat/test_merge_year"
            os.makedirs(outdir, exist_ok=True)
            shutil.copyfile(
                f"{PATH}/assets/tests_input/2021_with_nan_and_old_values.csv",
                f"{outdir}/2021_condastat.csv",
            )

            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = True
            write_conda_stat.merge_stored_data = True
            write_conda_stat.date_period = StatPeriod.YEAR
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2021-12-31",
                end_date="2022-01-02",
            )

            self.assertEqual(
                (
                    filecmp.cmp(
                        f"{outdir}/2021_condastat.csv",
                        f"{PATH}/assets/tests_ref/2021_merged.csv",
                    ),
                    filecmp.cmp(
                        f"{outdir}/2022_condastat.csv",
                        f"{PATH}/assets/tests_ref/2022_merged.csv",
                    ),
                ),
                (True, True),
            )

    def test_merge_stored_data_with_month(self) -> None:
        """A method for testing WriteCondaStat.merge_stored_data with month."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            outdir = f"{PATH}/.unittest/test_condastat/test_merge_month"
            os.makedirs(outdir, exist_ok=True)
            shutil.copyfile(
                f"{PATH}/assets/tests_input/2021_with_nan_and_old_values.csv",
                f"{outdir}/2021-12_condastat.csv",
            )

            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = True
            write_conda_stat.merge_stored_data = True
            write_conda_stat.date_period = StatPeriod.MONTH
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2021-12-31",
                end_date="2022-01-02",
            )

            self.assertEqual(
                (
                    filecmp.cmp(
                        f"{outdir}/2021-12_condastat.csv",
                        f"{PATH}/assets/tests_ref/2021_merged.csv",
                    ),
                    filecmp.cmp(
                        f"{outdir}/2022-01_condastat.csv",
                        f"{PATH}/assets/tests_ref/2022_merged.csv",
                    ),
                ),
                (True, True),
            )

    def test_merge_stored_data_with_day(self) -> None:
        """A method for testing WriteCondaStat.merge_stored_data with day."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            outdir = f"{PATH}/.unittest/test_condastat/test_merge_day"
            os.makedirs(outdir, exist_ok=True)
            shutil.copyfile(
                f"{PATH}/assets/tests_input/2021_with_nan_and_old_values.csv",
                f"{outdir}/2021-12-31_condastat.csv",
            )

            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = True
            write_conda_stat.merge_stored_data = True
            write_conda_stat.date_period = StatPeriod.DAY
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2021-12-31",
                end_date="2022-01-02",
            )

            self.assertEqual(
                (
                    filecmp.cmp(
                        f"{outdir}/2021-12-31_condastat.csv",
                        f"{PATH}/assets/tests_ref/2021_merged.csv",
                    ),
                    filecmp.cmp(
                        f"{outdir}/2022-01-01_condastat.csv",
                        f"{PATH}/assets/tests_ref/2022-01-01_merged.csv",
                    ),
                    filecmp.cmp(
                        f"{outdir}/2022-01-02_condastat.csv",
                        f"{PATH}/assets/tests_ref/2022-01-02_merged.csv",
                    ),
                ),
                (True, True, True),
            )

    def test_merge_stored_data_with_none(self) -> None:
        """A method for testing WriteCondaStat.merge_stored_data with none."""

        with unittest.mock.patch("dask.dataframe.read_parquet", return_value=STATS):
            outdir = f"{PATH}/.unittest/test_condastat/test_merge_none"
            os.makedirs(outdir, exist_ok=True)
            shutil.copyfile(
                f"{PATH}/assets/tests_input/2021_with_nan_and_old_values.csv",
                f"{outdir}/condastat.csv",
            )

            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = True
            write_conda_stat.merge_stored_data = True
            write_conda_stat.date_period = StatPeriod.NONE
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2021-12-31",
                end_date="2022-01-02",
            )

            self.assertTrue(
                filecmp.cmp(
                    f"{outdir}/condastat.csv", f"{PATH}/assets/tests_ref/merged.csv"
                ),
                "Csv files are different",
            )

    def test_merge_stored_data_if_no_stats_are_available(self) -> None:
        """A method for testing WriteCondaStat.merge_stored_data if no stats are available."""

        with unittest.mock.patch(
            "dask.dataframe.read_parquet", side_effect=FileNotFoundError
        ):
            outdir = (
                f"{PATH}/.unittest/test_condastat/test_merge_no_stats_are_available"
            )
            os.makedirs(outdir, exist_ok=True)
            shutil.copyfile(
                f"{PATH}/assets/tests_input/2021_with_nan_and_old_values.csv",
                f"{outdir}/2021_condastat.csv",
            )

            write_conda_stat = WriteCondaStat("pandas", outdir)
            write_conda_stat.fill_no_data = True
            write_conda_stat.merge_stored_data = True
            write_conda_stat.date_period = StatPeriod.YEAR
            write_conda_stat.write_condastat(
                CondaStatDataSource.CONDAFORGE,
                start_date="2021-12-31",
                end_date="2022-01-03",
            )

            self.assertEqual(
                (
                    filecmp.cmp(
                        f"{outdir}/2021_condastat.csv",
                        f"{PATH}/assets/tests_ref/2021_merged_partial.csv",
                    ),
                    filecmp.cmp(
                        f"{outdir}/2022_condastat.csv",
                        f"{PATH}/assets/tests_ref/nan.csv",
                    ),
                ),
                (True, True),
            )
