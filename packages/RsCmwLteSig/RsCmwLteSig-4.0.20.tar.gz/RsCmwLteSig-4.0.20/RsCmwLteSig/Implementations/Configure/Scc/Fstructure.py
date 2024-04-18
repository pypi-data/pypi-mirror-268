from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FstructureCls:
	"""Fstructure commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fstructure", core, parent)

	def set(self, structure: enums.FrameStructure, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC<Carrier>:FSTRucture \n
		Snippet: driver.configure.scc.fstructure.set(structure = enums.FrameStructure.T1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		The frame structure is only configurable for the TDD user-defined band. In any other case, only the query is relevant. \n
			:param structure: T1 | T2 | T3 T1: Type 1 - FDD T2: Type 2 - TDD normal operation T3: Type 3 - LAA operation mode
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(structure, enums.FrameStructure)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:FSTRucture {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.FrameStructure:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC<Carrier>:FSTRucture \n
		Snippet: value: enums.FrameStructure = driver.configure.scc.fstructure.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		The frame structure is only configurable for the TDD user-defined band. In any other case, only the query is relevant. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: T1 | T2 | T3 T1: Type 1 - FDD T2: Type 2 - TDD normal operation T3: Type 3 - LAA operation mode"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:FSTRucture?')
		return Conversions.str_to_scalar_enum(response, enums.FrameStructure)
