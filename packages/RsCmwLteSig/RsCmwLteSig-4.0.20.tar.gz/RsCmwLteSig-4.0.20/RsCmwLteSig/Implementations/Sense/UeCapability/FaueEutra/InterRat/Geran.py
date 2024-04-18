from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GeranCls:
	"""Geran commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("geran", core, parent)

	def get_supported(self) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:FAUeeutra:IRAT:GERan:SUPPorted \n
		Snippet: value: List[bool] = driver.sense.ueCapability.faueEutra.interRat.geran.get_supported() \n
		Returns a list of values indicating the support of the individual GERAN operating bands by the UE. \n
			:return: supported_band: OFF | ON 11 values: GSM 450, GSM 480, GSM 710, GSM 750, GSM 810, GSM 850, P-GSM 900, E-GSM 900, R-GSM 900, GSM 1800, GSM 1900
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:FAUeeutra:IRAT:GERan:SUPPorted?')
		return Conversions.str_to_bool_list(response)

	def get_phgeran(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:FAUeeutra:IRAT:GERan:PHGeran \n
		Snippet: value: bool = driver.sense.ueCapability.faueEutra.interRat.geran.get_phgeran() \n
		Returns whether the UE supports handover to GERAN or not. \n
			:return: ps_ho_geran: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:FAUeeutra:IRAT:GERan:PHGeran?')
		return Conversions.str_to_bool(response)
