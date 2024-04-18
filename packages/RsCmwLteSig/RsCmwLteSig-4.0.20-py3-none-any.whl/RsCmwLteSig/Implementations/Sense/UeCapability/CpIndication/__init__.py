from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CpIndicationCls:
	"""CpIndication commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cpIndication", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	def get_utran(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:CPINdication:UTRan \n
		Snippet: value: bool = driver.sense.ueCapability.cpIndication.get_utran() \n
		Returns whether the UE supports proximity indications for UTRAN CSG member cells or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:CPINdication:UTRan?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'CpIndicationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CpIndicationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
