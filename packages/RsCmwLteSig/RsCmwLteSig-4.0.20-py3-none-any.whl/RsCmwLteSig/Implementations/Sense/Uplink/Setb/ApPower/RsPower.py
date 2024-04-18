from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsPowerCls:
	"""RsPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsPower", core, parent)

	def get_basic(self) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SETB:APPower:RSPower:BASic \n
		Snippet: value: float = driver.sense.uplink.setb.apPower.rsPower.get_basic() \n
		Queries the 'referenceSignalPower' value, signaled to the UE if basic UL power configuration applies. \n
			:return: ref_signal_power: float Range: -60 dBm to 50 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UL:SETB:APPower:RSPower:BASic?')
		return Conversions.str_to_float(response)
