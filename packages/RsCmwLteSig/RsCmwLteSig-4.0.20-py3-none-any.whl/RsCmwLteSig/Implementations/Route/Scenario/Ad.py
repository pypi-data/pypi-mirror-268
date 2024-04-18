from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AdCls:
	"""Ad commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ad", core, parent)

	# noinspection PyTypeChecker
	class FlexibleStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Pcc_Bb_Board: enums.BasebandBoard: Signaling unit for all paths
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_1_Connector: enums.TxConnector: RF connector for the first output path
			- Tx_1_Converter: enums.TxConverter: TX module for the first output path
			- Tx_2_Connector: enums.TxConnector: RF connector for the second output path
			- Tx_2_Converter: enums.TxConverter: TX module for the second output path
			- Tx_3_Connector: enums.TxConnector: RF connector for the third output path
			- Tx_3_Converter: enums.TxConverter: TX module for the third output path
			- Tx_4_Connector: enums.TxConnector: RF connector for the fourth output path
			- Tx_4_Converter: enums.TxConverter: TX module for the fourth output path"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Pcc_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_3_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_4_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_4_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pcc_Bb_Board: enums.BasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_1_Connector: enums.TxConnector = None
			self.Tx_1_Converter: enums.TxConverter = None
			self.Tx_2_Connector: enums.TxConnector = None
			self.Tx_2_Converter: enums.TxConverter = None
			self.Tx_3_Connector: enums.TxConnector = None
			self.Tx_3_Converter: enums.TxConverter = None
			self.Tx_4_Connector: enums.TxConnector = None
			self.Tx_4_Converter: enums.TxConverter = None

	def get_flexible(self) -> FlexibleStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:AD[:FLEXible] \n
		Snippet: value: FlexibleStruct = driver.route.scenario.ad.get_flexible() \n
		Activates the scenario '1CC - nx4' and selects the signal paths. For possible parameter values, see 'Values for signal
		path selection'. \n
			:return: structure: for return value, see the help for FlexibleStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:AD:FLEXible?', self.__class__.FlexibleStruct())

	def set_flexible(self, value: FlexibleStruct) -> None:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:AD[:FLEXible] \n
		Snippet with structure: \n
		structure = driver.route.scenario.ad.FlexibleStruct() \n
		structure.Pcc_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Rx_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Rx_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Tx_1_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_1_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Tx_3_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_3_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Tx_4_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_4_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		driver.route.scenario.ad.set_flexible(value = structure) \n
		Activates the scenario '1CC - nx4' and selects the signal paths. For possible parameter values, see 'Values for signal
		path selection'. \n
			:param value: see the help for FlexibleStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:AD:FLEXible', value)
