from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PcIndexCls:
	"""PcIndex commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcIndex", core, parent)

	def get_fdd(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:PCINdex:FDD \n
		Snippet: value: int = driver.configure.cell.prach.pcIndex.get_fdd() \n
		Selects the PRACH configuration index for FDD. \n
			:return: prach_conf_index: numeric Range: 0 to 63
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:PCINdex:FDD?')
		return Conversions.str_to_int(response)

	def set_fdd(self, prach_conf_index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:PCINdex:FDD \n
		Snippet: driver.configure.cell.prach.pcIndex.set_fdd(prach_conf_index = 1) \n
		Selects the PRACH configuration index for FDD. \n
			:param prach_conf_index: numeric Range: 0 to 63
		"""
		param = Conversions.decimal_value_to_str(prach_conf_index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:PCINdex:FDD {param}')

	def get_tdd(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:PCINdex:TDD \n
		Snippet: value: int = driver.configure.cell.prach.pcIndex.get_tdd() \n
		Selects the PRACH configuration index for TDD. \n
			:return: prach_conf_index: numeric Range: depends on UL-DL configuration, see tables below
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:PCINdex:TDD?')
		return Conversions.str_to_int(response)

	def set_tdd(self, prach_conf_index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:PCINdex:TDD \n
		Snippet: driver.configure.cell.prach.pcIndex.set_tdd(prach_conf_index = 1) \n
		Selects the PRACH configuration index for TDD. \n
			:param prach_conf_index: numeric Range: depends on UL-DL configuration, see tables below
		"""
		param = Conversions.decimal_value_to_str(prach_conf_index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:PCINdex:TDD {param}')
