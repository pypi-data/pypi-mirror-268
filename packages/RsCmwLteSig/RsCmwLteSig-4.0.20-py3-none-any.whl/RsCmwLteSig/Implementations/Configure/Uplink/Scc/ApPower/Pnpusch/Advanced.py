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

	def set(self, p_0_nominal_pusch: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:APPower:PNPusch:ADVanced \n
		Snippet: driver.configure.uplink.scc.apPower.pnpusch.advanced.set(p_0_nominal_pusch = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'p0-NominalPUSCH' value, signaled to the UE if advanced UL power configuration applies. \n
			:param p_0_nominal_pusch: numeric Range: -126 dBm to 24 dBm, Unit: dBm
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(p_0_nominal_pusch)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:APPower:PNPusch:ADVanced {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:APPower:PNPusch:ADVanced \n
		Snippet: value: float = driver.configure.uplink.scc.apPower.pnpusch.advanced.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'p0-NominalPUSCH' value, signaled to the UE if advanced UL power configuration applies. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: p_0_nominal_pusch: numeric Range: -126 dBm to 24 dBm, Unit: dBm"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:APPower:PNPusch:ADVanced?')
		return Conversions.str_to_float(response)
