from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LaaCls:
	"""Laa commands group definition. 10 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("laa", core, parent)

	@property
	def tbursts(self):
		"""tbursts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbursts'):
			from .Tbursts import TburstsCls
			self._tbursts = TburstsCls(self._core, self._cmd_group)
		return self._tbursts

	@property
	def rburst(self):
		"""rburst commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_rburst'):
			from .Rburst import RburstCls
			self._rburst = RburstCls(self._core, self._cmd_group)
		return self._rburst

	@property
	def fburst(self):
		"""fburst commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fburst'):
			from .Fburst import FburstCls
			self._fburst = FburstCls(self._core, self._cmd_group)
		return self._fburst

	def clone(self) -> 'LaaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LaaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
