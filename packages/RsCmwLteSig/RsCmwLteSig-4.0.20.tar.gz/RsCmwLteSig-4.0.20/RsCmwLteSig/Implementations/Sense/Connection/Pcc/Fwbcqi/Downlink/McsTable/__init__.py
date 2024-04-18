from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsTableCls:
	"""McsTable commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsTable", core, parent)

	@property
	def determined(self):
		"""determined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_determined'):
			from .Determined import DeterminedCls
			self._determined = DeterminedCls(self._core, self._cmd_group)
		return self._determined

	@property
	def csirs(self):
		"""csirs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_csirs'):
			from .Csirs import CsirsCls
			self._csirs = CsirsCls(self._core, self._cmd_group)
		return self._csirs

	@property
	def ssubframe(self):
		"""ssubframe commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ssubframe'):
			from .Ssubframe import SsubframeCls
			self._ssubframe = SsubframeCls(self._core, self._cmd_group)
		return self._ssubframe

	def clone(self) -> 'McsTableCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = McsTableCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
