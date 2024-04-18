from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlCls:
	"""Sl commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sl", core, parent)

	def get_dslss(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:SL:DSLSs \n
		Snippet: value: bool = driver.sense.ueCapability.sl.get_dslss() \n
		Returns whether the UE supports SLSS transmission and reception. \n
			:return: slss: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:SL:DSLSs?')
		return Conversions.str_to_bool(response)

	def get_cstx(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:SL:CSTX \n
		Snippet: value: bool = driver.sense.ueCapability.sl.get_cstx() \n
		Returns whether the UE supports simultaneous transmission of EUTRA and sidelink communication on different carriers. \n
			:return: simultaneous: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:SL:CSTX?')
		return Conversions.str_to_bool(response)

	def get_dsr_alloc(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:SL:DSRalloc \n
		Snippet: value: bool = driver.sense.ueCapability.sl.get_dsr_alloc() \n
		Returns whether the UE supports transmission of discovery announcements based on network scheduled resource allocation. \n
			:return: alloc: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:SL:DSRalloc?')
		return Conversions.str_to_bool(response)

	def get_dusralloc(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:SL:DUSRalloc \n
		Snippet: value: bool = driver.sense.ueCapability.sl.get_dusralloc() \n
		Returns whether the UE supports transmission of discovery announcements based on UE autonomous resource selection. \n
			:return: alloc: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:SL:DUSRalloc?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_dsproc(self) -> enums.UeSidelinkProcessesCount:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:SL:DSPRoc \n
		Snippet: value: enums.UeSidelinkProcessesCount = driver.sense.ueCapability.sl.get_dsproc() \n
		Returns the number of processes supported by the UE for sidelink discovery. \n
			:return: proc: N50 | N400
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:SL:DSPRoc?')
		return Conversions.str_to_scalar_enum(response, enums.UeSidelinkProcessesCount)
