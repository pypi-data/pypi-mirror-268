from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmcsCls:
	"""Cmcs commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmcs", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RAR:CMCS:ENABle \n
		Snippet: value: bool = driver.configure.cell.rar.cmcs.get_enable() \n
		Enables the custom MCS index definition for RAR messages. \n
			:return: enable: OFF | ON OFF: MCS index selected automatically ON: MCS index set to configured custom value
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:RAR:CMCS:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RAR:CMCS:ENABle \n
		Snippet: driver.configure.cell.rar.cmcs.set_enable(enable = False) \n
		Enables the custom MCS index definition for RAR messages. \n
			:param enable: OFF | ON OFF: MCS index selected automatically ON: MCS index set to configured custom value
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:RAR:CMCS:ENABle {param}')

	def get_value(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RAR:CMCS \n
		Snippet: value: int = driver.configure.cell.rar.cmcs.get_value() \n
		Configures a custom MCS index for RAR messages. \n
			:return: custom_mcs: numeric Range: 0 to 13
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:RAR:CMCS?')
		return Conversions.str_to_int(response)

	def set_value(self, custom_mcs: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RAR:CMCS \n
		Snippet: driver.configure.cell.rar.cmcs.set_value(custom_mcs = 1) \n
		Configures a custom MCS index for RAR messages. \n
			:param custom_mcs: numeric Range: 0 to 13
		"""
		param = Conversions.decimal_value_to_str(custom_mcs)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:RAR:CMCS {param}')
