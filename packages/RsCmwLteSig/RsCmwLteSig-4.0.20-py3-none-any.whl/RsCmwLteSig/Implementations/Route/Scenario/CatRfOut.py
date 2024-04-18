from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatRfOutCls:
	"""CatRfOut commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catRfOut", core, parent)

	# noinspection PyTypeChecker
	class FlexibleStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Pcc_Bb_Board: enums.BasebandBoard: Signaling unit for the PCC
			- Rx_Connector: enums.RxConnector: RF connector for the PCC input path
			- Rx_Converter: enums.RxConverter: RX module for the PCC input path
			- Pcc_Tx_Connector: enums.TxConnector: RF connector for the PCC output path
			- Pcc_Tx_Converter: enums.TxConverter: TX module for the PCC output path
			- Scc_Bb_Board: enums.BasebandBoard: Signaling unit for the SCC
			- Scc_Tx_Connector: enums.TxConnector: RF connector for the SCC output path
			- Scc_Tx_Converter: enums.TxConverter: TX module for the SCC output path
			- Scc_Rx_Connector: enums.RxConnector: Optional setting parameter. RF connector for the SCC input path, for UL CA only
			- Scc_Rx_Converter: enums.RxConverter: Optional setting parameter. RX module for the SCC input path, for UL CA only"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Pcc_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum_optional('Scc_Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum_optional('Scc_Rx_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pcc_Bb_Board: enums.BasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Pcc_Tx_Connector: enums.TxConnector = None
			self.Pcc_Tx_Converter: enums.TxConverter = None
			self.Scc_Bb_Board: enums.BasebandBoard = None
			self.Scc_Tx_Connector: enums.TxConnector = None
			self.Scc_Tx_Converter: enums.TxConverter = None
			self.Scc_Rx_Connector: enums.RxConnector = None
			self.Scc_Rx_Converter: enums.RxConverter = None

	def get_flexible(self) -> FlexibleStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:CATRfout:FLEXible \n
		Snippet: value: FlexibleStruct = driver.route.scenario.catRfOut.get_flexible() \n
		Activates the scenario '2CC - 1x1 1x1' and selects the signal paths. For possible parameter values, see 'Values for
		signal path selection'. \n
			:return: structure: for return value, see the help for FlexibleStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:CATRfout:FLEXible?', self.__class__.FlexibleStruct())

	def set_flexible(self, value: FlexibleStruct) -> None:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:CATRfout:FLEXible \n
		Snippet with structure: \n
		structure = driver.route.scenario.catRfOut.FlexibleStruct() \n
		structure.Pcc_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Rx_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Rx_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Pcc_Tx_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Pcc_Tx_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Scc_Tx_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_Tx_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_Rx_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Scc_Rx_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		driver.route.scenario.catRfOut.set_flexible(value = structure) \n
		Activates the scenario '2CC - 1x1 1x1' and selects the signal paths. For possible parameter values, see 'Values for
		signal path selection'. \n
			:param value: see the help for FlexibleStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:CATRfout:FLEXible', value)
