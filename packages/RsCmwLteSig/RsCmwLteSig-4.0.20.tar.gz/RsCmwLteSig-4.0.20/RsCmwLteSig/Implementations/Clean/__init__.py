from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CleanCls:
	"""Clean commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clean", core, parent)

	@property
	def sms(self):
		"""sms commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sms'):
			from .Sms import SmsCls
			self._sms = SmsCls(self._core, self._cmd_group)
		return self._sms

	@property
	def eeLog(self):
		"""eeLog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eeLog'):
			from .EeLog import EeLogCls
			self._eeLog = EeLogCls(self._core, self._cmd_group)
		return self._eeLog

	@property
	def elog(self):
		"""elog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_elog'):
			from .Elog import ElogCls
			self._elog = ElogCls(self._core, self._cmd_group)
		return self._elog

	def clone(self) -> 'CleanCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CleanCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
