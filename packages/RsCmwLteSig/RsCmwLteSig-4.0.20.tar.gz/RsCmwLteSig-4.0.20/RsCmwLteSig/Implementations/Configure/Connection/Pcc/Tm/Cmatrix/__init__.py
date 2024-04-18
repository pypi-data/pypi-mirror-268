from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmatrixCls:
	"""Cmatrix commands group definition. 5 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmatrix", core, parent)

	@property
	def eight(self):
		"""eight commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eight'):
			from .Eight import EightCls
			self._eight = EightCls(self._core, self._cmd_group)
		return self._eight

	@property
	def four(self):
		"""four commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_four'):
			from .Four import FourCls
			self._four = FourCls(self._core, self._cmd_group)
		return self._four

	@property
	def two(self):
		"""two commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_two'):
			from .Two import TwoCls
			self._two = TwoCls(self._core, self._cmd_group)
		return self._two

	@property
	def mimo(self):
		"""mimo commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	def clone(self) -> 'CmatrixCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CmatrixCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
