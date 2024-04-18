from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApPowerCls:
	"""ApPower commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apPower", core, parent)

	@property
	def rsPower(self):
		"""rsPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsPower'):
			from .RsPower import RsPowerCls
			self._rsPower = RsPowerCls(self._core, self._cmd_group)
		return self._rsPower

	@property
	def pirPower(self):
		"""pirPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pirPower'):
			from .PirPower import PirPowerCls
			self._pirPower = PirPowerCls(self._core, self._cmd_group)
		return self._pirPower

	@property
	def pnpusch(self):
		"""pnpusch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pnpusch'):
			from .Pnpusch import PnpuschCls
			self._pnpusch = PnpuschCls(self._core, self._cmd_group)
		return self._pnpusch

	@property
	def pcAlpha(self):
		"""pcAlpha commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcAlpha'):
			from .PcAlpha import PcAlphaCls
			self._pcAlpha = PcAlphaCls(self._core, self._cmd_group)
		return self._pcAlpha

	@property
	def tprrcSetup(self):
		"""tprrcSetup commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tprrcSetup'):
			from .TprrcSetup import TprrcSetupCls
			self._tprrcSetup = TprrcSetupCls(self._core, self._cmd_group)
		return self._tprrcSetup

	@property
	def pathloss(self):
		"""pathloss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pathloss'):
			from .Pathloss import PathlossCls
			self._pathloss = PathlossCls(self._core, self._cmd_group)
		return self._pathloss

	@property
	def eppPower(self):
		"""eppPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eppPower'):
			from .EppPower import EppPowerCls
			self._eppPower = EppPowerCls(self._core, self._cmd_group)
		return self._eppPower

	@property
	def eoPower(self):
		"""eoPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eoPower'):
			from .EoPower import EoPowerCls
			self._eoPower = EoPowerCls(self._core, self._cmd_group)
		return self._eoPower

	def clone(self) -> 'ApPowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApPowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
