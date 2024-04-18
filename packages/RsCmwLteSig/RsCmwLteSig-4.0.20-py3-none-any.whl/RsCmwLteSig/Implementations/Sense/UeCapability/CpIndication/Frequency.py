from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get_intra(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:CPINdication:FREQuency:INTRa \n
		Snippet: value: bool = driver.sense.ueCapability.cpIndication.frequency.get_intra() \n
		Returns whether the UE supports proximity indications for intra-frequency E-UTRAN CSG member cells or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:CPINdication:FREQuency:INTRa?')
		return Conversions.str_to_bool(response)

	def get_inter(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:CPINdication:FREQuency:INTer \n
		Snippet: value: bool = driver.sense.ueCapability.cpIndication.frequency.get_inter() \n
		Returns whether the UE supports proximity indications for inter-frequency E-UTRAN CSG member cells or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:CPINdication:FREQuency:INTer?')
		return Conversions.str_to_bool(response)
