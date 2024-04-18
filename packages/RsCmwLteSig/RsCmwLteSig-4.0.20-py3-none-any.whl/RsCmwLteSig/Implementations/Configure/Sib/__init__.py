from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SibCls:
	"""Sib commands group definition. 5 total commands, 4 Subgroups, 0 group commands
	Repeated Capability: SystemInfoBlock, default value after init: SystemInfoBlock.Sib8"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sib", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_systemInfoBlock_get', 'repcap_systemInfoBlock_set', repcap.SystemInfoBlock.Sib8)

	def repcap_systemInfoBlock_set(self, systemInfoBlock: repcap.SystemInfoBlock) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SystemInfoBlock.Default
		Default value after init: SystemInfoBlock.Sib8"""
		self._cmd_group.set_repcap_enum_value(systemInfoBlock)

	def repcap_systemInfoBlock_get(self) -> repcap.SystemInfoBlock:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def update(self):
		"""update commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_update'):
			from .Update import UpdateCls
			self._update = UpdateCls(self._core, self._cmd_group)
		return self._update

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def syst(self):
		"""syst commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_syst'):
			from .Syst import SystCls
			self._syst = SystCls(self._core, self._cmd_group)
		return self._syst

	@property
	def tnfo(self):
		"""tnfo commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tnfo'):
			from .Tnfo import TnfoCls
			self._tnfo = TnfoCls(self._core, self._cmd_group)
		return self._tnfo

	def clone(self) -> 'SibCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SibCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
