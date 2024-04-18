from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def set(self, channel: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UDEFined:CHANnel:UL:MINimum \n
		Snippet: driver.configure.rfSettings.scc.userDefined.channel.uplink.minimum.set(channel = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the minimum uplink channel number for the user-defined band. Combinations that result in frequencies outside
		of the allowed range are corrected automatically. \n
			:param channel: decimal Range: 0 to 262143
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(channel)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UDEFined:CHANnel:UL:MINimum {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UDEFined:CHANnel:UL:MINimum \n
		Snippet: value: int = driver.configure.rfSettings.scc.userDefined.channel.uplink.minimum.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the minimum uplink channel number for the user-defined band. Combinations that result in frequencies outside
		of the allowed range are corrected automatically. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: channel: decimal Range: 0 to 262143"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UDEFined:CHANnel:UL:MINimum?')
		return Conversions.str_to_int(response)
