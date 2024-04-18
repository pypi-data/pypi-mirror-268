from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EaSettingsCls:
	"""EaSettings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eaSettings", core, parent)

	def set(self, enable: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:APPower:EASettings \n
		Snippet: driver.configure.uplink.scc.apPower.eaSettings.set(enable = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables or disables advanced configuration of the PRACH and open loop power settings via the other
		CONFigure:LTE:SIGN:UL:PCC/SCC<c>:APPower:... commands. \n
			:param enable: OFF | ON
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.bool_to_str(enable)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:APPower:EASettings {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:APPower:EASettings \n
		Snippet: value: bool = driver.configure.uplink.scc.apPower.eaSettings.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables or disables advanced configuration of the PRACH and open loop power settings via the other
		CONFigure:LTE:SIGN:UL:PCC/SCC<c>:APPower:... commands. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: enable: OFF | ON"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:APPower:EASettings?')
		return Conversions.str_to_bool(response)
