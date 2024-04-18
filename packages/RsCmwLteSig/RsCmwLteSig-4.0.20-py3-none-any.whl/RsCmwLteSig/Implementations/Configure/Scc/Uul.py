from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UulCls:
	"""Uul commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uul", core, parent)

	def set(self, use_uplink: bool, scc_rx_connector: enums.RxConnector = None, scc_rx_converter: enums.RxConverter = None, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC<Carrier>:UUL \n
		Snippet: driver.configure.scc.uul.set(use_uplink = False, scc_rx_connector = enums.RxConnector.I11I, scc_rx_converter = enums.RxConverter.IRX1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Activates the uplink for the SCC number <c> and optionally selects the signal path. For possible connector and converter
		values, see 'Values for signal path selection'. \n
			:param use_uplink: OFF | ON
			:param scc_rx_connector: RF connector for the SCC input path
			:param scc_rx_converter: RX module for the SCC input path
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('use_uplink', use_uplink, DataType.Boolean), ArgSingle('scc_rx_connector', scc_rx_connector, DataType.Enum, enums.RxConnector, is_optional=True), ArgSingle('scc_rx_converter', scc_rx_converter, DataType.Enum, enums.RxConverter, is_optional=True))
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:UUL {param}'.rstrip())

	# noinspection PyTypeChecker
	class UulStruct(StructBase):
		"""Response structure. Fields: \n
			- Use_Uplink: bool: OFF | ON
			- Scc_Rx_Connector: enums.RxConnector: RF connector for the SCC input path
			- Scc_Rx_Converter: enums.RxConverter: RX module for the SCC input path"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Use_Uplink'),
			ArgStruct.scalar_enum('Scc_Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Scc_Rx_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Use_Uplink: bool = None
			self.Scc_Rx_Connector: enums.RxConnector = None
			self.Scc_Rx_Converter: enums.RxConverter = None

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> UulStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC<Carrier>:UUL \n
		Snippet: value: UulStruct = driver.configure.scc.uul.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Activates the uplink for the SCC number <c> and optionally selects the signal path. For possible connector and converter
		values, see 'Values for signal path selection'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for UulStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:UUL?', self.__class__.UulStruct())
