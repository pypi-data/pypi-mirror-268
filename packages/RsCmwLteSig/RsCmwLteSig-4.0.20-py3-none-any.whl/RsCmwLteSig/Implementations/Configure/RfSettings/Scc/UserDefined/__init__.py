from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefinedCls:
	"""UserDefined commands group definition. 10 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("userDefined", core, parent)

	@property
	def bindicator(self):
		"""bindicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bindicator'):
			from .Bindicator import BindicatorCls
			self._bindicator = BindicatorCls(self._core, self._cmd_group)
		return self._bindicator

	@property
	def channel(self):
		"""channel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import ChannelCls
			self._channel = ChannelCls(self._core, self._cmd_group)
		return self._channel

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def udSeparation(self):
		"""udSeparation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_udSeparation'):
			from .UdSeparation import UdSeparationCls
			self._udSeparation = UdSeparationCls(self._core, self._cmd_group)
		return self._udSeparation

	def clone(self) -> 'UserDefinedCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UserDefinedCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
