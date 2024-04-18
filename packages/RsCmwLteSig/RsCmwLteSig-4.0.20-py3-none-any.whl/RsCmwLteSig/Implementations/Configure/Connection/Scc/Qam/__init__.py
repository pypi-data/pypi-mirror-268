from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QamCls:
	"""Qam commands group definition. 1 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: QAMmodulationOrderB, default value after init: QAMmodulationOrderB.QAM256"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qam", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_qAMmodulationOrderB_get', 'repcap_qAMmodulationOrderB_set', repcap.QAMmodulationOrderB.QAM256)

	def repcap_qAMmodulationOrderB_set(self, qAMmodulationOrderB: repcap.QAMmodulationOrderB) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to QAMmodulationOrderB.Default
		Default value after init: QAMmodulationOrderB.QAM256"""
		self._cmd_group.set_repcap_enum_value(qAMmodulationOrderB)

	def repcap_qAMmodulationOrderB_get(self) -> repcap.QAMmodulationOrderB:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	def clone(self) -> 'QamCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = QamCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
