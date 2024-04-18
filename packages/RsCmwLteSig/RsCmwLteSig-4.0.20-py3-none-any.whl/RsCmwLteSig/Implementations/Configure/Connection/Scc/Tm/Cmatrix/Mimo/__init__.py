from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	@property
	def mselection(self):
		"""mselection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mselection'):
			from .Mselection import MselectionCls
			self._mselection = MselectionCls(self._core, self._cmd_group)
		return self._mselection

	@property
	def line(self):
		"""line commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_line'):
			from .Line import LineCls
			self._line = LineCls(self._core, self._cmd_group)
		return self._line

	def clone(self) -> 'MimoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MimoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
