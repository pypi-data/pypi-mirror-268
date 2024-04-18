from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TprrcSetupCls:
	"""TprrcSetup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tprrcSetup", core, parent)

	def get_advanced(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:APPower:TPRRcsetup:ADVanced \n
		Snippet: value: bool = driver.configure.uplink.pcc.apPower.tprrcSetup.get_advanced() \n
		Enables or disables P0-UE-PUSCH toggling and thus determines the P0-UE-PUSCH values signaled to the UE during RRC
		connection setup if advanced UL power configuration applies. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:PCC:APPower:TPRRcsetup:ADVanced?')
		return Conversions.str_to_bool(response)

	def set_advanced(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:APPower:TPRRcsetup:ADVanced \n
		Snippet: driver.configure.uplink.pcc.apPower.tprrcSetup.set_advanced(enable = False) \n
		Enables or disables P0-UE-PUSCH toggling and thus determines the P0-UE-PUSCH values signaled to the UE during RRC
		connection setup if advanced UL power configuration applies. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:PCC:APPower:TPRRcsetup:ADVanced {param}')
