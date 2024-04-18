from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TdscdmaCls:
	"""Tdscdma commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdscdma", core, parent)

	def set(self, band: enums.OperatingBandA, dl_channel: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:TDSCdma \n
		Snippet: driver.configure.connection.csfb.tdscdma.set(band = enums.OperatingBandA.OB1, dl_channel = 1) \n
		Configures the TD-SCDMA target for MO CSFB. \n
			:param band: OB1 | OB2 | OB3 OB1: Band 1 (F) , 1880 MHz to 1920 MHz OB2: Band 2 (A) , 2010 MHz to 2025 MHz OB3: Band 3 (E) , 2300 MHz to 2400 MHz
			:param dl_channel: decimal Downlink channel number The allowed range depends on the frequency band: OB1: 9400 to 9600 OB2: 10050 to 10125 OB3: 11500 to 12000
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('band', band, DataType.Enum, enums.OperatingBandA), ArgSingle('dl_channel', dl_channel, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:TDSCdma {param}'.rstrip())

	# noinspection PyTypeChecker
	class TdscdmaStruct(StructBase):
		"""Response structure. Fields: \n
			- Band: enums.OperatingBandA: OB1 | OB2 | OB3 OB1: Band 1 (F) , 1880 MHz to 1920 MHz OB2: Band 2 (A) , 2010 MHz to 2025 MHz OB3: Band 3 (E) , 2300 MHz to 2400 MHz
			- Dl_Channel: int: decimal Downlink channel number The allowed range depends on the frequency band: OB1: 9400 to 9600 OB2: 10050 to 10125 OB3: 11500 to 12000"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperatingBandA),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperatingBandA = None
			self.Dl_Channel: int = None

	def get(self) -> TdscdmaStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:TDSCdma \n
		Snippet: value: TdscdmaStruct = driver.configure.connection.csfb.tdscdma.get() \n
		Configures the TD-SCDMA target for MO CSFB. \n
			:return: structure: for return value, see the help for TdscdmaStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:TDSCdma?', self.__class__.TdscdmaStruct())
