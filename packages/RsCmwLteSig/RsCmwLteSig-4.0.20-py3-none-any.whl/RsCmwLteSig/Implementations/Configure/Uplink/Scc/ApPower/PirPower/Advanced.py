from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AdvancedCls:
	"""Advanced commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("advanced", core, parent)

	def set(self, target_power: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:APPower:PIRPower:ADVanced \n
		Snippet: driver.configure.uplink.scc.apPower.pirPower.advanced.set(target_power = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'preambleInitialReceivedTargetPower' value, signaled to the UE if advanced UL power configuration applies. \n
			:param target_power: numeric Range: -120 dBm to -90 dBm, Unit: dBm
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(target_power)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:APPower:PIRPower:ADVanced {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:APPower:PIRPower:ADVanced \n
		Snippet: value: float = driver.configure.uplink.scc.apPower.pirPower.advanced.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'preambleInitialReceivedTargetPower' value, signaled to the UE if advanced UL power configuration applies. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: target_power: numeric Range: -120 dBm to -90 dBm, Unit: dBm"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:APPower:PIRPower:ADVanced?')
		return Conversions.str_to_float(response)
