from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CxrttCls:
	"""Cxrtt commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cxrtt", core, parent)

	def get_ecsfb(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:TAUeeutra:IRAT:CXRTt:ECSFb \n
		Snippet: value: bool = driver.sense.ueCapability.taueEutra.interRat.cxrtt.get_ecsfb() \n
		Returns whether the UE supports enhanced CS fallback to CDMA2000 1xRTT or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:TAUeeutra:IRAT:CXRTt:ECSFb?')
		return Conversions.str_to_bool(response)

	def get_eccmob(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:TAUeeutra:IRAT:CXRTt:ECCMob \n
		Snippet: value: bool = driver.sense.ueCapability.taueEutra.interRat.cxrtt.get_eccmob() \n
		Returns whether the UE supports concurrent enhanced CS fallback to CDMA2000 1xRTT and handover/redirection to CDMA2000
		HRPD or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:TAUeeutra:IRAT:CXRTt:ECCMob?')
		return Conversions.str_to_bool(response)

	def get_ec_dual(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:TAUeeutra:IRAT:CXRTt:ECDual \n
		Snippet: value: bool = driver.sense.ueCapability.taueEutra.interRat.cxrtt.get_ec_dual() \n
		Returns whether the UE supports enhanced CS fallback to CDMA2000 1xRTT for dual Rx/Tx configuration or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:TAUeeutra:IRAT:CXRTt:ECDual?')
		return Conversions.str_to_bool(response)
