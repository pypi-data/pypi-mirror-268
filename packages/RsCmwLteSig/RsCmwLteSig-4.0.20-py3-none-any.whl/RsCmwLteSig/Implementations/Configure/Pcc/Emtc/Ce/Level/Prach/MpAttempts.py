from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MpAttemptsCls:
	"""MpAttempts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mpAttempts", core, parent)

	def set(self, level: int, attempts: enums.TransmitAttempts) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:PRACh:MPATtempts \n
		Snippet: driver.configure.pcc.emtc.ce.level.prach.mpAttempts.set(level = 1, attempts = enums.TransmitAttempts.A10) \n
		Specifies the maximum number of preamble transmission attempts for a certain CE level. \n
			:param level: integer Selects a CE level Range: 0 to 3
			:param attempts: A3 | A4 | A5 | A6 | A7 | A8 | A10 Maximum attempts for the selected CE Level
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('level', level, DataType.Integer), ArgSingle('attempts', attempts, DataType.Enum, enums.TransmitAttempts))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:PRACh:MPATtempts {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, level: int) -> enums.TransmitAttempts:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:PRACh:MPATtempts \n
		Snippet: value: enums.TransmitAttempts = driver.configure.pcc.emtc.ce.level.prach.mpAttempts.get(level = 1) \n
		Specifies the maximum number of preamble transmission attempts for a certain CE level. \n
			:param level: integer Selects a CE level Range: 0 to 3
			:return: attempts: A3 | A4 | A5 | A6 | A7 | A8 | A10 Maximum attempts for the selected CE Level"""
		param = Conversions.decimal_value_to_str(level)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:PRACh:MPATtempts? {param}')
		return Conversions.str_to_scalar_enum(response, enums.TransmitAttempts)
