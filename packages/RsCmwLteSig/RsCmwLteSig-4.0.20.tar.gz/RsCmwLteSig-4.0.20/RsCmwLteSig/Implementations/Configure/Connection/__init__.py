from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectionCls:
	"""Connection commands group definition. 287 total commands, 13 Subgroups, 33 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connection", core, parent)

	@property
	def nta(self):
		"""nta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nta'):
			from .Nta import NtaCls
			self._nta = NtaCls(self._core, self._cmd_group)
		return self._nta

	@property
	def rohc(self):
		"""rohc commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_rohc'):
			from .Rohc import RohcCls
			self._rohc = RohcCls(self._core, self._cmd_group)
		return self._rohc

	@property
	def pcc(self):
		"""pcc commands group. 23 Sub-classes, 8 commands."""
		if not hasattr(self, '_pcc'):
			from .Pcc import PccCls
			self._pcc = PccCls(self._core, self._cmd_group)
		return self._pcc

	@property
	def easy(self):
		"""easy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_easy'):
			from .Easy import EasyCls
			self._easy = EasyCls(self._core, self._cmd_group)
		return self._easy

	@property
	def tdBearer(self):
		"""tdBearer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdBearer'):
			from .TdBearer import TdBearerCls
			self._tdBearer = TdBearerCls(self._core, self._cmd_group)
		return self._tdBearer

	@property
	def sipHandling(self):
		"""sipHandling commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sipHandling'):
			from .SipHandling import SipHandlingCls
			self._sipHandling = SipHandlingCls(self._core, self._cmd_group)
		return self._sipHandling

	@property
	def cdrx(self):
		"""cdrx commands group. 1 Sub-classes, 9 commands."""
		if not hasattr(self, '_cdrx'):
			from .Cdrx import CdrxCls
			self._cdrx = CdrxCls(self._core, self._cmd_group)
		return self._cdrx

	@property
	def scc(self):
		"""scc commands group. 29 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .Scc import SccCls
			self._scc = SccCls(self._core, self._cmd_group)
		return self._scc

	@property
	def uePosition(self):
		"""uePosition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uePosition'):
			from .UePosition import UePositionCls
			self._uePosition = UePositionCls(self._core, self._cmd_group)
		return self._uePosition

	@property
	def ueCategory(self):
		"""ueCategory commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueCategory'):
			from .UeCategory import UeCategoryCls
			self._ueCategory = UeCategoryCls(self._core, self._cmd_group)
		return self._ueCategory

	@property
	def edau(self):
		"""edau commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_edau'):
			from .Edau import EdauCls
			self._edau = EdauCls(self._core, self._cmd_group)
		return self._edau

	@property
	def csfb(self):
		"""csfb commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_csfb'):
			from .Csfb import CsfbCls
			self._csfb = CsfbCls(self._core, self._cmd_group)
		return self._csfb

	@property
	def harq(self):
		"""harq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import HarqCls
			self._harq = HarqCls(self._core, self._cmd_group)
		return self._harq

	def get_ded_bearer(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:DEDBearer \n
		Snippet: value: str = driver.configure.connection.get_ded_bearer() \n
		Selects a dedicated bearer as a preparation for a bearer release via CALL:LTE:SIGN:PSWitched:ACTion DISConnect. \n
			:return: idn: string Dedicated bearer ID Example: '6 (-5, Voice) ' To query a list of IDs for all established dedicated bearers, see method RsCmwLteSig.Catalog.Connection.dedBearer.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:DEDBearer?')
		return trim_str_response(response)

	def set_ded_bearer(self, idn: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:DEDBearer \n
		Snippet: driver.configure.connection.set_ded_bearer(idn = 'abc') \n
		Selects a dedicated bearer as a preparation for a bearer release via CALL:LTE:SIGN:PSWitched:ACTion DISConnect. \n
			:param idn: string Dedicated bearer ID Example: '6 (-5, Voice) ' To query a list of IDs for all established dedicated bearers, see method RsCmwLteSig.Catalog.Connection.dedBearer.
		"""
		param = Conversions.value_to_quoted_str(idn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:DEDBearer {param}')

	# noinspection PyTypeChecker
	def get_rlc_mode(self) -> enums.RlcMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:RLCMode \n
		Snippet: value: enums.RlcMode = driver.configure.connection.get_rlc_mode() \n
		Selects the RLC mode for downlink transmissions (default bearer) . \n
			:return: mode: UM | AM UM: unacknowledged mode AM: acknowledged mode
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:RLCMode?')
		return Conversions.str_to_scalar_enum(response, enums.RlcMode)

	def set_rlc_mode(self, mode: enums.RlcMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:RLCMode \n
		Snippet: driver.configure.connection.set_rlc_mode(mode = enums.RlcMode.AM) \n
		Selects the RLC mode for downlink transmissions (default bearer) . \n
			:param mode: UM | AM UM: unacknowledged mode AM: acknowledged mode
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.RlcMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:RLCMode {param}')

	# noinspection PyTypeChecker
	def get_ip_version(self) -> enums.IpVersion:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:IPVersion \n
		Snippet: value: enums.IpVersion = driver.configure.connection.get_ip_version() \n
		Configures the allowed IP versions for default bearers and data application tests. In test mode, the setting is fixed and
		can only be queried. \n
			:return: ip_version: IPV4 | IPV6 | IPV46 IPV4: IPV4 only IPV6: IPV6 only IPV46: IPv4 and IPv6
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:IPVersion?')
		return Conversions.str_to_scalar_enum(response, enums.IpVersion)

	def set_ip_version(self, ip_version: enums.IpVersion) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:IPVersion \n
		Snippet: driver.configure.connection.set_ip_version(ip_version = enums.IpVersion.IPV4) \n
		Configures the allowed IP versions for default bearers and data application tests. In test mode, the setting is fixed and
		can only be queried. \n
			:param ip_version: IPV4 | IPV6 | IPV46 IPV4: IPV4 only IPV6: IPV6 only IPV46: IPv4 and IPv6
		"""
		param = Conversions.enum_scalar_to_str(ip_version, enums.IpVersion)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:IPVersion {param}')

	def get_apn(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:APN \n
		Snippet: value: str = driver.configure.connection.get_apn() \n
		Configures the default APN for default bearers and data application tests. In test mode, the setting is fixed and can
		only be queried. \n
			:return: apn: string APN default value
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:APN?')
		return trim_str_response(response)

	def set_apn(self, apn: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:APN \n
		Snippet: driver.configure.connection.set_apn(apn = 'abc') \n
		Configures the default APN for default bearers and data application tests. In test mode, the setting is fixed and can
		only be queried. \n
			:param apn: string APN default value
		"""
		param = Conversions.value_to_quoted_str(apn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:APN {param}')

	def get_qci(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:QCI \n
		Snippet: value: int = driver.configure.connection.get_qci() \n
		Configures the QCI value for default bearers and data application tests. In test mode, the setting is fixed and can only
		be queried. \n
			:return: qci: numeric Quality-of-service class identifier Range: 5 to 9
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:QCI?')
		return Conversions.str_to_int(response)

	def set_qci(self, qci: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:QCI \n
		Snippet: driver.configure.connection.set_qci(qci = 1) \n
		Configures the QCI value for default bearers and data application tests. In test mode, the setting is fixed and can only
		be queried. \n
			:param qci: numeric Quality-of-service class identifier Range: 5 to 9
		"""
		param = Conversions.decimal_value_to_str(qci)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:QCI {param}')

	def get_ud_scheduling(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UDSCheduling \n
		Snippet: value: bool = driver.configure.connection.get_ud_scheduling() \n
		Enables or disables uplink dynamic scheduling. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:UDSCheduling?')
		return Conversions.str_to_bool(response)

	def set_ud_scheduling(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UDSCheduling \n
		Snippet: driver.configure.connection.set_ud_scheduling(enable = False) \n
		Enables or disables uplink dynamic scheduling. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UDSCheduling {param}')

	def get_iugnrb(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:IUGNrb \n
		Snippet: value: int = driver.configure.connection.get_iugnrb() \n
		Configures the number of resource blocks for the first UL grant after an UL grant request of the UE (uplink dynamic
		scheduling) . \n
			:return: nrb: decimal Range: 0 to 100 (depends on cell BW)
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:IUGNrb?')
		return Conversions.str_to_int(response)

	def set_iugnrb(self, nrb: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:IUGNrb \n
		Snippet: driver.configure.connection.set_iugnrb(nrb = 1) \n
		Configures the number of resource blocks for the first UL grant after an UL grant request of the UE (uplink dynamic
		scheduling) . \n
			:param nrb: decimal Range: 0 to 100 (depends on cell BW)
		"""
		param = Conversions.decimal_value_to_str(nrb)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:IUGNrb {param}')

	def get_iugmcsidx(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:IUGMcsidx \n
		Snippet: value: int = driver.configure.connection.get_iugmcsidx() \n
		Configures the MCS index value for the first UL grant after an UL grant request of the UE (uplink dynamic scheduling) . \n
			:return: mcs_index: numeric Range: 0 to 28
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:IUGMcsidx?')
		return Conversions.str_to_int(response)

	def set_iugmcsidx(self, mcs_index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:IUGMcsidx \n
		Snippet: driver.configure.connection.set_iugmcsidx(mcs_index = 1) \n
		Configures the MCS index value for the first UL grant after an UL grant request of the UE (uplink dynamic scheduling) . \n
			:param mcs_index: numeric Range: 0 to 28
		"""
		param = Conversions.decimal_value_to_str(mcs_index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:IUGMcsidx {param}')

	# noinspection PyTypeChecker
	def get_uet_selection(self) -> enums.TransmitAntenaSelection:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UETSelection \n
		Snippet: value: enums.TransmitAntenaSelection = driver.configure.connection.get_uet_selection() \n
		Configures the parameter 'ue-TransmitAntennaSelection' signaled to the UE. \n
			:return: selection: OFF | OLOop OFF UE transmit antenna selection not allowed OLOop Open-loop UE transmit antenna selection
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:UETSelection?')
		return Conversions.str_to_scalar_enum(response, enums.TransmitAntenaSelection)

	def set_uet_selection(self, selection: enums.TransmitAntenaSelection) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UETSelection \n
		Snippet: driver.configure.connection.set_uet_selection(selection = enums.TransmitAntenaSelection.OFF) \n
		Configures the parameter 'ue-TransmitAntennaSelection' signaled to the UE. \n
			:param selection: OFF | OLOop OFF UE transmit antenna selection not allowed OLOop Open-loop UE transmit antenna selection
		"""
		param = Conversions.enum_scalar_to_str(selection, enums.TransmitAntenaSelection)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UETSelection {param}')

	def get_srpr_index(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SRPRindex \n
		Snippet: value: int = driver.configure.connection.get_srpr_index() \n
		Specifies the 'sr-PUCCH ResourceIndex'. \n
			:return: index: integer Range: 0 to 2047
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:SRPRindex?')
		return Conversions.str_to_int(response)

	def set_srpr_index(self, index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SRPRindex \n
		Snippet: driver.configure.connection.set_srpr_index(index = 1) \n
		Specifies the 'sr-PUCCH ResourceIndex'. \n
			:param index: integer Range: 0 to 2047
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SRPRindex {param}')

	def get_src_index(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SRCindex \n
		Snippet: value: int = driver.configure.connection.get_src_index() \n
		Specifies the 'sr-ConfigIndex'. \n
			:return: index: integer Range: 0 to 157
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:SRCindex?')
		return Conversions.str_to_int(response)

	def set_src_index(self, index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SRCindex \n
		Snippet: driver.configure.connection.set_src_index(index = 1) \n
		Specifies the 'sr-ConfigIndex'. \n
			:param index: integer Range: 0 to 157
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SRCindex {param}')

	def get_ta_control(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:TAControl \n
		Snippet: value: bool = driver.configure.connection.get_ta_control() \n
		Enables the correction of a changing UL frame timing via timing advance commands. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:TAControl?')
		return Conversions.str_to_bool(response)

	def set_ta_control(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:TAControl \n
		Snippet: driver.configure.connection.set_ta_control(enable = False) \n
		Enables the correction of a changing UL frame timing via timing advance commands. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:TAControl {param}')

	def get_idchsindic(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:IDCHsindic \n
		Snippet: value: bool = driver.configure.connection.get_idchsindic() \n
		Enables sending the information element 'idc-HardwareSharingIndication' to the UE. \n
			:return: indication: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:IDCHsindic?')
		return Conversions.str_to_bool(response)

	def set_idchsindic(self, indication: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:IDCHsindic \n
		Snippet: driver.configure.connection.set_idchsindic(indication = False) \n
		Enables sending the information element 'idc-HardwareSharingIndication' to the UE. \n
			:param indication: OFF | ON
		"""
		param = Conversions.bool_to_str(indication)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:IDCHsindic {param}')

	# noinspection PyTypeChecker
	def get_sibre_config(self) -> enums.UeChangesType:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SIBReconfig \n
		Snippet: value: enums.UeChangesType = driver.configure.connection.get_sibre_config() \n
		Selects a method for information of the UE about changes in the system information, resulting from modified parameters:
		SIB paging or RRC reconfiguration. \n
			:return: type_py: SIBPaging | RRCReconfig
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:SIBReconfig?')
		return Conversions.str_to_scalar_enum(response, enums.UeChangesType)

	def set_sibre_config(self, type_py: enums.UeChangesType) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SIBReconfig \n
		Snippet: driver.configure.connection.set_sibre_config(type_py = enums.UeChangesType.RRCReconfig) \n
		Selects a method for information of the UE about changes in the system information, resulting from modified parameters:
		SIB paging or RRC reconfiguration. \n
			:param type_py: SIBPaging | RRCReconfig
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.UeChangesType)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SIBReconfig {param}')

	def get_ghopping(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:GHOPping \n
		Snippet: value: bool = driver.configure.connection.get_ghopping() \n
		Enables or disables group hopping. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:GHOPping?')
		return Conversions.str_to_bool(response)

	def set_ghopping(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:GHOPping \n
		Snippet: driver.configure.connection.set_ghopping(enable = False) \n
		Enables or disables group hopping. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:GHOPping {param}')

	def get_psm_allowed(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:PSMallowed \n
		Snippet: value: bool = driver.configure.connection.get_psm_allowed() \n
		Specifies whether a UE request for power-saving mode is accepted or rejected. \n
			:return: allowed: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PSMallowed?')
		return Conversions.str_to_bool(response)

	def set_psm_allowed(self, allowed: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:PSMallowed \n
		Snippet: driver.configure.connection.set_psm_allowed(allowed = False) \n
		Specifies whether a UE request for power-saving mode is accepted or rejected. \n
			:param allowed: OFF | ON
		"""
		param = Conversions.bool_to_str(allowed)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PSMallowed {param}')

	def get_iemergency(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:IEMergency \n
		Snippet: value: bool = driver.configure.connection.get_iemergency() \n
		Enables the optional field 'ims-EmergencySupport-r9' in system information block 1. \n
			:return: enable: OFF | ON OFF: field omitted ON: field included
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:IEMergency?')
		return Conversions.str_to_bool(response)

	def set_iemergency(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:IEMergency \n
		Snippet: driver.configure.connection.set_iemergency(enable = False) \n
		Enables the optional field 'ims-EmergencySupport-r9' in system information block 1. \n
			:param enable: OFF | ON OFF: field omitted ON: field included
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:IEMergency {param}')

	def get_eoi_support(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:EOISupport \n
		Snippet: value: bool = driver.configure.connection.get_eoi_support() \n
		Enables the optional field 'eCallOverIMS-Support-r14' in system information block 1. \n
			:return: support: OFF | ON OFF: field omitted ON: field included
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:EOISupport?')
		return Conversions.str_to_bool(response)

	def set_eoi_support(self, support: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:EOISupport \n
		Snippet: driver.configure.connection.set_eoi_support(support = False) \n
		Enables the optional field 'eCallOverIMS-Support-r14' in system information block 1. \n
			:param support: OFF | ON OFF: field omitted ON: field included
		"""
		param = Conversions.bool_to_str(support)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:EOISupport {param}')

	def get_sdnspco(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SDNSpco \n
		Snippet: value: bool = driver.configure.connection.get_sdnspco() \n
		Enables or disables sending of a DNS IP address to the UE. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:SDNSpco?')
		return Conversions.str_to_bool(response)

	def set_sdnspco(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SDNSpco \n
		Snippet: driver.configure.connection.set_sdnspco(enable = False) \n
		Enables or disables sending of a DNS IP address to the UE. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SDNSpco {param}')

	# noinspection PyTypeChecker
	def get_dp_cycle(self) -> enums.DpCycle:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:DPCYcle \n
		Snippet: value: enums.DpCycle = driver.configure.connection.get_dp_cycle() \n
		Selects the cell-specific default paging cycle. \n
			:return: cycle: P032 | P064 | P128 | P256 32, 64, 128 or 256 radio frames
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:DPCYcle?')
		return Conversions.str_to_scalar_enum(response, enums.DpCycle)

	def set_dp_cycle(self, cycle: enums.DpCycle) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:DPCYcle \n
		Snippet: driver.configure.connection.set_dp_cycle(cycle = enums.DpCycle.P032) \n
		Selects the cell-specific default paging cycle. \n
			:param cycle: P032 | P064 | P128 | P256 32, 64, 128 or 256 radio frames
		"""
		param = Conversions.enum_scalar_to_str(cycle, enums.DpCycle)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:DPCYcle {param}')

	# noinspection PyTypeChecker
	def get_pcnb(self) -> enums.NbValue:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:PCNB \n
		Snippet: value: enums.NbValue = driver.configure.connection.get_pcnb() \n
		Configures the field 'nB' in the 'PCCH-Config' in system information block 2. \n
			:return: value: NB4T | NB2T | NBT | NBT2 | NBT4 | NBT8 | NBT16 | NBT32 | NBT64 | NBT128 | NBT256 4T, 2T, T, T/2, T/4, T/8, T/16, T/32, T/64, T/128, T/256 The values NBT64, NBT128 and NBT256 are only allowed for eMTC. And they are only allowed, if the default paging cycle has the same or a greater value. Example: NBT64 needs cycle ≥ P064.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCNB?')
		return Conversions.str_to_scalar_enum(response, enums.NbValue)

	def set_pcnb(self, value: enums.NbValue) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:PCNB \n
		Snippet: driver.configure.connection.set_pcnb(value = enums.NbValue.NB2T) \n
		Configures the field 'nB' in the 'PCCH-Config' in system information block 2. \n
			:param value: NB4T | NB2T | NBT | NBT2 | NBT4 | NBT8 | NBT16 | NBT32 | NBT64 | NBT128 | NBT256 4T, 2T, T, T/2, T/4, T/8, T/16, T/32, T/64, T/128, T/256 The values NBT64, NBT128 and NBT256 are only allowed for eMTC. And they are only allowed, if the default paging cycle has the same or a greater value. Example: NBT64 needs cycle ≥ P064.
		"""
		param = Conversions.enum_scalar_to_str(value, enums.NbValue)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCNB {param}')

	# noinspection PyTypeChecker
	def get_ctype(self) -> enums.ConnectionType:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CTYPe \n
		Snippet: value: enums.ConnectionType = driver.configure.connection.get_ctype() \n
		Selects the connection type to be applied. \n
			:return: type_py: TESTmode | DAPPlication TESTmode: for signaling tests not involving the DAU DAPPlication: for data application measurements using the DAU
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.ConnectionType)

	def set_ctype(self, type_py: enums.ConnectionType) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CTYPe \n
		Snippet: driver.configure.connection.set_ctype(type_py = enums.ConnectionType.DAPPlication) \n
		Selects the connection type to be applied. \n
			:param type_py: TESTmode | DAPPlication TESTmode: for signaling tests not involving the DAU DAPPlication: for data application measurements using the DAU
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ConnectionType)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CTYPe {param}')

	def get_krrc(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:KRRC \n
		Snippet: value: bool = driver.configure.connection.get_krrc() \n
		Selects whether the RRC connection is kept or released after attach. \n
			:return: enable: OFF | ON OFF: The RRC connection is released. ON: The RRC connection is kept.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:KRRC?')
		return Conversions.str_to_bool(response)

	def set_krrc(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:KRRC \n
		Snippet: driver.configure.connection.set_krrc(enable = False) \n
		Selects whether the RRC connection is kept or released after attach. \n
			:param enable: OFF | ON OFF: The RRC connection is released. ON: The RRC connection is kept.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:KRRC {param}')

	def get_ri_timer(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:RITimer \n
		Snippet: value: int = driver.configure.connection.get_ri_timer() \n
		Configures the inactivity timeout for disabled 'Keep RRC Connection' (CONFigure:LTE:SIGN:CONNection:KRRC OFF) . \n
			:return: time: integer Range: 1 s to 255 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:RITimer?')
		return Conversions.str_to_int(response)

	def set_ri_timer(self, time: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:RITimer \n
		Snippet: driver.configure.connection.set_ri_timer(time = 1) \n
		Configures the inactivity timeout for disabled 'Keep RRC Connection' (CONFigure:LTE:SIGN:CONNection:KRRC OFF) . \n
			:param time: integer Range: 1 s to 255 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:RITimer {param}')

	# noinspection PyTypeChecker
	def get_fcoefficient(self) -> enums.FilterCoefficient:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:FCOefficient \n
		Snippet: value: enums.FilterCoefficient = driver.configure.connection.get_fcoefficient() \n
		Selects the value to be sent to the UE as 'filterCoefficient' in RRC messages containing this information element. \n
			:return: filter_py: FC4 | FC8
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:FCOefficient?')
		return Conversions.str_to_scalar_enum(response, enums.FilterCoefficient)

	def set_fcoefficient(self, filter_py: enums.FilterCoefficient) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:FCOefficient \n
		Snippet: driver.configure.connection.set_fcoefficient(filter_py = enums.FilterCoefficient.FC4) \n
		Selects the value to be sent to the UE as 'filterCoefficient' in RRC messages containing this information element. \n
			:param filter_py: FC4 | FC8
		"""
		param = Conversions.enum_scalar_to_str(filter_py, enums.FilterCoefficient)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:FCOefficient {param}')

	def get_tmode(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:TMODe \n
		Snippet: value: bool = driver.configure.connection.get_tmode() \n
		Specifies whether the UE is forced into a test mode. If enabled, the message 'ACTIVATE TEST MODE' is sent to the UE. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:TMODe?')
		return Conversions.str_to_bool(response)

	def set_tmode(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:TMODe \n
		Snippet: driver.configure.connection.set_tmode(enable = False) \n
		Specifies whether the UE is forced into a test mode. If enabled, the message 'ACTIVATE TEST MODE' is sent to the UE. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:TMODe {param}')

	def get_dle_insertion(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:DLEinsertion \n
		Snippet: value: int = driver.configure.connection.get_dle_insertion() \n
		Configures the rate of transport block errors to be inserted into the downlink data. \n
			:return: value: numeric Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:DLEinsertion?')
		return Conversions.str_to_int(response)

	def set_dle_insertion(self, value: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:DLEinsertion \n
		Snippet: driver.configure.connection.set_dle_insertion(value = 1) \n
		Configures the rate of transport block errors to be inserted into the downlink data. \n
			:param value: numeric Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:DLEinsertion {param}')

	def get_dl_padding(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:DLPadding \n
		Snippet: value: bool = driver.configure.connection.get_dl_padding() \n
		Activates or deactivates downlink padding at the MAC layer (filling an allocated RMC with padding bits when no data is
		available from higher layers) . \n
			:return: value: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:DLPadding?')
		return Conversions.str_to_bool(response)

	def set_dl_padding(self, value: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:DLPadding \n
		Snippet: driver.configure.connection.set_dl_padding(value = False) \n
		Activates or deactivates downlink padding at the MAC layer (filling an allocated RMC with padding bits when no data is
		available from higher layers) . \n
			:param value: OFF | ON
		"""
		param = Conversions.bool_to_str(value)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:DLPadding {param}')

	# noinspection PyTypeChecker
	def get_as_emission(self) -> enums.AddSpectrumEmission:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ASEMission \n
		Snippet: value: enums.AddSpectrumEmission = driver.configure.connection.get_as_emission() \n
		Selects a value signaled to the UE as additional ACLR and spectrum emission requirement. \n
			:return: value: NS01 | ... | NS288 Value NS_01 to NS_288
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:ASEMission?')
		return Conversions.str_to_scalar_enum(response, enums.AddSpectrumEmission)

	def set_as_emission(self, value: enums.AddSpectrumEmission) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ASEMission \n
		Snippet: driver.configure.connection.set_as_emission(value = enums.AddSpectrumEmission.NS01) \n
		Selects a value signaled to the UE as additional ACLR and spectrum emission requirement. \n
			:param value: NS01 | ... | NS288 Value NS_01 to NS_288
		"""
		param = Conversions.enum_scalar_to_str(value, enums.AddSpectrumEmission)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:ASEMission {param}')

	def get_sui_tx(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SUITx \n
		Snippet: value: bool = driver.configure.connection.get_sui_tx() \n
		Enables or disables the fields 'skipUplinkTxSPS' and 'skipUplinkTxDynamic'. \n
			:return: skip_ul_tx: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:SUITx?')
		return Conversions.str_to_bool(response)

	def set_sui_tx(self, skip_ul_tx: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SUITx \n
		Snippet: driver.configure.connection.set_sui_tx(skip_ul_tx = False) \n
		Enables or disables the fields 'skipUplinkTxSPS' and 'skipUplinkTxDynamic'. \n
			:param skip_ul_tx: OFF | ON
		"""
		param = Conversions.bool_to_str(skip_ul_tx)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SUITx {param}')

	# noinspection PyTypeChecker
	def get_ob_change(self) -> enums.InterBandHandoverMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:OBCHange \n
		Snippet: value: enums.InterBandHandoverMode = driver.configure.connection.get_ob_change() \n
		Selects the mechanism to be used for inter-band handover. \n
			:return: mode: BHANdover | REDirection Blind handover or redirection
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:OBCHange?')
		return Conversions.str_to_scalar_enum(response, enums.InterBandHandoverMode)

	def set_ob_change(self, mode: enums.InterBandHandoverMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:OBCHange \n
		Snippet: driver.configure.connection.set_ob_change(mode = enums.InterBandHandoverMode.BHANdover) \n
		Selects the mechanism to be used for inter-band handover. \n
			:param mode: BHANdover | REDirection Blind handover or redirection
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.InterBandHandoverMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:OBCHange {param}')

	# noinspection PyTypeChecker
	def get_fchange(self) -> enums.InterBandHandoverMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:FCHange \n
		Snippet: value: enums.InterBandHandoverMode = driver.configure.connection.get_fchange() \n
		Selects the mechanism to be used for inter-frequency handover (operating band not changed) . \n
			:return: mode: BHANdover | REDirection Blind handover or redirection
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:FCHange?')
		return Conversions.str_to_scalar_enum(response, enums.InterBandHandoverMode)

	def set_fchange(self, mode: enums.InterBandHandoverMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:FCHange \n
		Snippet: driver.configure.connection.set_fchange(mode = enums.InterBandHandoverMode.BHANdover) \n
		Selects the mechanism to be used for inter-frequency handover (operating band not changed) . \n
			:param mode: BHANdover | REDirection Blind handover or redirection
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.InterBandHandoverMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:FCHange {param}')

	def get_amd_bearer(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:AMDBearer \n
		Snippet: value: bool = driver.configure.connection.get_amd_bearer() \n
		Enables/disables accepting multiple default bearer requests. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:AMDBearer?')
		return Conversions.str_to_bool(response)

	def set_amd_bearer(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:AMDBearer \n
		Snippet: driver.configure.connection.set_amd_bearer(enable = False) \n
		Enables/disables accepting multiple default bearer requests. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:AMDBearer {param}')

	def clone(self) -> 'ConnectionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConnectionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
