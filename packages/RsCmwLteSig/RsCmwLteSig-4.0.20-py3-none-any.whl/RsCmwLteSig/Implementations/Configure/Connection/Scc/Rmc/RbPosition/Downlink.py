from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Stream, default value after init: Stream.S1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)
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

	def set(self, position: enums.DownlinkRsrcBlockPosition, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:RMC:RBPosition:DL<Stream> \n
		Snippet: driver.configure.connection.scc.rmc.rbPosition.downlink.set(position = enums.DownlinkRsrcBlockPosition.HIGH, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Selects the position of the allocated downlink resource blocks. Set the same value for both streams of a carrier.
			INTRO_CMD_HELP: Depending on other settings, only a subset of the listed values is allowed, see: \n
			- 'Scheduling type RMC'
			- 'Scheduling type RMC for eMTC'
			- 'Scheduling type RMC for LAA' \n
			:param position: LOW | HIGH | P5 | P10 | P23 | P35 | P48
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
		"""
		param = Conversions.enum_scalar_to_str(position, enums.DownlinkRsrcBlockPosition)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:RMC:RBPosition:DL{stream_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> enums.DownlinkRsrcBlockPosition:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:RMC:RBPosition:DL<Stream> \n
		Snippet: value: enums.DownlinkRsrcBlockPosition = driver.configure.connection.scc.rmc.rbPosition.downlink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Selects the position of the allocated downlink resource blocks. Set the same value for both streams of a carrier.
			INTRO_CMD_HELP: Depending on other settings, only a subset of the listed values is allowed, see: \n
			- 'Scheduling type RMC'
			- 'Scheduling type RMC for eMTC'
			- 'Scheduling type RMC for LAA' \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
			:return: position: LOW | HIGH | P5 | P10 | P23 | P35 | P48"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:RMC:RBPosition:DL{stream_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.DownlinkRsrcBlockPosition)

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
