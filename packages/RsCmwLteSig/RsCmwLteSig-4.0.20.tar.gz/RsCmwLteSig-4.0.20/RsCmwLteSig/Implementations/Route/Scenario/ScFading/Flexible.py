from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FlexibleCls:
	"""Flexible commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("flexible", core, parent)

	# noinspection PyTypeChecker
	class ExternalStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Pcc_Bb_Board: enums.BasebandBoard: No parameter help available
			- Rx_Connector: enums.RxConnector: No parameter help available
			- Rx_Converter: enums.RxConverter: No parameter help available
			- Tx_Connector: enums.TxConnector: No parameter help available
			- Tx_Converter: enums.TxConverter: No parameter help available
			- Iq_Connector: enums.TxConnector: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Pcc_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Iq_Connector', enums.TxConnector)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pcc_Bb_Board: enums.BasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Iq_Connector: enums.TxConnector = None

	def get_external(self) -> ExternalStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:SCFading:FLEXible[:EXTernal] \n
		Snippet: value: ExternalStruct = driver.route.scenario.scFading.flexible.get_external() \n
		No command help available \n
			:return: structure: for return value, see the help for ExternalStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:SCFading:FLEXible:EXTernal?', self.__class__.ExternalStruct())

	def set_external(self, value: ExternalStruct) -> None:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:SCFading:FLEXible[:EXTernal] \n
		Snippet with structure: \n
		structure = driver.route.scenario.scFading.flexible.ExternalStruct() \n
		structure.Pcc_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Rx_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Rx_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Tx_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Iq_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		driver.route.scenario.scFading.flexible.set_external(value = structure) \n
		No command help available \n
			:param value: see the help for ExternalStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:SCFading:FLEXible:EXTernal', value)

	# noinspection PyTypeChecker
	class InternalStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Pcc_Bb_Board: enums.BasebandBoard: Signaling unit
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector: enums.TxConnector: RF connector for the output path
			- Tx_Converter: enums.TxConverter: TX module for the output path
			- Pcc_Fading_Board: enums.FadingBoard: Internal fader"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Pcc_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Pcc_Fading_Board', enums.FadingBoard)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pcc_Bb_Board: enums.BasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Pcc_Fading_Board: enums.FadingBoard = None

	def get_internal(self) -> InternalStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:SCFading:FLEXible:INTernal \n
		Snippet: value: InternalStruct = driver.route.scenario.scFading.flexible.get_internal() \n
		Activates the scenario '1CC - Fading - 1x1' with internal fading and selects the signal paths. For possible parameter
		values, see 'Values for signal path selection'. \n
			:return: structure: for return value, see the help for InternalStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:SCFading:FLEXible:INTernal?', self.__class__.InternalStruct())

	def set_internal(self, value: InternalStruct) -> None:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:SCFading:FLEXible:INTernal \n
		Snippet with structure: \n
		structure = driver.route.scenario.scFading.flexible.InternalStruct() \n
		structure.Pcc_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Rx_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Rx_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Tx_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Pcc_Fading_Board: enums.FadingBoard = enums.FadingBoard.FAD012 \n
		driver.route.scenario.scFading.flexible.set_internal(value = structure) \n
		Activates the scenario '1CC - Fading - 1x1' with internal fading and selects the signal paths. For possible parameter
		values, see 'Values for signal path selection'. \n
			:param value: see the help for InternalStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:SCFading:FLEXible:INTernal', value)
