from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BypassCls:
	"""Bypass commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bypass", core, parent)

	def get_state(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:BYPass:STATe \n
		Snippet: value: bool = driver.configure.fading.pcc.fadingSimulator.bypass.get_state() \n
		No command help available \n
			:return: bypass: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:BYPass:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, bypass: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:BYPass:STATe \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.bypass.set_state(bypass = False) \n
		No command help available \n
			:param bypass: No help available
		"""
		param = Conversions.bool_to_str(bypass)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:BYPass:STATe {param}')
