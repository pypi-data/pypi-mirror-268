from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpcCls:
	"""Tpc commands group definition. 8 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpc", core, parent)

	@property
	def set(self):
		"""set commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_set'):
			from .Set import SetCls
			self._set = SetCls(self._core, self._cmd_group)
		return self._set

	@property
	def pexecute(self):
		"""pexecute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pexecute'):
			from .Pexecute import PexecuteCls
			self._pexecute = PexecuteCls(self._core, self._cmd_group)
		return self._pexecute

	@property
	def rpControl(self):
		"""rpControl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpControl'):
			from .RpControl import RpControlCls
			self._rpControl = RpControlCls(self._core, self._cmd_group)
		return self._rpControl

	@property
	def single(self):
		"""single commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_single'):
			from .Single import SingleCls
			self._single = SingleCls(self._core, self._cmd_group)
		return self._single

	@property
	def cltPower(self):
		"""cltPower commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cltPower'):
			from .CltPower import CltPowerCls
			self._cltPower = CltPowerCls(self._core, self._cmd_group)
		return self._cltPower

	@property
	def udPattern(self):
		"""udPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_udPattern'):
			from .UdPattern import UdPatternCls
			self._udPattern = UdPatternCls(self._core, self._cmd_group)
		return self._udPattern

	@property
	def tpower(self):
		"""tpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpower'):
			from .Tpower import TpowerCls
			self._tpower = TpowerCls(self._core, self._cmd_group)
		return self._tpower

	def clone(self) -> 'TpcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TpcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
