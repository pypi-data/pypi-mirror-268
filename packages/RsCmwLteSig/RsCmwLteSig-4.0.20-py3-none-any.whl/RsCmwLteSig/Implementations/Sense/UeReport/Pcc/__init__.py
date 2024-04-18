from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PccCls:
	"""Pcc commands group definition. 6 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcc", core, parent)

	@property
	def rsrp(self):
		"""rsrp commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rsrp'):
			from .Rsrp import RsrpCls
			self._rsrp = RsrpCls(self._core, self._cmd_group)
		return self._rsrp

	@property
	def rsrq(self):
		"""rsrq commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rsrq'):
			from .Rsrq import RsrqCls
			self._rsrq = RsrqCls(self._core, self._cmd_group)
		return self._rsrq

	@property
	def scell(self):
		"""scell commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scell'):
			from .Scell import ScellCls
			self._scell = ScellCls(self._core, self._cmd_group)
		return self._scell

	def clone(self) -> 'PccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
