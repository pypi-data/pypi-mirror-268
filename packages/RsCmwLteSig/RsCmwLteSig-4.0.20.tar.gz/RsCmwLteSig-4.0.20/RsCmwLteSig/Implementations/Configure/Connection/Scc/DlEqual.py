from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DlEqualCls:
	"""DlEqual commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlEqual", core, parent)

	def set(self, enable: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:DLEQual \n
		Snippet: driver.configure.connection.scc.dlEqual.set(enable = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables or disables the coupling of all MIMO downlink streams. When you switch on the coupling, the settings for DL
		stream 1 are applied to all DL streams. With enabled coupling, commands of the format CONFigure:...:DL<s>... configure
		all DL streams at once, independent of the specified <s>. With disabled coupling, such commands configure a single
		selected DL stream <s>. However, some settings are never configurable per stream and are always coupled. \n
			:param enable: OFF | ON
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.bool_to_str(enable)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:DLEQual {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:DLEQual \n
		Snippet: value: bool = driver.configure.connection.scc.dlEqual.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables or disables the coupling of all MIMO downlink streams. When you switch on the coupling, the settings for DL
		stream 1 are applied to all DL streams. With enabled coupling, commands of the format CONFigure:...:DL<s>... configure
		all DL streams at once, independent of the specified <s>. With disabled coupling, such commands configure a single
		selected DL stream <s>. However, some settings are never configurable per stream and are always coupled. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: enable: OFF | ON"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:DLEQual?')
		return Conversions.str_to_bool(response)
