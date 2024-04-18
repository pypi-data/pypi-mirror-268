from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PucchCls:
	"""Pucch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pucch", core, parent)

	def get_clt_power(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETA:PUCCh:CLTPower \n
		Snippet: value: int = driver.configure.uplink.seta.pucch.get_clt_power() \n
		No command help available \n
			:return: power: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETA:PUCCh:CLTPower?')
		return Conversions.str_to_int(response)

	def set_clt_power(self, power: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETA:PUCCh:CLTPower \n
		Snippet: driver.configure.uplink.seta.pucch.set_clt_power(power = 1) \n
		No command help available \n
			:param power: No help available
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETA:PUCCh:CLTPower {param}')
