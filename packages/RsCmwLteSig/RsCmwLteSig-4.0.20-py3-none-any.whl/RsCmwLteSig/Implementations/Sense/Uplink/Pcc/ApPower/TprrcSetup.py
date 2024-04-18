from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TprrcSetupCls:
	"""TprrcSetup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tprrcSetup", core, parent)

	def get_basic(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL[:PCC]:APPower:TPRRcsetup:BASic \n
		Snippet: value: bool = driver.sense.uplink.pcc.apPower.tprrcSetup.get_basic() \n
		Queries the state of P0-UE-PUSCH toggling, determining the P0-UE-PUSCH values signaled to the UE during RRC connection
		setup if basic UL power configuration applies. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UL:PCC:APPower:TPRRcsetup:BASic?')
		return Conversions.str_to_bool(response)
