from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnhancedCls:
	"""Enhanced commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enhanced", core, parent)

	def set(self, duplex_mode: enums.DuplexMode, band: enums.OperatingBandC, dl_channel: int, dl_bandwidth: enums.Bandwidth, add_spec_emission: enums.AddSpectrumEmission) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:ENHanced \n
		Snippet: driver.prepare.handover.enhanced.set(duplex_mode = enums.DuplexMode.FDD, band = enums.OperatingBandC.OB1, dl_channel = 1, dl_bandwidth = enums.Bandwidth.B014, add_spec_emission = enums.AddSpectrumEmission.NS01) \n
		Configures the destination parameters for an intra-RAT handover within the LTE signaling application. The duplex mode of
		the destination is configurable. \n
			:param duplex_mode: FDD | TDD Duplex mode of the handover destination
			:param band: FDD: UDEFined | OB1 | ... | OB28 | OB30 | OB31 | OB65 | OB66 | OB68 | OB70 | ... | OB74 | OB85 | OB87 | OB88 TDD: UDEFined | OB33 | ... | OB45 | OB48 | OB50 | ... | OB53 | OB250 Operating band of the handover destination
			:param dl_channel: decimal DL channel number valid for the selected operating band. The related UL channel number is calculated and set automatically. For channel numbers depending on operating bands, see 'Operating bands'. Range: depends on operating band
			:param dl_bandwidth: B014 | B030 | B050 | B100 | B150 | B200 DL cell bandwidth (also used for UL) 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz, 20 MHz
			:param add_spec_emission: NS01 | ... | NS288 Value signaled to the UE as additional ACLR and spectrum emission requirement
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('duplex_mode', duplex_mode, DataType.Enum, enums.DuplexMode), ArgSingle('band', band, DataType.Enum, enums.OperatingBandC), ArgSingle('dl_channel', dl_channel, DataType.Integer), ArgSingle('dl_bandwidth', dl_bandwidth, DataType.Enum, enums.Bandwidth), ArgSingle('add_spec_emission', add_spec_emission, DataType.Enum, enums.AddSpectrumEmission))
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:ENHanced {param}'.rstrip())

	# noinspection PyTypeChecker
	class EnhancedStruct(StructBase):
		"""Response structure. Fields: \n
			- Duplex_Mode: enums.DuplexMode: FDD | TDD Duplex mode of the handover destination
			- Band: enums.OperatingBandC: FDD: UDEFined | OB1 | ... | OB28 | OB30 | OB31 | OB65 | OB66 | OB68 | OB70 | ... | OB74 | OB85 | OB87 | OB88 TDD: UDEFined | OB33 | ... | OB45 | OB48 | OB50 | ... | OB53 | OB250 Operating band of the handover destination
			- Dl_Channel: int: decimal DL channel number valid for the selected operating band. The related UL channel number is calculated and set automatically. For channel numbers depending on operating bands, see 'Operating bands'. Range: depends on operating band
			- Dl_Bandwidth: enums.Bandwidth: B014 | B030 | B050 | B100 | B150 | B200 DL cell bandwidth (also used for UL) 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz, 20 MHz
			- Add_Spec_Emission: enums.AddSpectrumEmission: NS01 | ... | NS288 Value signaled to the UE as additional ACLR and spectrum emission requirement"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexMode),
			ArgStruct.scalar_enum('Band', enums.OperatingBandC),
			ArgStruct.scalar_int('Dl_Channel'),
			ArgStruct.scalar_enum('Dl_Bandwidth', enums.Bandwidth),
			ArgStruct.scalar_enum('Add_Spec_Emission', enums.AddSpectrumEmission)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Duplex_Mode: enums.DuplexMode = None
			self.Band: enums.OperatingBandC = None
			self.Dl_Channel: int = None
			self.Dl_Bandwidth: enums.Bandwidth = None
			self.Add_Spec_Emission: enums.AddSpectrumEmission = None

	def get(self) -> EnhancedStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:ENHanced \n
		Snippet: value: EnhancedStruct = driver.prepare.handover.enhanced.get() \n
		Configures the destination parameters for an intra-RAT handover within the LTE signaling application. The duplex mode of
		the destination is configurable. \n
			:return: structure: for return value, see the help for EnhancedStruct structure arguments."""
		return self._core.io.query_struct(f'PREPare:LTE:SIGNaling<Instance>:HANDover:ENHanced?', self.__class__.EnhancedStruct())
