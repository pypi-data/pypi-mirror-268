from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsymbolsCls:
	"""Psymbols commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psymbols", core, parent)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:PDCCh:PSYMbols \n
		Snippet: value: int = driver.sense.connection.scc.pdcch.psymbols.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the number of PDCCH symbols per normal subframe. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: pdcch_symbols: decimal Range: 1 to 4"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:PDCCh:PSYMbols?')
		return Conversions.str_to_int(response)
