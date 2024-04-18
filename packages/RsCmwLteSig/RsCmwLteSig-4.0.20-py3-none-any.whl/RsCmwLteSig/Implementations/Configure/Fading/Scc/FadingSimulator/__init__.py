from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FadingSimulatorCls:
	"""FadingSimulator commands group definition. 18 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fadingSimulator", core, parent)

	@property
	def globale(self):
		"""globale commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_globale'):
			from .Globale import GlobaleCls
			self._globale = GlobaleCls(self._core, self._cmd_group)
		return self._globale

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def bypass(self):
		"""bypass commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bypass'):
			from .Bypass import BypassCls
			self._bypass = BypassCls(self._core, self._cmd_group)
		return self._bypass

	@property
	def standard(self):
		"""standard commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_standard'):
			from .Standard import StandardCls
			self._standard = StandardCls(self._core, self._cmd_group)
		return self._standard

	@property
	def restart(self):
		"""restart commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_restart'):
			from .Restart import RestartCls
			self._restart = RestartCls(self._core, self._cmd_group)
		return self._restart

	@property
	def profile(self):
		"""profile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_profile'):
			from .Profile import ProfileCls
			self._profile = ProfileCls(self._core, self._cmd_group)
		return self._profile

	@property
	def iloss(self):
		"""iloss commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iloss'):
			from .Iloss import IlossCls
			self._iloss = IlossCls(self._core, self._cmd_group)
		return self._iloss

	@property
	def dshift(self):
		"""dshift commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dshift'):
			from .Dshift import DshiftCls
			self._dshift = DshiftCls(self._core, self._cmd_group)
		return self._dshift

	@property
	def matrix(self):
		"""matrix commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_matrix'):
			from .Matrix import MatrixCls
			self._matrix = MatrixCls(self._core, self._cmd_group)
		return self._matrix

	@property
	def hmat(self):
		"""hmat commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_hmat'):
			from .Hmat import HmatCls
			self._hmat = HmatCls(self._core, self._cmd_group)
		return self._hmat

	def clone(self) -> 'FadingSimulatorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FadingSimulatorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
