from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BfsmCls:
	"""Bfsm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bfsm", core, parent)

	# noinspection PyTypeChecker
	class FlexibleStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Pcc_Bb_Board: enums.BasebandBoard: Signaling unit for the PCC
			- Pcc_Rx_Connector: enums.RxConnector: RF connector for the PCC input path
			- Pcc_Rx_Converter: enums.RxConverter: RX module for the PCC input path
			- Pcc_Tx_1_Connector: enums.TxConnector: RF connector for the first PCC output path
			- Pcc_Tx_1_Converter: enums.TxConverter: TX module for the first PCC output path
			- Pcc_Tx_2_Connector: enums.TxConnector: RF connector for the second PCC output path
			- Pcc_Tx_2_Converter: enums.TxConverter: TX module for the second PCC output path
			- Scc_Bb_Board: enums.BasebandBoard: Signaling unit for the SCC
			- Scc_Tx_1_Connector: enums.TxConnector: RF connector for the first SCC output path
			- Scc_Tx_1_Converter: enums.TxConverter: TX module for the first SCC output path
			- Scc_Tx_2_Connector: enums.TxConnector: RF connector for the second SCC output path
			- Scc_Tx_2_Converter: enums.TxConverter: TX module for the second SCC output path
			- Scc_Tx_3_Connector: enums.TxConnector: RF connector for the third SCC output path
			- Scc_Tx_3_Converter: enums.TxConverter: TX module for the third SCC output path
			- Scc_Tx_4_Connector: enums.TxConnector: RF connector for the fourth SCC output path
			- Scc_Tx_4_Converter: enums.TxConverter: TX module for the fourth SCC output path"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Pcc_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Pcc_Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Pcc_Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_Tx_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_Tx_3_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_Tx_4_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_Tx_4_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pcc_Bb_Board: enums.BasebandBoard = None
			self.Pcc_Rx_Connector: enums.RxConnector = None
			self.Pcc_Rx_Converter: enums.RxConverter = None
			self.Pcc_Tx_1_Connector: enums.TxConnector = None
			self.Pcc_Tx_1_Converter: enums.TxConverter = None
			self.Pcc_Tx_2_Connector: enums.TxConnector = None
			self.Pcc_Tx_2_Converter: enums.TxConverter = None
			self.Scc_Bb_Board: enums.BasebandBoard = None
			self.Scc_Tx_1_Connector: enums.TxConnector = None
			self.Scc_Tx_1_Converter: enums.TxConverter = None
			self.Scc_Tx_2_Connector: enums.TxConnector = None
			self.Scc_Tx_2_Converter: enums.TxConverter = None
			self.Scc_Tx_3_Connector: enums.TxConnector = None
			self.Scc_Tx_3_Converter: enums.TxConverter = None
			self.Scc_Tx_4_Connector: enums.TxConnector = None
			self.Scc_Tx_4_Converter: enums.TxConverter = None

	def get_flexible(self) -> FlexibleStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:BFSM<MIMO4x4>[:FLEXible] \n
		Snippet: value: FlexibleStruct = driver.route.scenario.bfsm.get_flexible() \n
		Activates the scenario '2CC - nx2 nx4' and selects the signal paths. For possible parameter values, see 'Values for
		signal path selection'. \n
			:return: structure: for return value, see the help for FlexibleStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:BFSM4:FLEXible?', self.__class__.FlexibleStruct())

	def set_flexible(self, value: FlexibleStruct) -> None:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:BFSM<MIMO4x4>[:FLEXible] \n
		Snippet with structure: \n
		structure = driver.route.scenario.bfsm.FlexibleStruct() \n
		structure.Pcc_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Pcc_Rx_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Pcc_Rx_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Pcc_Tx_1_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Pcc_Tx_1_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Pcc_Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Pcc_Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Scc_Tx_1_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_Tx_1_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_Tx_3_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_Tx_3_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_Tx_4_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_Tx_4_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		driver.route.scenario.bfsm.set_flexible(value = structure) \n
		Activates the scenario '2CC - nx2 nx4' and selects the signal paths. For possible parameter values, see 'Values for
		signal path selection'. \n
			:param value: see the help for FlexibleStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:BFSM4:FLEXible', value)
