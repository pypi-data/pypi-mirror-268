from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WiwCls:
	"""Wiw commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wiw", core, parent)

	def get_wia_policies(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:WIW:WIAPolicies \n
		Snippet: value: bool = driver.sense.ueCapability.wiw.get_wia_policies() \n
		Returns whether the UE supports RAN-assisted WLAN interworking based on ANDSF policies specified in 3GPP TS 24.312. \n
			:return: policies: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:WIW:WIAPolicies?')
		return Conversions.str_to_bool(response)

	def get_wir_rules(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:WIW:WIRRules \n
		Snippet: value: bool = driver.sense.ueCapability.wiw.get_wir_rules() \n
		Returns whether the UE supports RAN-assisted WLAN interworking based on access network selection and traffic steering
		rules specified in 3GPP TS 36.304. \n
			:return: rules: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:WIW:WIRRules?')
		return Conversions.str_to_bool(response)
