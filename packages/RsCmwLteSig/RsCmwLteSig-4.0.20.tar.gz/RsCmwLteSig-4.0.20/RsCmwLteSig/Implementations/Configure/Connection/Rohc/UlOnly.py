from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UlOnlyCls:
	"""UlOnly commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ulOnly", core, parent)

	def get_profiles(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:ULONly:PROFiles \n
		Snippet: value: bool = driver.configure.connection.rohc.ulOnly.get_profiles() \n
		Enables header compression profiles for uplink-only header compression. \n
			:return: profile_0_x_0006: OFF | ON Profile 6, for IP/TCP/...
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:ULONly:PROFiles?')
		return Conversions.str_to_bool(response)

	def set_profiles(self, profile_0_x_0006: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:ULONly:PROFiles \n
		Snippet: driver.configure.connection.rohc.ulOnly.set_profiles(profile_0_x_0006 = False) \n
		Enables header compression profiles for uplink-only header compression. \n
			:param profile_0_x_0006: OFF | ON Profile 6, for IP/TCP/...
		"""
		param = Conversions.bool_to_str(profile_0_x_0006)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:ULONly:PROFiles {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:ULONly:ENABle \n
		Snippet: value: bool = driver.configure.connection.rohc.ulOnly.get_enable() \n
		Enables or disables uplink-only header compression. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:ULONly:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:ULONly:ENABle \n
		Snippet: driver.configure.connection.rohc.ulOnly.set_enable(enable = False) \n
		Enables or disables uplink-only header compression. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:ULONly:ENABle {param}')
