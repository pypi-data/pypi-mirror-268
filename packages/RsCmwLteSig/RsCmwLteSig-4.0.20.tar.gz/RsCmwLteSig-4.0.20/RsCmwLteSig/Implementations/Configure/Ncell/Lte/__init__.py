from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LteCls:
	"""Lte commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

	@property
	def cell(self):
		"""cell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import CellCls
			self._cell = CellCls(self._core, self._cmd_group)
		return self._cell

	@property
	def thresholds(self):
		"""thresholds commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_thresholds'):
			from .Thresholds import ThresholdsCls
			self._thresholds = ThresholdsCls(self._core, self._cmd_group)
		return self._thresholds

	def clone(self) -> 'LteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
