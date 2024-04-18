from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PnpuschCls:
	"""Pnpusch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pnpusch", core, parent)

	def get_advanced(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:APPower:PNPusch:ADVanced \n
		Snippet: value: float = driver.configure.uplink.pcc.apPower.pnpusch.get_advanced() \n
		Specifies the 'p0-NominalPUSCH' value, signaled to the UE if advanced UL power configuration applies. \n
			:return: p_0_nominal_pusch: numeric Range: -126 dBm to 24 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:PCC:APPower:PNPusch:ADVanced?')
		return Conversions.str_to_float(response)

	def set_advanced(self, p_0_nominal_pusch: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:APPower:PNPusch:ADVanced \n
		Snippet: driver.configure.uplink.pcc.apPower.pnpusch.set_advanced(p_0_nominal_pusch = 1.0) \n
		Specifies the 'p0-NominalPUSCH' value, signaled to the UE if advanced UL power configuration applies. \n
			:param p_0_nominal_pusch: numeric Range: -126 dBm to 24 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(p_0_nominal_pusch)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:PCC:APPower:PNPusch:ADVanced {param}')
