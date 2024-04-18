from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsatCls:
	"""Csat commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csat", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def dmtcPeriod(self):
		"""dmtcPeriod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmtcPeriod'):
			from .DmtcPeriod import DmtcPeriodCls
			self._dmtcPeriod = DmtcPeriodCls(self._core, self._cmd_group)
		return self._dmtcPeriod

	def clone(self) -> 'CsatCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CsatCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
