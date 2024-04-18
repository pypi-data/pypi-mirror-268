from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlayerCls:
	"""Player commands group definition. 29 total commands, 0 Subgroups, 29 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("player", core, parent)

	def get_uta_supported(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:UTASupported \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_uta_supported() \n
		Returns whether the UE supports transmit antenna selection or not. \n
			:return: ue_tx_ant_sel_supp: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:UTASupported?')
		return Conversions.str_to_bool(response)

	def get_usrs_support(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:USRSsupport \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_usrs_support() \n
		Returns whether the UE supports PDSCH transmission mode 7 for FDD or not. \n
			:return: ue_sp_ref_sigs_supp: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:USRSsupport?')
		return Conversions.str_to_bool(response)

	def get_edlf_support(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:EDLFsupport \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_edlf_support() \n
		Returns whether the UE supports enhanced dual layer (PDSCH TM 8) for FDD or not. \n
			:return: en_dual_lay_fdd_sup: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:EDLFsupport?')
		return Conversions.str_to_bool(response)

	def get_edlt_support(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:EDLTsupport \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_edlt_support() \n
		Returns whether the UE supports enhanced dual layer (PDSCH TM 8) for TDD or not. \n
			:return: en_dual_lay_tdd_sup: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:EDLTsupport?')
		return Conversions.str_to_bool(response)

	def get_tapp_support(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:TAPPsupport \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_tapp_support() \n
		Returns whether the UE supports transmit diversity for specific PUCCH formats. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:TAPPsupport?')
		return Conversions.str_to_bool(response)

	def get_twef_support(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:TWEFsupport \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_twef_support() \n
		Returns whether the UE supports PDSCH TM 9 with 8 CSI reference signal ports for FDD. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:TWEFsupport?')
		return Conversions.str_to_bool(response)

	def get_pd_support(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:PDSupport \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_pd_support() \n
		Returns whether the UE supports PMI disabling. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:PDSupport?')
		return Conversions.str_to_bool(response)

	def get_ccs_support(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:CCSSupport \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_ccs_support() \n
		Returns whether the UE supports cross-carrier scheduling for CA. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:CCSSupport?')
		return Conversions.str_to_bool(response)

	def get_spp_support(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:SPPSupport \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_spp_support() \n
		Returns whether the UE supports the simultaneous transmission of PUCCH and PUSCH. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:SPPSupport?')
		return Conversions.str_to_bool(response)

	def get_mcpc_support(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:MCPCsupport \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_mcpc_support() \n
		Returns whether the UE supports multi-cluster PUSCH transmission within a CC. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:MCPCsupport?')
		return Conversions.str_to_bool(response)

	def get_nurc_list(self) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:NURClist \n
		Snippet: value: List[bool] = driver.sense.ueCapability.player.get_nurc_list() \n
		Returns a list of values, indicating whether the UE supports non-contiguous UL resource allocations within a CC for the
		individual E-UTRA operating bands. \n
			:return: supported_band: OFF | ON 256 values: user-defined band, band 1 to band 255
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:NURClist?')
		return Conversions.str_to_bool_list(response)

	def get_cihandl(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:CIHandl \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_cihandl() \n
		Returns whether the UE supports CRS interference handling. \n
			:return: intf_handle: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:CIHandl?')
		return Conversions.str_to_bool(response)

	def get_epdcch(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:EPDCch \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_epdcch() \n
		Returns whether the UE supports DCI reception via UE-specific search space on enhanced PDCCH. \n
			:return: epdcch: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:EPDCch?')
		return Conversions.str_to_bool(response)

	def get_mac_reporting(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:MACReporting \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_mac_reporting() \n
		Returns whether the UE supports multi-cell HARQ ACK, periodic CSI reporting and SR on PUCCH format 3. \n
			:return: reporting: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:MACReporting?')
		return Conversions.str_to_bool(response)

	def get_sci_handl(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:SCIHandl \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_sci_handl() \n
		Returns whether the UE supports synchronization signal and common channel interference handling. \n
			:return: handle: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:SCIHandl?')
		return Conversions.str_to_bool(response)

	def get_ts_subframe(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:TSSubframe \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_ts_subframe() \n
		Returns whether the UE supports TDD special subframe as defined in 3GPP TS 36.211. \n
			:return: tdd_special_sf: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:TSSubframe?')
		return Conversions.str_to_bool(response)

	def get_tdpch_select(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:TDPChselect \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_tdpch_select() \n
		Returns whether the UE supports transmit diversity for PUCCH format 1b with channel selection. \n
			:return: tdpch: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:TDPChselect?')
		return Conversions.str_to_bool(response)

	def get_ul_comp(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:ULComp \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_ul_comp() \n
		Returns whether the UE supports UL coordinated multi-point operation. \n
			:return: comp: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:ULComp?')
		return Conversions.str_to_bool(response)

	def get_itc_with_diff(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:ITCWithdiff \n
		Snippet: value: str = driver.sense.ueCapability.player.get_itc_with_diff() \n
		Returns whether the UE supports inter-band TDD CA with different UL/DL configuration combinations. \n
			:return: inter_band: string Two bits, for example 'b00' or 'b01'
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:ITCWithdiff?')
		return trim_str_response(response)

	def get_ehpfdd(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:EHPFdd \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_ehpfdd() \n
		Returns whether the UE supports enhanced HARQ pattern for TTI bundling operation for FDD. \n
			:return: eh_pattern: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:EHPFdd?')
		return Conversions.str_to_bool(response)

	def get_eftcodebook(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:EFTCodebook \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_eftcodebook() \n
		Returns whether the UE supports enhanced 4 TX codebook. \n
			:return: codebook: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:EFTCodebook?')
		return Conversions.str_to_bool(response)

	def get_tfc_pcell_dplx(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:TFCPcelldplx \n
		Snippet: value: str = driver.sense.ueCapability.player.get_tfc_pcell_dplx() \n
		Returns whether the UE supports PCell in any supported band combination including at least one FDD band and at least one
		TDD band. \n
			:return: cell_duplex: string Two bits, for example 'b00' or 'b10'
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:TFCPcelldplx?')
		return trim_str_response(response)

	def get_trc_tddp_cell(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:TRCTddpcell \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_trc_tddp_cell() \n
		Returns whether the UE supports TDD UL/DL reconfiguration for TDD serving cell via monitoring PDCCH on a TDD PCell. \n
			:return: pcell: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:TRCTddpcell?')
		return Conversions.str_to_bool(response)

	def get_trc_fddp_cell(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:TRCFddpcell \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_trc_fddp_cell() \n
		Returns whether the UE supports TDD UL/DL reconfiguration for TDD serving cell via monitoring PDCCH on an FDD PCell. \n
			:return: pcell: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:TRCFddpcell?')
		return Conversions.str_to_bool(response)

	def get_pf_mode(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:PFMode \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_pf_mode() \n
		Returns whether the UE supports PUSCH feedback mode 3-2. \n
			:return: mode: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:PFMode?')
		return Conversions.str_to_bool(response)

	def get_pspsf_set(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:PSPSfset \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_pspsf_set() \n
		Returns whether the UE supports subframe set dependent UL power control for PUSCH and SRS. \n
			:return: sf_set: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:PSPSfset?')
		return Conversions.str_to_bool(response)

	def get_csf_set(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:CSFSet \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_csf_set() \n
		Returns whether the UE supports R12 DL CSI subframe set configuration. \n
			:return: sub_frame_set: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:CSFSet?')
		return Conversions.str_to_bool(response)

	def get_nrrt(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:NRRT \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_nrrt() \n
		Returns whether the UE supports TTI bundling without resource allocation restriction. \n
			:return: norr: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:NRRT?')
		return Conversions.str_to_bool(response)

	def get_dsd_cell(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PLAYer:DSDCell \n
		Snippet: value: bool = driver.sense.ueCapability.player.get_dsd_cell() \n
		Returns whether the UE supports discovery signal detection for deactivated SCells. \n
			:return: discovery: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PLAYer:DSDCell?')
		return Conversions.str_to_bool(response)
