from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StreamCls:
	"""Stream commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Stream, default value after init: Stream.S1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stream", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_stream_get', 'repcap_stream_set', repcap.Stream.S1)

	def repcap_stream_set(self, stream: repcap.Stream) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Stream.Default
		Default value after init: Stream.S1"""
		self._cmd_group.set_repcap_enum_value(stream)

	def repcap_stream_get(self) -> repcap.Stream:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection:ETHRoughput:DL:SCC<Carrier>:STReam<Stream> \n
		Snippet: value: float = driver.sense.connection.ethroughput.downlink.scc.stream.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Returns the expected maximum throughput (averaged over one frame) for one DL stream of one component carrier.
		The throughput is calculated for the currently selected scheduling type. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Stream')
			:return: throughput: float Unit: Mbit/s"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:CONNection:ETHRoughput:DL:SCC{secondaryCompCarrier_cmd_val}:STReam{stream_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'StreamCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StreamCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
