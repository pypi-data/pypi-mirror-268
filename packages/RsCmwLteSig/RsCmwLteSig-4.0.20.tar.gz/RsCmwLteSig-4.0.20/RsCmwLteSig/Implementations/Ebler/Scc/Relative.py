from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RelativeCls:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability indicator'
			- Ack: float: float Received acknowledgments (percentage of sent scheduled subframes) Unit: %
			- Nack: float: float Received negative acknowledgments (percentage of sent scheduled subframes) Unit: %
			- Bler: float: float Block error ratio (percentage of sent scheduled subframes for which no ACK has been received) Unit: %
			- Thougput_Avg_Rel: float: No parameter help available
			- Dtx: float: float Percentage of sent scheduled subframes for which no ACK and no NACK has been received Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ack'),
			ArgStruct.scalar_float('Nack'),
			ArgStruct.scalar_float('Bler'),
			ArgStruct.scalar_float('Thougput_Avg_Rel'),
			ArgStruct.scalar_float('Dtx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ack: float = None
			self.Nack: float = None
			self.Bler: float = None
			self.Thougput_Avg_Rel: float = None
			self.Dtx: float = None

	def fetch(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> FetchStruct:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer:SCC<Carrier>:RELative \n
		Snippet: value: FetchStruct = driver.ebler.scc.relative.fetch(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns the relative overall results of the BLER measurement for the sum of all DL streams of one carrier. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:EBLer:SCC{secondaryCompCarrier_cmd_val}:RELative?', self.__class__.FetchStruct())
