from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class BwChannelStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Band_Pcc: enums.OperatingBandC: FDD: UDEFined | OB1 | ... | OB28 | OB30 | OB31 | OB65 | OB66 | OB68 | OB70 | ... | OB74 | OB85 | OB87 | OB88 TDD: UDEFined | OB33 | ... | OB46 | OB48 | ... | OB53 | OB250 Selects the PCC operating band
			- Dl_Channel_Pcc: int: decimal PCC DL channel number Range: depends on operating band
			- Bandwidth_Pcc: enums.Bandwidth: B014 | B030 | B050 | B100 | B150 | B200 PCC cell bandwidth B014: 1.4 MHz B030: 3 MHz B050: 5 MHz B100: 10 MHz B150: 15 MHz B200: 20 MHz
			- Band_Scc_1: enums.OperatingBandC: Optional setting parameter. FDD: UDEFined | OB1 | ... | OB32 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB252 | OB255 TDD: UDEFined | OB33 | ... | OB46 | OB48 | ... | OB53 | OB250 SCC1 operating band
			- Dl_Channel_Scc_1: int: Optional setting parameter. decimal SCC1 DL channel number Range: depends on operating band
			- Bandwidth_Scc_1: enums.Bandwidth: Optional setting parameter. B014 | B030 | B050 | B100 | B150 | B200 SCC1 cell bandwidth
			- Band_Scc_2: enums.OperatingBandC: Optional setting parameter. FDD: UDEFined | OB1 | ... | OB32 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB252 | OB255 TDD: UDEFined | OB33 | ... | OB46 | OB48 | ... | OB53 | OB250 SCC2 operating band
			- Dl_Channel_Scc_2: int: Optional setting parameter. decimal SCC2 DL channel number Range: depends on operating band
			- Bandwidth_Scc_2: enums.Bandwidth: Optional setting parameter. B014 | B030 | B050 | B100 | B150 | B200 SCC2 cell bandwidth
			- Band_Scc_3: enums.OperatingBandC: Optional setting parameter. FDD: UDEFined | OB1 | ... | OB32 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB252 | OB255 TDD: UDEFined | OB33 | ... | OB46 | OB48 | ... | OB53 | OB250 SCC3 operating band
			- Dl_Channel_Scc_3: int: Optional setting parameter. decimal SCC3 DL channel number Range: depends on operating band
			- Bandwidth_Scc_3: enums.Bandwidth: Optional setting parameter. B014 | B030 | B050 | B100 | B150 | B200 SCC3 cell bandwidth
			- Band_Scc_4: enums.OperatingBandC: Optional setting parameter. FDD: UDEFined | OB1 | ... | OB32 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB252 | OB255 TDD: UDEFined | OB33 | ... | OB46 | OB48 | ... | OB53 | OB250 SCC4 operating band
			- Dl_Channel_Scc_4: int: Optional setting parameter. decimal SCC4 DL channel number Range: depends on operating band
			- Bandwidth_Scc_4: enums.Bandwidth: Optional setting parameter. B014 | B030 | B050 | B100 | B150 | B200 SCC4 cell bandwidth"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band_Pcc', enums.OperatingBandC),
			ArgStruct.scalar_int('Dl_Channel_Pcc'),
			ArgStruct.scalar_enum('Bandwidth_Pcc', enums.Bandwidth),
			ArgStruct.scalar_enum_optional('Band_Scc_1', enums.OperatingBandC),
			ArgStruct.scalar_int_optional('Dl_Channel_Scc_1'),
			ArgStruct.scalar_enum_optional('Bandwidth_Scc_1', enums.Bandwidth),
			ArgStruct.scalar_enum_optional('Band_Scc_2', enums.OperatingBandC),
			ArgStruct.scalar_int_optional('Dl_Channel_Scc_2'),
			ArgStruct.scalar_enum_optional('Bandwidth_Scc_2', enums.Bandwidth),
			ArgStruct.scalar_enum_optional('Band_Scc_3', enums.OperatingBandC),
			ArgStruct.scalar_int_optional('Dl_Channel_Scc_3'),
			ArgStruct.scalar_enum_optional('Bandwidth_Scc_3', enums.Bandwidth),
			ArgStruct.scalar_enum_optional('Band_Scc_4', enums.OperatingBandC),
			ArgStruct.scalar_int_optional('Dl_Channel_Scc_4'),
			ArgStruct.scalar_enum_optional('Bandwidth_Scc_4', enums.Bandwidth)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band_Pcc: enums.OperatingBandC = None
			self.Dl_Channel_Pcc: int = None
			self.Bandwidth_Pcc: enums.Bandwidth = None
			self.Band_Scc_1: enums.OperatingBandC = None
			self.Dl_Channel_Scc_1: int = None
			self.Bandwidth_Scc_1: enums.Bandwidth = None
			self.Band_Scc_2: enums.OperatingBandC = None
			self.Dl_Channel_Scc_2: int = None
			self.Bandwidth_Scc_2: enums.Bandwidth = None
			self.Band_Scc_3: enums.OperatingBandC = None
			self.Dl_Channel_Scc_3: int = None
			self.Bandwidth_Scc_3: enums.Bandwidth = None
			self.Band_Scc_4: enums.OperatingBandC = None
			self.Dl_Channel_Scc_4: int = None
			self.Bandwidth_Scc_4: enums.Bandwidth = None

	def get_bw_channel(self) -> BwChannelStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:ALL:BWCHannel \n
		Snippet: value: BwChannelStruct = driver.configure.rfSettings.all.get_bw_channel() \n
		Selects the operating band, the downlink channel number and the cell bandwidth for the PCC and optionally for the SCCs. A
		query returns only the component carriers that are supported by the current scenario. \n
			:return: structure: for return value, see the help for BwChannelStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:RFSettings:ALL:BWCHannel?', self.__class__.BwChannelStruct())

	def set_bw_channel(self, value: BwChannelStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:ALL:BWCHannel \n
		Snippet with structure: \n
		structure = driver.configure.rfSettings.all.BwChannelStruct() \n
		structure.Band_Pcc: enums.OperatingBandC = enums.OperatingBandC.OB1 \n
		structure.Dl_Channel_Pcc: int = 1 \n
		structure.Bandwidth_Pcc: enums.Bandwidth = enums.Bandwidth.B014 \n
		structure.Band_Scc_1: enums.OperatingBandC = enums.OperatingBandC.OB1 \n
		structure.Dl_Channel_Scc_1: int = 1 \n
		structure.Bandwidth_Scc_1: enums.Bandwidth = enums.Bandwidth.B014 \n
		structure.Band_Scc_2: enums.OperatingBandC = enums.OperatingBandC.OB1 \n
		structure.Dl_Channel_Scc_2: int = 1 \n
		structure.Bandwidth_Scc_2: enums.Bandwidth = enums.Bandwidth.B014 \n
		structure.Band_Scc_3: enums.OperatingBandC = enums.OperatingBandC.OB1 \n
		structure.Dl_Channel_Scc_3: int = 1 \n
		structure.Bandwidth_Scc_3: enums.Bandwidth = enums.Bandwidth.B014 \n
		structure.Band_Scc_4: enums.OperatingBandC = enums.OperatingBandC.OB1 \n
		structure.Dl_Channel_Scc_4: int = 1 \n
		structure.Bandwidth_Scc_4: enums.Bandwidth = enums.Bandwidth.B014 \n
		driver.configure.rfSettings.all.set_bw_channel(value = structure) \n
		Selects the operating band, the downlink channel number and the cell bandwidth for the PCC and optionally for the SCCs. A
		query returns only the component carriers that are supported by the current scenario. \n
			:param value: see the help for BwChannelStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:RFSettings:ALL:BWCHannel', value)
