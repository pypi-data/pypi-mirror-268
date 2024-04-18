from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrsCls:
	"""Srs commands group definition. 9 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srs", core, parent)

	@property
	def dconfig(self):
		"""dconfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dconfig'):
			from .Dconfig import DconfigCls
			self._dconfig = DconfigCls(self._core, self._cmd_group)
		return self._dconfig

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def bwConfig(self):
		"""bwConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwConfig'):
			from .BwConfig import BwConfigCls
			self._bwConfig = BwConfigCls(self._core, self._cmd_group)
		return self._bwConfig

	@property
	def hbandwidth(self):
		"""hbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hbandwidth'):
			from .Hbandwidth import HbandwidthCls
			self._hbandwidth = HbandwidthCls(self._core, self._cmd_group)
		return self._hbandwidth

	@property
	def mcEnable(self):
		"""mcEnable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcEnable'):
			from .McEnable import McEnableCls
			self._mcEnable = McEnableCls(self._core, self._cmd_group)
		return self._mcEnable

	@property
	def sfConfig(self):
		"""sfConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfConfig'):
			from .SfConfig import SfConfigCls
			self._sfConfig = SfConfigCls(self._core, self._cmd_group)
		return self._sfConfig

	@property
	def scIndex(self):
		"""scIndex commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_scIndex'):
			from .ScIndex import ScIndexCls
			self._scIndex = ScIndexCls(self._core, self._cmd_group)
		return self._scIndex

	@property
	def poffset(self):
		"""poffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_poffset'):
			from .Poffset import PoffsetCls
			self._poffset = PoffsetCls(self._core, self._cmd_group)
		return self._poffset

	def clone(self) -> 'SrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
