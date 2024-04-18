from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UtcCls:
	"""Utc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utc", core, parent)

	def set(self, time_10_ms: int, systemInfoBlock=repcap.SystemInfoBlock.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SIB<n>:TNFO<tnfo>:UTC \n
		Snippet: driver.configure.sib.tnfo.utc.set(time_10_ms = 1, systemInfoBlock = repcap.SystemInfoBlock.Default) \n
		No command help available \n
			:param time_10_ms: No help available
			:param systemInfoBlock: optional repeated capability selector. Default value: Sib8 (settable in the interface 'Sib')
		"""
		param = Conversions.decimal_value_to_str(time_10_ms)
		systemInfoBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(systemInfoBlock, repcap.SystemInfoBlock)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SIB{systemInfoBlock_cmd_val}:TNFO11:UTC {param}')

	def get(self, systemInfoBlock=repcap.SystemInfoBlock.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SIB<n>:TNFO<tnfo>:UTC \n
		Snippet: value: int = driver.configure.sib.tnfo.utc.get(systemInfoBlock = repcap.SystemInfoBlock.Default) \n
		No command help available \n
			:param systemInfoBlock: optional repeated capability selector. Default value: Sib8 (settable in the interface 'Sib')
			:return: time_10_ms: No help available"""
		systemInfoBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(systemInfoBlock, repcap.SystemInfoBlock)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:SIB{systemInfoBlock_cmd_val}:TNFO11:UTC?')
		return Conversions.str_to_int(response)
