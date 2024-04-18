from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandwidthCls:
	"""Bandwidth commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def get_ratio(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:BWIDth:RATio \n
		Snippet: value: float = driver.configure.fading.pcc.awgn.bandwidth.get_ratio() \n
		Specifies the minimum ratio between the noise bandwidth and the cell bandwidth. \n
			:return: ratio: numeric Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:BWIDth:RATio?')
		return Conversions.str_to_float(response)

	def set_ratio(self, ratio: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:BWIDth:RATio \n
		Snippet: driver.configure.fading.pcc.awgn.bandwidth.set_ratio(ratio = 1.0) \n
		Specifies the minimum ratio between the noise bandwidth and the cell bandwidth. \n
			:param ratio: numeric Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:BWIDth:RATio {param}')

	def get_noise(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:BWIDth:NOISe \n
		Snippet: value: float = driver.configure.fading.pcc.awgn.bandwidth.get_noise() \n
		Queries the noise bandwidth. \n
			:return: noise_bandwidth: float Range: 0 Hz to 80 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:BWIDth:NOISe?')
		return Conversions.str_to_float(response)
