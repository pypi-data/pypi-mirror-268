from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BCls:
	"""B commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("b", core, parent)

	# noinspection PyTypeChecker
	def get_ce_repetition(self) -> enums.CeRepetitionsB:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PUSCh:B:CERepetition \n
		Snippet: value: enums.CeRepetitionsB = driver.configure.pcc.emtc.pusch.b.get_ce_repetition() \n
		Configures the number of PDSCH or PUSCH repetitions for CE mode B. \n
			:return: repetitions: R1 | R4 | R8 | R16 | R32 | R64 | R128 | R192 | R256 | R384 | R512 | R768 | R1024 | R1536 | R2048
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PUSCh:B:CERepetition?')
		return Conversions.str_to_scalar_enum(response, enums.CeRepetitionsB)

	def set_ce_repetition(self, repetitions: enums.CeRepetitionsB) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PUSCh:B:CERepetition \n
		Snippet: driver.configure.pcc.emtc.pusch.b.set_ce_repetition(repetitions = enums.CeRepetitionsB.R1) \n
		Configures the number of PDSCH or PUSCH repetitions for CE mode B. \n
			:param repetitions: R1 | R4 | R8 | R16 | R32 | R64 | R128 | R192 | R256 | R384 | R512 | R768 | R1024 | R1536 | R2048
		"""
		param = Conversions.enum_scalar_to_str(repetitions, enums.CeRepetitionsB)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PUSCh:B:CERepetition {param}')

	# noinspection PyTypeChecker
	def get_mrce(self) -> enums.MpschBrepetitions:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PUSCh:B:MRCE \n
		Snippet: value: enums.MpschBrepetitions = driver.configure.pcc.emtc.pusch.b.get_mrce() \n
		Configures the maximum number of PDSCH or PUSCH repetitions for CE mode B. \n
			:return: max_repetitions: NCON | MR192 | MR256 | MR384 | MR512 | MR768 | MR1024 | MR1536 | MR2048 Not configured (omit field) , 192, 256, ..., 2048
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PUSCh:B:MRCE?')
		return Conversions.str_to_scalar_enum(response, enums.MpschBrepetitions)

	def set_mrce(self, max_repetitions: enums.MpschBrepetitions) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PUSCh:B:MRCE \n
		Snippet: driver.configure.pcc.emtc.pusch.b.set_mrce(max_repetitions = enums.MpschBrepetitions.MR1024) \n
		Configures the maximum number of PDSCH or PUSCH repetitions for CE mode B. \n
			:param max_repetitions: NCON | MR192 | MR256 | MR384 | MR512 | MR768 | MR1024 | MR1536 | MR2048 Not configured (omit field) , 192, 256, ..., 2048
		"""
		param = Conversions.enum_scalar_to_str(max_repetitions, enums.MpschBrepetitions)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PUSCh:B:MRCE {param}')
