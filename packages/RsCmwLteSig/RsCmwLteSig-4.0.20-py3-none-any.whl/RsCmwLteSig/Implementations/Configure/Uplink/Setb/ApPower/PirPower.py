from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PirPowerCls:
	"""PirPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pirPower", core, parent)

	def get_advanced(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETB:APPower:PIRPower:ADVanced \n
		Snippet: value: float = driver.configure.uplink.setb.apPower.pirPower.get_advanced() \n
		Specifies the 'preambleInitialReceivedTargetPower' value, signaled to the UE if advanced UL power configuration applies. \n
			:return: target_power: numeric Range: -120 dBm to -90 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETB:APPower:PIRPower:ADVanced?')
		return Conversions.str_to_float(response)

	def set_advanced(self, target_power: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETB:APPower:PIRPower:ADVanced \n
		Snippet: driver.configure.uplink.setb.apPower.pirPower.set_advanced(target_power = 1.0) \n
		Specifies the 'preambleInitialReceivedTargetPower' value, signaled to the UE if advanced UL power configuration applies. \n
			:param target_power: numeric Range: -120 dBm to -90 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(target_power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETB:APPower:PIRPower:ADVanced {param}')
