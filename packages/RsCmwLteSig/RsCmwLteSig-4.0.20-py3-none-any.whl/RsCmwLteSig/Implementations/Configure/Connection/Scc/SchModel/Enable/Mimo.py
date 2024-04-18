from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	def set(self, enable: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:SCHModel:ENABle:MIMO<Mimo> \n
		Snippet: driver.configure.connection.scc.schModel.enable.mimo.set(enable = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables or disables the MIMO 4x4 static channel matrix. Disabling the channel matrix results in an ideal radio channel
		without any coupling between the downlink signals. \n
			:param enable: OFF | ON
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.bool_to_str(enable)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:SCHModel:ENABle:MIMO44 {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:SCHModel:ENABle:MIMO<Mimo> \n
		Snippet: value: bool = driver.configure.connection.scc.schModel.enable.mimo.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables or disables the MIMO 4x4 static channel matrix. Disabling the channel matrix results in an ideal radio channel
		without any coupling between the downlink signals. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: enable: OFF | ON"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:SCHModel:ENABle:MIMO44?')
		return Conversions.str_to_bool(response)
