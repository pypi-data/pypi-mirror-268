from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeAddressCls:
	"""UeAddress commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueAddress", core, parent)

	@property
	def ipv(self):
		"""ipv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipv'):
			from .Ipv import IpvCls
			self._ipv = IpvCls(self._core, self._cmd_group)
		return self._ipv

	@property
	def dedBearer(self):
		"""dedBearer commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dedBearer'):
			from .DedBearer import DedBearerCls
			self._dedBearer = DedBearerCls(self._core, self._cmd_group)
		return self._dedBearer

	def clone(self) -> 'UeAddressCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeAddressCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
