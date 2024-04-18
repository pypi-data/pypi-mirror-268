from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdschCls:
	"""Pdsch commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdsch", core, parent)

	@property
	def pa(self):
		"""pa commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pa'):
			from .Pa import PaCls
			self._pa = PaCls(self._core, self._cmd_group)
		return self._pa

	@property
	def rindex(self):
		"""rindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rindex'):
			from .Rindex import RindexCls
			self._rindex = RindexCls(self._core, self._cmd_group)
		return self._rindex

	def clone(self) -> 'PdschCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PdschCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
