from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SttiCls:
	"""Stti commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stti", core, parent)

	def set(self, scheduled: List[bool], secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FCRI:DL:STTI \n
		Snippet: driver.configure.connection.scc.fcri.downlink.stti.set(scheduled = [True, False, True], secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures which subframes are scheduled for the DL of the scheduling type 'Follow WB CQI-RI'. For most subframes, the
		setting is fixed, depending on the duplex mode and the UL-DL configuration. For these subframes, your setting is ignored. \n
			:param scheduled: OFF | ON Comma-separated list of 10 values, for subframe 0 to 9
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.list_to_csv_str(scheduled)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FCRI:DL:STTI {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> List[bool]:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FCRI:DL:STTI \n
		Snippet: value: List[bool] = driver.configure.connection.scc.fcri.downlink.stti.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures which subframes are scheduled for the DL of the scheduling type 'Follow WB CQI-RI'. For most subframes, the
		setting is fixed, depending on the duplex mode and the UL-DL configuration. For these subframes, your setting is ignored. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: scheduled: OFF | ON Comma-separated list of 10 values, for subframe 0 to 9"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FCRI:DL:STTI?')
		return Conversions.str_to_bool_list(response)
