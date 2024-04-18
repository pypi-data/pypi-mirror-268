from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AbsoluteCls:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability indicator'
			- Sent: List[int]: decimal Number of sent subframes
			- Ack: List[int]: decimal Number of received acknowledgments
			- Nack: List[int]: decimal Number of received negative acknowledgments
			- Dtx: List[int]: decimal Number of sent subframes for which no ACK and no NACK has been received"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Sent', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Ack', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Nack', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Dtx', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Sent: List[int] = None
			self.Ack: List[int] = None
			self.Nack: List[int] = None
			self.Dtx: List[int] = None

	def fetch(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> FetchStruct:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer:SCC<Carrier>:HARQ:STReam<Stream>:TRANsmission:ABSolute \n
		Snippet: value: FetchStruct = driver.ebler.scc.harq.stream.transmission.absolute.fetch(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Returns absolute HARQ results for one downlink stream. All columns of the 'HARQ per Transmissions' result table are
		returned: <Reliability>, {<Sent>, <ACK>, <NACK>, <DTX>}column 1, {...}col. 2, {...}col. 3, {...}col. 4 \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Stream')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:EBLer:SCC{secondaryCompCarrier_cmd_val}:HARQ:STReam{stream_cmd_val}:TRANsmission:ABSolute?', self.__class__.FetchStruct())
