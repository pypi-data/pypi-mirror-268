from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfConfigCls:
	"""SfConfig commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfConfig", core, parent)

	def set(self, subframe: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:SRS:SFConfig \n
		Snippet: driver.configure.cell.scc.srs.sfConfig.set(subframe = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'srs-SubframeConfig' value. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param subframe: decimal Range: 0 to 15
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(subframe)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SRS:SFConfig {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:SRS:SFConfig \n
		Snippet: value: int = driver.configure.cell.scc.srs.sfConfig.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'srs-SubframeConfig' value. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: subframe: decimal Range: 0 to 15"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SRS:SFConfig?')
		return Conversions.str_to_int(response)
