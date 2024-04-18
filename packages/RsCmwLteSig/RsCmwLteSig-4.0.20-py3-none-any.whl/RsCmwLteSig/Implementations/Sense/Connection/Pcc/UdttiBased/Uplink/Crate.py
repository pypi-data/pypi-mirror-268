from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrateCls:
	"""Crate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crate", core, parent)

	def get_all(self) -> List[float]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:UL:CRATe:ALL \n
		Snippet: value: List[float] = driver.sense.connection.pcc.udttiBased.uplink.crate.get_all() \n
		Queries the code rate for all uplink subframes, applicable to all scheduling types with a TTI-based UL definition. \n
			:return: coderate: float Comma-separated list of 10 values (subframe 0 to subframe 9) Range: 0 to 10
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SENSe:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:UL:CRATe:ALL?')
		return response
