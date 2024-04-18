from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubframeCls:
	"""Subframe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subframe", core, parent)

	def set(self, config: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:CSIRs:SUBFrame \n
		Snippet: driver.configure.connection.scc.tm.csirs.subframe.set(config = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the CSI-RS subframe configuration. \n
			:param config: numeric Range: 0 to 154
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(config)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CSIRs:SUBFrame {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:CSIRs:SUBFrame \n
		Snippet: value: int = driver.configure.connection.scc.tm.csirs.subframe.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the CSI-RS subframe configuration. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: config: numeric Range: 0 to 154"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CSIRs:SUBFrame?')
		return Conversions.str_to_int(response)
