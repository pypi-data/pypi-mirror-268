def test_requisites(test_df):
    from motordecalidad.rules import validateRequisites
    data = validateRequisites(test_df,["id","value","date"])
    assert data[-1] == 0

def test_requisites_two(test_df_requisites):
    from motordecalidad.rules import validateRequisites
    data = validateRequisites(test_df_requisites,["id","value","date"])
    assert data[-1] == 0

def test_requisites_three(test_df):
    from motordecalidad.rules import validateRequisites
    data = validateRequisites(test_df,["id","value","date","extra"])
    assert data[-1] == 3

def test_null(test_df):
    from motordecalidad.rules import validateNull
    data,errorDf = validateNull(test_df,"id",3,"TEST","100")
    assert data[-1] == 0

def test_null_empty_errorDF(test_df):
    from motordecalidad.rules import validateNull
    data,errorDf = validateNull(test_df,"id",3,"TEST","50")
    assert errorDf.count() == 0

def test_duplicates(test_df):
    from motordecalidad.rules import validateDuplicates

    data,errorDf = validateDuplicates(test_df,["id"],3,"TEST","100")
    assert data[-1] == 0

def test_duplicates_empty_errorDF(test_df):
    from motordecalidad.rules import validateDuplicates
    data,errorDf = validateDuplicates(test_df,["id"],3,"TEST","50")
    assert errorDf.count() == 0

def test_integrity(test_df):
    from motordecalidad.rules import validateReferentialIntegrity
    data,errorDf = validateReferentialIntegrity(test_df,test_df,["id"],["id"],3,"TEST","TEST","100")
    assert data[-1] == 0

def test_integrity_empty_errorDF(test_df):
    from motordecalidad.rules import validateReferentialIntegrity
    data,errorDf = validateReferentialIntegrity(test_df,test_df,["id"],["id"],3,"TEST","TEST","50")
    assert errorDf.count() == 0

def test_format_date(test_df,spark_session):
    from motordecalidad.rules import validateFormatDate
    data,errorDf = validateFormatDate(test_df,"yyyy-MM-dd","date","TEST","100",spark_session)
    assert data[-1] == 0

def test_format_date_timestamp(test_df,spark_session):
    from motordecalidad.rules import validateFormatDate
    data,errorDf = validateFormatDate(test_df,"yyyy-MM-dd HH:mm:ss","nullCol","TEST","100",spark_session)
    assert data[-1] == 0

def test_format_date_null(test_df,spark_session):
    from motordecalidad.rules import validateFormatDate
    data,errorDf = validateFormatDate(test_df,"yyyy-MM-dd HH:mm:ss","date","TEST","100",spark_session)
    assert data[-1] == 3

def test_format_date_empty_errorDF(test_df,spark_session):
    from motordecalidad.rules import validateFormatDate
    data,errorDf = validateFormatDate(test_df,"yyyy-MM-dd","date","TEST","50",spark_session)
    assert errorDf.count() == 0

def test_validate_range(test_df):
    from motordecalidad.rules import validateRange
    data, errorDF = validateRange(test_df,"value",3,"TEST","100","0","4")
    assert data[-1] == 0

def test_validate_range_two(test_df):
    from motordecalidad.rules import validateRange
    data, errorDF = validateRange(test_df,"value",3,"TEST","100","0")
    assert data[-1] == 0

def test_validate_range_three(test_df):
    from motordecalidad.rules import validateRange
    data, errorDF = validateRange(test_df,"value",3,"TEST","100","0",inclusive=False)
    assert data[-1] == 0

def test_validate_range_four(test_df):
    from motordecalidad.rules import validateRange
    data, errorDF = validateRange(test_df,"value",3,"TEST","100",maxRange="4")
    assert data[-1] == 0

def test_validate_range_col(test_df):
    from motordecalidad.rules import validateRange
    data, errorDF = validateRange(test_df,"value",3,"TEST","100","min","max")
    assert data[-1] == 0

