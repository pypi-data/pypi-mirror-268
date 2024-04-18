from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CoThresholdCls:
	"""CoThreshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coThreshold", core, parent)

	def set(self, threshold: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RSSI:COTHreshold \n
		Snippet: driver.configure.ueReport.scc.rssi.coThreshold.set(threshold = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies a threshold for channel occupancy measurements for LAA.
		The setting is signaled to the UE as 'channelOccupancyThreshold'. The same value applies to all SCCs with frame structure
		type 3. \n
			:param threshold: numeric Range: 0 to 76
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(threshold)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RSSI:COTHreshold {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RSSI:COTHreshold \n
		Snippet: value: int = driver.configure.ueReport.scc.rssi.coThreshold.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies a threshold for channel occupancy measurements for LAA.
		The setting is signaled to the UE as 'channelOccupancyThreshold'. The same value applies to all SCCs with frame structure
		type 3. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: threshold: numeric Range: 0 to 76"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RSSI:COTHreshold?')
		return Conversions.str_to_int(response)
