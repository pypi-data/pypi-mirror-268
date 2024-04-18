from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	def get_maxtx(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:UL:MAXTx \n
		Snippet: value: int = driver.configure.connection.harq.uplink.get_maxtx() \n
		Specifies the signaling parameter 'maxHARQ-Tx'. The setting is only relevant for the scheduling type SPS. \n
			:return: number: numeric Range: 1 to 4
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:UL:MAXTx?')
		return Conversions.str_to_int(response)

	def set_maxtx(self, number: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:UL:MAXTx \n
		Snippet: driver.configure.connection.harq.uplink.set_maxtx(number = 1) \n
		Specifies the signaling parameter 'maxHARQ-Tx'. The setting is only relevant for the scheduling type SPS. \n
			:param number: numeric Range: 1 to 4
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:UL:MAXTx {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:UL:ENABle \n
		Snippet: value: bool = driver.configure.connection.harq.uplink.get_enable() \n
		Enables or disables HARQ for uplink transmissions. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:UL:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:UL:ENABle \n
		Snippet: driver.configure.connection.harq.uplink.set_enable(enable = False) \n
		Enables or disables HARQ for uplink transmissions. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:UL:ENABle {param}')

	def get_nht(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:UL:NHT \n
		Snippet: value: int = driver.configure.connection.harq.uplink.get_nht() \n
		Specifies the maximum number of uplink transmissions, including initial transmissions and retransmissions. \n
			:return: number: numeric Range: 1 to 5
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:UL:NHT?')
		return Conversions.str_to_int(response)

	def set_nht(self, number: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:UL:NHT \n
		Snippet: driver.configure.connection.harq.uplink.set_nht(number = 1) \n
		Specifies the maximum number of uplink transmissions, including initial transmissions and retransmissions. \n
			:param number: numeric Range: 1 to 5
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:UL:NHT {param}')

	# noinspection PyTypeChecker
	def get_dphich(self) -> enums.UlHarqMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:UL:DPHich \n
		Snippet: value: enums.UlHarqMode = driver.configure.connection.harq.uplink.get_dphich() \n
		Selects how the UE is informed about required UL retransmissions / successful UL transmissions, for UL HARQ. \n
			:return: mode: D0ONly | PHIChonly | D0PHich | PNACk | PND0 D0ONly DCI-0 only, normal operation PHIChonly PHICH only, normal operation D0PHich DCI-0 & PHICH, normal operation PNACk PHICH NACK, always retransmission PND0 PHICH NACK & DCI-0, always retransmission
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:UL:DPHich?')
		return Conversions.str_to_scalar_enum(response, enums.UlHarqMode)

	def set_dphich(self, mode: enums.UlHarqMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:UL:DPHich \n
		Snippet: driver.configure.connection.harq.uplink.set_dphich(mode = enums.UlHarqMode.D0ONly) \n
		Selects how the UE is informed about required UL retransmissions / successful UL transmissions, for UL HARQ. \n
			:param mode: D0ONly | PHIChonly | D0PHich | PNACk | PND0 D0ONly DCI-0 only, normal operation PHIChonly PHICH only, normal operation D0PHich DCI-0 & PHICH, normal operation PNACk PHICH NACK, always retransmission PND0 PHICH NACK & DCI-0, always retransmission
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.UlHarqMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:UL:DPHich {param}')
