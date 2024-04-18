from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InterRatCls:
	"""InterRat commands group definition. 7 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interRat", core, parent)

	@property
	def eredirection(self):
		"""eredirection commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_eredirection'):
			from .Eredirection import EredirectionCls
			self._eredirection = EredirectionCls(self._core, self._cmd_group)
		return self._eredirection

	@property
	def geran(self):
		"""geran commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_geran'):
			from .Geran import GeranCls
			self._geran = GeranCls(self._core, self._cmd_group)
		return self._geran

	@property
	def cxrtt(self):
		"""cxrtt commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_cxrtt'):
			from .Cxrtt import CxrttCls
			self._cxrtt = CxrttCls(self._core, self._cmd_group)
		return self._cxrtt

	def clone(self) -> 'InterRatCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InterRatCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
