from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfCls:
	"""Rf commands group definition. 20 total commands, 3 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rf", core, parent)

	@property
	def uplink(self):
		"""uplink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	@property
	def bcombination(self):
		"""bcombination commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bcombination'):
			from .Bcombination import BcombinationCls
			self._bcombination = BcombinationCls(self._core, self._cmd_group)
		return self._bcombination

	@property
	def dcSupport(self):
		"""dcSupport commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dcSupport'):
			from .DcSupport import DcSupportCls
			self._dcSupport = DcSupportCls(self._core, self._cmd_group)
		return self._dcSupport

	def get_mt_advance(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:MTADvance \n
		Snippet: value: int = driver.sense.ueCapability.rf.get_mt_advance() \n
		Returns whether the UE supports multiple timing advances. \n
			:return: timing: decimal Comma-separated list of values, one value per band combination (combination 0 to n)
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:MTADvance?')
		return Conversions.str_to_int(response)

	def get_supported(self) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:SUPPorted \n
		Snippet: value: List[bool] = driver.sense.ueCapability.rf.get_supported() \n
		Returns a list of values indicating the support of the individual E-UTRA operating bands by the UE. \n
			:return: supported_band: OFF | ON 256 values: user-defined band, band 1 to band 255
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:SUPPorted?')
		return Conversions.str_to_bool_list(response)

	def get_hduplex(self) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:HDUPlex \n
		Snippet: value: List[bool] = driver.sense.ueCapability.rf.get_hduplex() \n
		Returns a list of values indicating whether the UE supports only half duplex operation for the individual E-UTRA
		operating bands. \n
			:return: half_duplex: OFF | ON 256 values: user-defined band, band 1 to band 255
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:HDUPlex?')
		return Conversions.str_to_bool_list(response)

	def get_downlink(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:DL<qam> \n
		Snippet: value: int = driver.sense.ueCapability.rf.get_downlink() \n
		Returns a list of values indicating whether the UE supports DL 256-QAM in the individual E-UTRA operating bands. \n
			:return: capabilities: 0 | 1 256 values: user-defined band, band 1 to band 255
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:DL256?')
		return Conversions.str_to_int(response)

	def get_fb_retrieval(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:FBRetrieval \n
		Snippet: value: bool = driver.sense.ueCapability.rf.get_fb_retrieval() \n
		Returns whether the UE supports the reception of 'requestedFrequencyBands'. \n
			:return: retrieval: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:FBRetrieval?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_rbands(self) -> List[enums.OperatingBandC]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:RBANds \n
		Snippet: value: List[enums.OperatingBandC] = driver.sense.ueCapability.rf.get_rbands() \n
		Returns all frequency bands requested by E-UTRAN. \n
			:return: requested_bands: UDEFined | OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB250 | OB252 | OB255 Comma-separated list of 64 values Typically, fewer than 64 bands are requested and the remaining values are filled with NAV.
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:RBANds?')
		return Conversions.str_to_list_enum(response, enums.OperatingBandC)

	def get_fbp_adjust(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:FBPadjust \n
		Snippet: value: bool = driver.sense.ueCapability.rf.get_fbp_adjust() \n
		Returns whether the UE supports the prioritization of frequency bands as requested by 'freqBandIndicatorPriority-r12'. \n
			:return: adjustment: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:FBPadjust?')
		return Conversions.str_to_bool(response)

	def get_mmpr_behavior(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:MMPRbehavior \n
		Snippet: value: str = driver.sense.ueCapability.rf.get_mmpr_behavior() \n
		Returns which MPR/A-MPR behaviors the UE supports. \n
			:return: behavior: string Sequence of bits The leftmost bit refers to behavior 0, the next bit to behavior 1, and so on. 1 means supported. 0 means not supported.
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:MMPRbehavior?')
		return trim_str_response(response)

	def get_srtx(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:SRTX \n
		Snippet: value: int = driver.sense.ueCapability.rf.get_srtx() \n
		Returns whether the UE supports the simultaneous reception and transmission on different bands. \n
			:return: simultaneous: 0 | 1 Comma-separated list of values, one value per band combination (combination 0 to n)
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:SRTX?')
		return Conversions.str_to_int(response)

	def get_sncap(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:SNCap \n
		Snippet: value: str = driver.sense.ueCapability.rf.get_sncap() \n
		Returns the bitstring from the element 'supportedNAICS-2CRS-AP'. \n
			:return: naics: string Comma-separated list of strings, one string per band combination (combination 0 to n)
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:SNCap?')
		return trim_str_response(response)

	def clone(self) -> 'RfCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
