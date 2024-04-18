from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RowCls:
	"""Row commands group definition. 2 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: HMatrixRow, default value after init: HMatrixRow.Row1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("row", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_hMatrixRow_get', 'repcap_hMatrixRow_set', repcap.HMatrixRow.Row1)

	def repcap_hMatrixRow_set(self, hMatrixRow: repcap.HMatrixRow) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to HMatrixRow.Default
		Default value after init: HMatrixRow.Row1"""
		self._cmd_group.set_repcap_enum_value(hMatrixRow)

	def repcap_hMatrixRow_get(self) -> repcap.HMatrixRow:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def col(self):
		"""col commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_col'):
			from .Col import ColCls
			self._col = ColCls(self._core, self._cmd_group)
		return self._col

	def clone(self) -> 'RowCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RowCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
