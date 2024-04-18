from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WcdmaCls:
	"""Wcdma commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wcdma", core, parent)

	def set(self, band: enums.OperatingBandB, dl_channel: int) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:WCDMa \n
		Snippet: driver.prepare.handover.external.wcdma.set(band = enums.OperatingBandB.OB1, dl_channel = 1) \n
		Configures the destination parameters for handover to a WCDMA destination at another instrument. \n
			:param band: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB19 | OB20 | OB21 | OB22 | OB25 | OBS1 | OBS2 | OBS3 | OBL1 | OB26 OB1, ..., OB14: band I to XIV OB19, ..., OB22: band XIX to XXII OB25, OB26: band XXV, XXVI OBS1: band S OBS2: band S 170 MHz OBS3: band S 190 MHz OBL1: band L
			:param dl_channel: decimal Downlink channel number Range: Depends on operating band, see table below
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('band', band, DataType.Enum, enums.OperatingBandB), ArgSingle('dl_channel', dl_channel, DataType.Integer))
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:WCDMa {param}'.rstrip())

	# noinspection PyTypeChecker
	class WcdmaStruct(StructBase):
		"""Response structure. Fields: \n
			- Band: enums.OperatingBandB: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB19 | OB20 | OB21 | OB22 | OB25 | OBS1 | OBS2 | OBS3 | OBL1 | OB26 OB1, ..., OB14: band I to XIV OB19, ..., OB22: band XIX to XXII OB25, OB26: band XXV, XXVI OBS1: band S OBS2: band S 170 MHz OBS3: band S 190 MHz OBL1: band L
			- Dl_Channel: int: decimal Downlink channel number Range: Depends on operating band, see table below"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperatingBandB),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperatingBandB = None
			self.Dl_Channel: int = None

	def get(self) -> WcdmaStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:WCDMa \n
		Snippet: value: WcdmaStruct = driver.prepare.handover.external.wcdma.get() \n
		Configures the destination parameters for handover to a WCDMA destination at another instrument. \n
			:return: structure: for return value, see the help for WcdmaStruct structure arguments."""
		return self._core.io.query_struct(f'PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:WCDMa?', self.__class__.WcdmaStruct())
