from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelCls:
	"""Channel commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("channel", core, parent)

	def get_downlink(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:CHANnel:DL \n
		Snippet: value: int = driver.configure.rfSettings.pcc.channel.get_downlink() \n
		Selects the DL channel number. It must be valid for the current operating band. The related UL channel number is
		calculated and set automatically. By appending a Hz unit (e.g. Hz, kHz, MHz) to a setting command, you can set the
		channel via its center frequency (only integer numbers accepted) . By appending a Hz unit to a query command, you can
		query the center frequency instead of the channel number. For channel numbers and frequencies depending on operating
		bands, see 'Operating bands'. \n
			:return: channel: decimal Range: depends on operating band
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:CHANnel:DL?')
		return Conversions.str_to_int(response)

	def set_downlink(self, channel: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:CHANnel:DL \n
		Snippet: driver.configure.rfSettings.pcc.channel.set_downlink(channel = 1) \n
		Selects the DL channel number. It must be valid for the current operating band. The related UL channel number is
		calculated and set automatically. By appending a Hz unit (e.g. Hz, kHz, MHz) to a setting command, you can set the
		channel via its center frequency (only integer numbers accepted) . By appending a Hz unit to a query command, you can
		query the center frequency instead of the channel number. For channel numbers and frequencies depending on operating
		bands, see 'Operating bands'. \n
			:param channel: decimal Range: depends on operating band
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:CHANnel:DL {param}')

	def get_uplink(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:CHANnel:UL \n
		Snippet: value: int = driver.configure.rfSettings.pcc.channel.get_uplink() \n
		Selects the UL channel number. It must be valid for the current operating band. The related DL channel number is
		calculated and set automatically. By appending a Hz unit (e.g. Hz, kHz, MHz) to a setting command, you can set the
		channel via its center frequency (only integer numbers accepted) . By appending a Hz unit to a query command, you can
		query the center frequency instead of the channel number. For channel numbers and frequencies depending on operating
		bands, see 'Operating bands'. \n
			:return: channel: decimal Range: depends on operating band
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:CHANnel:UL?')
		return Conversions.str_to_int(response)

	def set_uplink(self, channel: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:CHANnel:UL \n
		Snippet: driver.configure.rfSettings.pcc.channel.set_uplink(channel = 1) \n
		Selects the UL channel number. It must be valid for the current operating band. The related DL channel number is
		calculated and set automatically. By appending a Hz unit (e.g. Hz, kHz, MHz) to a setting command, you can set the
		channel via its center frequency (only integer numbers accepted) . By appending a Hz unit to a query command, you can
		query the center frequency instead of the channel number. For channel numbers and frequencies depending on operating
		bands, see 'Operating bands'. \n
			:param channel: decimal Range: depends on operating band
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:CHANnel:UL {param}')
