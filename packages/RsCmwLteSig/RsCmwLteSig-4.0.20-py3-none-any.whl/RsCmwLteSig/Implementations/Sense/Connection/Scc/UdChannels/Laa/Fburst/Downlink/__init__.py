from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 3 total commands, 3 Subgroups, 0 group commands
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

	@property
	def fullSubFrames(self):
		"""fullSubFrames commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fullSubFrames'):
			from .FullSubFrames import FullSubFramesCls
			self._fullSubFrames = FullSubFramesCls(self._core, self._cmd_group)
		return self._fullSubFrames

	@property
	def pipSubFrames(self):
		"""pipSubFrames commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pipSubFrames'):
			from .PipSubFrames import PipSubFramesCls
			self._pipSubFrames = PipSubFramesCls(self._core, self._cmd_group)
		return self._pipSubFrames

	@property
	def pepSubFrames(self):
		"""pepSubFrames commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pepSubFrames'):
			from .PepSubFrames import PepSubFramesCls
			self._pepSubFrames = PepSubFramesCls(self._core, self._cmd_group)
		return self._pepSubFrames

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
