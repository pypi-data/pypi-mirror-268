from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RarCls:
	"""Rar commands group definition. 2 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rar", core, parent)

	@property
	def cmcs(self):
		"""cmcs commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cmcs'):
			from .Cmcs import CmcsCls
			self._cmcs = CmcsCls(self._core, self._cmd_group)
		return self._cmcs

	def clone(self) -> 'RarCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RarCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
