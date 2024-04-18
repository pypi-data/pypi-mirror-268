from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FburstCls:
	"""Fburst commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fburst", core, parent)

	@property
	def blength(self):
		"""blength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blength'):
			from .Blength import BlengthCls
			self._blength = BlengthCls(self._core, self._cmd_group)
		return self._blength

	@property
	def pbtr(self):
		"""pbtr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pbtr'):
			from .Pbtr import PbtrCls
			self._pbtr = PbtrCls(self._core, self._cmd_group)
		return self._pbtr

	@property
	def spfSubframe(self):
		"""spfSubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spfSubframe'):
			from .SpfSubframe import SpfSubframeCls
			self._spfSubframe = SpfSubframeCls(self._core, self._cmd_group)
		return self._spfSubframe

	@property
	def oslSubframe(self):
		"""oslSubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oslSubframe'):
			from .OslSubframe import OslSubframeCls
			self._oslSubframe = OslSubframeCls(self._core, self._cmd_group)
		return self._oslSubframe

	def clone(self) -> 'FburstCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FburstCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
