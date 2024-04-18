from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdSequenceCls:
	"""UdSequence commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("udSequence", core, parent)

	def get_length(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:UDSequence:LENGth \n
		Snippet: value: int = driver.configure.connection.harq.downlink.udSequence.get_length() \n
		Specifies the length of the user-defined redundancy version sequence. \n
			:return: length: numeric Range: 1 to 4
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:UDSequence:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, length: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:UDSequence:LENGth \n
		Snippet: driver.configure.connection.harq.downlink.udSequence.set_length(length = 1) \n
		Specifies the length of the user-defined redundancy version sequence. \n
			:param length: numeric Range: 1 to 4
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:UDSequence:LENGth {param}')

	def set(self, value_1: int, value_2: int = None, value_3: int = None, value_4: int = None) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:UDSequence \n
		Snippet: driver.configure.connection.harq.downlink.udSequence.set(value_1 = 1, value_2 = 1, value_3 = 1, value_4 = 1) \n
		Specifies the user-defined redundancy version sequence. Only the first n values are used, according to the specified
		length, see method RsCmwLteSig.Configure.Connection.Harq.Downlink.UdSequence.length. You can either set the first value
		only (relevant for initial transmissions) or all four values. \n
			:param value_1: numeric In this software version fixed set to 0 Range: 0
			:param value_2: numeric Range: 0 to 3
			:param value_3: numeric Range: 0 to 3
			:param value_4: numeric Range: 0 to 3
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('value_1', value_1, DataType.Integer), ArgSingle('value_2', value_2, DataType.Integer, None, is_optional=True), ArgSingle('value_3', value_3, DataType.Integer, None, is_optional=True), ArgSingle('value_4', value_4, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:UDSequence {param}'.rstrip())

	# noinspection PyTypeChecker
	class UdSequenceStruct(StructBase):
		"""Response structure. Fields: \n
			- Value_1: int: numeric In this software version fixed set to 0 Range: 0
			- Value_2: int: numeric Range: 0 to 3
			- Value_3: int: numeric Range: 0 to 3
			- Value_4: int: numeric Range: 0 to 3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Value_1'),
			ArgStruct.scalar_int('Value_2'),
			ArgStruct.scalar_int('Value_3'),
			ArgStruct.scalar_int('Value_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Value_1: int = None
			self.Value_2: int = None
			self.Value_3: int = None
			self.Value_4: int = None

	def get(self) -> UdSequenceStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:UDSequence \n
		Snippet: value: UdSequenceStruct = driver.configure.connection.harq.downlink.udSequence.get() \n
		Specifies the user-defined redundancy version sequence. Only the first n values are used, according to the specified
		length, see method RsCmwLteSig.Configure.Connection.Harq.Downlink.UdSequence.length. You can either set the first value
		only (relevant for initial transmissions) or all four values. \n
			:return: structure: for return value, see the help for UdSequenceStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:UDSequence?', self.__class__.UdSequenceStruct())
