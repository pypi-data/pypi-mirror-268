from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TaueEutraCls:
	"""TaueEutra commands group definition. 22 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("taueEutra", core, parent)

	@property
	def player(self):
		"""player commands group. 0 Sub-classes, 9 commands."""
		if not hasattr(self, '_player'):
			from .Player import PlayerCls
			self._player = PlayerCls(self._core, self._cmd_group)
		return self._player

	@property
	def fgIndicators(self):
		"""fgIndicators commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_fgIndicators'):
			from .FgIndicators import FgIndicatorsCls
			self._fgIndicators = FgIndicatorsCls(self._core, self._cmd_group)
		return self._fgIndicators

	@property
	def interRat(self):
		"""interRat commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_interRat'):
			from .InterRat import InterRatCls
			self._interRat = InterRatCls(self._core, self._cmd_group)
		return self._interRat

	@property
	def ncsacq(self):
		"""ncsacq commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncsacq'):
			from .Ncsacq import NcsacqCls
			self._ncsacq = NcsacqCls(self._core, self._cmd_group)
		return self._ncsacq

	def clone(self) -> 'TaueEutraCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TaueEutraCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
