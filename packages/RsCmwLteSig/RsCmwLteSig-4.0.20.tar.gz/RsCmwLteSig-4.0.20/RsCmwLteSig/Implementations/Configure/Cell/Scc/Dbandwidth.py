from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DbandwidthCls:
	"""Dbandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dbandwidth", core, parent)

	def set(self, dedicated_bw: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:DBANdwidth \n
		Snippet: driver.configure.cell.scc.dbandwidth.set(dedicated_bw = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'srs-Bandwidth' value. The setting is only used if manual configuration is enabled, see method RsCmwLteSig.
		Configure.Cell.Pcc.Srs.mcEnable. \n
			:param dedicated_bw: numeric Range: 0 to 3
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(dedicated_bw)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:DBANdwidth {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:DBANdwidth \n
		Snippet: value: int = driver.configure.cell.scc.dbandwidth.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'srs-Bandwidth' value. The setting is only used if manual configuration is enabled, see method RsCmwLteSig.
		Configure.Cell.Pcc.Srs.mcEnable. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: dedicated_bw: numeric Range: 0 to 3"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:DBANdwidth?')
		return Conversions.str_to_int(response)
