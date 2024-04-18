from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HpuschCls:
	"""Hpusch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hpusch", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:HPUSch:ENABle \n
		Snippet: value: bool = driver.configure.connection.pcc.hpusch.get_enable() \n
		Enables inter-subframe PUSCH frequency hopping, type 2. \n
			:return: hopping: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:HPUSch:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, hopping: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:HPUSch:ENABle \n
		Snippet: driver.configure.connection.pcc.hpusch.set_enable(hopping = False) \n
		Enables inter-subframe PUSCH frequency hopping, type 2. \n
			:param hopping: OFF | ON
		"""
		param = Conversions.bool_to_str(hopping)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:HPUSch:ENABle {param}')
