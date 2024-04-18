from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EredirectionCls:
	"""Eredirection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eredirection", core, parent)

	def get_utra(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:UFDD:EREDirection:UTRA \n
		Snippet: value: bool = driver.sense.ueCapability.interRat.ufdd.eredirection.get_utra() \n
		Returns whether the UE supports an enhanced redirection to UTRA FDD or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:UFDD:EREDirection:UTRA?')
		return Conversions.str_to_bool(response)
