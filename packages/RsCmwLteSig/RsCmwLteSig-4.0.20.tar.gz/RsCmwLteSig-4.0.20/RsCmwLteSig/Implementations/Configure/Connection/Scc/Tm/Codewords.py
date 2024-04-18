from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CodewordsCls:
	"""Codewords commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("codewords", core, parent)

	def set(self, codewords: enums.AntennasTxA, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:CODewords \n
		Snippet: driver.configure.connection.scc.tm.codewords.set(codewords = enums.AntennasTxA.FOUR, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the number of code words for TM 9. \n
			:param codewords: ONE | TWO | FOUR
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(codewords, enums.AntennasTxA)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CODewords {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.AntennasTxA:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:CODewords \n
		Snippet: value: enums.AntennasTxA = driver.configure.connection.scc.tm.codewords.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the number of code words for TM 9. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: codewords: ONE | TWO | FOUR"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CODewords?')
		return Conversions.str_to_scalar_enum(response, enums.AntennasTxA)
