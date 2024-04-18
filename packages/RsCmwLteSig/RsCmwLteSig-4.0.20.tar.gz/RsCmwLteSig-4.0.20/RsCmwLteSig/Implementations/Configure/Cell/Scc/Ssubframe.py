from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsubframeCls:
	"""Ssubframe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssubframe", core, parent)

	def set(self, special_subframe: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:SSUBframe \n
		Snippet: driver.configure.cell.scc.ssubframe.set(special_subframe = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a special subframe configuration, defining the inner structure of special subframes. This parameter is only
		relevant for TDD signals. The special subframe configurations are defined in 3GPP TS 36.211, chapter 4, 'Frame Structure'.
		See also method RsCmwLteSig.Configure.Cell.Tdd.specific. \n
			:param special_subframe: integer Value 8 and 9 can only be used with normal cyclic prefix. Range: 0 to 9
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(special_subframe)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SSUBframe {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:SSUBframe \n
		Snippet: value: int = driver.configure.cell.scc.ssubframe.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a special subframe configuration, defining the inner structure of special subframes. This parameter is only
		relevant for TDD signals. The special subframe configurations are defined in 3GPP TS 36.211, chapter 4, 'Frame Structure'.
		See also method RsCmwLteSig.Configure.Cell.Tdd.specific. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: special_subframe: integer Value 8 and 9 can only be used with normal cyclic prefix. Range: 0 to 9"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SSUBframe?')
		return Conversions.str_to_int(response)
