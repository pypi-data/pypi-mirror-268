from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 86 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def scc(self):
		"""scc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .Scc import SccCls
			self._scc = SccCls(self._core, self._cmd_group)
		return self._scc

	@property
	def seta(self):
		"""seta commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_seta'):
			from .Seta import SetaCls
			self._seta = SetaCls(self._core, self._cmd_group)
		return self._seta

	@property
	def setb(self):
		"""setb commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_setb'):
			from .Setb import SetbCls
			self._setb = SetbCls(self._core, self._cmd_group)
		return self._setb

	@property
	def setc(self):
		"""setc commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_setc'):
			from .Setc import SetcCls
			self._setc = SetcCls(self._core, self._cmd_group)
		return self._setc

	@property
	def pcc(self):
		"""pcc commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_pcc'):
			from .Pcc import PccCls
			self._pcc = PccCls(self._core, self._cmd_group)
		return self._pcc

	def clone(self) -> 'UplinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UplinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
