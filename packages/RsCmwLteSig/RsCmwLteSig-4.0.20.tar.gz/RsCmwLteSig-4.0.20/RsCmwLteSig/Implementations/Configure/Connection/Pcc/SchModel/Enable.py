from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def get_mimo(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SCHModel:ENABle:MIMO<Mimo> \n
		Snippet: value: bool = driver.configure.connection.pcc.schModel.enable.get_mimo() \n
		Enables or disables the MIMO 4x4 static channel matrix. Disabling the channel matrix results in an ideal radio channel
		without any coupling between the downlink signals. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SCHModel:ENABle:MIMO44?')
		return Conversions.str_to_bool(response)

	def set_mimo(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SCHModel:ENABle:MIMO<Mimo> \n
		Snippet: driver.configure.connection.pcc.schModel.enable.set_mimo(enable = False) \n
		Enables or disables the MIMO 4x4 static channel matrix. Disabling the channel matrix results in an ideal radio channel
		without any coupling between the downlink signals. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SCHModel:ENABle:MIMO44 {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SCHModel:ENABle \n
		Snippet: value: bool = driver.configure.connection.pcc.schModel.enable.get_value() \n
		Enables or disables the MIMO 2x2 static channel matrix. Disabling the channel matrix results in an ideal radio channel
		without any coupling between the downlink signals. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SCHModel:ENABle?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SCHModel:ENABle \n
		Snippet: driver.configure.connection.pcc.schModel.enable.set_value(enable = False) \n
		Enables or disables the MIMO 2x2 static channel matrix. Disabling the channel matrix results in an ideal radio channel
		without any coupling between the downlink signals. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SCHModel:ENABle {param}')
