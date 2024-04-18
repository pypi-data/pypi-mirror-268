from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	def get_minimum(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:CHANnel:DL:MINimum \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.channel.downlink.get_minimum() \n
		Configures channel numbers for the user-defined band: the minimum downlink channel number and the maximum downlink
		channel number. Combinations that result in frequencies outside of the allowed range are corrected automatically. \n
			:return: channel: decimal Range: 0 to 262143
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:CHANnel:DL:MINimum?')
		return Conversions.str_to_int(response)

	def set_minimum(self, channel: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:CHANnel:DL:MINimum \n
		Snippet: driver.configure.rfSettings.pcc.userDefined.channel.downlink.set_minimum(channel = 1) \n
		Configures channel numbers for the user-defined band: the minimum downlink channel number and the maximum downlink
		channel number. Combinations that result in frequencies outside of the allowed range are corrected automatically. \n
			:param channel: decimal Range: 0 to 262143
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:CHANnel:DL:MINimum {param}')

	def get_maximum(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:CHANnel:DL:MAXimum \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.channel.downlink.get_maximum() \n
		Configures channel numbers for the user-defined band: the minimum downlink channel number and the maximum downlink
		channel number. Combinations that result in frequencies outside of the allowed range are corrected automatically. \n
			:return: channel: decimal Range: 0 to 262143
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:CHANnel:DL:MAXimum?')
		return Conversions.str_to_int(response)

	def set_maximum(self, channel: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:CHANnel:DL:MAXimum \n
		Snippet: driver.configure.rfSettings.pcc.userDefined.channel.downlink.set_maximum(channel = 1) \n
		Configures channel numbers for the user-defined band: the minimum downlink channel number and the maximum downlink
		channel number. Combinations that result in frequencies outside of the allowed range are corrected automatically. \n
			:param channel: decimal Range: 0 to 262143
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:CHANnel:DL:MAXimum {param}')
