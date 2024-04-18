from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdttiBasedCls:
	"""UdttiBased commands group definition. 5 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("udttiBased", core, parent)

	@property
	def qam(self):
		"""qam commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qam'):
			from .Qam import QamCls
			self._qam = QamCls(self._core, self._cmd_group)
		return self._qam

	@property
	def downlink(self):
		"""downlink commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	def clone(self) -> 'UdttiBasedCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UdttiBasedCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
