from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, level: int, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:ENABle \n
		Snippet: driver.configure.pcc.emtc.ce.level.enable.set(level = 1, enable = False) \n
		Selects whether the eNodeB supports a certain CE level. If you disable a CE level, the higher CE levels are disabled
		automatically. You can enable a CE level only if all lower CE levels are enabled. \n
			:param level: integer Selects a CE level Range: 1 to 3
			:param enable: OFF | ON Disables or enables the selected CE Level
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('level', level, DataType.Integer), ArgSingle('enable', enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:ENABle {param}'.rstrip())

	def get(self, level: int) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:ENABle \n
		Snippet: value: bool = driver.configure.pcc.emtc.ce.level.enable.get(level = 1) \n
		Selects whether the eNodeB supports a certain CE level. If you disable a CE level, the higher CE levels are disabled
		automatically. You can enable a CE level only if all lower CE levels are enabled. \n
			:param level: integer Selects a CE level Range: 1 to 3
			:return: enable: OFF | ON Disables or enables the selected CE Level"""
		param = Conversions.decimal_value_to_str(level)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:ENABle? {param}')
		return Conversions.str_to_bool(response)
