"""A module for testing the writecondastat.condastat module."""

import unittest
import unittest.mock
from pathlib import Path
from datetime import datetime, date

from writecondastat.statdate import StatPeriod
from writecondastat.condastat import CondaStatDataSource, WriteCondaStat


PATH = Path(__file__).parent


class TestWriteActualCondaStat(unittest.TestCase):
    """A class for testing WriteCondaStat.write_actual_condastat() method."""

    def test_if_stats_are_not_available(self) -> None:
        """
        A method for testing WriteCondaStat.write_actual_condastat()
        if stats are not available.
        """

        outdir = f"{PATH}/.unittest/test_condastat/test_stats_are_not_available_actual"
        write_conda_stat = WriteCondaStat("not-available-package", outdir)
        write_conda_stat.fill_no_data = False
        write_conda_stat.merge_stored_data = False
        write_conda_stat.write_actual_condastat(
            CondaStatDataSource.CONDAFORGE,
        )
        csv = f"{outdir}/2022_condastat.csv"
        self.assertEqual((csv, Path(csv).is_file()), (csv, False))

    def test_stats_fill_no_data_and_write_package_name(self) -> None:
        """
        A method for testing WriteCondaStat.write_actual_condastat()
        if fill no data and write package name.
        """

        outdir = f"{PATH}/.unittest/test_condastat/test_fill_no_data_and_write_package_name_actual"
        write_conda_stat = WriteCondaStat("not-available-package", outdir)
        write_conda_stat.write_package_name = True
        write_conda_stat.fill_no_data = True
        write_conda_stat.merge_stored_data = False
        write_conda_stat.write_actual_condastat(
            CondaStatDataSource.CONDAFORGE,
        )
        csv = f"{outdir}/{datetime.now().strftime('%Y')}_condastat_actual.csv"
        with open(csv, "r", encoding="utf8") as out, open(
            f"{PATH}/assets/tests_ref/nan_with_packagename_actual.csv",
            "r",
            encoding="utf8",
        ) as ref:
            self.assertTrue(
                out.read(),
                ref.read().replace("today", datetime.now().strftime("%Y-%m-%d")),
            )

    def test_stats_fill_no_data_and_not_write_package_name(self) -> None:
        """
        A method for testing WriteCondaStat.write_actual_condastat()
        if fill no data and not write package name.
        """

        outdir = f"{PATH}/.unittest/test_condastat/test_fill_no_data_actual"
        write_conda_stat = WriteCondaStat("not-available-package", outdir)
        write_conda_stat.fill_no_data = True
        write_conda_stat.merge_stored_data = False
        write_conda_stat.write_actual_condastat(
            CondaStatDataSource.CONDAFORGE,
        )
        csv = f"{outdir}/{datetime.now().strftime('%Y')}_condastat_actual.csv"
        with open(csv, "r", encoding="utf8") as out, open(
            f"{PATH}/assets/tests_ref/nan_actual.csv",
            "r",
            encoding="utf8",
        ) as ref:
            self.assertTrue(
                out.read(),
                ref.read().replace("today", datetime.now().strftime("%Y-%m-%d")),
            )

    def test_date_period_with_year(self) -> None:
        """A method for testing WriteCondaStat.date_period with year."""

        outdir = f"{PATH}/.unittest/test_condastat/test_date_period_year_actual"
        write_conda_stat = WriteCondaStat("pandas", outdir)
        write_conda_stat.fill_no_data = False
        write_conda_stat.merge_stored_data = False
        write_conda_stat.date_period = StatPeriod.YEAR
        write_conda_stat.write_actual_condastat(
            CondaStatDataSource.CONDAFORGE,
        )
        year = date.today().strftime("%Y")
        csv = f"{outdir}/{year}_condastat_actual.csv"
        self.assertEqual(
            (csv, Path(csv).is_file()),
            (csv, True),
        )

    def test_date_period_with_month(self) -> None:
        """A method for testing WriteCondaStat.date_period with month."""

        outdir = f"{PATH}/.unittest/test_condastat/test_date_period_month_actual"
        write_conda_stat = WriteCondaStat("pandas", outdir)
        write_conda_stat.fill_no_data = False
        write_conda_stat.merge_stored_data = False
        write_conda_stat.date_period = StatPeriod.MONTH
        write_conda_stat.write_actual_condastat(
            CondaStatDataSource.CONDAFORGE,
        )
        year = date.today().strftime("%Y")
        month = date.today().strftime("%m")
        csv = f"{outdir}/{year}-{month}_condastat_actual.csv"
        self.assertEqual(
            (csv, Path(csv).is_file()),
            (csv, True),
        )

    def test_date_period_with_day(self) -> None:
        """A method for testing WriteCondaStat.date_period with day."""

        outdir = f"{PATH}/.unittest/test_condastat/test_date_period_day_actual"
        write_conda_stat = WriteCondaStat("pandas", outdir)
        write_conda_stat.fill_no_data = False
        write_conda_stat.merge_stored_data = False
        write_conda_stat.date_period = StatPeriod.DAY
        write_conda_stat.write_actual_condastat(
            CondaStatDataSource.CONDAFORGE,
        )
        year = date.today().strftime("%Y")
        month = date.today().strftime("%m")
        day = date.today().strftime("%d")
        csv = f"{outdir}/{year}-{month}-{day}_condastat_actual.csv"
        self.assertEqual(
            (csv, Path(csv).is_file()),
            (csv, True),
        )

    def test_date_period_with_none(self) -> None:
        """A method for testing WriteCondaStat.date_period with none."""

        outdir = f"{PATH}/.unittest/test_condastat/test_date_period_none_actual"
        write_conda_stat = WriteCondaStat("pandas", outdir)
        write_conda_stat.fill_no_data = False
        write_conda_stat.merge_stored_data = False
        write_conda_stat.date_period = StatPeriod.NONE
        write_conda_stat.write_actual_condastat(
            CondaStatDataSource.CONDAFORGE,
        )
        csv = f"{outdir}/condastat_actual.csv"
        self.assertEqual(
            (csv, Path(csv).is_file()),
            (csv, True),
        )
