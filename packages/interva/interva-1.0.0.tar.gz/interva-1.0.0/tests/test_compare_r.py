# # -*- coding: utf-8 -*-

from interva.interva5 import InterVA5, get_example_input
from interva.utils import csmf
from rpy2.robjects.packages import data, importr
import rpy2.robjects as robjects
from rpy2.robjects.conversion import get_conversion, localconverter
from rpy2.robjects import pandas2ri

r_iva5 = importr("InterVA5")
randomva5 = data(r_iva5).fetch("RandomVA5")["RandomVA5"]
probbasev5 = data(r_iva5).fetch("probbaseV5")["probbaseV5"]

robjects.r("data(probbaseV5, package='InterVA5')")
robjects.r("data(RandomVA5, package='InterVA5')")
robjects.r('''
  ra5 <- as.matrix(RandomVA5)
  r_va5 <- InterVA5(ra5, HIV="h", Malaria="l", directory=".",
                    groupcode=FALSE)$VA5
  prob <- matrix(NA, nrow=nrow(ra5), ncol=length(r_va5[[1]]$wholeprob))
  r_prob_names <- colnames(r_va5[[1]]$wholeprob)
  for (i in 1:nrow(ra5)) {
    prob[i,] <- r_va5[[i]]$wholeprob
  }
  csmf <- InterVA5::CSMF.interVA5(r_va5)
  csmf5_no_rule <- InterVA5::CSMF5(r_va5, noplot=TRUE)
  csmf5_no_rule2 <- InterVA5::CSMF5(r_va5, top.aggregate = 8, noplot=TRUE)

  r_prob_df <- as.data.frame(prob, colnames=r_prob_names)
  csmf_top15 <- as.data.frame(csmf[order(csmf, decreasing=TRUE)[1:15]])
  df_csmf5_1 <- as.data.frame(csmf5_no_rule)
  df_csmf5_2 <- as.data.frame(csmf5_no_rule2)
''')
r_prob_df = robjects.globalenv["r_prob_df"]
csmf_top15 = robjects.globalenv["csmf_top15"]
df_csmf5_1 = robjects.globalenv["df_csmf5_1"]
df_csmf5_2 = robjects.globalenv["df_csmf5_2"]

with localconverter(robjects.default_converter + pandas2ri.converter):
    r_prob_check = get_conversion().rpy2py(r_prob_df)
    r_csmf_top15_check = get_conversion().rpy2py(csmf_top15)
    r_csmf5_1 = get_conversion().rpy2py(df_csmf5_1)
    r_csmf5_2 = get_conversion().rpy2py(df_csmf5_2)

va_data = get_example_input()
iv5out = InterVA5(va_data, hiv="h", malaria="l", directory=".",
                  groupcode=False)
iv5out.run()
py_prob_check = iv5out.results["VA5"].loc[:, "WHOLEPROB"]
py_csmf_top15_check = iv5out.get_csmf(top=15, groupcode=False)
py_csmf5_1 = csmf(iv5out, interva_rule=False, top=15)
py_csmf5_2 = csmf(iv5out, interva_rule=False,
                  top=15, top_aggregate=8)


def test_r_va5_comparison():
    for i in range(r_prob_check.shape[0]):
        for j in range(r_prob_check.shape[1]):
            a = round(r_prob_check.iloc[i, j], 10)
            b = round(py_prob_check.iloc[i].iloc[j], 10)
            assert a == b


def test_r_csmf_top15_comparison():
    assert (py_csmf_top15_check.index == r_csmf_top15_check.index).all()
    py_csmf_top15 = py_csmf_top15_check.to_numpy()
    r_csmf_top15 = r_csmf_top15_check.to_numpy()
    for i in range(len(r_csmf_top15_check)):
        a = round(float(py_csmf_top15[i]), 10)
        b = round(float(r_csmf_top15[i][0]), 10)
        assert a == b


def tests_utils_csmf_1():
    r_csmf5_1_top15 = r_csmf5_1.sort_values(
        by="csmf5_no_rule", ascending=False)[0:15]
    py_csmf5_1_top15 = py_csmf5_1.sort_values(ascending=False)
    assert (r_csmf5_1_top15.index == py_csmf5_1_top15.index).all()
    py_csmf5_1_top15 = py_csmf5_1_top15.to_numpy()
    r_csmf5_1_top15 = r_csmf5_1_top15.to_numpy()
    for i in range(len(r_csmf5_1_top15)):
        a = round(float(py_csmf5_1_top15[i]), 10)
        b = round(float(r_csmf5_1_top15[i][0]), 10)
        assert a == b


def tests_utils_csmf_2():
    r_csmf5_2_top15 = r_csmf5_2.sort_values(
        by="csmf5_no_rule2", ascending=False)[0:15]
    py_csmf5_2_top15 = py_csmf5_2.sort_values(ascending=False)
    assert (r_csmf5_2_top15.index == py_csmf5_2_top15.index).all()
    py_csmf5_2_top15 = py_csmf5_2_top15.to_numpy()
    r_csmf5_2_top15 = r_csmf5_2_top15.to_numpy()
    for i in range(len(r_csmf5_2_top15)):
        a = round(float(py_csmf5_2_top15[i]), 4)
        b = round(float(r_csmf5_2_top15[i][0]), 4)
        assert a == b
