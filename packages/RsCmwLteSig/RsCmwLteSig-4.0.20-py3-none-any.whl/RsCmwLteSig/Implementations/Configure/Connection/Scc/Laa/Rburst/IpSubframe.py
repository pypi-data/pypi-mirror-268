from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpSubframeCls:
	"""IpSubframe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipSubframe", core, parent)

	def set(self, enable: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:RBURst:IPSubframe \n
		Snippet: driver.configure.connection.scc.laa.rburst.ipSubframe.set(enable = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Allows or forbids partial allocation for initial subframes, for LAA with random bursts. \n
			:param enable: OFF | ON ON: initial partial subframes allowed OFF: only full allocation in initial subframes
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.bool_to_str(enable)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:RBURst:IPSubframe {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:RBURst:IPSubframe \n
		Snippet: value: bool = driver.configure.connection.scc.laa.rburst.ipSubframe.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Allows or forbids partial allocation for initial subframes, for LAA with random bursts. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: enable: OFF | ON ON: initial partial subframes allowed OFF: only full allocation in initial subframes"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:RBURst:IPSubframe?')
		return Conversions.str_to_bool(response)
