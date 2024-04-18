from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CbsCls:
	"""Cbs commands group definition. 19 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbs", core, parent)

	@property
	def message(self):
		"""message commands group. 5 Sub-classes, 11 commands."""
		if not hasattr(self, '_message'):
			from .Message import MessageCls
			self._message = MessageCls(self._core, self._cmd_group)
		return self._message

	def clone(self) -> 'CbsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CbsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
