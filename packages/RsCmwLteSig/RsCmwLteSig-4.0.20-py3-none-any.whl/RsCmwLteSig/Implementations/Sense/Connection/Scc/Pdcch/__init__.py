from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcchCls:
	"""Pdcch commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcch", core, parent)

	@property
	def psymbols(self):
		"""psymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psymbols'):
			from .Psymbols import PsymbolsCls
			self._psymbols = PsymbolsCls(self._core, self._cmd_group)
		return self._psymbols

	@property
	def alevel(self):
		"""alevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alevel'):
			from .Alevel import AlevelCls
			self._alevel = AlevelCls(self._core, self._cmd_group)
		return self._alevel

	def clone(self) -> 'PdcchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PdcchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
