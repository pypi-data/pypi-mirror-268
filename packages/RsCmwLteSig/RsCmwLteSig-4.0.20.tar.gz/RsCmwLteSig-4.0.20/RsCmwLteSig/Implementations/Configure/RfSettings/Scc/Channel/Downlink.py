from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	def set(self, channel: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:CHANnel:DL \n
		Snippet: driver.configure.rfSettings.scc.channel.downlink.set(channel = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the DL channel number. It must be valid for the current operating band. The related UL channel number is
		calculated and set automatically. By appending a Hz unit (e.g. Hz, kHz, MHz) to a setting command, you can set the
		channel via its center frequency (only integer numbers accepted) . By appending a Hz unit to a query command, you can
		query the center frequency instead of the channel number. For channel numbers and frequencies depending on operating
		bands, see 'Operating bands'. \n
			:param channel: decimal Range: depends on operating band
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(channel)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:CHANnel:DL {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:CHANnel:DL \n
		Snippet: value: int = driver.configure.rfSettings.scc.channel.downlink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the DL channel number. It must be valid for the current operating band. The related UL channel number is
		calculated and set automatically. By appending a Hz unit (e.g. Hz, kHz, MHz) to a setting command, you can set the
		channel via its center frequency (only integer numbers accepted) . By appending a Hz unit to a query command, you can
		query the center frequency instead of the channel number. For channel numbers and frequencies depending on operating
		bands, see 'Operating bands'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: channel: decimal Range: depends on operating band"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:CHANnel:DL?')
		return Conversions.str_to_int(response)
