from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UtddCls:
	"""Utdd commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: UTddFreq, default value after init: UTddFreq.Freq128"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utdd", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_uTddFreq_get', 'repcap_uTddFreq_set', repcap.UTddFreq.Freq128)

	def repcap_uTddFreq_set(self, uTddFreq: repcap.UTddFreq) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UTddFreq.Default
		Default value after init: UTddFreq.Freq128"""
		self._cmd_group.set_repcap_enum_value(uTddFreq)

	def repcap_uTddFreq_get(self) -> repcap.UTddFreq:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def supported(self):
		"""supported commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_supported'):
			from .Supported import SupportedCls
			self._supported = SupportedCls(self._core, self._cmd_group)
		return self._supported

	@property
	def eredirection(self):
		"""eredirection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eredirection'):
			from .Eredirection import EredirectionCls
			self._eredirection = EredirectionCls(self._core, self._cmd_group)
		return self._eredirection

	def clone(self) -> 'UtddCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UtddCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
