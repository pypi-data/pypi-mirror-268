from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PortsCls:
	"""Ports commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ports", core, parent)

	def set(self, power: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<carrier>:POWer:PORTs \n
		Snippet: driver.configure.downlink.scc.power.ports.set(power = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the power offset for the antenna ports 7 to 10. \n
			:param power: numeric Range: -12 dB to 0 dB, Unit: dB
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(power)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:POWer:PORTs {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<carrier>:POWer:PORTs \n
		Snippet: value: int = driver.configure.downlink.scc.power.ports.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the power offset for the antenna ports 7 to 10. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: power: numeric Range: -12 dB to 0 dB, Unit: dB"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:POWer:PORTs?')
		return Conversions.str_to_int(response)
