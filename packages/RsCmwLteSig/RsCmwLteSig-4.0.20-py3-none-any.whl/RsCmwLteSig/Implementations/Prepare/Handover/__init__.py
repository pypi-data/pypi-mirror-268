from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HandoverCls:
	"""Handover commands group definition. 13 total commands, 3 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("handover", core, parent)

	@property
	def enhanced(self):
		"""enhanced commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enhanced'):
			from .Enhanced import EnhancedCls
			self._enhanced = EnhancedCls(self._core, self._cmd_group)
		return self._enhanced

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	@property
	def external(self):
		"""external commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_external'):
			from .External import ExternalCls
			self._external = ExternalCls(self._core, self._cmd_group)
		return self._external

	def set(self, band: enums.OperatingBandC, dl_channel: int, dl_bandwidth: enums.Bandwidth, add_spec_emission: enums.AddSpectrumEmission) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover \n
		Snippet: driver.prepare.handover.set(band = enums.OperatingBandC.OB1, dl_channel = 1, dl_bandwidth = enums.Bandwidth.B014, add_spec_emission = enums.AddSpectrumEmission.NS01) \n
		Configures the destination parameters for an intra-RAT handover within the LTE signaling application. The duplex mode of
		the destination is the same as the duplex mode of the source. For a handover with duplex mode change, see method
		RsCmwLteSig.Prepare.Handover.Enhanced.set. \n
			:param band: FDD: UDEFined | OB1 | ... | OB28 | OB30 | OB31 | OB65 | OB66 | OB68 | OB70 | ... | OB74 | OB85 | OB87 | OB88 TDD: UDEFined | OB33 | ... | OB45 | OB48 | OB50 | ... | OB53 | OB250 Operating band of the handover destination
			:param dl_channel: decimal DL channel number valid for the selected operating band. The related UL channel number is calculated and set automatically. For channel numbers depending on operating bands, see 'Operating bands'. Range: depends on operating band
			:param dl_bandwidth: B014 | B030 | B050 | B100 | B150 | B200 DL cell bandwidth (also used for UL) 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz, 20 MHz
			:param add_spec_emission: NS01 | ... | NS288 Value signaled to the UE as additional ACLR and spectrum emission requirement
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('band', band, DataType.Enum, enums.OperatingBandC), ArgSingle('dl_channel', dl_channel, DataType.Integer), ArgSingle('dl_bandwidth', dl_bandwidth, DataType.Enum, enums.Bandwidth), ArgSingle('add_spec_emission', add_spec_emission, DataType.Enum, enums.AddSpectrumEmission))
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover {param}'.rstrip())

	# noinspection PyTypeChecker
	class HandoverStruct(StructBase):
		"""Response structure. Fields: \n
			- Band: enums.OperatingBandC: FDD: UDEFined | OB1 | ... | OB28 | OB30 | OB31 | OB65 | OB66 | OB68 | OB70 | ... | OB74 | OB85 | OB87 | OB88 TDD: UDEFined | OB33 | ... | OB45 | OB48 | OB50 | ... | OB53 | OB250 Operating band of the handover destination
			- Dl_Channel: int: decimal DL channel number valid for the selected operating band. The related UL channel number is calculated and set automatically. For channel numbers depending on operating bands, see 'Operating bands'. Range: depends on operating band
			- Dl_Bandwidth: enums.Bandwidth: B014 | B030 | B050 | B100 | B150 | B200 DL cell bandwidth (also used for UL) 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz, 20 MHz
			- Add_Spec_Emission: enums.AddSpectrumEmission: NS01 | ... | NS288 Value signaled to the UE as additional ACLR and spectrum emission requirement"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperatingBandC),
			ArgStruct.scalar_int('Dl_Channel'),
			ArgStruct.scalar_enum('Dl_Bandwidth', enums.Bandwidth),
			ArgStruct.scalar_enum('Add_Spec_Emission', enums.AddSpectrumEmission)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperatingBandC = None
			self.Dl_Channel: int = None
			self.Dl_Bandwidth: enums.Bandwidth = None
			self.Add_Spec_Emission: enums.AddSpectrumEmission = None

	def get(self) -> HandoverStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover \n
		Snippet: value: HandoverStruct = driver.prepare.handover.get() \n
		Configures the destination parameters for an intra-RAT handover within the LTE signaling application. The duplex mode of
		the destination is the same as the duplex mode of the source. For a handover with duplex mode change, see method
		RsCmwLteSig.Prepare.Handover.Enhanced.set. \n
			:return: structure: for return value, see the help for HandoverStruct structure arguments."""
		return self._core.io.query_struct(f'PREPare:LTE:SIGNaling<Instance>:HANDover?', self.__class__.HandoverStruct())

	def get_destination(self) -> str:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:DESTination \n
		Snippet: value: str = driver.prepare.handover.get_destination() \n
		Selects the handover destination. A complete list of all supported values can be displayed using method RsCmwLteSig.
		Prepare.Handover.Catalog.destination. \n
			:return: destination: string
		"""
		response = self._core.io.query_str('PREPare:LTE:SIGNaling<Instance>:HANDover:DESTination?')
		return trim_str_response(response)

	def set_destination(self, destination: str) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:DESTination \n
		Snippet: driver.prepare.handover.set_destination(destination = 'abc') \n
		Selects the handover destination. A complete list of all supported values can be displayed using method RsCmwLteSig.
		Prepare.Handover.Catalog.destination. \n
			:param destination: string
		"""
		param = Conversions.value_to_quoted_str(destination)
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:DESTination {param}')

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.HandoverMode:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:MMODe \n
		Snippet: value: enums.HandoverMode = driver.prepare.handover.get_mmode() \n
		Selects the mechanism to be used for handover to another signaling application. \n
			:return: mode: REDirection | MTCSfallback | HANDover
		"""
		response = self._core.io.query_str('PREPare:LTE:SIGNaling<Instance>:HANDover:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.HandoverMode)

	def set_mmode(self, mode: enums.HandoverMode) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:MMODe \n
		Snippet: driver.prepare.handover.set_mmode(mode = enums.HandoverMode.HANDover) \n
		Selects the mechanism to be used for handover to another signaling application. \n
			:param mode: REDirection | MTCSfallback | HANDover
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HandoverMode)
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:MMODe {param}')

	# noinspection PyTypeChecker
	def get_ctype(self) -> enums.VolteHandoverType:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:CTYPe \n
		Snippet: value: enums.VolteHandoverType = driver.prepare.handover.get_ctype() \n
		Selects the call type to be set up at the destination, for handover of VoLTE calls. \n
			:return: type_py: PSData | PSVolte PSData: E2E packet data connection PSVolte: Voice call, use handover with SRVCC
		"""
		response = self._core.io.query_str('PREPare:LTE:SIGNaling<Instance>:HANDover:CTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.VolteHandoverType)

	def set_ctype(self, type_py: enums.VolteHandoverType) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:CTYPe \n
		Snippet: driver.prepare.handover.set_ctype(type_py = enums.VolteHandoverType.PSData) \n
		Selects the call type to be set up at the destination, for handover of VoLTE calls. \n
			:param type_py: PSData | PSVolte PSData: E2E packet data connection PSVolte: Voice call, use handover with SRVCC
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.VolteHandoverType)
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:CTYPe {param}')

	def clone(self) -> 'HandoverCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HandoverCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
