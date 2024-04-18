from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CindexCls:
	"""Cindex commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cindex", core, parent)

	@property
	def laa(self):
		"""laa commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_laa'):
			from .Laa import LaaCls
			self._laa = LaaCls(self._core, self._cmd_group)
		return self._laa

	@property
	def fdd(self):
		"""fdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdd'):
			from .Fdd import FddCls
			self._fdd = FddCls(self._core, self._cmd_group)
		return self._fdd

	@property
	def tdd(self):
		"""tdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdd'):
			from .Tdd import TddCls
			self._tdd = TddCls(self._core, self._cmd_group)
		return self._tdd

	def clone(self) -> 'CindexCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CindexCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
