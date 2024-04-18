from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PccCls:
	"""Pcc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcc", core, parent)

	def get_fc_power(self) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:DL[:PCC]:FCPower \n
		Snippet: value: float = driver.sense.downlink.pcc.get_fc_power() \n
		Queries the 'Full Cell BW Power'. The power results from the configured RS EPRE and the cell bandwidth. \n
			:return: level: float Range: -220 dBm to 48 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:DL:PCC:FCPower?')
		return Conversions.str_to_float(response)
