from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsirsCls:
	"""Csirs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csirs", core, parent)

	def get_subframe(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:ZP:CSIRs:SUBFrame \n
		Snippet: value: int = driver.configure.connection.pcc.tm.zp.csirs.get_subframe() \n
		Selects the zero power CSI-RS subframe configuration. \n
			:return: config: numeric Range: 0 to 154
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:ZP:CSIRs:SUBFrame?')
		return Conversions.str_to_int(response)

	def set_subframe(self, config: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:ZP:CSIRs:SUBFrame \n
		Snippet: driver.configure.connection.pcc.tm.zp.csirs.set_subframe(config = 1) \n
		Selects the zero power CSI-RS subframe configuration. \n
			:param config: numeric Range: 0 to 154
		"""
		param = Conversions.decimal_value_to_str(config)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:ZP:CSIRs:SUBFrame {param}')
