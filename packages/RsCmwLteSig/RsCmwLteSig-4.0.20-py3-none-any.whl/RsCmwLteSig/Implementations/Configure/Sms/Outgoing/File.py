from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FileCls:
	"""File commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	# noinspection PyTypeChecker
	class InfoStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Message_Encoding: str: string Encoding of the message (7-bit ASCII, 8-bit binary, 16-bit Unicode)
			- Message_Text: str: string
			- Message_Length: int: decimal Number of characters in the message Range: 0 to 10E+3"""
		__meta_args_list = [
			ArgStruct.scalar_str('Message_Encoding'),
			ArgStruct.scalar_str('Message_Text'),
			ArgStruct.scalar_int('Message_Length')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Message_Encoding: str = None
			self.Message_Text: str = None
			self.Message_Length: int = None

	def get_info(self) -> InfoStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:FILE:INFO \n
		Snippet: value: InfoStruct = driver.configure.sms.outgoing.file.get_info() \n
		Displays information about the file selected via method RsCmwLteSig.Configure.Sms.Outgoing.File.value. \n
			:return: structure: for return value, see the help for InfoStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:FILE:INFO?', self.__class__.InfoStruct())

	def get_value(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:FILE \n
		Snippet: value: str = driver.configure.sms.outgoing.file.get_value() \n
		Selects a file containing the message to be transmitted. \n
			:return: sms_file: string Path of the file, for example: '@USERDATA/sms/LTE/Send/example_ascii.sms'
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:FILE?')
		return trim_str_response(response)

	def set_value(self, sms_file: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:FILE \n
		Snippet: driver.configure.sms.outgoing.file.set_value(sms_file = 'abc') \n
		Selects a file containing the message to be transmitted. \n
			:param sms_file: string Path of the file, for example: '@USERDATA/sms/LTE/Send/example_ascii.sms'
		"""
		param = Conversions.value_to_quoted_str(sms_file)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:FILE {param}')
