from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RpAttemptCls:
	"""RpAttempt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpAttempt", core, parent)

	def set(self, level: int, repetitions: enums.PreambleTransmReps) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:PRACh:RPATtempt \n
		Snippet: driver.configure.pcc.emtc.ce.level.prach.rpAttempt.set(level = 1, repetitions = enums.PreambleTransmReps.R1) \n
		Specifies the number of repetitions per preamble transmission attempt, for a certain CE level. \n
			:param level: integer Selects a CE level Range: 0 to 3
			:param repetitions: R1 | R2 | R4 | R8 | R16 | R32 | R64 | R128 Maximum repetitions for the selected CE Level
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('level', level, DataType.Integer), ArgSingle('repetitions', repetitions, DataType.Enum, enums.PreambleTransmReps))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:PRACh:RPATtempt {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, level: int) -> enums.PreambleTransmReps:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:PRACh:RPATtempt \n
		Snippet: value: enums.PreambleTransmReps = driver.configure.pcc.emtc.ce.level.prach.rpAttempt.get(level = 1) \n
		Specifies the number of repetitions per preamble transmission attempt, for a certain CE level. \n
			:param level: integer Selects a CE level Range: 0 to 3
			:return: repetitions: R1 | R2 | R4 | R8 | R16 | R32 | R64 | R128 Maximum repetitions for the selected CE Level"""
		param = Conversions.decimal_value_to_str(level)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:PRACh:RPATtempt? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PreambleTransmReps)
