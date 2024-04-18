from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LaaCls:
	"""Laa commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("laa", core, parent)

	def set(self, conf_index: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting:SCC<Carrier>:CINDex:LAA \n
		Snippet: driver.configure.cqiReporting.scc.cindex.laa.set(conf_index = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the LAA 'cqi-pmi-ConfigIndex' (ICQI/PMI) . \n
			:param conf_index: numeric Range: 0 to 316, 318 to 541
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(conf_index)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CQIReporting:SCC{secondaryCompCarrier_cmd_val}:CINDex:LAA {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting:SCC<Carrier>:CINDex:LAA \n
		Snippet: value: int = driver.configure.cqiReporting.scc.cindex.laa.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the LAA 'cqi-pmi-ConfigIndex' (ICQI/PMI) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: conf_index: numeric Range: 0 to 316, 318 to 541"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CQIReporting:SCC{secondaryCompCarrier_cmd_val}:CINDex:LAA?')
		return Conversions.str_to_int(response)
