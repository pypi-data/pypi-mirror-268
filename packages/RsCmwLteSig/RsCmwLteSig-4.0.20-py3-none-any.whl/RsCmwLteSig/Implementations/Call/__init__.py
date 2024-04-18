from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CallCls:
	"""Call commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("call", core, parent)

	@property
	def pswitched(self):
		"""pswitched commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pswitched'):
			from .Pswitched import PswitchedCls
			self._pswitched = PswitchedCls(self._core, self._cmd_group)
		return self._pswitched

	@property
	def scc(self):
		"""scc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .Scc import SccCls
			self._scc = SccCls(self._core, self._cmd_group)
		return self._scc

	@property
	def a(self):
		"""a commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_a'):
			from .A import ACls
			self._a = ACls(self._core, self._cmd_group)
		return self._a

	@property
	def b(self):
		"""b commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_b'):
			from .B import BCls
			self._b = BCls(self._core, self._cmd_group)
		return self._b

	def clone(self) -> 'CallCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CallCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
