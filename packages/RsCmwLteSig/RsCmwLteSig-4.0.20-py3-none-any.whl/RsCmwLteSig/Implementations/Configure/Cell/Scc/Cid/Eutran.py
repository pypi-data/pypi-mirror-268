from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EutranCls:
	"""Eutran commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eutran", core, parent)

	def set(self, cid: str, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<Carrier>:CID:EUTRan \n
		Snippet: driver.configure.cell.scc.cid.eutran.set(cid = rawAbc, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the E-UTRAN cell identifier (28-digit binary number) . If you use carrier aggregation, configure different
		values for the component carriers. \n
			:param cid: binary Range: #B0 to #B1111111111111111111111111111
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.value_to_str(cid)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:CID:EUTRan {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<Carrier>:CID:EUTRan \n
		Snippet: value: str = driver.configure.cell.scc.cid.eutran.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the E-UTRAN cell identifier (28-digit binary number) . If you use carrier aggregation, configure different
		values for the component carriers. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: cid: binary Range: #B0 to #B1111111111111111111111111111"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:CID:EUTRan?')
		return trim_str_response(response)
