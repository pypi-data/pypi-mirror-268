from pyspark.sql.functions import col
from pyspark.sql.types import StructType,StructField,StringType, IntegerType
##Definición de clase Field que permite acceder a métodos sobre los campos definidos sobre esta clase
class Field:
    def __init__(self,colName):
        self.name = colName
        self.column = col(colName)
    def value(self,colValue):
        return (colValue).alias(self.name)
##Definición de campos    
CountryId = Field("CODIGO_DE_PAIS")
DataDate = Field("FECHA_DE_INFORMACION")
Project = Field("PROYECTO")
Entity = Field("ENTIDAD")
AuditDate = Field("FECHA_EJECUCION_REGLA")
Domain  = Field("DOMINIO_ENTIDAD")
SubDomain = Field("SUBDOMINIO_ENTIDAD")
Segment = Field("SEGMENTO_ENTIDAD")
Area = Field("AREA_FUNCIONAL_ENTIDAD")
TestedFields = Field("ATRIBUTOS")
RuleCode = Field("CODIGO_REGLA")
RuleDescription = Field("DESCRIPCION_FUNCION")
SucessRate = Field("PORCENTAJE_CALIDAD_OK")
TestedRegisterAmount = Field("TOTAL_REGISTROS_VALIDADOS")
FailedRegistersAmount = Field("TOTAL_REGISTROS_ERRONEOS")
PassedRegistersAmount = Field("TOTAL_REGISTROS_CORRECTOS")
DataRequirement = Field("REQUISITO_DATOS")
QualityRequirement = Field("REQUISITO_CALIDAD")
RiskApetite = Field("APETITO_RIESGO")
Threshold = Field("UMBRAL_ACEPTACION")
RuleGroup = Field("CARACTERISTICA_REGLA")
RuleProperty = Field("PROPIEDAD_REGLA")
FailRate = Field("PORCENTAJE_CALIDAD_KO")
FunctionCode = Field("CODIGO_FUNCION")
LibraryVersion = Field("VERSION_LIBRERIA")

#Esquema para la creación del dataframe de prerequisitos
RequisitesSchema = StructType(
[StructField(TestedRegisterAmount.name,IntegerType()),
StructField(FunctionCode.name,StringType()),
StructField(RuleGroup.name,StringType()),
StructField(RuleProperty.name,StringType()),
StructField(RuleCode.name,StringType()),
StructField(Threshold.name,StringType()),
StructField(DataRequirement.name,StringType()),
StructField(TestedFields.name,StringType()),
StructField(SucessRate.name,StringType()),
StructField(FailedRegistersAmount.name,IntegerType())]
)

OutputDataFrameColumns = [TestedRegisterAmount.name,FunctionCode.name,RuleGroup.name,RuleProperty.name,RuleCode.name,Threshold.name,DataRequirement.name,TestedFields.name,SucessRate.name,FailedRegistersAmount.name]