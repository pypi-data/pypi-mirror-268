from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmodeCls:
	"""Dmode commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmode", core, parent)

	def get_uc_specific(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:DMODe:UCSPecific \n
		Snippet: value: bool = driver.configure.pcc.dmode.get_uc_specific() \n
			INTRO_CMD_HELP: Enables the carrier-specific duplex mode configuration. \n
			- Enabled - The duplex mode is configured per carrier via: method RsCmwLteSig.Configure.Pcc.Dmode.value method RsCmwLteSig.Configure.Scc.Dmode.set
			- Disabled - All carriers have the same duplex mode, configured via: method RsCmwLteSig.Configure.Pcc.Dmode.value \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:PCC:DMODe:UCSPecific?')
		return Conversions.str_to_bool(response)

	def set_uc_specific(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:DMODe:UCSPecific \n
		Snippet: driver.configure.pcc.dmode.set_uc_specific(enable = False) \n
			INTRO_CMD_HELP: Enables the carrier-specific duplex mode configuration. \n
			- Enabled - The duplex mode is configured per carrier via: method RsCmwLteSig.Configure.Pcc.Dmode.value method RsCmwLteSig.Configure.Scc.Dmode.set
			- Disabled - All carriers have the same duplex mode, configured via: method RsCmwLteSig.Configure.Pcc.Dmode.value \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:PCC:DMODe:UCSPecific {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.DuplexMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:DMODe \n
		Snippet: value: enums.DuplexMode = driver.configure.pcc.dmode.get_value() \n
		Selects the duplex mode of the LTE signal: FDD or TDD. See also method RsCmwLteSig.Configure.Pcc.Dmode.ucSpecific. \n
			:return: mode: FDD | TDD
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.DuplexMode)

	def set_value(self, mode: enums.DuplexMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:DMODe \n
		Snippet: driver.configure.pcc.dmode.set_value(mode = enums.DuplexMode.FDD) \n
		Selects the duplex mode of the LTE signal: FDD or TDD. See also method RsCmwLteSig.Configure.Pcc.Dmode.ucSpecific. \n
			:param mode: FDD | TDD
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DuplexMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:DMODe {param}')
