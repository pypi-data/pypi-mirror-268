from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectionCls:
	"""Connection commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connection", core, parent)

	def get_def_bearer(self) -> List[str]:
		"""SCPI: CATalog:LTE:SIGNaling<instance>:CONNection:DEFBearer \n
		Snippet: value: List[str] = driver.catalog.connection.get_def_bearer() \n
		Queries a list of all established default bearers. \n
			:return: idn: string Comma-separated list of bearer IDs as strings String example: '5 (cmw500.rohde-schwarz.com) '
		"""
		response = self._core.io.query_str('CATalog:LTE:SIGNaling<Instance>:CONNection:DEFBearer?')
		return Conversions.str_to_str_list(response)

	def get_ded_bearer(self) -> List[str]:
		"""SCPI: CATalog:LTE:SIGNaling<instance>:CONNection:DEDBearer \n
		Snippet: value: List[str] = driver.catalog.connection.get_ded_bearer() \n
		Queries a list of all established dedicated bearers. \n
			:return: idn: string Comma-separated list of bearer IDs as strings String example: '6 (-5, Voice) '
		"""
		response = self._core.io.query_str('CATalog:LTE:SIGNaling<Instance>:CONNection:DEDBearer?')
		return Conversions.str_to_str_list(response)
