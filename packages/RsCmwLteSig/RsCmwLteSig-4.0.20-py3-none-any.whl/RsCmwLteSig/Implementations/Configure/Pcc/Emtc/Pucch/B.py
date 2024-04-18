from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BCls:
	"""B commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("b", core, parent)

	# noinspection PyTypeChecker
	def get_ce_repetition(self) -> enums.CePucchRepsB:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PUCCh:B:CERepetition \n
		Snippet: value: enums.CePucchRepsB = driver.configure.pcc.emtc.pucch.b.get_ce_repetition() \n
		Configures the number of PUCCH repetitions for CE mode B. \n
			:return: repetitions: R4 | R8 | R16 | R32 | R64 | R128
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PUCCh:B:CERepetition?')
		return Conversions.str_to_scalar_enum(response, enums.CePucchRepsB)

	def set_ce_repetition(self, repetitions: enums.CePucchRepsB) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:PUCCh:B:CERepetition \n
		Snippet: driver.configure.pcc.emtc.pucch.b.set_ce_repetition(repetitions = enums.CePucchRepsB.R128) \n
		Configures the number of PUCCH repetitions for CE mode B. \n
			:param repetitions: R4 | R8 | R16 | R32 | R64 | R128
		"""
		param = Conversions.enum_scalar_to_str(repetitions, enums.CePucchRepsB)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:PUCCh:B:CERepetition {param}')
