from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StypeCls:
	"""Stype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stype", core, parent)

	def set(self, type_py: enums.SchedulingType, cqi_mode: enums.CqiMode = None) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:STYPe \n
		Snippet: driver.configure.connection.pcc.stype.set(type_py = enums.SchedulingType.CQI, cqi_mode = enums.CqiMode.FCPRi) \n
		Selects the scheduling type. \n
			:param type_py: RMC | UDCHannels | UDTTibased | CQI | SPS | EMAMode | EMCSched RMC: 3GPP-compliant reference measurement channel UDCHannels: user-defined channel UDTTibased: user-defined channel configurable per TTI CQI: CQI channel, as specified by next parameter SPS: semi-persistent scheduling (only PCC, not SCC) EMAMode: eMTC auto mode EMCSched: eMTC compact scheduling
			:param cqi_mode: TTIBased | FWB | FPMI | FCPRi | FCRI | FPRI Only relevant for Type = CQI TTIBased: fixed CQI FWB: follow wideband CQI FPMI: follow wideband PMI FCPRi: follow wideband CQI-PMI-RI FCRI: follow wideband CQI-RI FPRI: follow wideband PMI-RI
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('type_py', type_py, DataType.Enum, enums.SchedulingType), ArgSingle('cqi_mode', cqi_mode, DataType.Enum, enums.CqiMode, is_optional=True))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:STYPe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StypeStruct(StructBase):
		"""Response structure. Fields: \n
			- Type_Py: enums.SchedulingType: RMC | UDCHannels | UDTTibased | CQI | SPS | EMAMode | EMCSched RMC: 3GPP-compliant reference measurement channel UDCHannels: user-defined channel UDTTibased: user-defined channel configurable per TTI CQI: CQI channel, as specified by next parameter SPS: semi-persistent scheduling (only PCC, not SCC) EMAMode: eMTC auto mode EMCSched: eMTC compact scheduling
			- Cqi_Mode: enums.CqiMode: TTIBased | FWB | FPMI | FCPRi | FCRI | FPRI Only relevant for Type = CQI TTIBased: fixed CQI FWB: follow wideband CQI FPMI: follow wideband PMI FCPRi: follow wideband CQI-PMI-RI FCRI: follow wideband CQI-RI FPRI: follow wideband PMI-RI"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Type_Py', enums.SchedulingType),
			ArgStruct.scalar_enum('Cqi_Mode', enums.CqiMode)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Type_Py: enums.SchedulingType = None
			self.Cqi_Mode: enums.CqiMode = None

	def get(self) -> StypeStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:STYPe \n
		Snippet: value: StypeStruct = driver.configure.connection.pcc.stype.get() \n
		Selects the scheduling type. \n
			:return: structure: for return value, see the help for StypeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:STYPe?', self.__class__.StypeStruct())
