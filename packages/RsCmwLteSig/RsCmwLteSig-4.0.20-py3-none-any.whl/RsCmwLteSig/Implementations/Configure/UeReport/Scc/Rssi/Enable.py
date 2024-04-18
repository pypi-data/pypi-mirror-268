from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RSSI:ENABle \n
		Snippet: driver.configure.ueReport.scc.rssi.enable.set(enable = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables or disables the signaling of the IE 'measRSSI-ReportConfig' to the UE. \n
			:param enable: OFF | ON
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.bool_to_str(enable)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RSSI:ENABle {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RSSI:ENABle \n
		Snippet: value: bool = driver.configure.ueReport.scc.rssi.enable.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables or disables the signaling of the IE 'measRSSI-ReportConfig' to the UE. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: enable: OFF | ON"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RSSI:ENABle?')
		return Conversions.str_to_bool(response)
