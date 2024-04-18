from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TprobabilityCls:
	"""Tprobability commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tprobability", core, parent)

	def set(self, probability: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:RBURst:TPRobability \n
		Snippet: driver.configure.connection.scc.laa.rburst.tprobability.set(probability = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the burst transmission probability, for LAA with random bursts. \n
			:param probability: numeric Range: 0 % to 100 %, Unit: %
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(probability)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:RBURst:TPRobability {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:RBURst:TPRobability \n
		Snippet: value: int = driver.configure.connection.scc.laa.rburst.tprobability.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the burst transmission probability, for LAA with random bursts. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: probability: numeric Range: 0 % to 100 %, Unit: %"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:RBURst:TPRobability?')
		return Conversions.str_to_int(response)
