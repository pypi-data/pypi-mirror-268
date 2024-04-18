from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MdurationCls:
	"""Mduration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mduration", core, parent)

	def set(self, duration: enums.SymbolsDuration, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RSSI:MDURation \n
		Snippet: driver.configure.ueReport.scc.rssi.mduration.set(duration = enums.SymbolsDuration.S1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the duration of UE measurements for LAA. \n
			:param duration: S1 | S14 | S28 | S42 | S70 Duration in OFDM symbols
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(duration, enums.SymbolsDuration)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RSSI:MDURation {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.SymbolsDuration:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RSSI:MDURation \n
		Snippet: value: enums.SymbolsDuration = driver.configure.ueReport.scc.rssi.mduration.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the duration of UE measurements for LAA. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: duration: S1 | S14 | S28 | S42 | S70 Duration in OFDM symbols"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RSSI:MDURation?')
		return Conversions.str_to_scalar_enum(response, enums.SymbolsDuration)
