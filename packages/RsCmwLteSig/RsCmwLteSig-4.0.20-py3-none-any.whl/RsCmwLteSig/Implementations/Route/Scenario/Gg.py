from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GgCls:
	"""Gg commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gg", core, parent)

	# noinspection PyTypeChecker
	class FlexibleStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Bb_Board_1: enums.BasebandBoard: Signaling unit for the PCC
			- Rx_Connector: enums.RxConnector: RF connector for the PCC input path
			- Rx_Converter: enums.RxConverter: RX module for the PCC input path
			- Tx_1_Connector: enums.TxConnector: RF connector for the PCC output path
			- Tx_1_Converter: enums.TxConverter: TX module for the PCC output path
			- Bb_Board_2: enums.BasebandBoard: Signaling unit for the SCC1
			- Tx_2_Connector: enums.TxConnector: RF connector for the SCC1 output path
			- Tx_2_Converter: enums.TxConverter: TX module for the SCC1 output path
			- Bb_Board_3: enums.BasebandBoard: Signaling unit for the SCC2
			- Tx_3_Connector: enums.TxConnector: RF connector for the SCC2 output path
			- Tx_3_Converter: enums.TxConverter: TX module for the SCC2 output path
			- Bb_Board_4: enums.BasebandBoard: Signaling unit for the SCC3
			- Tx_4_Connector: enums.TxConnector: RF connector for the SCC3 output path
			- Tx_4_Converter: enums.TxConverter: TX module for the SCC3 output path
			- Bb_Board_5: enums.BasebandBoard: Signaling unit for the SCC4
			- Tx_5_Connector: enums.TxConnector: RF connector for the SCC4 output path
			- Tx_5_Converter: enums.TxConverter: TX module for the SCC4 output path
			- Bb_Board_6: enums.BasebandBoard: Signaling unit for the SCC5
			- Tx_6_Connector: enums.TxConnector: RF connector for the SCC5 output path
			- Tx_6_Converter: enums.TxConverter: TX module for the SCC5 output path
			- Bb_Board_7: enums.BasebandBoard: Signaling unit for the SCC6
			- Tx_7_Connector: enums.TxConnector: RF connector for the SCC6 output path
			- Tx_7_Converter: enums.TxConverter: TX module for the SCC6 output path
			- Coprocessor: enums.BasebandBoard: Optional setting parameter. SUA for coprocessing"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bb_Board_1', enums.BasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Bb_Board_2', enums.BasebandBoard),
			ArgStruct.scalar_enum('Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Bb_Board_3', enums.BasebandBoard),
			ArgStruct.scalar_enum('Tx_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_3_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Bb_Board_4', enums.BasebandBoard),
			ArgStruct.scalar_enum('Tx_4_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_4_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Bb_Board_5', enums.BasebandBoard),
			ArgStruct.scalar_enum('Tx_5_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_5_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Bb_Board_6', enums.BasebandBoard),
			ArgStruct.scalar_enum('Tx_6_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_6_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Bb_Board_7', enums.BasebandBoard),
			ArgStruct.scalar_enum('Tx_7_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_7_Converter', enums.TxConverter),
			ArgStruct.scalar_enum_optional('Coprocessor', enums.BasebandBoard)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bb_Board_1: enums.BasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_1_Connector: enums.TxConnector = None
			self.Tx_1_Converter: enums.TxConverter = None
			self.Bb_Board_2: enums.BasebandBoard = None
			self.Tx_2_Connector: enums.TxConnector = None
			self.Tx_2_Converter: enums.TxConverter = None
			self.Bb_Board_3: enums.BasebandBoard = None
			self.Tx_3_Connector: enums.TxConnector = None
			self.Tx_3_Converter: enums.TxConverter = None
			self.Bb_Board_4: enums.BasebandBoard = None
			self.Tx_4_Connector: enums.TxConnector = None
			self.Tx_4_Converter: enums.TxConverter = None
			self.Bb_Board_5: enums.BasebandBoard = None
			self.Tx_5_Connector: enums.TxConnector = None
			self.Tx_5_Converter: enums.TxConverter = None
			self.Bb_Board_6: enums.BasebandBoard = None
			self.Tx_6_Connector: enums.TxConnector = None
			self.Tx_6_Converter: enums.TxConverter = None
			self.Bb_Board_7: enums.BasebandBoard = None
			self.Tx_7_Connector: enums.TxConnector = None
			self.Tx_7_Converter: enums.TxConverter = None
			self.Coprocessor: enums.BasebandBoard = None

	def get_flexible(self) -> FlexibleStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:GG[:FLEXible] \n
		Snippet: value: FlexibleStruct = driver.route.scenario.gg.get_flexible() \n
		Activates the scenario '7CC - 1x1 1x1 1x1 1x1 1x1 1x1 1x1' and selects the signal paths. For possible parameter values,
		see 'Values for signal path selection'. \n
			:return: structure: for return value, see the help for FlexibleStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:GG:FLEXible?', self.__class__.FlexibleStruct())

	def set_flexible(self, value: FlexibleStruct) -> None:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:GG[:FLEXible] \n
		Snippet with structure: \n
		structure = driver.route.scenario.gg.FlexibleStruct() \n
		structure.Bb_Board_1: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Rx_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Rx_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Tx_1_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_1_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Bb_Board_2: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Bb_Board_3: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Tx_3_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_3_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Bb_Board_4: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Tx_4_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_4_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Bb_Board_5: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Tx_5_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_5_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Bb_Board_6: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Tx_6_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_6_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Bb_Board_7: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Tx_7_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Tx_7_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Coprocessor: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		driver.route.scenario.gg.set_flexible(value = structure) \n
		Activates the scenario '7CC - 1x1 1x1 1x1 1x1 1x1 1x1 1x1' and selects the signal paths. For possible parameter values,
		see 'Values for signal path selection'. \n
			:param value: see the help for FlexibleStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:GG:FLEXible', value)
