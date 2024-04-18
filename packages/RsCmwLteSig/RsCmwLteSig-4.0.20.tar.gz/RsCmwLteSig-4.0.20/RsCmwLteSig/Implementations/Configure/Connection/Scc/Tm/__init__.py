from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TmCls:
	"""Tm commands group definition. 15 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tm", core, parent)

	@property
	def chMatrix(self):
		"""chMatrix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chMatrix'):
			from .ChMatrix import ChMatrixCls
			self._chMatrix = ChMatrixCls(self._core, self._cmd_group)
		return self._chMatrix

	@property
	def cmatrix(self):
		"""cmatrix commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmatrix'):
			from .Cmatrix import CmatrixCls
			self._cmatrix = CmatrixCls(self._core, self._cmd_group)
		return self._cmatrix

	@property
	def zp(self):
		"""zp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_zp'):
			from .Zp import ZpCls
			self._zp = ZpCls(self._core, self._cmd_group)
		return self._zp

	@property
	def csirs(self):
		"""csirs commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_csirs'):
			from .Csirs import CsirsCls
			self._csirs = CsirsCls(self._core, self._cmd_group)
		return self._csirs

	@property
	def pmatrix(self):
		"""pmatrix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmatrix'):
			from .Pmatrix import PmatrixCls
			self._pmatrix = PmatrixCls(self._core, self._cmd_group)
		return self._pmatrix

	@property
	def codewords(self):
		"""codewords commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_codewords'):
			from .Codewords import CodewordsCls
			self._codewords = CodewordsCls(self._core, self._cmd_group)
		return self._codewords

	@property
	def ntxAntennas(self):
		"""ntxAntennas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntxAntennas'):
			from .NtxAntennas import NtxAntennasCls
			self._ntxAntennas = NtxAntennasCls(self._core, self._cmd_group)
		return self._ntxAntennas

	def clone(self) -> 'TmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