def test_validate_range_empty_errorDF(test_df):
    from motordecalidad.rules import validateRange
    data, errorDF = validateRange(test_df,"value",3,"TEST","50","0","4")
    assert errorDF.count() == 0

def test_validate_catalog(test_df_catalog):
    from motordecalidad.rules import validateCatalog
    data, errorDf = validateCatalog(test_df_catalog,"id",4,"TEST","100",["á","é","í","ó","ú","Híbrido"])
    assert data[-1] == 1

def test_validate_catalog_empty_errorDF(test_df_catalog):
    from motordecalidad.rules import validateCatalog
    data, errorDf = validateCatalog(test_df_catalog,"id",4,"TEST","50",["á","é","í","ó","ú","Híbrido"])
    assert errorDf.count() == 0

def test_validate_forb_char(test_df):
    from motordecalidad.rules import validateForbiddenCharacters
    data, errorDf = validateForbiddenCharacters(test_df,"id",["-"],3,"TEST","100")
    assert data[-1] == 0

def test_validate_forb_char_empty_errorDF(test_df):
    from motordecalidad.rules import validateForbiddenCharacters
    data, errorDf = validateForbiddenCharacters(test_df,"id",["-"],3,"TEST","50")
    assert errorDf.count() == 0

def test_validate_type(test_df):
    from motordecalidad.rules import validateType
    data, errorDF = validateType(test_df,"string","id",3,"TEST","100")
    assert data[-1] == 0

def test_validate_type_empty_errorDF(test_df):
    from motordecalidad.rules import validateType
    data, errorDF = validateType(test_df,"string","id",3,"TEST","50")
    assert errorDF.count() == 0

def test_validate_composision(test_df):
    from motordecalidad.rules import validateComposision
    data, errorDf = validateComposision(test_df,"mix",["id","value"],3,"TEST","100","_")
    assert data[-1] == 0

def test_validate_composision_empty_errorDF(test_df):
    from motordecalidad.rules import validateComposision
    data, errorDf = validateComposision(test_df,"mix",["id","value"],3,"TEST","50","_")
    assert errorDf.count() == 0

def test_validate_length(test_df):
    from motordecalidad.rules import validateLength
    data, errorDf = validateLength(test_df,"id",3,"TEST","100","0","2")
    assert data[-1] == 0

def test_validate_length_two(test_df):
    from motordecalidad.rules import validateLength
    data, errorDf = validateLength(test_df,"id",3,"TEST","100","0")
    assert data[-1] == 0

def test_validate_length_three(test_df):
    from motordecalidad.rules import validateLength
    data, errorDf = validateLength(test_df,"id",3,"TEST","100",maxRange="2")
    assert data[-1] == 0

def test_validate_length_empty_errorDF(test_df):
    from motordecalidad.rules import validateLength
    data, errorDf = validateLength(test_df,"id",3,"TEST","50","0","2")
    assert errorDf.count() == 0

def test_validate_data_type(test_df):
    from motordecalidad.rules import validateDataType
    data = validateDataType(test_df,"id",3,"TEST","100","StringType()")
    assert data[-1] == 0

def test_validate_data_type_two(test_df):
    from motordecalidad.rules import validateDataType
    data = validateDataType(test_df,"id",3,"TEST","100","IntegerType()")
    assert data[-1] == 3

def test_validate_data_type_lower_one(test_df):
    from motordecalidad.rules import validateDataType
    data = validateDataType(test_df,"iD",3,"TEST","100","StringType()")
    assert data[-1] == 0
    
def test_validate_data_type_lower_two(test_df):
    from motordecalidad.rules import validateDataType
    data = validateDataType(test_df,"iD",3,"TEST","100","IntegerType()")
    assert data[-1] == 3


def test_validate_data_type_upper_one(test_df):
    from motordecalidad.rules import validateDataType
    data = validateDataType(test_df,"identifier",3,"TEST","100","StringType()")
    assert data[-1] == 0
    
