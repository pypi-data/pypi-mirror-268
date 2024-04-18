from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SenseCls:
	"""Sense commands group definition. 319 total commands, 13 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def iqOut(self):
		"""iqOut commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOut'):
			from .IqOut import IqOutCls
			self._iqOut = IqOutCls(self._core, self._cmd_group)
		return self._iqOut

	@property
	def fading(self):
		"""fading commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fading'):
			from .Fading import FadingCls
			self._fading = FadingCls(self._core, self._cmd_group)
		return self._fading

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
	def connection(self):
		"""connection commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Connection import ConnectionCls
			self._connection = ConnectionCls(self._core, self._cmd_group)
		return self._connection

	@property
	def cqiReporting(self):
		"""cqiReporting commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cqiReporting'):
			from .CqiReporting import CqiReportingCls
			self._cqiReporting = CqiReportingCls(self._core, self._cmd_group)
		return self._cqiReporting

	@property
	def ueReport(self):
		"""ueReport commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueReport'):
			from .UeReport import UeReportCls
			self._ueReport = UeReportCls(self._core, self._cmd_group)
		return self._ueReport

	@property
	def uesInfo(self):
		"""uesInfo commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_uesInfo'):
			from .UesInfo import UesInfoCls
			self._uesInfo = UesInfoCls(self._core, self._cmd_group)
		return self._uesInfo

	@property
	def ueCapability(self):
		"""ueCapability commands group. 19 Sub-classes, 9 commands."""
		if not hasattr(self, '_ueCapability'):
			from .UeCapability import UeCapabilityCls
			self._ueCapability = UeCapabilityCls(self._core, self._cmd_group)
		return self._ueCapability

	@property
	def sms(self):
		"""sms commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sms'):
			from .Sms import SmsCls
			self._sms = SmsCls(self._core, self._cmd_group)
		return self._sms

	@property
	def eeLog(self):
		"""eeLog commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_eeLog'):
			from .EeLog import EeLogCls
			self._eeLog = EeLogCls(self._core, self._cmd_group)
		return self._eeLog

	@property
	def elog(self):
		"""elog commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_elog'):
			from .Elog import ElogCls
			self._elog = ElogCls(self._core, self._cmd_group)
		return self._elog

	@property
	def sib(self):
		"""sib commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sib'):
			from .Sib import SibCls
			self._sib = SibCls(self._core, self._cmd_group)
		return self._sib

	# noinspection PyTypeChecker
	def get_rrc_state(self) -> enums.RrcState:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:RRCState \n
		Snippet: value: enums.RrcState = driver.sense.get_rrc_state() \n
		Queries whether an RRC connection is established (connected) or not (idle) . \n
			:return: state: IDLE | CONNected
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:RRCState?')
		return Conversions.str_to_scalar_enum(response, enums.RrcState)

	def clone(self) -> 'SenseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SenseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
