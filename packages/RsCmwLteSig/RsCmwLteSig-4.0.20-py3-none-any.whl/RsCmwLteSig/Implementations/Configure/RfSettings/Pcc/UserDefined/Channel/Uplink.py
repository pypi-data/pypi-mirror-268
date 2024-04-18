from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	def get_minimum(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:CHANnel:UL:MINimum \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.channel.uplink.get_minimum() \n
		Configures the minimum uplink channel number for the user-defined band. Combinations that result in frequencies outside
		of the allowed range are corrected automatically. \n
			:return: channel: decimal Range: 0 to 262143
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:CHANnel:UL:MINimum?')
		return Conversions.str_to_int(response)

	def set_minimum(self, channel: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:CHANnel:UL:MINimum \n
		Snippet: driver.configure.rfSettings.pcc.userDefined.channel.uplink.set_minimum(channel = 1) \n
		Configures the minimum uplink channel number for the user-defined band. Combinations that result in frequencies outside
		of the allowed range are corrected automatically. \n
			:param channel: decimal Range: 0 to 262143
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:CHANnel:UL:MINimum {param}')

	def get_maximum(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:CHANnel:UL:MAXimum \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.channel.uplink.get_maximum() \n
		Queries the maximum uplink channel number for the user-defined band, resulting from the other channel number settings. \n
			:return: channel: decimal Maximum uplink channel number CHAN:UL:MAX = CHAN:UL:MIN + CHAN:DL:MAX - CHAN:DL:MIN
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:CHANnel:UL:MAXimum?')
		return Conversions.str_to_int(response)
