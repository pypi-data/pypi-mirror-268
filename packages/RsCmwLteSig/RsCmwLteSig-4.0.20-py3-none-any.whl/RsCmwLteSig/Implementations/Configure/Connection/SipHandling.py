from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SipHandlingCls:
	"""SipHandling commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sipHandling", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SIPHandling:ENABle \n
		Snippet: value: bool = driver.configure.connection.sipHandling.get_enable() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:SIPHandling:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SIPHandling:ENABle \n
		Snippet: driver.configure.connection.sipHandling.set_enable(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SIPHandling:ENABle {param}')

	def get_apn(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SIPHandling:APN \n
		Snippet: value: str = driver.configure.connection.sipHandling.get_apn() \n
		No command help available \n
			:return: apn: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:SIPHandling:APN?')
		return trim_str_response(response)

	def set_apn(self, apn: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SIPHandling:APN \n
		Snippet: driver.configure.connection.sipHandling.set_apn(apn = 'abc') \n
		No command help available \n
			:param apn: No help available
		"""
		param = Conversions.value_to_quoted_str(apn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SIPHandling:APN {param}')
