from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmcCls:
	"""Rmc commands group definition. 6 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmc", core, parent)

	@property
	def mcluster(self):
		"""mcluster commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcluster'):
			from .Mcluster import MclusterCls
			self._mcluster = MclusterCls(self._core, self._cmd_group)
		return self._mcluster

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def rbPosition(self):
		"""rbPosition commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rbPosition'):
			from .RbPosition import RbPositionCls
			self._rbPosition = RbPositionCls(self._core, self._cmd_group)
		return self._rbPosition

	@property
	def version(self):
		"""version commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_version'):
			from .Version import VersionCls
			self._version = VersionCls(self._core, self._cmd_group)
		return self._version

	@property
	def uplink(self):
		"""uplink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	def clone(self) -> 'RmcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RmcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
