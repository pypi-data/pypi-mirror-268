from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LaaCls:
	"""Laa commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("laa", core, parent)

	def get_downlink(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:LAA:DL \n
		Snippet: value: int = driver.sense.ueCapability.laa.get_downlink() \n
		Returns whether the UE supports DL LAA operation. \n
			:return: downlink: 0 | 1
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:LAA:DL?')
		return Conversions.str_to_int(response)

	def get_edpts(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:LAA:EDPTs \n
		Snippet: value: int = driver.sense.ueCapability.laa.get_edpts() \n
		Returns whether the UE supports partial allocation in the ending subframe of an LAA burst. \n
			:return: pts: 0 | 1
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:LAA:EDPTs?')
		return Conversions.str_to_int(response)

	def get_sss_position(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:LAA:SSSPosition \n
		Snippet: value: int = driver.sense.ueCapability.laa.get_sss_position() \n
		Returns whether the UE supports partial allocation in the initial subframe of an LAA burst. \n
			:return: position: 0 | 1
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:LAA:SSSPosition?')
		return Conversions.str_to_int(response)

	def get_tm(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:LAA:TM<TMnr> \n
		Snippet: value: int = driver.sense.ueCapability.laa.get_tm() \n
		Returns whether the UE supports transmission mode 9 for LAA downlinks. \n
			:return: tm: 0 | 1
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:LAA:TM9?')
		return Conversions.str_to_int(response)
