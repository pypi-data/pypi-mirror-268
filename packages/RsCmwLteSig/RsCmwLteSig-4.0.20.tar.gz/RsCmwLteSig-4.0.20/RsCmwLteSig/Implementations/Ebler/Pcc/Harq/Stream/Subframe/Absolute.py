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
			- Sent: List[int]: NAV returned, for future use
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

	def fetch(self, stream=repcap.Stream.Default) -> FetchStruct:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer[:PCC]:HARQ:STReam<Stream>:SUBFrame:ABSolute \n
		Snippet: value: FetchStruct = driver.ebler.pcc.harq.stream.subframe.absolute.fetch(stream = repcap.Stream.Default) \n
		Returns absolute HARQ results for one downlink stream. All columns of the 'HARQ per Subframe' result table are returned:
		<Reliability>, {<Sent>, <ACK>, <NACK>, <DTX>}column 0, {...}column 1, ..., {...}column 9 \n
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Stream')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:EBLer:PCC:HARQ:STReam{stream_cmd_val}:SUBFrame:ABSolute?', self.__class__.FetchStruct())
