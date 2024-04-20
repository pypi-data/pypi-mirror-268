def test_prerequisites_class():
    from motordecalidad.constants import Rules
    assert Rules.Pre_Requisites.name == "Prerequisitos de Validación"
    assert Rules.Pre_Requisites.property == "Integridad de Data"
    assert Rules.Pre_Requisites.code == "100"
def test_null_class():
    from motordecalidad.constants import Rules
    assert Rules.NullRule.name == "Completitud de Registro"
    assert Rules.NullRule.property == "Completitud"
    assert Rules.NullRule.code == "101"
def test_duplicated_class():
    from motordecalidad.constants import Rules
    assert Rules.DuplicatedRule.name == "Riesgo de Inconsistencia por Duplicidad"
    assert Rules.DuplicatedRule.property == "Consistencia"
    assert Rules.DuplicatedRule.code == "102"
def test_integrity_class():
    from motordecalidad.constants import Rules
    assert Rules.IntegrityRule.name == "Integridad Referencial"
    assert Rules.IntegrityRule.property == "Consistencia"
    assert Rules.IntegrityRule.code == "103"
def test_format_date_class():
    from motordecalidad.constants import Rules
    assert Rules.FormatDate.name == "Exactitud de Formato de Fecha"
    assert Rules.FormatDate.property == "Exactitud Sintactica"
    assert Rules.FormatDate.code == "104"
def test_range_class():
    from motordecalidad.constants import Rules
    assert Rules.RangeRule.name == "Exactitud de Rango de Valores"
    assert Rules.RangeRule.property == "Exactitud"
    assert Rules.RangeRule.code == "105"
def test_catalog_class():
    from motordecalidad.constants import Rules
    assert Rules.CatalogRule.name == "Exactitud de Catalogo de Valores"
    assert Rules.CatalogRule.property == "Exactitud"
    assert Rules.CatalogRule.code == "106"
def test_forbidden_class():
    from motordecalidad.constants import Rules
    assert Rules.ForbiddenRule.name == "Exactitud de Caracteres Permitidos"
    assert Rules.ForbiddenRule.property == "Exactitud Sintactica"
    assert Rules.ForbiddenRule.code == "107"
def test_type_class():
    from motordecalidad.constants import Rules
    assert Rules.TypeRule.name == "Consistencia de Formato (CSV)"
    assert Rules.TypeRule.property == "Consistencia"
    assert Rules.TypeRule.code == "108"
def test_composision_class():
    from motordecalidad.constants import Rules
    assert Rules.ComposisionRule.name == "Consistencia de Composición"
    assert Rules.ComposisionRule.property == "Consistencia"
    assert Rules.ComposisionRule.code == "109"
def test_length_class():
    from motordecalidad.constants import Rules
    assert Rules.LengthRule.name == "Consistencia de Longitud de dato"
    assert Rules.LengthRule.property == "Consistencia"
    assert Rules.LengthRule.code == "110"
def test_data_type_class():
    from motordecalidad.constants import Rules
    assert Rules.DataTypeRule.name == "Consistencia de Formato"
    assert Rules.DataTypeRule.property == "Consistencia"
    assert Rules.DataTypeRule.code == "111"
def test_numeric_format_class():
    from motordecalidad.constants import Rules
    assert Rules.NumericFormatRule.name == "Consistencia de Formato Numerico"
    assert Rules.NumericFormatRule.property == "Consistencia"
    assert Rules.NumericFormatRule.code == "112"
def test_operation_class():
    from motordecalidad.constants import Rules
    assert Rules.OperationRule.name == "Exactitud de Resultado"
    assert Rules.OperationRule.property == "Exactitud"
    assert Rules.OperationRule.code == "113"
def test_statistics_class():
    from motordecalidad.constants import Rules
    assert Rules.StatisticsResult.name == "Exactitud Estadistica"
    assert Rules.StatisticsResult.property == "Exactitud"
    assert Rules.StatisticsResult.code == "114"
def test_time_in_range_class():
    from motordecalidad.constants import Rules
    assert Rules.validateTimeInRangeRule.name == "Exactitud de rango de fecha"
    assert Rules.validateTimeInRangeRule.property == "Exactitud"
    assert Rules.validateTimeInRangeRule.code == "115"
def test_conditional_class():
    from motordecalidad.constants import Rules
    assert Rules.validateConditionalRule.name == "Exactitud de Validacion Condicional"
    assert Rules.validateConditionalRule.property == "Exactitud"
    assert Rules.validateConditionalRule.code == "116"
def test_position_class():
    from motordecalidad.constants import Rules
    assert Rules.validatePositionValueRule.name == "Exactitud de valor de Posición Específica"
    assert Rules.validatePositionValueRule.property == "Exactitud"
    assert Rules.validatePositionValueRule.code == "117"
def test_email_class():
    from motordecalidad.constants import Rules
    assert Rules.validateEmailRule.name == "Validez de la estructura del Correo Electrónico"
    assert Rules.validateEmailRule.property == "Validez"
    assert Rules.validateEmailRule.code == "118"
def test_value_tendency_class():
    from motordecalidad.constants import Rules
    assert Rules.validateValueTendencyRule.name == "Exactitud de Valor dentro de una Tendencia"
    assert Rules.validateValueTendencyRule.property == "Exactitud"
    assert Rules.validateValueTendencyRule.code == "119"
    
