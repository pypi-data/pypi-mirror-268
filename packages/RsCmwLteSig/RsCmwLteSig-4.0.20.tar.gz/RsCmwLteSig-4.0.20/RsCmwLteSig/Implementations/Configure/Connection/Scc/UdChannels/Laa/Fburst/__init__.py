from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FburstCls:
	"""Fburst commands group definition. 6 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fburst", core, parent)

	@property
	def fullSubFrames(self):
		"""fullSubFrames commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fullSubFrames'):
			from .FullSubFrames import FullSubFramesCls
			self._fullSubFrames = FullSubFramesCls(self._core, self._cmd_group)
		return self._fullSubFrames

	@property
	def pipSubFrames(self):
		"""pipSubFrames commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pipSubFrames'):
			from .PipSubFrames import PipSubFramesCls
			self._pipSubFrames = PipSubFramesCls(self._core, self._cmd_group)
		return self._pipSubFrames

	@property
	def pepSubFrames(self):
		"""pepSubFrames commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pepSubFrames'):
			from .PepSubFrames import PepSubFramesCls
			self._pepSubFrames = PepSubFramesCls(self._core, self._cmd_group)
		return self._pepSubFrames

	def clone(self) -> 'FburstCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FburstCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
