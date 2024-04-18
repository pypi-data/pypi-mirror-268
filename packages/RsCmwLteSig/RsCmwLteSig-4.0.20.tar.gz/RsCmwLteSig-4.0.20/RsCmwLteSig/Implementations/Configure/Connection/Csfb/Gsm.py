from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GsmCls:
	"""Gsm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gsm", core, parent)

	def set(self, band: enums.GsmBand, dl_channel: int, band_indicator: enums.BandIndicator) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:GSM \n
		Snippet: driver.configure.connection.csfb.gsm.set(band = enums.GsmBand.G04, dl_channel = 1, band_indicator = enums.BandIndicator.G18) \n
		Configures the GSM target for MO CSFB. \n
			:param band: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
			:param dl_channel: decimal Channel number used for the broadcast control channel (BCCH) Range: 0 to 1023, depending on GSM band, see table below
			:param band_indicator: G18 | G19 Band indicator for distinction of GSM 1800 and GSM 1900 bands. The two bands partially use the same channel numbers for different frequencies.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('band', band, DataType.Enum, enums.GsmBand), ArgSingle('dl_channel', dl_channel, DataType.Integer), ArgSingle('band_indicator', band_indicator, DataType.Enum, enums.BandIndicator))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:GSM {param}'.rstrip())

	# noinspection PyTypeChecker
	class GsmStruct(StructBase):
		"""Response structure. Fields: \n
			- Band: enums.GsmBand: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
			- Dl_Channel: int: decimal Channel number used for the broadcast control channel (BCCH) Range: 0 to 1023, depending on GSM band, see table below
			- Band_Indicator: enums.BandIndicator: G18 | G19 Band indicator for distinction of GSM 1800 and GSM 1900 bands. The two bands partially use the same channel numbers for different frequencies."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.GsmBand),
			ArgStruct.scalar_int('Dl_Channel'),
			ArgStruct.scalar_enum('Band_Indicator', enums.BandIndicator)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.GsmBand = None
			self.Dl_Channel: int = None
			self.Band_Indicator: enums.BandIndicator = None

	def get(self) -> GsmStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:GSM \n
		Snippet: value: GsmStruct = driver.configure.connection.csfb.gsm.get() \n
		Configures the GSM target for MO CSFB. \n
			:return: structure: for return value, see the help for GsmStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:GSM?', self.__class__.GsmStruct())
