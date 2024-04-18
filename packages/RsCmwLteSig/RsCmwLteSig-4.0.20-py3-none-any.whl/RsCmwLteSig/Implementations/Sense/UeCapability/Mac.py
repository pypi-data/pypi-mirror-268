from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MacCls:
	"""Mac commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mac", core, parent)

	def get_ldrx_command(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MAC:LDRXcommand \n
		Snippet: value: bool = driver.sense.ueCapability.mac.get_ldrx_command() \n
		Returns whether the UE supports the long DRX command MAC control element as specified in 3GPP TS 36.321. \n
			:return: command: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:MAC:LDRXcommand?')
		return Conversions.str_to_bool(response)

	def get_lcsp_timer(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MAC:LCSPtimer \n
		Snippet: value: bool = driver.sense.ueCapability.mac.get_lcsp_timer() \n
		Returns whether the UE supports the logical channel SR prohibit timer as specified in 3GPP TS 36.321. \n
			:return: channel: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:MAC:LCSPtimer?')
		return Conversions.str_to_bool(response)
