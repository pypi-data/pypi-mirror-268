"""A module for testing the writecondastat.statdate module."""

import unittest
from datetime import date, datetime
from dateutil.relativedelta import relativedelta  # type: ignore


from writecondastat.statdate import StatDate


class TestStatDate(unittest.TestCase):
    """A class for testing StatDate class."""

    def test_init_if_end_is_before_start(self) -> None:
        """A method for testing StatDate.__init__() if end is before start."""

        with self.assertRaises(AssertionError):
            StatDate(start="2022-01-01", end="2021-12-31")

    def test_start(self) -> None:
        """A method for testing StatDate.start."""

        start = "2022-01-01"
        statdate = StatDate()
        statdate.start = start  # type: ignore
        self.assertEqual(
            statdate.start.strftime("%Y-%m-%d"),  # type: ignore  # pylint: disable=no-member
            start,
        )

    def test_start_if_after_end(self) -> None:
        """A method for testing StatDate.start if after end."""

        statdate = StatDate(start="2021-12-31", end="2022-01-01")
        with self.assertRaises(AssertionError):
            statdate.start = "2022-01-02"  # type: ignore

    def test_end(self) -> None:
        """A method for testing StatDate.end."""

        end = "2022-01-01"
        statdate = StatDate(start="2021-12-31")
        statdate.end = end  # type: ignore
        self.assertEqual(
            statdate.end.strftime("%Y-%m-%d"),  # type: ignore  # pylint: disable=no-member
            end,
        )

    def test_end_if_before_start(self) -> None:
        """A method for testing StatDate.end if before start."""

        statdate = StatDate(start="2021-12-31", end="2022-01-01")
        with self.assertRaises(AssertionError):
            statdate.end = "2021-12-20"  # type: ignore

    def test_format_start_with_none(self) -> None:
        """A method for testing StatDate.format_start with None."""

        start = StatDate.format_start(None)
        self.assertEqual(
            start.strftime("%Y-%m-%d"),
            (date.today() + relativedelta(months=-2)).strftime("%Y-%m-%d"),
        )

    def test_format_start_with_datetime(self) -> None:
        """A method for testing StatDate.format_start with datetime."""

        now = datetime.now()
        start = StatDate.format_start(now)
        self.assertEqual(
            start.strftime("%Y-%m-%d"),
            now.strftime("%Y-%m-%d"),
        )

    def test_format_start_with_year(self) -> None:
        """A method for testing StatDate.format_start with year."""

        start = StatDate.format_start("2022")
        self.assertEqual(
            start.strftime("%Y-%m-%d"),
            "2022-01-01",
        )

    def test_format_start_with_month(self) -> None:
        """A method for testing StatDate.format_start with month."""

        start = StatDate.format_start("2022-01")
        self.assertEqual(
            start.strftime("%Y-%m-%d"),
            "2022-01-01",
        )

    def test_format_start_with_day(self) -> None:
        """A method for testing StatDate.format_start with day."""

        start = StatDate.format_start("2022-01-01")
        self.assertEqual(
            start.strftime("%Y-%m-%d"),
            "2022-01-01",
        )

    def test_format_start_with_invalid(self) -> None:
        """A method for testing StatDate.format_start with invalid."""

        with self.assertRaises(ValueError):
            StatDate.format_start("2022-01-01-01")

    def test_format_end_with_none(self) -> None:
        """A method for testing StatDate.format_end with None."""

        end = StatDate.format_end(None)
        self.assertEqual(
            end.strftime("%Y-%m-%d"),
            datetime.now().strftime("%Y-%m-%d"),
        )

    def test_format_end_with_datetime(self) -> None:
        """A method for testing StatDate.format_end with datetime."""

        now = datetime.now()
        end = StatDate.format_end(now)
        self.assertEqual(
            end.strftime("%Y-%m-%d"),
            now.strftime("%Y-%m-%d"),
        )

    def test_format_end_with_year(self) -> None:
        """A method for testing StatDate.format_end with year."""

        end = StatDate.format_end("2022")
        self.assertEqual(
            end.strftime("%Y-%m-%d"),
            "2022-12-31",
        )

    def test_format_end_with_month(self) -> None:
        """A method for testing StatDate.format_end with month."""

        end = StatDate.format_end("2022-12")
        self.assertEqual(
            end.strftime("%Y-%m-%d"),
            "2022-12-31",
        )

    def test_format_end_with_day(self) -> None:
        """A method for testing StatDate.format_end with day."""

        end = StatDate.format_end("2022-12-31")
        self.assertEqual(
            end.strftime("%Y-%m-%d"),
            "2022-12-31",
        )

    def test_format_end_with_invalid(self) -> None:
        """A method for testing StatDate.format_end with invalid."""

        with self.assertRaises(ValueError):
            StatDate.format_end("2022-12-31-31")
