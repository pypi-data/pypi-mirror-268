from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RssiCls:
	"""Rssi commands group definition. 5 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rssi", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def rmtc(self):
		"""rmtc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmtc'):
			from .Rmtc import RmtcCls
			self._rmtc = RmtcCls(self._core, self._cmd_group)
		return self._rmtc

	@property
	def coThreshold(self):
		"""coThreshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coThreshold'):
			from .CoThreshold import CoThresholdCls
			self._coThreshold = CoThresholdCls(self._core, self._cmd_group)
		return self._coThreshold

	@property
	def mduration(self):
		"""mduration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mduration'):
			from .Mduration import MdurationCls
			self._mduration = MdurationCls(self._core, self._cmd_group)
		return self._mduration

	def clone(self) -> 'RssiCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RssiCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
