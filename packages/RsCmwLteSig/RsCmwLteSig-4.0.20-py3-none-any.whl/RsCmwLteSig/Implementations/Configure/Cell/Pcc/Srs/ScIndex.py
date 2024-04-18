from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScIndexCls:
	"""ScIndex commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scIndex", core, parent)

	def get_fdd(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SRS:SCINdex:FDD \n
		Snippet: value: int = driver.configure.cell.pcc.srs.scIndex.get_fdd() \n
		Specifies the 'srs-ConfigIndex' value for FDD. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:return: index: numeric Range: 0 to 636
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:SCINdex:FDD?')
		return Conversions.str_to_int(response)

	def set_fdd(self, index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SRS:SCINdex:FDD \n
		Snippet: driver.configure.cell.pcc.srs.scIndex.set_fdd(index = 1) \n
		Specifies the 'srs-ConfigIndex' value for FDD. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param index: numeric Range: 0 to 636
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:SCINdex:FDD {param}')

	def get_tdd(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SRS:SCINdex:TDD \n
		Snippet: value: int = driver.configure.cell.pcc.srs.scIndex.get_tdd() \n
		Specifies the 'srs-ConfigIndex' value for TDD. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:return: index: numeric Range: 0 to 644
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:SCINdex:TDD?')
		return Conversions.str_to_int(response)

	def set_tdd(self, index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SRS:SCINdex:TDD \n
		Snippet: driver.configure.cell.pcc.srs.scIndex.set_tdd(index = 1) \n
		Specifies the 'srs-ConfigIndex' value for TDD. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param index: numeric Range: 0 to 644
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:SCINdex:TDD {param}')
