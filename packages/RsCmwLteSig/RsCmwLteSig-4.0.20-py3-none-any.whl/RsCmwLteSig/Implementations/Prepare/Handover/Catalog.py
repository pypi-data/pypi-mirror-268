from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get_destination(self) -> List[str]:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:CATalog:DESTination \n
		Snippet: value: List[str] = driver.prepare.handover.catalog.get_destination() \n
		Lists all handover destinations that can be selected using method RsCmwLteSig.Prepare.Handover.destination. \n
			:return: destination: string Comma-separated list of all supported destinations. Each destination is represented as a string. 'No Connection' means handover to another instrument. The '...Sig...' strings refer to signaling applications at the same instrument.
		"""
		response = self._core.io.query_str('PREPare:LTE:SIGNaling<Instance>:HANDover:CATalog:DESTination?')
		return Conversions.str_to_str_list(response)
