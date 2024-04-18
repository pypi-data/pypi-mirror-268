from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ACls:
	"""A commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("a", core, parent)

	# noinspection PyTypeChecker
	def get_ce_repetition(self) -> enums.CePucchRepsA:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PUCCh:A:CERepetition \n
		Snippet: value: enums.CePucchRepsA = driver.configure.pcc.emtc.pucch.a.get_ce_repetition() \n
		Configures the number of PUCCH repetitions for CE mode A. \n
			:return: repetitions: R1 | R2 | R4 | R8
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PUCCh:A:CERepetition?')
		return Conversions.str_to_scalar_enum(response, enums.CePucchRepsA)

	def set_ce_repetition(self, repetitions: enums.CePucchRepsA) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PUCCh:A:CERepetition \n
		Snippet: driver.configure.pcc.emtc.pucch.a.set_ce_repetition(repetitions = enums.CePucchRepsA.R1) \n
		Configures the number of PUCCH repetitions for CE mode A. \n
			:param repetitions: R1 | R2 | R4 | R8
		"""
		param = Conversions.enum_scalar_to_str(repetitions, enums.CePucchRepsA)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PUCCh:A:CERepetition {param}')
