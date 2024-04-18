from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SccCls:
	"""Scc commands group definition. 14 total commands, 12 Subgroups, 0 group commands
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
	def rsepre(self):
		"""rsepre commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsepre'):
			from .Rsepre import RsepreCls
			self._rsepre = RsepreCls(self._core, self._cmd_group)
		return self._rsepre

	@property
	def pss(self):
		"""pss commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pss'):
			from .Pss import PssCls
			self._pss = PssCls(self._core, self._cmd_group)
		return self._pss

	@property
	def sss(self):
		"""sss commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sss'):
			from .Sss import SssCls
			self._sss = SssCls(self._core, self._cmd_group)
		return self._sss

	@property
	def pbch(self):
		"""pbch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pbch'):
			from .Pbch import PbchCls
			self._pbch = PbchCls(self._core, self._cmd_group)
		return self._pbch

	@property
	def pcfich(self):
		"""pcfich commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcfich'):
			from .Pcfich import PcfichCls
			self._pcfich = PcfichCls(self._core, self._cmd_group)
		return self._pcfich

	@property
	def phich(self):
		"""phich commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_phich'):
			from .Phich import PhichCls
			self._phich = PhichCls(self._core, self._cmd_group)
		return self._phich

	@property
	def pdcch(self):
		"""pdcch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pdcch import PdcchCls
			self._pdcch = PdcchCls(self._core, self._cmd_group)
		return self._pdcch

	@property
	def pdsch(self):
		"""pdsch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdsch'):
			from .Pdsch import PdschCls
			self._pdsch = PdschCls(self._core, self._cmd_group)
		return self._pdsch

	@property
	def csirs(self):
		"""csirs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_csirs'):
			from .Csirs import CsirsCls
			self._csirs = CsirsCls(self._core, self._cmd_group)
		return self._csirs

	@property
	def ocng(self):
		"""ocng commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ocng'):
			from .Ocng import OcngCls
			self._ocng = OcngCls(self._core, self._cmd_group)
		return self._ocng

	@property
	def awgn(self):
		"""awgn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import AwgnCls
			self._awgn = AwgnCls(self._core, self._cmd_group)
		return self._awgn

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	def clone(self) -> 'SccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
