from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InfoCls:
	"""Info commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	def get_dcoding(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<Instance>:SMS:INComing:INFO:DCODing \n
		Snippet: value: str = driver.sense.sms.incoming.info.get_dcoding() \n
		Returns the data coding of the last message received from the UE. \n
			:return: message_encoding: string Encoding ('7bit' ASCII, '8bit' binary, '16bit' Unicode)
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:SMS:INComing:INFO:DCODing?')
		return trim_str_response(response)

	def get_mtext(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:SMS:INComing:INFO:MTEXt \n
		Snippet: value: str = driver.sense.sms.incoming.info.get_mtext() \n
		Returns the text of the last SMS message received from the UE. \n
			:return: message_text: string
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:SMS:INComing:INFO:MTEXt?')
		return trim_str_response(response)

	def get_mlength(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:SMS:INComing:INFO:MLENgth \n
		Snippet: value: int = driver.sense.sms.incoming.info.get_mlength() \n
		Returns the length of the last SMS message received from the UE. \n
			:return: message_length: decimal Number of characters of the message
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:SMS:INComing:INFO:MLENgth?')
		return Conversions.str_to_int(response)
