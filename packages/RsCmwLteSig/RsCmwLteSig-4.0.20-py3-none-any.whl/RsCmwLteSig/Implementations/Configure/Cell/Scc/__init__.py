from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SccCls:
	"""Scc commands group definition. 21 total commands, 10 Subgroups, 0 group commands
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
	def pcid(self):
		"""pcid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcid'):
			from .Pcid import PcidCls
			self._pcid = PcidCls(self._core, self._cmd_group)
		return self._pcid

	@property
	def ulDl(self):
		"""ulDl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulDl'):
			from .UlDl import UlDlCls
			self._ulDl = UlDlCls(self._core, self._cmd_group)
		return self._ulDl

	@property
	def ssubframe(self):
		"""ssubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssubframe'):
			from .Ssubframe import SsubframeCls
			self._ssubframe = SsubframeCls(self._core, self._cmd_group)
		return self._ssubframe

	@property
	def csat(self):
		"""csat commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_csat'):
			from .Csat import CsatCls
			self._csat = CsatCls(self._core, self._cmd_group)
		return self._csat

	@property
	def scMuting(self):
		"""scMuting commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_scMuting'):
			from .ScMuting import ScMutingCls
			self._scMuting = ScMutingCls(self._core, self._cmd_group)
		return self._scMuting

	@property
	def ulSupport(self):
		"""ulSupport commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ulSupport'):
			from .UlSupport import UlSupportCls
			self._ulSupport = UlSupportCls(self._core, self._cmd_group)
		return self._ulSupport

	@property
	def srs(self):
		"""srs commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import SrsCls
			self._srs = SrsCls(self._core, self._cmd_group)
		return self._srs

	@property
	def dbandwidth(self):
		"""dbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbandwidth'):
			from .Dbandwidth import DbandwidthCls
			self._dbandwidth = DbandwidthCls(self._core, self._cmd_group)
		return self._dbandwidth

	@property
	def cid(self):
		"""cid commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cid'):
			from .Cid import CidCls
			self._cid = CidCls(self._core, self._cmd_group)
		return self._cid

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import SyncCls
			self._sync = SyncCls(self._core, self._cmd_group)
		return self._sync

	def clone(self) -> 'SccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
