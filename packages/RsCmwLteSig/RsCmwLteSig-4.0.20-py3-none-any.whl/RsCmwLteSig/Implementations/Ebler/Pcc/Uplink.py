from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability indicator'
			- Bler: int: decimal Block error ratio (percentage of received uplink subframes with failed CRC check) Unit: %
			- Throughput: int: decimal Average uplink throughput Unit: kbit/s
			- Crc_Pass: int: decimal Number of received subframes with passed CRC check
			- Crc_Fail: int: decimal Number of received subframes with failed CRC check
			- Dtx: int: decimal Number of scheduled UL subframes not sent by the UE Only evaluated if skipping UL transmissions is not allowed.
			- Skipped: int: decimal Number of scheduled UL subframes not sent by the UE Only evaluated if skipping UL transmissions is allowed."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Bler'),
			ArgStruct.scalar_int('Throughput'),
			ArgStruct.scalar_int('Crc_Pass'),
			ArgStruct.scalar_int('Crc_Fail'),
			ArgStruct.scalar_int('Dtx'),
			ArgStruct.scalar_int('Skipped')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bler: int = None
			self.Throughput: int = None
			self.Crc_Pass: int = None
			self.Crc_Fail: int = None
			self.Dtx: int = None
			self.Skipped: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer[:PCC]:UPLink \n
		Snippet: value: FetchStruct = driver.ebler.pcc.uplink.fetch() \n
		Returns the uplink results of the BLER measurement. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:EBLer:PCC:UPLink?', self.__class__.FetchStruct())
