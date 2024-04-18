from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EdcCls:
	"""Edc commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edc", core, parent)

	def get_output(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:EDC:OUTPut \n
		Snippet: value: float = driver.configure.rfSettings.edc.get_output() \n
		Defines the value of an external time delay in the output path and in the input path, so that it can be compensated. \n
			:return: time: numeric Range: 0 s to 20E-6 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:EDC:OUTPut?')
		return Conversions.str_to_float(response)

	def set_output(self, time: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:EDC:OUTPut \n
		Snippet: driver.configure.rfSettings.edc.set_output(time = 1.0) \n
		Defines the value of an external time delay in the output path and in the input path, so that it can be compensated. \n
			:param time: numeric Range: 0 s to 20E-6 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:EDC:OUTPut {param}')

	def get_input_py(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:EDC:INPut \n
		Snippet: value: float = driver.configure.rfSettings.edc.get_input_py() \n
		Defines the value of an external time delay in the output path and in the input path, so that it can be compensated. \n
			:return: time: numeric Range: 0 s to 20E-6 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:EDC:INPut?')
		return Conversions.str_to_float(response)

	def set_input_py(self, time: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:EDC:INPut \n
		Snippet: driver.configure.rfSettings.edc.set_input_py(time = 1.0) \n
		Defines the value of an external time delay in the output path and in the input path, so that it can be compensated. \n
			:param time: numeric Range: 0 s to 20E-6 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:EDC:INPut {param}')
