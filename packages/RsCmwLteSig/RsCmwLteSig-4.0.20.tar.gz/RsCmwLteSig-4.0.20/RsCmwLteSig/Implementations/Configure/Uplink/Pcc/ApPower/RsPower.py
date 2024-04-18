from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsPowerCls:
	"""RsPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsPower", core, parent)

	def get_advanced(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:APPower:RSPower:ADVanced \n
		Snippet: value: float = driver.configure.uplink.pcc.apPower.rsPower.get_advanced() \n
		Specifies the 'referenceSignalPower' value, signaled to the UE if advanced UL power configuration applies. \n
			:return: ref_signal_power: numeric Range: -60 dBm to 50 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:PCC:APPower:RSPower:ADVanced?')
		return Conversions.str_to_float(response)

	def set_advanced(self, ref_signal_power: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:APPower:RSPower:ADVanced \n
		Snippet: driver.configure.uplink.pcc.apPower.rsPower.set_advanced(ref_signal_power = 1.0) \n
		Specifies the 'referenceSignalPower' value, signaled to the UE if advanced UL power configuration applies. \n
			:param ref_signal_power: numeric Range: -60 dBm to 50 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(ref_signal_power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:PCC:APPower:RSPower:ADVanced {param}')
