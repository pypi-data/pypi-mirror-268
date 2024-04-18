from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TddCls:
	"""Tdd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdd", core, parent)

	def get_specific(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TDD:SPECific \n
		Snippet: value: bool = driver.configure.cell.tdd.get_specific() \n
		Enables the carrier-specific configuration of the UL/DL configuration and of the special subframe configuration.
			INTRO_CMD_HELP: Rules for valid parameter combinations: \n
			- Enabled: Configuration per carrier via method RsCmwLteSig.Configure.Cell.Pcc.ulDl method RsCmwLteSig.Configure.Cell.Scc.UlDl.set method RsCmwLteSig.Configure.Cell.Pcc.ssubframe method RsCmwLteSig.Configure.Cell.Scc.Ssubframe.set
			- Disabled: Global configuration via method RsCmwLteSig.Configure.Cell.Pcc.ulDl method RsCmwLteSig.Configure.Cell.Pcc.ssubframe \n
			:return: use_specific: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:TDD:SPECific?')
		return Conversions.str_to_bool(response)

	def set_specific(self, use_specific: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TDD:SPECific \n
		Snippet: driver.configure.cell.tdd.set_specific(use_specific = False) \n
		Enables the carrier-specific configuration of the UL/DL configuration and of the special subframe configuration.
			INTRO_CMD_HELP: Rules for valid parameter combinations: \n
			- Enabled: Configuration per carrier via method RsCmwLteSig.Configure.Cell.Pcc.ulDl method RsCmwLteSig.Configure.Cell.Scc.UlDl.set method RsCmwLteSig.Configure.Cell.Pcc.ssubframe method RsCmwLteSig.Configure.Cell.Scc.Ssubframe.set
			- Disabled: Global configuration via method RsCmwLteSig.Configure.Cell.Pcc.ulDl method RsCmwLteSig.Configure.Cell.Pcc.ssubframe \n
			:param use_specific: OFF | ON
		"""
		param = Conversions.bool_to_str(use_specific)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:TDD:SPECific {param}')
