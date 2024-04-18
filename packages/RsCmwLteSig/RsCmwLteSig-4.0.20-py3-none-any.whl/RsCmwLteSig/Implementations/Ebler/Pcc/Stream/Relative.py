from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


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
			- Throughput: float: float Average DL throughput (percentage of maximum reachable throughput) Unit: %
			- Dtx: float: float Percentage of sent scheduled subframes for which no ACK and no NACK has been received Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ack'),
			ArgStruct.scalar_float('Nack'),
			ArgStruct.scalar_float('Bler'),
			ArgStruct.scalar_float('Throughput'),
			ArgStruct.scalar_float('Dtx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ack: float = None
			self.Nack: float = None
			self.Bler: float = None
			self.Throughput: float = None
			self.Dtx: float = None

	def fetch(self, stream=repcap.Stream.Default) -> FetchStruct:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer[:PCC]:STReam<Stream>:RELative \n
		Snippet: value: FetchStruct = driver.ebler.pcc.stream.relative.fetch(stream = repcap.Stream.Default) \n
		Returns the relative results of the BLER measurement for one downlink stream of one carrier. \n
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Stream')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:EBLer:PCC:STReam{stream_cmd_val}:RELative?', self.__class__.FetchStruct())
