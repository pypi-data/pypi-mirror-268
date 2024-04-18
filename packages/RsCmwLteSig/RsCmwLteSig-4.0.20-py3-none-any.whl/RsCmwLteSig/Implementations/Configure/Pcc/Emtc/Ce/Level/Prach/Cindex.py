from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CindexCls:
	"""Cindex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cindex", core, parent)

	def set(self, level: int, index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:PRACh:CINDex \n
		Snippet: driver.configure.pcc.emtc.ce.level.prach.cindex.set(level = 1, index = 1) \n
		Sets the PRACH configuration index for a certain CE level. \n
			:param level: integer Selects a CE level Range: 0 to 3
			:param index: numeric PRACH configuration index for the selected CE Level Range: 0 to 63
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('level', level, DataType.Integer), ArgSingle('index', index, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:PRACh:CINDex {param}'.rstrip())

	def get(self, level: int) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:PRACh:CINDex \n
		Snippet: value: int = driver.configure.pcc.emtc.ce.level.prach.cindex.get(level = 1) \n
		Sets the PRACH configuration index for a certain CE level. \n
			:param level: integer Selects a CE level Range: 0 to 3
			:return: index: numeric PRACH configuration index for the selected CE Level Range: 0 to 63"""
		param = Conversions.decimal_value_to_str(level)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:PRACh:CINDex? {param}')
		return Conversions.str_to_int(response)
