from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChrpdCls:
	"""Chrpd commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chrpd", core, parent)

	def get_supported(self) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:CHRPd:SUPPorted \n
		Snippet: value: List[bool] = driver.sense.ueCapability.interRat.chrpd.get_supported() \n
		Returns a list of values indicating the support of the individual CDMA2000 HRPD band classes by the UE. \n
			:return: supported_band: OFF | ON 18 values: band class 0 to 17
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:CHRPd:SUPPorted?')
		return Conversions.str_to_bool_list(response)

	# noinspection PyTypeChecker
	def get_tconfig(self) -> enums.TxRxConfiguration:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:CHRPd:TCONfig \n
		Snippet: value: enums.TxRxConfiguration = driver.sense.ueCapability.interRat.chrpd.get_tconfig() \n
		Returns whether the UE supports dual transmitter for HRPD/E-UTRAN or only single transmitter. \n
			:return: tx_configuration: SINGle | DUAL
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:CHRPd:TCONfig?')
		return Conversions.str_to_scalar_enum(response, enums.TxRxConfiguration)

	# noinspection PyTypeChecker
	def get_rconfig(self) -> enums.TxRxConfiguration:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:CHRPd:RCONfig \n
		Snippet: value: enums.TxRxConfiguration = driver.sense.ueCapability.interRat.chrpd.get_rconfig() \n
		Returns whether the UE supports dual receiver for HRPD/E-UTRAN or only single receiver. \n
			:return: rx_configuration: SINGle | DUAL
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:CHRPd:RCONfig?')
		return Conversions.str_to_scalar_enum(response, enums.TxRxConfiguration)
