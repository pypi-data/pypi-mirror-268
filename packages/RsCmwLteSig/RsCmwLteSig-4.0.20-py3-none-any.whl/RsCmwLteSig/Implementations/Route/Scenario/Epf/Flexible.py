from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FlexibleCls:
	"""Flexible commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("flexible", core, parent)

	# noinspection PyTypeChecker
	class InternalStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Pcc_Bb_Board: enums.BasebandBoard: Signaling unit for the PCC
			- Rx_Connector: enums.RxConnector: RF connector for the PCC input path
			- Rx_Converter: enums.RxConverter: RX module for the PCC input path
			- Pcc_Tx_1_Connector: enums.TxConnector: RF connector for the first PCC output path
			- Pcc_Tx_1_Converter: enums.TxConverter: TX module for the first PCC output path
			- Pcc_Tx_2_Connector: enums.TxConnector: RF connector for the second PCC output path
			- Pcc_Tx_2_Converter: enums.TxConverter: TX module for the second PCC output path
			- Pcc_Tx_3_Connector: enums.TxConnector: RF connector for the third PCC output path
			- Pcc_Tx_3_Converter: enums.TxConverter: TX module for the third PCC output path
			- Pcc_Tx_4_Connector: enums.TxConnector: RF connector for the fourth PCC output path
			- Pcc_Tx_4_Converter: enums.TxConverter: TX module for the fourth PCC output path
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
			- Scc_3_Bb_Board: enums.BasebandBoard: Signaling unit for the SCC3
			- Scc_3_Tx_1_Connector: enums.TxConnector: RF connector for the first SCC3 output path
			- Scc_3_Tx_1_Converter: enums.TxConverter: TX module for the first SCC3 output path
			- Scc_3_Tx_2_Connector: enums.TxConnector: RF connector for the second SCC3 output path
			- Scc_3_Tx_2_Converter: enums.TxConverter: TX module for the second SCC3 output path
			- Scc_4_Bb_Board: enums.BasebandBoard: Signaling unit for the SCC4
			- Scc_4_Tx_1_Connector: enums.TxConnector: RF connector for the first SCC4 output path
			- Scc_4_Tx_1_Converter: enums.TxConverter: TX module for the first SCC4 output path
			- Scc_4_Tx_2_Connector: enums.TxConnector: RF connector for the second SCC4 output path
			- Scc_4_Tx_2_Converter: enums.TxConverter: TX module for the second SCC4 output path
			- Pcc_Fading_Board: enums.FadingBoard: Optional setting parameter. Internal fader for the PCC
			- Scc_1_Fading_Board: enums.FadingBoard: Optional setting parameter. Internal fader for the SCC1
			- Scc_2_Fading_Board: enums.FadingBoard: Optional setting parameter. Internal fader for the SCC2
			- Scc_3_Fading_Board: enums.FadingBoard: Optional setting parameter. Internal fader for the SCC3
			- Scc_4_Fading_Board: enums.FadingBoard: Optional setting parameter. Internal fader for the SCC4
			- Coprocessor: enums.BasebandBoard: Optional setting parameter. SUA for coprocessing"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Pcc_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_3_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_4_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_4_Converter', enums.TxConverter),
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
			ArgStruct.scalar_enum('Scc_3_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_3_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_3_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_3_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_3_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_4_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_4_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_4_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_4_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_4_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum_optional('Pcc_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum_optional('Scc_1_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum_optional('Scc_2_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum_optional('Scc_3_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum_optional('Scc_4_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum_optional('Coprocessor', enums.BasebandBoard)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pcc_Bb_Board: enums.BasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Pcc_Tx_1_Connector: enums.TxConnector = None
			self.Pcc_Tx_1_Converter: enums.TxConverter = None
			self.Pcc_Tx_2_Connector: enums.TxConnector = None
			self.Pcc_Tx_2_Converter: enums.TxConverter = None
			self.Pcc_Tx_3_Connector: enums.TxConnector = None
			self.Pcc_Tx_3_Converter: enums.TxConverter = None
			self.Pcc_Tx_4_Connector: enums.TxConnector = None
			self.Pcc_Tx_4_Converter: enums.TxConverter = None
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
			self.Scc_3_Bb_Board: enums.BasebandBoard = None
			self.Scc_3_Tx_1_Connector: enums.TxConnector = None
			self.Scc_3_Tx_1_Converter: enums.TxConverter = None
			self.Scc_3_Tx_2_Connector: enums.TxConnector = None
			self.Scc_3_Tx_2_Converter: enums.TxConverter = None
			self.Scc_4_Bb_Board: enums.BasebandBoard = None
			self.Scc_4_Tx_1_Connector: enums.TxConnector = None
			self.Scc_4_Tx_1_Converter: enums.TxConverter = None
			self.Scc_4_Tx_2_Connector: enums.TxConnector = None
			self.Scc_4_Tx_2_Converter: enums.TxConverter = None
			self.Pcc_Fading_Board: enums.FadingBoard = None
			self.Scc_1_Fading_Board: enums.FadingBoard = None
			self.Scc_2_Fading_Board: enums.FadingBoard = None
			self.Scc_3_Fading_Board: enums.FadingBoard = None
			self.Scc_4_Fading_Board: enums.FadingBoard = None
			self.Coprocessor: enums.BasebandBoard = None

	def get_internal(self) -> InternalStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:EPF[:FLEXible]:INTernal \n
		Snippet: value: InternalStruct = driver.route.scenario.epf.flexible.get_internal() \n
		Activates the scenario '5CC - Fading - nx4 nx4 nx4 nx2 nx2' with internal fading and selects the signal paths.
		For possible parameter values, see 'Values for signal path selection'. \n
			:return: structure: for return value, see the help for InternalStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:EPF:FLEXible:INTernal?', self.__class__.InternalStruct())

	def set_internal(self, value: InternalStruct) -> None:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:EPF[:FLEXible]:INTernal \n
		Snippet with structure: \n
		structure = driver.route.scenario.epf.flexible.InternalStruct() \n
		structure.Pcc_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Rx_Connector: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Rx_Converter: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Pcc_Tx_1_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Pcc_Tx_1_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Pcc_Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Pcc_Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Pcc_Tx_3_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Pcc_Tx_3_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Pcc_Tx_4_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Pcc_Tx_4_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
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
		structure.Scc_3_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Scc_3_Tx_1_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_3_Tx_1_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_3_Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_3_Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_4_Bb_Board: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		structure.Scc_4_Tx_1_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_4_Tx_1_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Scc_4_Tx_2_Connector: enums.TxConnector = enums.TxConnector.I12O \n
		structure.Scc_4_Tx_2_Converter: enums.TxConverter = enums.TxConverter.ITX1 \n
		structure.Pcc_Fading_Board: enums.FadingBoard = enums.FadingBoard.FAD012 \n
		structure.Scc_1_Fading_Board: enums.FadingBoard = enums.FadingBoard.FAD012 \n
		structure.Scc_2_Fading_Board: enums.FadingBoard = enums.FadingBoard.FAD012 \n
		structure.Scc_3_Fading_Board: enums.FadingBoard = enums.FadingBoard.FAD012 \n
		structure.Scc_4_Fading_Board: enums.FadingBoard = enums.FadingBoard.FAD012 \n
		structure.Coprocessor: enums.BasebandBoard = enums.BasebandBoard.BBR1 \n
		driver.route.scenario.epf.flexible.set_internal(value = structure) \n
		Activates the scenario '5CC - Fading - nx4 nx4 nx4 nx2 nx2' with internal fading and selects the signal paths.
		For possible parameter values, see 'Values for signal path selection'. \n
			:param value: see the help for InternalStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:EPF:FLEXible:INTernal', value)
