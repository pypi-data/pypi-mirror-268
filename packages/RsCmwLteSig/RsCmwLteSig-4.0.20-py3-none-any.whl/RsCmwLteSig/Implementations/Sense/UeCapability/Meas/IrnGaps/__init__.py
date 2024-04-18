from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IrnGapsCls:
	"""IrnGaps commands group definition. 10 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("irnGaps", core, parent)

	@property
	def ufdd(self):
		"""ufdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ufdd'):
			from .Ufdd import UfddCls
			self._ufdd = UfddCls(self._core, self._cmd_group)
		return self._ufdd

	@property
	def utdd(self):
		"""utdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_utdd'):
			from .Utdd import UtddCls
			self._utdd = UtddCls(self._core, self._cmd_group)
		return self._utdd

	@property
	def geran(self):
		"""geran commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_geran'):
			from .Geran import GeranCls
			self._geran = GeranCls(self._core, self._cmd_group)
		return self._geran

	@property
	def chrpd(self):
		"""chrpd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chrpd'):
			from .Chrpd import ChrpdCls
			self._chrpd = ChrpdCls(self._core, self._cmd_group)
		return self._chrpd

	@property
	def cxrtt(self):
		"""cxrtt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cxrtt'):
			from .Cxrtt import CxrttCls
			self._cxrtt = CxrttCls(self._core, self._cmd_group)
		return self._cxrtt

	@property
	def v(self):
		"""v commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_v'):
			from .V import VCls
			self._v = VCls(self._core, self._cmd_group)
		return self._v

	def clone(self) -> 'IrnGapsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IrnGapsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
