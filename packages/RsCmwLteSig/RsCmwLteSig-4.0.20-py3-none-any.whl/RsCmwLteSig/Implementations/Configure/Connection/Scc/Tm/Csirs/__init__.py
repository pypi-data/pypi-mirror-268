from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsirsCls:
	"""Csirs commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csirs", core, parent)

	@property
	def aports(self):
		"""aports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aports'):
			from .Aports import AportsCls
			self._aports = AportsCls(self._core, self._cmd_group)
		return self._aports

	@property
	def subframe(self):
		"""subframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_subframe'):
			from .Subframe import SubframeCls
			self._subframe = SubframeCls(self._core, self._cmd_group)
		return self._subframe

	@property
	def resource(self):
		"""resource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resource'):
			from .Resource import ResourceCls
			self._resource = ResourceCls(self._core, self._cmd_group)
		return self._resource

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	def clone(self) -> 'CsirsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CsirsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
