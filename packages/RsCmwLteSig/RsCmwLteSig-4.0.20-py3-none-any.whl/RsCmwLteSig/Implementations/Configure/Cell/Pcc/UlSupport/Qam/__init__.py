from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QamCls:
	"""Qam commands group definition. 1 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: QAMmodulationOrder, default value after init: QAMmodulationOrder.QAM64"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qam", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_qAMmodulationOrder_get', 'repcap_qAMmodulationOrder_set', repcap.QAMmodulationOrder.QAM64)

	def repcap_qAMmodulationOrder_set(self, qAMmodulationOrder: repcap.QAMmodulationOrder) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to QAMmodulationOrder.Default
		Default value after init: QAMmodulationOrder.QAM64"""
		self._cmd_group.set_repcap_enum_value(qAMmodulationOrder)

	def repcap_qAMmodulationOrder_get(self) -> repcap.QAMmodulationOrder:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	def clone(self) -> 'QamCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = QamCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
