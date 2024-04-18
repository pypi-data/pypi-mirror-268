from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PirPowerCls:
	"""PirPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pirPower", core, parent)

	def get_basic(self) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SETC:APPower:PIRPower:BASic \n
		Snippet: value: float = driver.sense.uplink.setc.apPower.pirPower.get_basic() \n
		Queries the 'preambleInitialReceivedTargetPower' value, signaled to the UE if basic UL power configuration applies. \n
			:return: target_power: float Range: -120 dBm to -90 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UL:SETC:APPower:PIRPower:BASic?')
		return Conversions.str_to_float(response)