def test_validate_data_type_upper_two(test_df):
    from motordecalidad.rules import validateDataType
    data = validateDataType(test_df,"identifier",3,"TEST","100","IntegerType()")
    assert data[-1] == 3

def test_validate_numeric_format(test_df):
    from motordecalidad.rules import validateFormatNumeric
    data,errorDf = validateFormatNumeric(test_df,"value",3,"TEST","100","2","2")
    assert data[-1] == 0

def test_validate_numeric_format_empty_errorDF(test_df):
    from motordecalidad.rules import validateFormatNumeric
    data,errorDf = validateFormatNumeric(test_df,"value",3,"TEST","50","2","2")
    assert errorDf.count() == 0

def test_validate_time_in_range(test_df):
    from motordecalidad.rules import validateTimeInRange
    data,errorDf = validateTimeInRange(test_df,"date","2022-12-31","yyyy-MM-dd","YEAR",3,"TEST","100",maxRange="1")
    assert data[-1] == 0

def test_validate_time_in_range_two(test_df):
    from motordecalidad.rules import validateTimeInRange
    data,errorDf = validateTimeInRange(test_df,"date","ref_date","yyyy-MM-dd","YEAR",3,"TEST","100",maxRange="1")
    assert data[-1] == 0

def test_validate_time_in_range_three(test_df):
    from motordecalidad.rules import validateTimeInRange
    data,errorDf = validateTimeInRange(test_df,"date","hoy","yyyy-MM-dd","YEAR",3,"TEST","100",maxRange="2")
    assert data[-1] == 0

def test_validate_time_in_range_month(test_df):
    from motordecalidad.rules import validateTimeInRange
    data,errorDf = validateTimeInRange(test_df,"date","2022-12-31","yyyy-MM-dd","MONTH",3,"TEST","100",maxRange="60")
    assert data[-1] == 0

def test_validate_time_in_range_days(test_df):
    from motordecalidad.rules import validateTimeInRange
    data,errorDf = validateTimeInRange(test_df,"date","2022-12-31","yyyy-MM-dd","DAYS",3,"TEST","100",maxRange="1000")
    assert data[-1] == 0

def test_validate_time_in_range_empty_errorDF(test_df):
    from motordecalidad.rules import validateTimeInRange
    data,errorDf = validateTimeInRange(test_df,"date","2022-12-31","yyyy-MM-dd","YEAR",3,"TEST","50",maxRange="1")
    assert errorDf.count() == 0

def test_validate_value_tendency(test_df_tendency):
    from motordecalidad.rules import validateValueTendency
    data,errorDf = validateValueTendency(3,test_df_tendency,"value",["id"],"","TEST","100")
    assert data[-1] == 1

def test_validate_value_tendency_chebyshev(test_df_tendency):
    from motordecalidad.rules import validateValueTendency
    data,errorDf = validateValueTendency(3,test_df_tendency,"value",["id"],"chebyshev","TEST","100")
    assert data[-1] == 0

def test_validate_value_tendency_ind(test_df_tendency):
    from motordecalidad.rules import validateValueTendency
    data,errorDf = validateValueTendency(3,test_df_tendency,"value",None,"","TEST","100")
    assert data[-1] == 2

def test_validate_value_tendency_chebyshev_ind(test_df_tendency):
    from motordecalidad.rules import validateValueTendency
    data,errorDf = validateValueTendency(3,test_df_tendency,"value",None,"chebyshev","TEST","100")
    assert data[-1] == 0

def test_validate_value_tendency_empty_errorDF(test_df_tendency):
    from motordecalidad.rules import validateValueTendency
    data,errorDf = validateValueTendency(3,test_df_tendency,"value",["id"],"","TEST","50")
    assert errorDf.count() == 0

def test_validate_position_value(test_df):
    from motordecalidad.rules import validatePositionValue
    data, errorDf = validatePositionValue(test_df,"mix",3,"TEST","100","0","0",["a","b","c"])
    assert data[-1] == 0

