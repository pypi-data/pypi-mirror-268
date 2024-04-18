from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MmrRepetitionCls:
	"""MmrRepetition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mmrRepetition", core, parent)

	def set(self, level: int, max_repetitions: enums.MprachRepetitions) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:PRACh:MMRRepetitio \n
		Snippet: driver.configure.pcc.emtc.ce.level.prach.mmrRepetition.set(level = 1, max_repetitions = enums.MprachRepetitions.R1) \n
		Specifies the maximum number of MPDCCH repetitions for the random access response, for a certain CE level. \n
			:param level: integer Selects a CE level Range: 0 to 3
			:param max_repetitions: R1 | R2 | R4 | R8 | R16 | R32 | R64 | R128 | R256 Maximum repetitions for the selected CE Level
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('level', level, DataType.Integer), ArgSingle('max_repetitions', max_repetitions, DataType.Enum, enums.MprachRepetitions))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:PRACh:MMRRepetitio {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, level: int) -> enums.MprachRepetitions:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:PRACh:MMRRepetitio \n
		Snippet: value: enums.MprachRepetitions = driver.configure.pcc.emtc.ce.level.prach.mmrRepetition.get(level = 1) \n
		Specifies the maximum number of MPDCCH repetitions for the random access response, for a certain CE level. \n
			:param level: integer Selects a CE level Range: 0 to 3
			:return: max_repetitions: R1 | R2 | R4 | R8 | R16 | R32 | R64 | R128 | R256 Maximum repetitions for the selected CE Level"""
		param = Conversions.decimal_value_to_str(level)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:PRACh:MMRRepetitio? {param}')
		return Conversions.str_to_scalar_enum(response, enums.MprachRepetitions)
