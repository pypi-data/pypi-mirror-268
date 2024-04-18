from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ACls:
	"""A commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("a", core, parent)

	# noinspection PyTypeChecker
	def get_ce_repetition(self) -> enums.CeRepetitionsA:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PDSCh:A:CERepetition \n
		Snippet: value: enums.CeRepetitionsA = driver.configure.pcc.emtc.pdsch.a.get_ce_repetition() \n
		Configures the number of PDSCH or PUSCH repetitions for CE mode A. \n
			:return: repetitions: R1 | R2 | R4 | R8 | R16 | R32
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PDSCh:A:CERepetition?')
		return Conversions.str_to_scalar_enum(response, enums.CeRepetitionsA)

	def set_ce_repetition(self, repetitions: enums.CeRepetitionsA) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PDSCh:A:CERepetition \n
		Snippet: driver.configure.pcc.emtc.pdsch.a.set_ce_repetition(repetitions = enums.CeRepetitionsA.R1) \n
		Configures the number of PDSCH or PUSCH repetitions for CE mode A. \n
			:param repetitions: R1 | R2 | R4 | R8 | R16 | R32
		"""
		param = Conversions.enum_scalar_to_str(repetitions, enums.CeRepetitionsA)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PDSCh:A:CERepetition {param}')

	# noinspection PyTypeChecker
	def get_mrce(self) -> enums.MpschArepetitions:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PDSCh:A:MRCE \n
		Snippet: value: enums.MpschArepetitions = driver.configure.pcc.emtc.pdsch.a.get_mrce() \n
		Configures the maximum number of PDSCH or PUSCH repetitions for CE mode A. \n
			:return: max_repetition: NCON | MR16 | MR32 Not configured (omit field) , 16, 32
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PDSCh:A:MRCE?')
		return Conversions.str_to_scalar_enum(response, enums.MpschArepetitions)

	def set_mrce(self, max_repetition: enums.MpschArepetitions) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PDSCh:A:MRCE \n
		Snippet: driver.configure.pcc.emtc.pdsch.a.set_mrce(max_repetition = enums.MpschArepetitions.MR16) \n
		Configures the maximum number of PDSCH or PUSCH repetitions for CE mode A. \n
			:param max_repetition: NCON | MR16 | MR32 Not configured (omit field) , 16, 32
		"""
		param = Conversions.enum_scalar_to_str(max_repetition, enums.MpschArepetitions)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PDSCh:A:MRCE {param}')
