from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrachCls:
	"""Prach commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def foffset(self):
		"""foffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_foffset'):
			from .Foffset import FoffsetCls
			self._foffset = FoffsetCls(self._core, self._cmd_group)
		return self._foffset

	@property
	def mpAttempts(self):
		"""mpAttempts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpAttempts'):
			from .MpAttempts import MpAttemptsCls
			self._mpAttempts = MpAttemptsCls(self._core, self._cmd_group)
		return self._mpAttempts

	@property
	def rpAttempt(self):
		"""rpAttempt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpAttempt'):
			from .RpAttempt import RpAttemptCls
			self._rpAttempt = RpAttemptCls(self._core, self._cmd_group)
		return self._rpAttempt

	@property
	def mmrRepetition(self):
		"""mmrRepetition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmrRepetition'):
			from .MmrRepetition import MmrRepetitionCls
			self._mmrRepetition = MmrRepetitionCls(self._core, self._cmd_group)
		return self._mmrRepetition

	@property
	def cindex(self):
		"""cindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cindex'):
			from .Cindex import CindexCls
			self._cindex = CindexCls(self._core, self._cmd_group)
		return self._cindex

	def clone(self) -> 'PrachCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrachCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
