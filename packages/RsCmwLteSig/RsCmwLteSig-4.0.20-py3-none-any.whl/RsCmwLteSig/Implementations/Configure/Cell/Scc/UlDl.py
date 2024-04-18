from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UlDlCls:
	"""UlDl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ulDl", core, parent)

	def set(self, uplink_downlink: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:ULDL \n
		Snippet: driver.configure.cell.scc.ulDl.set(uplink_downlink = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a UL-DL configuration, defining the combination of UL, DL and special subframes within a radio frame.
		This command is only relevant for duplex mode TDD. See also method RsCmwLteSig.Configure.Cell.Tdd.specific. \n
			:param uplink_downlink: integer Range: 0 to 6
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(uplink_downlink)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:ULDL {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:ULDL \n
		Snippet: value: int = driver.configure.cell.scc.ulDl.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a UL-DL configuration, defining the combination of UL, DL and special subframes within a radio frame.
		This command is only relevant for duplex mode TDD. See also method RsCmwLteSig.Configure.Cell.Tdd.specific. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: uplink_downlink: integer Range: 0 to 6"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:ULDL?')
		return Conversions.str_to_int(response)
