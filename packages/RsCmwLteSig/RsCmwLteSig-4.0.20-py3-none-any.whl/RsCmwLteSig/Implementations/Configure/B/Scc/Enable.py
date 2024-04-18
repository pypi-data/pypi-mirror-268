from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:B:SCC<Carrier>:ENABle \n
		Snippet: driver.configure.b.scc.enable.set(enable = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures whether the SCC<c> belongs to the SCC synchronization set A/B or not. An SCC can only belong to one of the
		sets. Adding it to one set, removes it from the other set (if applicable) . Adding an SCC to a set is only possible, if
		the set and the SCC have the same state (for example 'RRC added') . \n
			:param enable: OFF | ON OFF: The SCC does not belong to the set. ON: The SCC belongs to the set.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.bool_to_str(enable)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:B:SCC{secondaryCompCarrier_cmd_val}:ENABle {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:B:SCC<Carrier>:ENABle \n
		Snippet: value: bool = driver.configure.b.scc.enable.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures whether the SCC<c> belongs to the SCC synchronization set A/B or not. An SCC can only belong to one of the
		sets. Adding it to one set, removes it from the other set (if applicable) . Adding an SCC to a set is only possible, if
		the set and the SCC have the same state (for example 'RRC added') . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: enable: OFF | ON OFF: The SCC does not belong to the set. ON: The SCC belongs to the set."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:B:SCC{secondaryCompCarrier_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
