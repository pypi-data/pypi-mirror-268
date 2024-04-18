# -*- coding: utf-8 -*-

import pytest
from pandas import concat, DataFrame, Series
from numpy import nan
from interva.interva5 import InterVA5, get_example_input
from interva.utils import (csmf, get_indiv_cod, _get_age_group,
                           _get_age_group_all, _get_cod_with_dem,
                           _get_dem_groups, _get_sex_group)
from interva.exceptions import ArgumentException

va_data = get_example_input()
iv5out = InterVA5(va_data, hiv="h", malaria="l", write=False)
iv5out.run()
y = [1, "y", "Y", "yes", "Yes", "YES"]
n = [0, ".", "n", "N", "no", "NO", "No", nan]
age_letters = ["a", "b", "c", "d", "e", "f", "g"]
age_indicators = [f"i022{i}" for i in age_letters]
adult_indicators = [f"i022{i}" for i in ["a", "b", "c"]]
child_indicators = [f"i022{i}" for i in ["d", "e", "f"]]
age_labels = [("age 65+", "adult"), ("age 50-64", "adult"),
              ("age 15-49", "adult"), ("age 5-14", "child"),
              ("age 1-4", "child"), ("age 1-11m", "child"),
              ("age 0-27d", "neonate")]
all_age_groups = dict(zip(age_indicators, age_labels))


def make_age_test_data(age_group, yes, no):
    sex_groups = Series({"ID": "d1", "i019a": "y", "i019b": "n"})
    age_groups = Series({f"i022{i}": no for i in age_letters}).astype(object)
    age_groups[age_group] = yes
    va_record = concat([sex_groups, age_groups])
    age_all, age = all_age_groups[age_group]
    return va_record, age, age_all


def test_get_sex_group_exception():
    with pytest.raises(ArgumentException):
        _get_sex_group("a")


@pytest.mark.parametrize("female", y)
@pytest.mark.parametrize("male", n)
def test_get_sex_group_female(male, female):
    va_record = Series({"ID": "d1", "i019a": male, "i019b": female})
    assert _get_sex_group(va_record) == "female"
    assert _get_dem_groups(va_record).get("sex") == "female"


@pytest.mark.parametrize("male", y)
@pytest.mark.parametrize("female", n)
def test_get_sex_group_male(male, female):
    va_record = Series({"ID": "d1", "i019a": male, "i019b": female})
    assert _get_sex_group(va_record) == "male"
    assert _get_dem_groups(va_record).get("sex") == "male"


def test_get_sex_group_unknown():
    va_record = Series({"ID": "d1", "i019a": 0, "i019b": 0})
    assert _get_sex_group(va_record) == "unknown"
    assert _get_dem_groups(va_record).get("sex") == "unknown"


def test_get_age_group_exception():
    with pytest.raises(ArgumentException):
        _get_age_group("a")


def test_get_age_group_all_exception():
    with pytest.raises(ArgumentException):
        _get_age_group_all("a")


@pytest.mark.parametrize("age", age_indicators)
@pytest.mark.parametrize("yes", y)
@pytest.mark.parametrize("no", n)
def test_get_age_groups(age, yes, no):
    va_record, age_label, age_all_label = make_age_test_data(age, yes, no)
    assert _get_age_group(va_record) == age_label
    assert _get_age_group_all(va_record) == age_all_label
    assert _get_dem_groups(va_record).get("age") == age_label


def test_get_age_groups_unknown():
    va_record, age_label, age_all_label = make_age_test_data("i022a", 0, 0)
    assert _get_age_group(va_record) == "unknown"
    assert _get_dem_groups(va_record).get("age") == "unknown"


# def test_csmf_exception_df_input():
#     with pytest.raises(ArgumentException):
#         csmf("a")


def test_csmf_exception_zero_rows():
    bad_input = InterVA5(va_data, hiv="h", malaria="l", write=False)
    with pytest.raises(ArgumentException):
        csmf(bad_input)


def test_csmf_exception_df_columns():
    bad_input = InterVA5(va_data, hiv="h", malaria="l", write=False)
    bad_input.results["VA5"] = iv5out.results["VA5"].drop(columns="MALPREV")
    with pytest.raises(ArgumentException):
        csmf(bad_input)


def test_csmf_returns_series():
    out1 = csmf(iv5out, top=10, interva_rule=True, top_aggregate=None)
    out2 = csmf(iv5out, top=10, interva_rule=False, top_aggregate=None)
    out3 = csmf(iv5out, top=10, interva_rule=True, top_aggregate=10)
    out4 = csmf(iv5out)
    assert isinstance(out1, Series)
    assert isinstance(out2, Series)
    assert isinstance(out3, Series)
    assert isinstance(out4, Series)


def test_get_cod_with_dem():
    out = _get_cod_with_dem(iv5out)
    assert "age" in out.columns
    assert "sex" in out.columns


def test_get_indiv_cod():
    out1 = get_indiv_cod(iv5out)
    out2 = get_indiv_cod(iv5out, top=5, interva_rule=False)
    out3 = get_indiv_cod(iv5out, top=5,
                         include_propensities=True,
                         interva_rule=False)
    assert out1.equals(iv5out.get_indiv_prob())
    assert (out2["CAUSE5"] != " ").all()
    assert out2.shape[1] == 6
    assert (out3["PROPENSITY5"] != " ").all()
    assert out3.shape[1] == 11
