from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CxrttCls:
	"""Cxrtt commands group definition. 6 total commands, 0 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cxrtt", core, parent)

	def get_supported(self) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:CXRTt:SUPPorted \n
		Snippet: value: List[bool] = driver.sense.ueCapability.interRat.cxrtt.get_supported() \n
		Returns a list of values indicating the support of the individual CDMA2000 1xRTT band classes by the UE. \n
			:return: supported_band: OFF | ON 18 values: band class 0 to 17
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:CXRTt:SUPPorted?')
		return Conversions.str_to_bool_list(response)

	# noinspection PyTypeChecker
	def get_tconfig(self) -> enums.TxRxConfiguration:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:CXRTt:TCONfig \n
		Snippet: value: enums.TxRxConfiguration = driver.sense.ueCapability.interRat.cxrtt.get_tconfig() \n
		Returns whether the UE supports dual transmitter for 1xRTT/E-UTRAN or only single transmitter. \n
			:return: tx_configuration: SINGle | DUAL
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:CXRTt:TCONfig?')
		return Conversions.str_to_scalar_enum(response, enums.TxRxConfiguration)

	# noinspection PyTypeChecker
	def get_rconfig(self) -> enums.TxRxConfiguration:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:CXRTt:RCONfig \n
		Snippet: value: enums.TxRxConfiguration = driver.sense.ueCapability.interRat.cxrtt.get_rconfig() \n
		Returns whether the UE supports dual receiver for 1xRTT/E-UTRAN or only single receiver. \n
			:return: rx_configuration: SINGle | DUAL
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:CXRTt:RCONfig?')
		return Conversions.str_to_scalar_enum(response, enums.TxRxConfiguration)

	def get_ecsfb(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:CXRTt:ECSFb \n
		Snippet: value: bool = driver.sense.ueCapability.interRat.cxrtt.get_ecsfb() \n
		Returns whether the UE supports enhanced CS fallback to CDMA2000 1xRTT or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:CXRTt:ECSFb?')
		return Conversions.str_to_bool(response)

	def get_eccmob(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:CXRTt:ECCMob \n
		Snippet: value: bool = driver.sense.ueCapability.interRat.cxrtt.get_eccmob() \n
		Returns whether the UE supports concurrent enhanced CS fallback to CDMA2000 1xRTT and handover/redirection to CDMA2000
		HRPD or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:CXRTt:ECCMob?')
		return Conversions.str_to_bool(response)

	def get_ec_dual(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:CXRTt:ECDual \n
		Snippet: value: bool = driver.sense.ueCapability.interRat.cxrtt.get_ec_dual() \n
		Returns whether the UE supports enhanced CS fallback to CDMA2000 1xRTT for dual Rx/Tx configuration or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:CXRTt:ECDual?')
		return Conversions.str_to_bool(response)
