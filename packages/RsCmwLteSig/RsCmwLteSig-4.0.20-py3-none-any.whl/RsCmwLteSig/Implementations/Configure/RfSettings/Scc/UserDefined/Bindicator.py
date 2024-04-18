from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BindicatorCls:
	"""Bindicator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bindicator", core, parent)

	def set(self, band_indicator: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UDEFined:BINDicator \n
		Snippet: driver.configure.rfSettings.scc.userDefined.bindicator.set(band_indicator = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the frequency band indicator, identifying the user-defined band in signaling messages. \n
			:param band_indicator: numeric Range: 1 to 256
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(band_indicator)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UDEFined:BINDicator {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UDEFined:BINDicator \n
		Snippet: value: int = driver.configure.rfSettings.scc.userDefined.bindicator.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the frequency band indicator, identifying the user-defined band in signaling messages. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: band_indicator: numeric Range: 1 to 256"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UDEFined:BINDicator?')
		return Conversions.str_to_int(response)
