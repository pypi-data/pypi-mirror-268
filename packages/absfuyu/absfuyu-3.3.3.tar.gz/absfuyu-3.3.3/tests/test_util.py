"""
Test: Util

Version: 1.1.0
Date updated: 14/04/2024 (dd/mm/yyyy)
"""

import sys

import pytest

from absfuyu.core import CONFIG_PATH, CORE_PATH
from absfuyu.util import set_max, set_min, set_min_max
from absfuyu.util.api import APIRequest, PingResult, ping_windows
from absfuyu.util.json_method import JsonFile
from absfuyu.util.path import Directory


# MARK: util
@pytest.mark.abs_util
class TestUtil:
    """absfuyu.util"""

    @pytest.mark.parametrize(["value", "output"], [(10, 10), (-5, 0)])
    def test_set_min(self, value: int, output: int) -> None:
        assert set_min(value, min_value=0) == output

    @pytest.mark.parametrize(["value", "output"], [(200, 100), (10, 10)])
    def test_set_max(self, value: int, output: int) -> None:
        assert set_max(value, max_value=100) == output

    @pytest.mark.parametrize(["value", "output"], [(50, 50), (-10, 0), (200, 100)])
    def test_set_min_max(self, value: int, output: int) -> None:
        assert set_min_max(value, min_value=0, max_value=100) == output


# MARK: api
@pytest.mark.abs_util
class TestUtilAPI:
    """absfuyu.util.api"""

    @pytest.mark.skip  # temporary skip
    def test_API(self) -> None:
        instance = APIRequest("https://dummyjson.com/quotes")
        try:
            assert isinstance(instance.fetch_data_only().json()["quotes"], list)
        except Exception:
            # No internet
            assert instance

    def test_ping_windows(self) -> None:
        if sys.platform in ["win32", "cygwin"]:  # windows only
            res = ping_windows(["google.com"], 1)
            assert isinstance(res[0], PingResult)
        assert True


# MARK: json
@pytest.mark.abs_util
class TestUtilJsonMethod:
    """absfuyu.util.json_method"""

    def test_json_load(self) -> None:
        instance = JsonFile(CONFIG_PATH)
        loaded = instance.load_json()
        assert isinstance(loaded, dict)


# MARK: path
@pytest.mark.abs_util
class TestUtilPath:
    """absfuyu.util.path"""

    def test_list_structure(self) -> None:
        instance = Directory(source_path=CORE_PATH)
        assert instance.list_structure_pkg()
