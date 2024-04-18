from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PzeroCls:
	"""Pzero commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pzero", core, parent)

	@property
	def mapping(self):
		"""mapping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mapping'):
			from .Mapping import MappingCls
			self._mapping = MappingCls(self._core, self._cmd_group)
		return self._mapping

	def clone(self) -> 'PzeroCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PzeroCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
