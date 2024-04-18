from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CjsmCls:
	"""Cjsm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cjsm", core, parent)

	# noinspection PyTypeChecker
	class FlexibleStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Pcc_Bb_Board: enums.BasebandBoard: Signaling unit for the PCC
			- Pcc_Rx_Connector: enums.RxConnector: RF connector for the PCC input path
			- Pcc_Rx_Converter: enums.RxConverter: RX module for the PCC input path
			- Pcc_Tx_1_Connector: enums.TxConnector: RF connector for the first PCC output path
			- Pcc_Tx_1_Converter: enums.TxConverter: TX module for the first PCC output path
			- Pcc_Tx_2_Connector: enums.TxConnector: RF connector for the second PCC output path
			- Pcc_Tx_2_Converter: enums.TxConverter: TX module for the second PCC output path
			- Scc_1_Bb_Board: enums.BasebandBoard: Signaling unit for the SCC1
			- Scc_1_Tx_1_Connector: enums.TxConnector: RF connector for the first SCC1 output path
			- Scc_1_Tx_1_Converter: enums.TxConverter: TX module for the first SCC1 output path
			- Scc_1_Tx_2_Connector: enums.TxConnector: RF connector for the second SCC1 output path
			- Scc_1_Tx_2_Converter: enums.TxConverter: TX module for the second SCC1 output path
			- Scc_1_Tx_3_Connector: enums.TxConnector: RF connector for the third SCC1 output path
			- Scc_1_Tx_3_Converter: enums.TxConverter: TX module for the third SCC1 output path
			- Scc_1_Tx_4_Connector: enums.TxConnector: RF connector for the fourth SCC1 output path
			- Scc_1_Tx_4_Converter: enums.TxConverter: TX module for the fourth SCC1 output path
			- Scc_2_Bb_Board: enums.BasebandBoard: Signaling unit for the SCC2
			- Scc_2_Tx_1_Connector: enums.TxConnector: RF connector for the first SCC2 output path
			- Scc_2_Tx_1_Converter: enums.TxConverter: TX module for the first SCC2 output path
			- Scc_2_Tx_2_Connector: enums.TxConnector: RF connector for the second SCC2 output path
			- Scc_2_Tx_2_Converter: enums.TxConverter: TX module for the second SCC2 output path
			- Scc_2_Tx_3_Connector: enums.TxConnector: RF connector for the third SCC2 output path
			- Scc_2_Tx_3_Converter: enums.TxConverter: TX module for the third SCC2 output path
			- Scc_2_Tx_4_Connector: enums.TxConnector: RF connector for the fourth SCC2 output path
			- Scc_2_Tx_4_Converter: enums.TxConverter: TX module for the fourth SCC2 output path
			- Coprocessor: enums.BasebandBoard: Optional setting parameter. SUA for coprocessing"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Pcc_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Pcc_Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Pcc_Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_1_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_1_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_1_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_1_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_1_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_1_Tx_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_1_Tx_3_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_1_Tx_4_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_1_Tx_4_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_2_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_2_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_2_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_2_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_2_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_2_Tx_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_2_Tx_3_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_2_Tx_4_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_2_Tx_4_Converter', enums.TxConverter),
			ArgStruct.scalar_enum_optional('Coprocessor', enums.BasebandBoard)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pcc_Bb_Board: enums.BasebandBoard = None
			self.Pcc_Rx_Connector: enums.RxConnector = None
			self.Pcc_Rx_Converter: enums.RxConverter = None
			self.Pcc_Tx_1_Connector: enums.TxConnector = None
			self.Pcc_Tx_1_Converter: enums.TxConverter = None
			self.Pcc_Tx_2_Connector: enums.TxConnector = None
			self.Pcc_Tx_2_Converter: enums.TxConverter = None
			self.Scc_1_Bb_Board: enums.BasebandBoard = None
			self.Scc_1_Tx_1_Connector: enums.TxConnector = None
			self.Scc_1_Tx_1_Converter: enums.TxConverter = None
			self.Scc_1_Tx_2_Connector: enums.TxConnector = None
			self.Scc_1_Tx_2_Converter: enums.TxConverter = None
			self.Scc_1_Tx_3_Connector: enums.TxConnector = None
			self.Scc_1_Tx_3_Converter: enums.TxConverter = None
			self.Scc_1_Tx_4_Connector: enums.TxConnector = None
			self.Scc_1_Tx_4_Converter: enums.TxConverter = None
			self.Scc_2_Bb_Board: enums.BasebandBoard = None
			self.Scc_2_Tx_1_Connector: enums.TxConnector = None
			self.Scc_2_Tx_1_Converter: enums.TxConverter = None
			self.Scc_2_Tx_2_Connector: enums.TxConnector = None
			self.Scc_2_Tx_2_Converter: enums.TxConverter = None
			self.Scc_2_Tx_3_Connector: enums.TxConnector = None
			self.Scc_2_Tx_3_Converter: enums.TxConverter = None
			self.Scc_2_Tx_4_Connector: enums.TxConnector = None
			self.Scc_2_Tx_4_Converter: enums.TxConverter = None
			self.Coprocessor: enums.BasebandBoard = None

	def get_flexible(self) -> FlexibleStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:CJSM<MIMO44>[:FLEXible] \n
		Snippet: value: FlexibleStruct = driver.route.scenario.cjsm.get_flexible() \n
		Activates the scenario '3CC - nx2 nx4 nx4' and selects the signal paths. For possible parameter values, see 'Values for
		signal path selection'. \n
			:return: structure: for return value, see the help for FlexibleStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:CJSM4:FLEXible?', self.__class__.FlexibleStruct())

	def set_flexible(self, value: FlexibleStruct) -> None:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:CJSM<MIMO44>[:FLEXible] \n
		Snippet with structure: \n
		structure = driver.route.scenario.cjsm.FlexibleStruct() \n
		structure.Pcc_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Pcc_Rx_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Pcc_Rx_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Pcc_Tx_1_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Pcc_Tx_1_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Pcc_Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Pcc_Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_1_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Scc_1_Tx_1_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_1_Tx_1_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_1_Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_1_Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_1_Tx_3_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_1_Tx_3_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_1_Tx_4_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_1_Tx_4_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_2_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Scc_2_Tx_1_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_2_Tx_1_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_2_Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_2_Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_2_Tx_3_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_2_Tx_3_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_2_Tx_4_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_2_Tx_4_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Coprocessor: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		driver.route.scenario.cjsm.set_flexible(value = structure) \n
		Activates the scenario '3CC - nx2 nx4 nx4' and selects the signal paths. For possible parameter values, see 'Values for
		signal path selection'. \n
			:param value: see the help for FlexibleStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:CJSM4:FLEXible', value)
