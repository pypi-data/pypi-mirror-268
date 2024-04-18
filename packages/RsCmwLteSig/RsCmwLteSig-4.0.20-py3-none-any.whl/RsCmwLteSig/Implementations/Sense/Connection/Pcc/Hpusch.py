from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HpuschCls:
	"""Hpusch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hpusch", core, parent)

	def get_active(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection[:PCC]:HPUSch:ACTive \n
		Snippet: value: bool = driver.sense.connection.pcc.hpusch.get_active() \n
		Queries whether PUSCH frequency hopping is active. \n
			:return: active: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:CONNection:PCC:HPUSch:ACTive?')
		return Conversions.str_to_bool(response)
