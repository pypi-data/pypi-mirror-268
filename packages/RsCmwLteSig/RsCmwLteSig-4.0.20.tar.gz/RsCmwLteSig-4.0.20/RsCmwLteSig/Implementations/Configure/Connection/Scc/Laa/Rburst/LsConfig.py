from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LsConfigCls:
	"""LsConfig commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lsConfig", core, parent)

	def set(self, config: List[bool], secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:RBURst:LSConfig \n
		Snippet: driver.configure.connection.scc.laa.rburst.lsConfig.set(config = [True, False, True], secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the possible number of allocated OFDM symbols in ending subframes for LAA with random bursts. At least one
		value must be allowed (ON) . \n
			:param config: OFF | ON Comma-separated list of 6 values Allowing (6, 9, 10, 11, 12, 14) symbols
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.list_to_csv_str(config)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:RBURst:LSConfig {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> List[bool]:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:RBURst:LSConfig \n
		Snippet: value: List[bool] = driver.configure.connection.scc.laa.rburst.lsConfig.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the possible number of allocated OFDM symbols in ending subframes for LAA with random bursts. At least one
		value must be allowed (ON) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: config: OFF | ON Comma-separated list of 6 values Allowing (6, 9, 10, 11, 12, 14) symbols"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:RBURst:LSConfig?')
		return Conversions.str_to_bool_list(response)
