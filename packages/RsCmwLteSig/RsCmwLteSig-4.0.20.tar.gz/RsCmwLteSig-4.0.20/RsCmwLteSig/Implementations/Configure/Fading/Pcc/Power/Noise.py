from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoiseCls:
	"""Noise commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noise", core, parent)

	def get_total(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:POWer:NOISe:TOTal \n
		Snippet: value: float = driver.configure.fading.pcc.power.noise.get_total() \n
		Queries the total noise power for one carrier. \n
			:return: noise_power: float Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:POWer:NOISe:TOTal?')
		return Conversions.str_to_float(response)

	def get_value(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:POWer:NOISe \n
		Snippet: value: float = driver.configure.fading.pcc.power.noise.get_value() \n
		Queries the calculated noise power on the DL channel, i.e. within the cell bandwidth. \n
			:return: noise_power: float Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:POWer:NOISe?')
		return Conversions.str_to_float(response)
