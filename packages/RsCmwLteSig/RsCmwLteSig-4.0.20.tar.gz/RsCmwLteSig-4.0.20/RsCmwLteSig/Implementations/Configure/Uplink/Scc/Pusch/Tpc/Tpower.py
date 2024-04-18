from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpowerCls:
	"""Tpower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpower", core, parent)

	def set(self, power: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:TPOWer \n
		Snippet: driver.configure.uplink.scc.pusch.tpc.tpower.set(power = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the target powers for power control with the TPC setup FULPower. \n
			:param power: numeric Range: -50 dBm to 33 dBm, Unit: dBm
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(power)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:TPOWer {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:TPOWer \n
		Snippet: value: float = driver.configure.uplink.scc.pusch.tpc.tpower.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the target powers for power control with the TPC setup FULPower. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: power: numeric Range: -50 dBm to 33 dBm, Unit: dBm"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:TPOWer?')
		return Conversions.str_to_float(response)
