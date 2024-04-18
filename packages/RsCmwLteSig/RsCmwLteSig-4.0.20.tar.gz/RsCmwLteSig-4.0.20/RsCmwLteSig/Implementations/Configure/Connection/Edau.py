from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EdauCls:
	"""Edau commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edau", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:EDAU:ENABle \n
		Snippet: value: bool = driver.configure.connection.edau.get_enable() \n
		Enables usage of an external DAU. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:EDAU:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:EDAU:ENABle \n
		Snippet: driver.configure.connection.edau.set_enable(enable = False) \n
		Enables usage of an external DAU. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:EDAU:ENABle {param}')

	# noinspection PyTypeChecker
	def get_nsegment(self) -> enums.NetworkSegment:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:EDAU:NSEGment \n
		Snippet: value: enums.NetworkSegment = driver.configure.connection.edau.get_nsegment() \n
		Specifies the network segment of the instrument where the external DAU is installed. \n
			:return: network_segment: A | B | C
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:EDAU:NSEGment?')
		return Conversions.str_to_scalar_enum(response, enums.NetworkSegment)

	def set_nsegment(self, network_segment: enums.NetworkSegment) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:EDAU:NSEGment \n
		Snippet: driver.configure.connection.edau.set_nsegment(network_segment = enums.NetworkSegment.A) \n
		Specifies the network segment of the instrument where the external DAU is installed. \n
			:param network_segment: A | B | C
		"""
		param = Conversions.enum_scalar_to_str(network_segment, enums.NetworkSegment)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:EDAU:NSEGment {param}')

	def get_nid(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:EDAU:NID \n
		Snippet: value: int = driver.configure.connection.edau.get_nid() \n
		Specifies the subnet node ID of the instrument where the external DAU is installed. \n
			:return: idn: integer Range: 1 to 254
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:EDAU:NID?')
		return Conversions.str_to_int(response)

	def set_nid(self, idn: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:EDAU:NID \n
		Snippet: driver.configure.connection.edau.set_nid(idn = 1) \n
		Specifies the subnet node ID of the instrument where the external DAU is installed. \n
			:param idn: integer Range: 1 to 254
		"""
		param = Conversions.decimal_value_to_str(idn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:EDAU:NID {param}')
