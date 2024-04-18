from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OlnPowerCls:
	"""OlnPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("olnPower", core, parent)

	def set(self, power: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:OLNPower \n
		Snippet: driver.configure.uplink.scc.pusch.olnPower.set(power = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines a cell-specific nominal power value for full resource block allocation in the UL (entire cell bandwidth used) .
		From this value, the cell-specific nominal power value PO_NOMINAL_PUSCH related to one resource block is determined and
		sent to all UEs via broadcast. This command is only relevant for basic configuration and rejected if advanced
		configuration is active. \n
			:param power: numeric Range: -50 dBm to 23 dBm, Unit: dBm
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(power)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:OLNPower {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:OLNPower \n
		Snippet: value: float = driver.configure.uplink.scc.pusch.olnPower.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines a cell-specific nominal power value for full resource block allocation in the UL (entire cell bandwidth used) .
		From this value, the cell-specific nominal power value PO_NOMINAL_PUSCH related to one resource block is determined and
		sent to all UEs via broadcast. This command is only relevant for basic configuration and rejected if advanced
		configuration is active. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: power: numeric Range: -50 dBm to 23 dBm, Unit: dBm"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:OLNPower?')
		return Conversions.str_to_float(response)
