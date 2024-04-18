from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	def get_uc_specific(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:FOFFset:UL:UCSPecific \n
		Snippet: value: bool = driver.configure.rfSettings.pcc.foffset.uplink.get_uc_specific() \n
		Enables or disables the usage of different frequency offset values for the individual downlink or uplink component
		carriers. \n
			:return: enable: OFF | ON OFF: The configured PCC offset is also used for the SCCs. The configured SCC offsets have no effect. ON: You can configure the frequency offset per carrier.
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:FOFFset:UL:UCSPecific?')
		return Conversions.str_to_bool(response)

	def set_uc_specific(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:FOFFset:UL:UCSPecific \n
		Snippet: driver.configure.rfSettings.pcc.foffset.uplink.set_uc_specific(enable = False) \n
		Enables or disables the usage of different frequency offset values for the individual downlink or uplink component
		carriers. \n
			:param enable: OFF | ON OFF: The configured PCC offset is also used for the SCCs. The configured SCC offsets have no effect. ON: You can configure the frequency offset per carrier.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:FOFFset:UL:UCSPecific {param}')

	def get_value(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:FOFFset:UL \n
		Snippet: value: int = driver.configure.rfSettings.pcc.foffset.uplink.get_value() \n
		Specifies a positive or negative frequency offset to be added to the center frequency of the configured uplink channel. \n
			:return: offset: numeric Range: -100 kHz to 100 kHz, Unit: Hz
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:FOFFset:UL?')
		return Conversions.str_to_int(response)

	def set_value(self, offset: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:FOFFset:UL \n
		Snippet: driver.configure.rfSettings.pcc.foffset.uplink.set_value(offset = 1) \n
		Specifies a positive or negative frequency offset to be added to the center frequency of the configured uplink channel. \n
			:param offset: numeric Range: -100 kHz to 100 kHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:FOFFset:UL {param}')
