from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DconfigCls:
	"""Dconfig commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dconfig", core, parent)

	def set(self, dconfiguration: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:SRS:DCONfig \n
		Snippet: driver.configure.cell.scc.srs.dconfig.set(dconfiguration = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects whether the UE-specific SRS parameters are signaled to the UE or not. The setting is only used if manual
		configuration is enabled, see method RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param dconfiguration: OFF | ON OFF: send only cell-specific SRS parameters ON: send also UE-specific SRS parameters
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.bool_to_str(dconfiguration)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SRS:DCONfig {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:SRS:DCONfig \n
		Snippet: value: bool = driver.configure.cell.scc.srs.dconfig.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects whether the UE-specific SRS parameters are signaled to the UE or not. The setting is only used if manual
		configuration is enabled, see method RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: dconfiguration: OFF | ON OFF: send only cell-specific SRS parameters ON: send also UE-specific SRS parameters"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SRS:DCONfig?')
		return Conversions.str_to_bool(response)
