from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FoffsetCls:
	"""Foffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foffset", core, parent)

	def set(self, level: int, offset: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:PRACh:FOFFset \n
		Snippet: driver.configure.pcc.emtc.ce.level.prach.foffset.set(level = 1, offset = 1) \n
		Sets the frequency offset for the preamble RBs, for a certain CE level. \n
			:param level: integer Selects a CE level Range: 0 to 3
			:param offset: numeric Frequency offset for the selected CE Level Range: 0 to 94
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('level', level, DataType.Integer), ArgSingle('offset', offset, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:PRACh:FOFFset {param}'.rstrip())

	def get(self, level: int) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:PRACh:FOFFset \n
		Snippet: value: int = driver.configure.pcc.emtc.ce.level.prach.foffset.get(level = 1) \n
		Sets the frequency offset for the preamble RBs, for a certain CE level. \n
			:param level: integer Selects a CE level Range: 0 to 3
			:return: offset: numeric Frequency offset for the selected CE Level Range: 0 to 94"""
		param = Conversions.decimal_value_to_str(level)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:PRACh:FOFFset? {param}')
		return Conversions.str_to_int(response)
