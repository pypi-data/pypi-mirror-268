from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ColCls:
	"""Col commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: HMatrixColumn, default value after init: HMatrixColumn.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("col", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_hMatrixColumn_get', 'repcap_hMatrixColumn_set', repcap.HMatrixColumn.Nr1)

	def repcap_hMatrixColumn_set(self, hMatrixColumn: repcap.HMatrixColumn) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to HMatrixColumn.Default
		Default value after init: HMatrixColumn.Nr1"""
		self._cmd_group.set_repcap_enum_value(hMatrixColumn)

	def repcap_hMatrixColumn_get(self) -> repcap.HMatrixColumn:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def imag(self):
		"""imag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imag'):
			from .Imag import ImagCls
			self._imag = ImagCls(self._core, self._cmd_group)
		return self._imag

	@property
	def real(self):
		"""real commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_real'):
			from .Real import RealCls
			self._real = RealCls(self._core, self._cmd_group)
		return self._real

	def clone(self) -> 'ColCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ColCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
