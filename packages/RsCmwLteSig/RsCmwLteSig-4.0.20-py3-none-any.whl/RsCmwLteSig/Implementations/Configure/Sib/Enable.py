from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, systemInfoBlock=repcap.SystemInfoBlock.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SIB<n>:ENABle \n
		Snippet: driver.configure.sib.enable.set(enable = False, systemInfoBlock = repcap.SystemInfoBlock.Default) \n
		No command help available \n
			:param enable: No help available
			:param systemInfoBlock: optional repeated capability selector. Default value: Sib8 (settable in the interface 'Sib')
		"""
		param = Conversions.bool_to_str(enable)
		systemInfoBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(systemInfoBlock, repcap.SystemInfoBlock)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SIB{systemInfoBlock_cmd_val}:ENABle {param}')

	def get(self, systemInfoBlock=repcap.SystemInfoBlock.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SIB<n>:ENABle \n
		Snippet: value: bool = driver.configure.sib.enable.get(systemInfoBlock = repcap.SystemInfoBlock.Default) \n
		No command help available \n
			:param systemInfoBlock: optional repeated capability selector. Default value: Sib8 (settable in the interface 'Sib')
			:return: enable: No help available"""
		systemInfoBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(systemInfoBlock, repcap.SystemInfoBlock)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:SIB{systemInfoBlock_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
