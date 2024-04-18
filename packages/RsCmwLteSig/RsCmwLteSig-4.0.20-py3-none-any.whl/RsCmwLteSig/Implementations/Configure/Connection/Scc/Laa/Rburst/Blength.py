from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlengthCls:
	"""Blength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("blength", core, parent)

	def set(self, burst_length: List[bool], secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:RBURst:BLENgth \n
		Snippet: driver.configure.connection.scc.laa.rburst.blength.set(burst_length = [True, False, True], secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the possible burst lengths for LAA with random bursts. At least one value must be allowed (ON) . \n
			:param burst_length: OFF | ON Comma-separated list of 10 values Allowing lengths of (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) subframes
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.list_to_csv_str(burst_length)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:RBURst:BLENgth {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> List[bool]:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:RBURst:BLENgth \n
		Snippet: value: List[bool] = driver.configure.connection.scc.laa.rburst.blength.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the possible burst lengths for LAA with random bursts. At least one value must be allowed (ON) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: burst_length: OFF | ON Comma-separated list of 10 values Allowing lengths of (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) subframes"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:RBURst:BLENgth?')
		return Conversions.str_to_bool_list(response)
