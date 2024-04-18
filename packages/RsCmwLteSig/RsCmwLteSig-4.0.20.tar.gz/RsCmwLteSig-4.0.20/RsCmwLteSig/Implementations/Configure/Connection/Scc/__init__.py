from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SccCls:
	"""Scc commands group definition. 103 total commands, 29 Subgroups, 0 group commands
	Repeated Capability: SecondaryCompCarrier, default value after init: SecondaryCompCarrier.CC1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_secondaryCompCarrier_get', 'repcap_secondaryCompCarrier_set', repcap.SecondaryCompCarrier.CC1)

	def repcap_secondaryCompCarrier_set(self, secondaryCompCarrier: repcap.SecondaryCompCarrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondaryCompCarrier.Default
		Default value after init: SecondaryCompCarrier.CC1"""
		self._cmd_group.set_repcap_enum_value(secondaryCompCarrier)

	def repcap_secondaryCompCarrier_get(self) -> repcap.SecondaryCompCarrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def mcluster(self):
		"""mcluster commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcluster'):
			from .Mcluster import MclusterCls
			self._mcluster = MclusterCls(self._core, self._cmd_group)
		return self._mcluster

	@property
	def stype(self):
		"""stype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stype'):
			from .Stype import StypeCls
			self._stype = StypeCls(self._core, self._cmd_group)
		return self._stype

	@property
	def asEmission(self):
		"""asEmission commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_asEmission'):
			from .AsEmission import AsEmissionCls
			self._asEmission = AsEmissionCls(self._core, self._cmd_group)
		return self._asEmission

	@property
	def sexecute(self):
		"""sexecute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sexecute'):
			from .Sexecute import SexecuteCls
			self._sexecute = SexecuteCls(self._core, self._cmd_group)
		return self._sexecute

	@property
	def cexecute(self):
		"""cexecute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cexecute'):
			from .Cexecute import CexecuteCls
			self._cexecute = CexecuteCls(self._core, self._cmd_group)
		return self._cexecute

	@property
	def hpusch(self):
		"""hpusch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hpusch'):
			from .Hpusch import HpuschCls
			self._hpusch = HpuschCls(self._core, self._cmd_group)
		return self._hpusch

	@property
	def laa(self):
		"""laa commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_laa'):
			from .Laa import LaaCls
			self._laa = LaaCls(self._core, self._cmd_group)
		return self._laa

	@property
	def tia(self):
		"""tia commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tia'):
			from .Tia import TiaCls
			self._tia = TiaCls(self._core, self._cmd_group)
		return self._tia

	@property
	def pzero(self):
		"""pzero commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pzero'):
			from .Pzero import PzeroCls
			self._pzero = PzeroCls(self._core, self._cmd_group)
		return self._pzero

	@property
	def tm(self):
		"""tm commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_tm'):
			from .Tm import TmCls
			self._tm = TmCls(self._core, self._cmd_group)
		return self._tm

	@property
	def dlEqual(self):
		"""dlEqual commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlEqual'):
			from .DlEqual import DlEqualCls
			self._dlEqual = DlEqualCls(self._core, self._cmd_group)
		return self._dlEqual

	@property
	def transmission(self):
		"""transmission commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transmission'):
			from .Transmission import TransmissionCls
			self._transmission = TransmissionCls(self._core, self._cmd_group)
		return self._transmission

	@property
	def dciFormat(self):
		"""dciFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dciFormat'):
			from .DciFormat import DciFormatCls
			self._dciFormat = DciFormatCls(self._core, self._cmd_group)
		return self._dciFormat

	@property
	def nenbAntennas(self):
		"""nenbAntennas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nenbAntennas'):
			from .NenbAntennas import NenbAntennasCls
			self._nenbAntennas = NenbAntennasCls(self._core, self._cmd_group)
		return self._nenbAntennas

	@property
	def noLayers(self):
		"""noLayers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noLayers'):
			from .NoLayers import NoLayersCls
			self._noLayers = NoLayersCls(self._core, self._cmd_group)
		return self._noLayers

	@property
	def beamforming(self):
		"""beamforming commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_beamforming'):
			from .Beamforming import BeamformingCls
			self._beamforming = BeamformingCls(self._core, self._cmd_group)
		return self._beamforming

	@property
	def pmatrix(self):
		"""pmatrix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmatrix'):
			from .Pmatrix import PmatrixCls
			self._pmatrix = PmatrixCls(self._core, self._cmd_group)
		return self._pmatrix

	@property
	def schModel(self):
		"""schModel commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_schModel'):
			from .SchModel import SchModelCls
			self._schModel = SchModelCls(self._core, self._cmd_group)
		return self._schModel

	@property
	def rmc(self):
		"""rmc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmc'):
			from .Rmc import RmcCls
			self._rmc = RmcCls(self._core, self._cmd_group)
		return self._rmc

	@property
	def udChannels(self):
		"""udChannels commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_udChannels'):
			from .UdChannels import UdChannelsCls
			self._udChannels = UdChannelsCls(self._core, self._cmd_group)
		return self._udChannels

	@property
	def udttiBased(self):
		"""udttiBased commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_udttiBased'):
			from .UdttiBased import UdttiBasedCls
			self._udttiBased = UdttiBasedCls(self._core, self._cmd_group)
		return self._udttiBased

	@property
	def qam(self):
		"""qam commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_qam'):
			from .Qam import QamCls
			self._qam = QamCls(self._core, self._cmd_group)
		return self._qam

	@property
	def fcttiBased(self):
		"""fcttiBased commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcttiBased'):
			from .FcttiBased import FcttiBasedCls
			self._fcttiBased = FcttiBasedCls(self._core, self._cmd_group)
		return self._fcttiBased

	@property
	def fwbcqi(self):
		"""fwbcqi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fwbcqi'):
			from .Fwbcqi import FwbcqiCls
			self._fwbcqi = FwbcqiCls(self._core, self._cmd_group)
		return self._fwbcqi

	@property
	def fpmi(self):
		"""fpmi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fpmi'):
			from .Fpmi import FpmiCls
			self._fpmi = FpmiCls(self._core, self._cmd_group)
		return self._fpmi

	@property
	def fcri(self):
		"""fcri commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcri'):
			from .Fcri import FcriCls
			self._fcri = FcriCls(self._core, self._cmd_group)
		return self._fcri

	@property
	def fcpri(self):
		"""fcpri commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcpri'):
			from .Fcpri import FcpriCls
			self._fcpri = FcpriCls(self._core, self._cmd_group)
		return self._fcpri

	@property
	def fpri(self):
		"""fpri commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fpri'):
			from .Fpri import FpriCls
			self._fpri = FpriCls(self._core, self._cmd_group)
		return self._fpri

	@property
	def pdcch(self):
		"""pdcch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pdcch import PdcchCls
			self._pdcch = PdcchCls(self._core, self._cmd_group)
		return self._pdcch

	def clone(self) -> 'SccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
