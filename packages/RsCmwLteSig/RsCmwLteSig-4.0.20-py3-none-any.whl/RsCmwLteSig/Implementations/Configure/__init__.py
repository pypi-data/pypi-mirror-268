from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigureCls:
	"""Configure commands group definition. 752 total commands, 23 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def scc(self):
		"""scc commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_scc'):
			from .Scc import SccCls
			self._scc = SccCls(self._core, self._cmd_group)
		return self._scc

	@property
	def pcc(self):
		"""pcc commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_pcc'):
			from .Pcc import PccCls
			self._pcc = PccCls(self._core, self._cmd_group)
		return self._pcc

	@property
	def rfSettings(self):
		"""rfSettings commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def iqIn(self):
		"""iqIn commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqIn'):
			from .IqIn import IqInCls
			self._iqIn = IqInCls(self._core, self._cmd_group)
		return self._iqIn

	@property
	def fading(self):
		"""fading commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fading'):
			from .Fading import FadingCls
			self._fading = FadingCls(self._core, self._cmd_group)
		return self._fading

	@property
	def caggregation(self):
		"""caggregation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_caggregation'):
			from .Caggregation import CaggregationCls
			self._caggregation = CaggregationCls(self._core, self._cmd_group)
		return self._caggregation

	@property
	def ncell(self):
		"""ncell commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_ncell'):
			from .Ncell import NcellCls
			self._ncell = NcellCls(self._core, self._cmd_group)
		return self._ncell

	@property
	def a(self):
		"""a commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_a'):
			from .A import ACls
			self._a = ACls(self._core, self._cmd_group)
		return self._a

	@property
	def b(self):
		"""b commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_b'):
			from .B import BCls
			self._b = BCls(self._core, self._cmd_group)
		return self._b

	@property
	def downlink(self):
		"""downlink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	@property
	def cell(self):
		"""cell commands group. 15 Sub-classes, 3 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import CellCls
			self._cell = CellCls(self._core, self._cmd_group)
		return self._cell

	@property
	def connection(self):
		"""connection commands group. 13 Sub-classes, 33 commands."""
		if not hasattr(self, '_connection'):
			from .Connection import ConnectionCls
			self._connection = ConnectionCls(self._core, self._cmd_group)
		return self._connection

	@property
	def cqiReporting(self):
		"""cqiReporting commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_cqiReporting'):
			from .CqiReporting import CqiReportingCls
			self._cqiReporting = CqiReportingCls(self._core, self._cmd_group)
		return self._cqiReporting

	@property
	def ueReport(self):
		"""ueReport commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_ueReport'):
			from .UeReport import UeReportCls
			self._ueReport = UeReportCls(self._core, self._cmd_group)
		return self._ueReport

	@property
	def ueCapability(self):
		"""ueCapability commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_ueCapability'):
			from .UeCapability import UeCapabilityCls
			self._ueCapability = UeCapabilityCls(self._core, self._cmd_group)
		return self._ueCapability

	@property
	def sms(self):
		"""sms commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sms'):
			from .Sms import SmsCls
			self._sms = SmsCls(self._core, self._cmd_group)
		return self._sms

	@property
	def cbs(self):
		"""cbs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cbs'):
			from .Cbs import CbsCls
			self._cbs = CbsCls(self._core, self._cmd_group)
		return self._cbs

	@property
	def eeLog(self):
		"""eeLog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eeLog'):
			from .EeLog import EeLogCls
			self._eeLog = EeLogCls(self._core, self._cmd_group)
		return self._eeLog

	@property
	def ebler(self):
		"""ebler commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_ebler'):
			from .Ebler import EblerCls
			self._ebler = EblerCls(self._core, self._cmd_group)
		return self._ebler

	@property
	def throughput(self):
		"""throughput commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_throughput'):
			from .Throughput import ThroughputCls
			self._throughput = ThroughputCls(self._core, self._cmd_group)
		return self._throughput

	@property
	def mmonitor(self):
		"""mmonitor commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmonitor'):
			from .Mmonitor import MmonitorCls
			self._mmonitor = MmonitorCls(self._core, self._cmd_group)
		return self._mmonitor

	@property
	def sib(self):
		"""sib commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sib'):
			from .Sib import SibCls
			self._sib = SibCls(self._core, self._cmd_group)
		return self._sib

	def get_etoe(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:ETOE \n
		Snippet: value: bool = driver.configure.get_etoe() \n
		No command help available \n
			:return: end_to_end_enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:ETOE?')
		return Conversions.str_to_bool(response)

	def set_etoe(self, end_to_end_enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:ETOE \n
		Snippet: driver.configure.set_etoe(end_to_end_enable = False) \n
		No command help available \n
			:param end_to_end_enable: No help available
		"""
		param = Conversions.bool_to_str(end_to_end_enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:ETOE {param}')

	def clone(self) -> 'ConfigureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConfigureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