def test_validate_position_value_empty_errorDF(test_df):
    from motordecalidad.rules import validatePositionValue
    data, errorDf = validatePositionValue(test_df,"mix",3,"TEST","50","0","0",["a","b","c"])
    assert errorDf.count() == 0

def test_conditional(test_df):
    from motordecalidad.rules import validateConditional
    data,errorDf = validateConditional(test_df,3,"NO",[["id","in","a"]],"TEST","100",["validateNull","id","","",""])
    assert data[-1] == 0

def test_conditional_adicional_1(test_df):
    from motordecalidad.rules import validateConditional
    data,errorDf = validateConditional(test_df,3,"NO",[["id","not in","a"]],"TEST","100",["validateNull","id","","",""])
    assert data[-1] == 0

def test_conditional_adicional_2(test_df):
    from motordecalidad.rules import validateConditional
    data,errorDf = validateConditional(test_df,3,"NO",[["id","is","Null"]],"TEST","100",["validateNull","id","","",""])
    assert data[-1] == 0

def test_conditional_adicional_3(test_df):
    from motordecalidad.rules import validateConditional
    data,errorDf = validateConditional(test_df,3,"NO",[["id","is","NotNull"]],"TEST","100",["validateNull","id","","",""])
    assert data[-1] == 0

def test_conditional_adicional_4(test_df):
    from motordecalidad.rules import validateConditional
    data,errorDf = validateConditional(test_df,3,"NO",[["value",">","0"]],"TEST","100",["validateNull","id","","",""])
    assert data[-1] == 0

def test_conditional_adicional_5(test_df):
    from motordecalidad.rules import validateConditional
    data,errorDf = validateConditional(test_df,3,"AND",[["id","in","a"],["id","not in","b"]],"TEST","100",["validateNull","id","","",""])
    assert data[-1] == 0

def test_conditional_adicional_6(test_df):
    from motordecalidad.rules import validateConditional
    data,errorDf = validateConditional(test_df,3,"OR",[["id","in","a"],["id","not in","b"]],"TEST","100",["validateNull","id","","",""])
    assert data[-1] == 0

def test_conditional_adicional_5(test_df):
    from motordecalidad.rules import validateConditional
    data,errorDf = validateConditional(test_df,3,"AND",[["nullCol","is","Null"],["id","is","NotNull"],["value",">","0"]],"TEST","100",["validateNull","id","","",""])
    assert data[-1] == 0

def test_conditional_empty_errorDF(test_df):
    from motordecalidad.rules import validateConditional
    data,errorDf = validateConditional(test_df,3,"NO",[["id","in","a"]],"TEST","50",["validateNull","id","","",""])
    assert errorDf.count() == 0

def test_correo(df_correo,df_dominios):
    from motordecalidad.rules import validateEmail
    data,errorDf = validateEmail(df_correo,"correo",1,"TEST","==",df_dominios,"dominio",[".","/"])
    assert data[-1] == 0

def test_measure_central_tendency(test_df_tendency,spark_session):
    from motordecalidad.rules import measuresCentralTendency
    finalDf = measuresCentralTendency(test_df_tendency,["value"],spark_session)
    assert "CAMPOS" in finalDf.columns

def test_measure_central_tendency_adicional(test_df_tendency_2,spark_session):
    from motordecalidad.rules import measuresCentralTendency
    finalDf = measuresCentralTendency(test_df_tendency_2,["value","booleanCol"],spark_session)
    assert "CAMPOS" in finalDf.columns

def test_validate_operation(test_df):
    from motordecalidad.rules import validateOperation
    data,errorDf = validateOperation(test_df,"max",3,"TEST","100","==","value + 0")
    assert data[-1] == 3

def test_validate_operation_2(test_df):
    from motordecalidad.rules import validateOperation
    data,errorDf = validateOperation(test_df,"max",3,"TEST","100",">=","value + 0")
    assert data[-1] == 0