def testJsonParts():
    from motordecalidad.constants import JsonParts
    assert JsonParts.Method == "METHOD"
    assert JsonParts.Input == "INPUT"
    assert JsonParts.Output == "OUTPUT"
    assert JsonParts.Rules == "RULES"
    assert JsonParts.Header == "HEADER"
    assert JsonParts.Delimiter == "DELIMITER"
    assert JsonParts.Fields == "FIELDS"
    assert JsonParts.ReferenceFields == "REFERENCE_FIELDS"
    assert JsonParts.Country == "COUNTRY_ID"
    assert JsonParts.Entity == "ENTITY_ID"
    assert JsonParts.Project == "PROJECT"
    assert JsonParts.Path == "PATH"
    assert JsonParts.Account == "ACCOUNT"
    assert JsonParts.Key == "KEY"
    assert JsonParts.FormatDate == "FORMAT_DATE"
    assert JsonParts.Domain == "DOMAIN"
    assert JsonParts.SubDomain == "SUB_DOMAIN"
    assert JsonParts.Segment == "SEGMENT"
    assert JsonParts.Area == "AREA"
    assert JsonParts.Threshold == "THRESHOLD"
    assert JsonParts.Values == "VALUES"
    assert JsonParts.MinRange == "MIN_RANGE"
    assert JsonParts.MaxRange == "MAX_RANGE"
    assert JsonParts.DataType == "DATA_TYPE"
    assert JsonParts.RepetitionNumber == "REPETITION_NUMBER"
    assert JsonParts.ReferenceDate == "REFERENCE_DATE"
    assert JsonParts.diffUnit == "DIFFERENT_UNIT"
    assert JsonParts.includeLimitRight == "INCLUDE_LIMIT_RIGHT"
    assert JsonParts.includeLimitLeft == "INCLUDE_LIMIT_LEFT"
    assert JsonParts.inclusive == "INCLUSIVE"
    assert JsonParts.condition == "CONDITION"
    assert JsonParts.filterList == "FILTER_LIST"
    assert JsonParts.qualityFunction == "QUALITY_FUNCTION"
    assert JsonParts.initialPosition == "INITIAL_POSITION"
    assert JsonParts.finalPosition == "FINAL_POSITION"
    assert JsonParts.expectedValue == "EXPECTED_VALUE"
    assert JsonParts.expressionForbidden == "EXPRESSION_FORBIDDEN"
    assert JsonParts.Type == "TYPE"
    assert JsonParts.Write == "WRITE"
    assert JsonParts.Error == "ERROR"
    assert JsonParts.Host == "HOST"
    assert JsonParts.Port == "PORT"
    assert JsonParts.DBName == "DATABASE_NAME"
    assert JsonParts.DBTable == "DATABASE_TABLE"
    assert JsonParts.DBUser == "DATABASE_USER"
    assert JsonParts.DBPassword == "DATABASE_PASSWORD"
    assert JsonParts.MaxInt == "MAX_INT"
    assert JsonParts.Sep == "SEP"
    assert JsonParts.NumDec == "NUM_DEC"
    assert JsonParts.TempPath == "TEMPORAL_PATH"
    assert JsonParts.Filter == "FILTER"
    assert JsonParts.Input_val == "INPUT_VAL"
    assert JsonParts.Error_val == "ERROR_VAL"
    assert JsonParts.Operator == "OPERATOR"
    assert JsonParts.Scope == "SCOPE"
    assert JsonParts.Partitions == "PARTITIONS"
    assert JsonParts.DataDate == "DATA_DATE"
    assert JsonParts.ValidData == "VALID_DATA"
    assert JsonParts.Data == "DATA"
    assert JsonParts.SendEmail == "SEND_EMAIL"
    assert JsonParts.Email == "EMAIL"
    assert JsonParts.Encrypt == "ENCRYPT"

def test_prerequisitessucessmsg():
    from motordecalidad.constants import PreRequisitesSucessMsg
    assert PreRequisitesSucessMsg == "Validación de PreRequesitos Exitosa"

def test_constant_values():
    from motordecalidad.constants import EncryptKey,ConnectionString,LeftAntiType,Country,Year,Month,Week,Day,Overwrite,PartitionOverwriteMode,DynamicMode,Delimiter,Header,DatabricksCsv,Two,One,Zero,OneHundred,PermitedFormatDate,DateFormats,TimeStampFormats
    assert EncryptKey == "'j5uuSPUfbIN0CiBOvYceooGR5qu2bg64p1kY7ravNRw='"
    assert ConnectionString == "DefaultEndpointsProtocol=https;AccountName=adlseu2edthdev001;AccountKey=T1RZsgj62zrRWcsYRW3QGr3+TEhtalj8o/fU3Zqmh4ef3TYxZw0P7+neqmgOPmbFOoVPZhLFT9GV+AStAj2YpA==;EndpointSuffix=core.windows.net"
    assert LeftAntiType == "leftanti"
    assert Country == "country"
    assert Year == "year"
    assert Month == "month"
    assert Week == "week"
    assert Day == "day"
    assert Overwrite == "overwrite"
    assert PartitionOverwriteMode == "partitionOverwriteMode"
    assert DynamicMode == "dynamic"
    assert Delimiter == "delimiter"
    assert Header == "header"
    assert DatabricksCsv == "com.databricks.spark.csv"
    assert Two == 2
    assert One == 1
    assert Zero == 0
    assert OneHundred == 100
    assert PermitedFormatDate == ["yyyy-MM-dd","yyyy/MM/dd", "yyyyMMdd", "yyyyMM","yyyy-MM-dd HH:mm:ss","yyyyddMM'T'HHmmss"]
    assert DateFormats == ["yyyy-MM-dd","yyyy/MM/dd", "yyyyMMdd", "yyyyMM"]
    assert TimeStampFormats == ["yyyy-MM-dd HH:mm:ss","yyyyddMM'T'HHmmss"]
