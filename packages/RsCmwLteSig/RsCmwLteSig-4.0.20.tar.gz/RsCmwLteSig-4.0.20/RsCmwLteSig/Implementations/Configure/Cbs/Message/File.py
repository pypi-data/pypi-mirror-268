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
			- Message_Encoding: str: string
			- Message_Text: str: string
			- Message_Length: int: decimal Number of characters in the message Range: 0 to 600"""
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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:FILE:INFO \n
		Snippet: value: InfoStruct = driver.configure.cbs.message.file.get_info() \n
		Queries information about the message in the selected file (see method RsCmwLteSig.Configure.Cbs.Message.File.value) . \n
			:return: structure: for return value, see the help for InfoStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:FILE:INFO?', self.__class__.InfoStruct())

	def get_value(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:FILE \n
		Snippet: value: str = driver.configure.cbs.message.file.get_value() \n
		Selects a message file for the data source FILE.
		Store your message files in the directory D:/Rohde-Schwarz/CMW/Data/cbs/LTE/. \n
			:return: file: string Path and filename
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:FILE?')
		return trim_str_response(response)

	def set_value(self, file: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:FILE \n
		Snippet: driver.configure.cbs.message.file.set_value(file = 'abc') \n
		Selects a message file for the data source FILE.
		Store your message files in the directory D:/Rohde-Schwarz/CMW/Data/cbs/LTE/. \n
			:param file: string Path and filename
		"""
		param = Conversions.value_to_quoted_str(file)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:FILE {param}')
