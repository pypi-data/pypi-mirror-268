from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LteCls:
	"""Lte commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

	def set(self, band: enums.OperatingBandC, dl_channel: int) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:LTE \n
		Snippet: driver.prepare.handover.external.lte.set(band = enums.OperatingBandC.OB1, dl_channel = 1) \n
		Configures the destination parameters for handover to an LTE destination at another instrument. For channel number ranges
		depending on operating bands, see 'Operating bands'. \n
			:param band: UDEFined | OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB250 | OB252 | OB255 Operating band
			:param dl_channel: decimal Downlink channel number Range: depends on operating band
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('band', band, DataType.Enum, enums.OperatingBandC), ArgSingle('dl_channel', dl_channel, DataType.Integer))
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:LTE {param}'.rstrip())

	# noinspection PyTypeChecker
	class LteStruct(StructBase):
		"""Response structure. Fields: \n
			- Band: enums.OperatingBandC: UDEFined | OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB250 | OB252 | OB255 Operating band
			- Dl_Channel: int: decimal Downlink channel number Range: depends on operating band"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperatingBandC),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperatingBandC = None
			self.Dl_Channel: int = None

	def get(self) -> LteStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:LTE \n
		Snippet: value: LteStruct = driver.prepare.handover.external.lte.get() \n
		Configures the destination parameters for handover to an LTE destination at another instrument. For channel number ranges
		depending on operating bands, see 'Operating bands'. \n
			:return: structure: for return value, see the help for LteStruct structure arguments."""
		return self._core.io.query_struct(f'PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:LTE?', self.__class__.LteStruct())
