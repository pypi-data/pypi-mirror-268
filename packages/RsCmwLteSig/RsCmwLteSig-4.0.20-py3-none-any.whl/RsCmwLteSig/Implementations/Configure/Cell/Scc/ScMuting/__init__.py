from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScMutingCls:
	"""ScMuting commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scMuting", core, parent)

	@property
	def onsDuration(self):
		"""onsDuration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_onsDuration'):
			from .OnsDuration import OnsDurationCls
			self._onsDuration = OnsDurationCls(self._core, self._cmd_group)
		return self._onsDuration

	@property
	def offsDuration(self):
		"""offsDuration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offsDuration'):
			from .OffsDuration import OffsDurationCls
			self._offsDuration = OffsDurationCls(self._core, self._cmd_group)
		return self._offsDuration

	@property
	def pmac(self):
		"""pmac commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmac'):
			from .Pmac import PmacCls
			self._pmac = PmacCls(self._core, self._cmd_group)
		return self._pmac

	def clone(self) -> 'ScMutingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScMutingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
