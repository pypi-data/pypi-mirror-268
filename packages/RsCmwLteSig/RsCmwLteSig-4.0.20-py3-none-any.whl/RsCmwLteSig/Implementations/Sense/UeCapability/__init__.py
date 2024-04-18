from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCapabilityCls:
	"""UeCapability commands group definition. 172 total commands, 19 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueCapability", core, parent)

	@property
	def ueCategory(self):
		"""ueCategory commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueCategory'):
			from .UeCategory import UeCategoryCls
			self._ueCategory = UeCategoryCls(self._core, self._cmd_group)
		return self._ueCategory

	@property
	def pdcp(self):
		"""pdcp commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_pdcp'):
			from .Pdcp import PdcpCls
			self._pdcp = PdcpCls(self._core, self._cmd_group)
		return self._pdcp

	@property
	def player(self):
		"""player commands group. 0 Sub-classes, 29 commands."""
		if not hasattr(self, '_player'):
			from .Player import PlayerCls
			self._player = PlayerCls(self._core, self._cmd_group)
		return self._player

	@property
	def rf(self):
		"""rf commands group. 3 Sub-classes, 10 commands."""
		if not hasattr(self, '_rf'):
			from .Rf import RfCls
			self._rf = RfCls(self._core, self._cmd_group)
		return self._rf

	@property
	def meas(self):
		"""meas commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_meas'):
			from .Meas import MeasCls
			self._meas = MeasCls(self._core, self._cmd_group)
		return self._meas

	@property
	def fgIndicators(self):
		"""fgIndicators commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_fgIndicators'):
			from .FgIndicators import FgIndicatorsCls
			self._fgIndicators = FgIndicatorsCls(self._core, self._cmd_group)
		return self._fgIndicators

	@property
	def interRat(self):
		"""interRat commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_interRat'):
			from .InterRat import InterRatCls
			self._interRat = InterRatCls(self._core, self._cmd_group)
		return self._interRat

	@property
	def mbms(self):
		"""mbms commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mbms'):
			from .Mbms import MbmsCls
			self._mbms = MbmsCls(self._core, self._cmd_group)
		return self._mbms

	@property
	def cpIndication(self):
		"""cpIndication commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cpIndication'):
			from .CpIndication import CpIndicationCls
			self._cpIndication = CpIndicationCls(self._core, self._cmd_group)
		return self._cpIndication

	@property
	def ncsacq(self):
		"""ncsacq commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncsacq'):
			from .Ncsacq import NcsacqCls
			self._ncsacq = NcsacqCls(self._core, self._cmd_group)
		return self._ncsacq

	@property
	def ubnpMeas(self):
		"""ubnpMeas commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ubnpMeas'):
			from .UbnpMeas import UbnpMeasCls
			self._ubnpMeas = UbnpMeasCls(self._core, self._cmd_group)
		return self._ubnpMeas

	@property
	def wiw(self):
		"""wiw commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_wiw'):
			from .Wiw import WiwCls
			self._wiw = WiwCls(self._core, self._cmd_group)
		return self._wiw

	@property
	def laa(self):
		"""laa commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_laa'):
			from .Laa import LaaCls
			self._laa = LaaCls(self._core, self._cmd_group)
		return self._laa

	@property
	def ceParameters(self):
		"""ceParameters commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ceParameters'):
			from .CeParameters import CeParametersCls
			self._ceParameters = CeParametersCls(self._core, self._cmd_group)
		return self._ceParameters

	@property
	def dcParameters(self):
		"""dcParameters commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dcParameters'):
			from .DcParameters import DcParametersCls
			self._dcParameters = DcParametersCls(self._core, self._cmd_group)
		return self._dcParameters

	@property
	def mac(self):
		"""mac commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mac'):
			from .Mac import MacCls
			self._mac = MacCls(self._core, self._cmd_group)
		return self._mac

	@property
	def sl(self):
		"""sl commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_sl'):
			from .Sl import SlCls
			self._sl = SlCls(self._core, self._cmd_group)
		return self._sl

	@property
	def faueEutra(self):
		"""faueEutra commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_faueEutra'):
			from .FaueEutra import FaueEutraCls
			self._faueEutra = FaueEutraCls(self._core, self._cmd_group)
		return self._faueEutra

	@property
	def taueEutra(self):
		"""taueEutra commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_taueEutra'):
			from .TaueEutra import TaueEutraCls
			self._taueEutra = TaueEutraCls(self._core, self._cmd_group)
		return self._taueEutra

	# noinspection PyTypeChecker
	def get_as_release(self) -> enums.AccStratRelease:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:ASRelease \n
		Snippet: value: enums.AccStratRelease = driver.sense.ueCapability.get_as_release() \n
		Returns the 'Access Stratum Release' according to the UE capability information. \n
			:return: acc_strat_release: REL8 | REL9 | REL10 | REL11 | REL12 | REL13 | REL14
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:ASRelease?')
		return Conversions.str_to_scalar_enum(response, enums.AccStratRelease)

	def get_dciulca(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:DCIulca \n
		Snippet: value: bool = driver.sense.ueCapability.get_dciulca() \n
		Returns whether the UE supports in-device coexistence indication for UL CA. \n
			:return: index: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:DCIulca?')
		return Conversions.str_to_bool(response)

	def get_urt_time_diff(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:URTTimediff \n
		Snippet: value: bool = driver.sense.ueCapability.get_urt_time_diff() \n
		Returns whether the UE supports RX-TX time difference measurements. \n
			:return: time_diff: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:URTTimediff?')
		return Conversions.str_to_bool(response)

	def get_idc_index(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IDCindex \n
		Snippet: value: bool = driver.sense.ueCapability.get_idc_index() \n
		Returns whether the UE supports in-device coexistence indication and autonomous denial functionality. \n
			:return: index: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IDCindex?')
		return Conversions.str_to_bool(response)

	def get_pp_index(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PPINdex \n
		Snippet: value: bool = driver.sense.ueCapability.get_pp_index() \n
		Returns whether the UE supports power preference indication. \n
			:return: index: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PPINdex?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_dtype(self) -> enums.DeviceType:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:DTYPe \n
		Snippet: value: enums.DeviceType = driver.sense.ueCapability.get_dtype() \n
		Returns whether the UE benefits from NW-based battery consumption optimization or not. \n
			:return: device_type: NBFBcopt | NAV NBFBcopt: UE does not benefit NAV: UE does benefit
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:DTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.DeviceType)

	def get_rreport(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RREPort \n
		Snippet: value: bool = driver.sense.ueCapability.get_rreport() \n
		Returns whether the UE supports the delivery of RACH reports or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RREPort?')
		return Conversions.str_to_bool(response)

	def get_erl_field(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:ERLField \n
		Snippet: value: bool = driver.sense.ueCapability.get_erl_field() \n
		Returns whether the UE supports 15-bit RLC length indicators. \n
			:return: field: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:ERLField?')
		return Conversions.str_to_bool(response)

	def get_lm_meas(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:LMMeas \n
		Snippet: value: bool = driver.sense.ueCapability.get_lm_meas() \n
		Returns whether the UE supports logged MBSFN measurements in RRC idle and connected mode. \n
			:return: lmbsfn: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:LMMeas?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'UeCapabilityCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCapabilityCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
