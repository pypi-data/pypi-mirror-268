from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SccCls:
	"""Scc commands group definition. 25 total commands, 8 Subgroups, 0 group commands
	Repeated Capability: SecondaryCompCarrier, default value after init: SecondaryCompCarrier.CC1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_secondaryCompCarrier_get', 'repcap_secondaryCompCarrier_set', repcap.SecondaryCompCarrier.CC1)

	def repcap_secondaryCompCarrier_set(self, secondaryCompCarrier: repcap.SecondaryCompCarrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondaryCompCarrier.Default
		Default value after init: SecondaryCompCarrier.CC1"""
		self._cmd_group.set_repcap_enum_value(secondaryCompCarrier)

	def repcap_secondaryCompCarrier_get(self) -> repcap.SecondaryCompCarrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def hpusch(self):
		"""hpusch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hpusch'):
			from .Hpusch import HpuschCls
			self._hpusch = HpuschCls(self._core, self._cmd_group)
		return self._hpusch

	@property
	def tscheme(self):
		"""tscheme commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tscheme'):
			from .Tscheme import TschemeCls
			self._tscheme = TschemeCls(self._core, self._cmd_group)
		return self._tscheme

	@property
	def udChannels(self):
		"""udChannels commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_udChannels'):
			from .UdChannels import UdChannelsCls
			self._udChannels = UdChannelsCls(self._core, self._cmd_group)
		return self._udChannels

	@property
	def udttiBased(self):
		"""udttiBased commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_udttiBased'):
			from .UdttiBased import UdttiBasedCls
			self._udttiBased = UdttiBasedCls(self._core, self._cmd_group)
		return self._udttiBased

	@property
	def fwbcqi(self):
		"""fwbcqi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fwbcqi'):
			from .Fwbcqi import FwbcqiCls
			self._fwbcqi = FwbcqiCls(self._core, self._cmd_group)
		return self._fwbcqi

	@property
	def fcri(self):
		"""fcri commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcri'):
			from .Fcri import FcriCls
			self._fcri = FcriCls(self._core, self._cmd_group)
		return self._fcri

	@property
	def fcpri(self):
		"""fcpri commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcpri'):
			from .Fcpri import FcpriCls
			self._fcpri = FcpriCls(self._core, self._cmd_group)
		return self._fcpri

	@property
	def pdcch(self):
		"""pdcch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pdcch import PdcchCls
			self._pdcch = PdcchCls(self._core, self._cmd_group)
		return self._pdcch

	def clone(self) -> 'SccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
