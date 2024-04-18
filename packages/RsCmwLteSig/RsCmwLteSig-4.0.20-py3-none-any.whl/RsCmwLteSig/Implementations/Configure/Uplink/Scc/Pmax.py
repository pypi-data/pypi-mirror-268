from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmaxCls:
	"""Pmax commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmax", core, parent)

	def set(self, power: float or bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PMAX \n
		Snippet: driver.configure.uplink.scc.pmax.set(power = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the maximum allowed UE power. \n
			:param power: (float or boolean) numeric | ON | OFF Range: -30 dBm to 33 dBm, Unit: dBm ON | OFF enables or disables signaling of the value to the UE.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_or_bool_value_to_str(power)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PMAX {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float or bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PMAX \n
		Snippet: value: float or bool = driver.configure.uplink.scc.pmax.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the maximum allowed UE power. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: power: (float or boolean) numeric | ON | OFF Range: -30 dBm to 33 dBm, Unit: dBm ON | OFF enables or disables signaling of the value to the UE."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PMAX?')
		return Conversions.str_to_float_or_bool(response)
