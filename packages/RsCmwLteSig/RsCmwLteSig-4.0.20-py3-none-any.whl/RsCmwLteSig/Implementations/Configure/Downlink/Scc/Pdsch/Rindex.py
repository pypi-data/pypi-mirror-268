from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RindexCls:
	"""Rindex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rindex", core, parent)

	def set(self, ratio_index: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:PDSCh:RINDex \n
		Snippet: driver.configure.downlink.scc.pdsch.rindex.set(ratio_index = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the power ratio index PB. The index is required for calculation of the power level of a PDSCH resource element. \n
			:param ratio_index: numeric Range: 0 to 3
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(ratio_index)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:PDSCh:RINDex {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:PDSCh:RINDex \n
		Snippet: value: int = driver.configure.downlink.scc.pdsch.rindex.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the power ratio index PB. The index is required for calculation of the power level of a PDSCH resource element. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: ratio_index: numeric Range: 0 to 3"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:PDSCh:RINDex?')
		return Conversions.str_to_int(response)
