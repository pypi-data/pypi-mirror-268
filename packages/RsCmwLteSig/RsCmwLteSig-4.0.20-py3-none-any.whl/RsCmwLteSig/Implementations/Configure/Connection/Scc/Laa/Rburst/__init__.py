from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RburstCls:
	"""Rburst commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rburst", core, parent)

	@property
	def psfConfig(self):
		"""psfConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psfConfig'):
			from .PsfConfig import PsfConfigCls
			self._psfConfig = PsfConfigCls(self._core, self._cmd_group)
		return self._psfConfig

	@property
	def blength(self):
		"""blength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blength'):
			from .Blength import BlengthCls
			self._blength = BlengthCls(self._core, self._cmd_group)
		return self._blength

	@property
	def lsConfig(self):
		"""lsConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lsConfig'):
			from .LsConfig import LsConfigCls
			self._lsConfig = LsConfigCls(self._core, self._cmd_group)
		return self._lsConfig

	@property
	def ipSubframe(self):
		"""ipSubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipSubframe'):
			from .IpSubframe import IpSubframeCls
			self._ipSubframe = IpSubframeCls(self._core, self._cmd_group)
		return self._ipSubframe

	@property
	def tprobability(self):
		"""tprobability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tprobability'):
			from .Tprobability import TprobabilityCls
			self._tprobability = TprobabilityCls(self._core, self._cmd_group)
		return self._tprobability

	def clone(self) -> 'RburstCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RburstCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
