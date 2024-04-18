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

	def set(self, frequency: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UDEFined:FREQuency:DL:MINimum \n
		Snippet: driver.configure.rfSettings.scc.userDefined.frequency.downlink.minimum.set(frequency = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the carrier center frequency corresponding to the minimum downlink channel number for the user-defined band.
		The other frequencies are calculated from the settings as follows: FREQ:DL:MAX = FREQ:DL:MIN + (CHAN:DL:MAX -
		CHAN:DL:MIN) * 100 kHz FREQ:UL:MIN = FREQ:DL:MIN - UDSeparation FREQ:UL:MAX = FREQ:DL:MIN - UDSeparation + (CHAN:DL:MAX -
		CHAN:DL:MIN) * 100 kHz \n
			:param frequency: numeric The allowed range depends on the remaining user-defined band settings. All frequencies resulting from the calculations stated above must be located within the following frequency range. Range: 70 MHz to 6 GHz, Unit: Hz
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UDEFined:FREQuency:DL:MINimum {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UDEFined:FREQuency:DL:MINimum \n
		Snippet: value: int = driver.configure.rfSettings.scc.userDefined.frequency.downlink.minimum.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the carrier center frequency corresponding to the minimum downlink channel number for the user-defined band.
		The other frequencies are calculated from the settings as follows: FREQ:DL:MAX = FREQ:DL:MIN + (CHAN:DL:MAX -
		CHAN:DL:MIN) * 100 kHz FREQ:UL:MIN = FREQ:DL:MIN - UDSeparation FREQ:UL:MAX = FREQ:DL:MIN - UDSeparation + (CHAN:DL:MAX -
		CHAN:DL:MIN) * 100 kHz \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: frequency: numeric The allowed range depends on the remaining user-defined band settings. All frequencies resulting from the calculations stated above must be located within the following frequency range. Range: 70 MHz to 6 GHz, Unit: Hz"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UDEFined:FREQuency:DL:MINimum?')
		return Conversions.str_to_int(response)
