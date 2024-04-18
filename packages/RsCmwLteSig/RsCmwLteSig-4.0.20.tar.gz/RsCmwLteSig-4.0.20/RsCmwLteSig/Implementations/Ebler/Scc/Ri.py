from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RiCls:
	"""Ri commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ri", core, parent)

	def fetch(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> List[int]:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer:SCC<Carrier>:RI \n
		Snippet: value: List[int] = driver.ebler.scc.ri.fetch(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns the rank indicator (RI) results. \n
		Use RsCmwLteSig.reliability.last_value to read the updated reliability indicator. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: ri: decimal Comma-separated list of four values: Number of received 'RI = 1', Number of received 'RI = 2', Number of received 'RI = 3', Number of received 'RI = 4'"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:LTE:SIGNaling<Instance>:EBLer:SCC{secondaryCompCarrier_cmd_val}:RI?', suppressed)
		return response
