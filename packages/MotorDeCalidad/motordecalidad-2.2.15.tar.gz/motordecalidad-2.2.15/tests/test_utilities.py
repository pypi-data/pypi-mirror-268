import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def ipython_mock(mocker):
    ipython_mock = MagicMock()
    user_ns_mock = MagicMock()
    ipython_mock.user_ns = user_ns_mock
    with patch("IPython.get_ipython", return_value=ipython_mock):
        yield ipython_mock

def test_normalization():
    from motordecalidad.utilities import normalizeValue
    result = normalizeValue(None)
    assert result == None

def test_normalization2():
    from motordecalidad.utilities import normalizeValue
    result = normalizeValue("Híbrido")
    assert result == "Hibrido"

def test_apply_filter(test_df,expected_df):
    from motordecalidad.utilities import applyFilter
    mocked_filtered = {
        "FIELDS":"id",
        "VALUES":"a"
    }
    df = applyFilter(test_df,mocked_filtered)
    assert df.collect() == expected_df.collect()

def test_apply_filter_null(test_df,expected_df):
    from motordecalidad.utilities import applyFilter
    mocked_filtered = {
    }
    df = applyFilter(test_df,mocked_filtered)
    assert df.collect() == test_df.collect()

def test_chooseComparisonOperator(spark_session):
    from operator import ge, gt, le, lt
    from motordecalidad.utilities import chooseComparisonOparator
    result1 = chooseComparisonOparator(True,True,True)
    result2 = chooseComparisonOparator(True,False,True)
    result3 = chooseComparisonOparator(False,True,True)
    result4 = chooseComparisonOparator(False, False, True)
    result5 = chooseComparisonOparator(True,True,False)
    result6 = chooseComparisonOparator(True,False,False)
    result7 = chooseComparisonOparator(False,True,False)
    result8 = chooseComparisonOparator(False, False, False)
    assert result1 == (lt, gt)
    assert result2 == (lt, ge)
    assert result3 == (le, gt)
    assert result4 == (le, ge)
    assert result5 == (ge, le)
    assert result6 == (ge, lt)
    assert result7 == (gt, le)
    assert result8 == (gt, lt)

def test_get_dbutils(ipython_mock):
    from motordecalidad.utilities import get_dbutils
    ipython_mock.user_ns.__getitem__.return_value = "Valor de dbutils en Databricks"
    result = get_dbutils()
    assert result == "Valor de dbutils en Databricks"

def test_utf8_to_latin1():
    from motordecalidad.utilities import utf8_to_latin1
    result = utf8_to_latin1(None)
    assert result == None

def test_convert_field_to_struct(spark_session,test_df):
    from motordecalidad.utilities import convert_field_to_struct
    from pyspark.sql.types import StructField,StringType,StructType
    Fields = convert_field_to_struct(test_df,["id","value","date","mix"])
    expectedFields = StructType([StructField("id", StringType()), StructField("value", StringType()),StructField("date", StringType()),StructField("mix", StringType())])
    assert Fields == expectedFields

def test_choose_oper(spark_session):
    from motordecalidad.utilities import chooseOper
    from pyspark.sql.functions import col
    from operator import eq, ne, gt, lt, le, ge
    op_function_sum = chooseOper(col("campo"), '+')
    op_function_sust = chooseOper(col("campo"), '-')
    op_function_mul = chooseOper(col("campo"),"*")
    op_function_div = chooseOper(col("campo"),"/")
    op_function_eq = chooseOper(col("campo"), '==')
    op_function_not_eq = chooseOper(col("campo"), '!=')
    op_function_gt_eq = chooseOper(col("campo"), '<=')
    op_function_lt_eq = chooseOper(col("campo"), '>=')
    op_function_gt = chooseOper(col("campo"), '>')
    op_function_lt = chooseOper(col("campo"), '<')
    assert op_function_sum.__func__ == col("campo").__add__.__func__
    assert op_function_sust.__func__ == col("campo").__sub__.__func__
    assert op_function_mul.__func__ == col("campo").__mul__.__func__
    assert op_function_div.__func__ == col("campo").__div__.__func__
    assert op_function_eq == ne
    assert op_function_not_eq == eq
    assert op_function_gt_eq == gt
    assert op_function_lt_eq == lt
    assert op_function_gt == le
    assert op_function_lt == ge

def test_operation(test_df):
    from motordecalidad.utilities import operation
    result_df = operation(test_df, "value + 10")
    assert "ss" in result_df.columns