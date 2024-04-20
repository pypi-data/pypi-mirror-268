MotorVersion = "2.2.15"
##Definición de clase Rules que contiene los datos de las reglas
class Rules:
    class Pre_Requisites:
        name  = "Prerequisitos de Validación"
        property = "Integridad de Data"
        code = "100"
    class NullRule:
        name = "Completitud de Registro"
        property = "Completitud"
        code = "101"
    class DuplicatedRule:
        name = "Riesgo de Inconsistencia por Duplicidad"
        property = "Consistencia"
        code = "102"
    class IntegrityRule:
        name = "Integridad Referencial"
        property = "Consistencia"
        code = "103"
    class FormatDate:
        name = "Exactitud de Formato de Fecha"
        property = "Exactitud Sintactica"
        code = "104"
    class RangeRule:
        name = "Exactitud de Rango de Valores"
        property = "Exactitud"
        code = "105"
    class CatalogRule:
        name = "Exactitud de Catalogo de Valores"
        property = "Exactitud"
        code = "106"
    class ForbiddenRule:
        name = "Exactitud de Caracteres Permitidos"
        property = "Exactitud Sintactica"
        code = "107"
    class TypeRule:
        name = "Consistencia de Formato (CSV)"
        property = "Consistencia"
        code = "108"
    class ComposisionRule:
        name = "Consistencia de Composición"
        property = "Consistencia"
        code = "109"
    class LengthRule:
        name = "Consistencia de Longitud de dato"
        property = "Consistencia"
        code = "110"
    class DataTypeRule:
        name = "Consistencia de Formato"
        property = "Consistencia"
        code = "111"
    class NumericFormatRule:
        name = "Consistencia de Formato Numerico"
        property = "Consistencia"
        code = "112" 
    class OperationRule:
        name = "Exactitud de Resultado"
        property = "Exactitud"
        code = "113"
    class StatisticsResult:
        name = "Exactitud Estadistica"
        property = "Exactitud"
        code = "114"
    class validateTimeInRangeRule:
        name = "Exactitud de rango de fecha"
        property = "Exactitud"
        code = "115"
    class validateConditionalRule:
        name = "Exactitud de Validacion Condicional"
        property = "Exactitud"
        code = "116"
    class validatePositionValueRule:
        name = "Exactitud de valor de Posición Específica"
        property = "Exactitud"
        code = "117"
    class validateEmailRule:
        name = "Validez de la estructura del Correo Electrónico"
        property = "Validez"
        code = "118"
    class validateValueTendencyRule:
        name = "Exactitud de Valor dentro de una Tendencia"
        property = "Exactitud"
        code = "119"

## Definición de la clase JsonParts que contiene todos los posibles atributos del JSON
class JsonParts:
    Method = "METHOD"
    Input = "INPUT"
    Output = "OUTPUT"
    Rules = "RULES"
    Header= "HEADER"
    Delimiter = "DELIMITER"
    Fields = "FIELDS"
    ReferenceFields = "REFERENCE_FIELDS"
    Country = "COUNTRY_ID"
    Entity = "ENTITY_ID"
    Project = "PROJECT"
    Path = "PATH"
    Account = "ACCOUNT"
    Key = "KEY"
    FormatDate = "FORMAT_DATE"
    Domain = "DOMAIN"
    SubDomain = "SUB_DOMAIN"
    Segment = "SEGMENT"
    Area = "AREA"
    Threshold = "THRESHOLD"
    Values = "VALUES"
    MinRange = "MIN_RANGE"
    MaxRange = "MAX_RANGE"
    DataType = "DATA_TYPE"
    RepetitionNumber = "REPETITION_NUMBER"
    ReferenceDate = "REFERENCE_DATE"
    diffUnit = "DIFFERENT_UNIT"
    includeLimitRight = "INCLUDE_LIMIT_RIGHT"
    includeLimitLeft = "INCLUDE_LIMIT_LEFT"
    inclusive = "INCLUSIVE"
    condition = "CONDITION"
    filterList = "FILTER_LIST"
    qualityFunction = "QUALITY_FUNCTION"
    initialPosition = "INITIAL_POSITION"
    finalPosition = "FINAL_POSITION"
    expectedValue = "EXPECTED_VALUE"
    expressionForbidden = "EXPRESSION_FORBIDDEN"
    Type = "TYPE"
    Write = "WRITE"
    Error = "ERROR"
    Host = "HOST"
    Port = "PORT"
    DBName = "DATABASE_NAME"
    DBTable = "DATABASE_TABLE"
    DBUser = "DATABASE_USER"
    DBPassword = "DATABASE_PASSWORD"
    MaxInt = "MAX_INT"
    Sep = "SEP"
    NumDec = "NUM_DEC"
    TempPath = "TEMPORAL_PATH"
    Filter = "FILTER"
    Input_val = "INPUT_VAL"
    Error_val = "ERROR_VAL"
    Operator = "OPERATOR"
    Scope = "SCOPE"
    Partitions = "PARTITIONS"
    DataDate = "DATA_DATE"
    ValidData = "VALID_DATA"
    Data = "DATA"
    SendEmail = "SEND_EMAIL"
    Email ="EMAIL"
    Encrypt = "ENCRYPT"

# Definición de la excepción personalizada
class ExcepciónDePreRequisitos(Exception):
    pass
#Mensaje de Prerequisitos
PreRequisitesSucessMsg = "Validación de PreRequesitos Exitosa"

EncryptKey = "'j5uuSPUfbIN0CiBOvYceooGR5qu2bg64p1kY7ravNRw='"
ConnectionString = "DefaultEndpointsProtocol=https;AccountName=adlseu2edthdev001;AccountKey=T1RZsgj62zrRWcsYRW3QGr3+TEhtalj8o/fU3Zqmh4ef3TYxZw0P7+neqmgOPmbFOoVPZhLFT9GV+AStAj2YpA==;EndpointSuffix=core.windows.net"
LeftAntiType = "leftanti"
Country = "country"
Year = "year"
Month = "month"
Week = "week"
Day = "day"
Overwrite = "overwrite"
PartitionOverwriteMode = "partitionOverwriteMode"
DynamicMode = "dynamic"
Delimiter = "delimiter"
Header = "header"
DatabricksCsv = "com.databricks.spark.csv"
Two = 2
One = 1
Zero = 0
OneHundred = 100
PermitedFormatDate = ["yyyy-MM-dd","yyyy/MM/dd", "yyyyMMdd", "yyyyMM","yyyy-MM-dd HH:mm:ss","yyyyddMM'T'HHmmss"]
DateFormats = ["yyyy-MM-dd","yyyy/MM/dd", "yyyyMMdd", "yyyyMM"]
TimeStampFormats = ["yyyy-MM-dd HH:mm:ss","yyyyddMM'T'HHmmss"]