from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PccCls:
	"""Pcc commands group definition. 107 total commands, 23 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcc", core, parent)

	@property
	def mcluster(self):
		"""mcluster commands group. 0 Sub-classes, 2 commands."""
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
	def hpusch(self):
		"""hpusch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hpusch'):
			from .Hpusch import HpuschCls
			self._hpusch = HpuschCls(self._core, self._cmd_group)
		return self._hpusch

	@property
	def tia(self):
		"""tia commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tia'):
			from .Tia import TiaCls
			self._tia = TiaCls(self._core, self._cmd_group)
		return self._tia

	@property
	def beamforming(self):
		"""beamforming commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_beamforming'):
			from .Beamforming import BeamformingCls
			self._beamforming = BeamformingCls(self._core, self._cmd_group)
		return self._beamforming

	@property
	def schModel(self):
		"""schModel commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_schModel'):
			from .SchModel import SchModelCls
			self._schModel = SchModelCls(self._core, self._cmd_group)
		return self._schModel

	@property
	def tm(self):
		"""tm commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_tm'):
			from .Tm import TmCls
			self._tm = TmCls(self._core, self._cmd_group)
		return self._tm

	@property
	def pzero(self):
		"""pzero commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pzero'):
			from .Pzero import PzeroCls
			self._pzero = PzeroCls(self._core, self._cmd_group)
		return self._pzero

	@property
	def rmc(self):
		"""rmc commands group. 6 Sub-classes, 0 commands."""
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
	def sps(self):
		"""sps commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_sps'):
			from .Sps import SpsCls
			self._sps = SpsCls(self._core, self._cmd_group)
		return self._sps

	@property
	def udttiBased(self):
		"""udttiBased commands group. 2 Sub-classes, 0 commands."""
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
	def emamode(self):
		"""emamode commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_emamode'):
			from .Emamode import EmamodeCls
			self._emamode = EmamodeCls(self._core, self._cmd_group)
		return self._emamode

	@property
	def cscheduling(self):
		"""cscheduling commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_cscheduling'):
			from .Cscheduling import CschedulingCls
			self._cscheduling = CschedulingCls(self._core, self._cmd_group)
		return self._cscheduling

	@property
	def pdcch(self):
		"""pdcch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pdcch import PdcchCls
			self._pdcch = PdcchCls(self._core, self._cmd_group)
		return self._pdcch

	@property
	def pucch(self):
		"""pucch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	def get_hduplex(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:HDUPlex \n
		Snippet: value: bool = driver.configure.connection.pcc.get_hduplex() \n
		Selects between half-duplex operation and full-duplex operation. \n
			:return: half_duplex: OFF | ON OFF: full-duplex operation ON: half-duplex operation
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:HDUPlex?')
		return Conversions.str_to_bool(response)

	def set_hduplex(self, half_duplex: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:HDUPlex \n
		Snippet: driver.configure.connection.pcc.set_hduplex(half_duplex = False) \n
		Selects between half-duplex operation and full-duplex operation. \n
			:param half_duplex: OFF | ON OFF: full-duplex operation ON: half-duplex operation
		"""
		param = Conversions.bool_to_str(half_duplex)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:HDUPlex {param}')

	def get_tti_bundling(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TTIBundling \n
		Snippet: value: bool = driver.configure.connection.pcc.get_tti_bundling() \n
		Enables or disables TTI bundling for the uplink. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TTIBundling?')
		return Conversions.str_to_bool(response)

	def set_tti_bundling(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TTIBundling \n
		Snippet: driver.configure.connection.pcc.set_tti_bundling(enable = False) \n
		Enables or disables TTI bundling for the uplink. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TTIBundling {param}')

	def get_dl_equal(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:DLEQual \n
		Snippet: value: bool = driver.configure.connection.pcc.get_dl_equal() \n
		Enables or disables the coupling of all MIMO downlink streams. When you switch on the coupling, the settings for DL
		stream 1 are applied to all DL streams. With enabled coupling, commands of the format CONFigure:...:DL<s>... configure
		all DL streams at once, independent of the specified <s>. With disabled coupling, such commands configure a single
		selected DL stream <s>. However, some settings are never configurable per stream and are always coupled. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:DLEQual?')
		return Conversions.str_to_bool(response)

	def set_dl_equal(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:DLEQual \n
		Snippet: driver.configure.connection.pcc.set_dl_equal(enable = False) \n
		Enables or disables the coupling of all MIMO downlink streams. When you switch on the coupling, the settings for DL
		stream 1 are applied to all DL streams. With enabled coupling, commands of the format CONFigure:...:DL<s>... configure
		all DL streams at once, independent of the specified <s>. With disabled coupling, such commands configure a single
		selected DL stream <s>. However, some settings are never configurable per stream and are always coupled. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:DLEQual {param}')

	# noinspection PyTypeChecker
	def get_transmission(self) -> enums.TransmissionMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TRANsmission \n
		Snippet: value: enums.TransmissionMode = driver.configure.connection.pcc.get_transmission() \n
		Selects the LTE transmission mode. The value must be compatible to the active scenario, see Table 'Transmission scheme
		overview'. \n
			:return: mode: TM1 | TM2 | TM3 | TM4 | TM6 | TM7 | TM8 | TM9 Transmission mode 1, 2, 3, 4, 6, 7, 8, 9
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TRANsmission?')
		return Conversions.str_to_scalar_enum(response, enums.TransmissionMode)

	def set_transmission(self, mode: enums.TransmissionMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TRANsmission \n
		Snippet: driver.configure.connection.pcc.set_transmission(mode = enums.TransmissionMode.TM1) \n
		Selects the LTE transmission mode. The value must be compatible to the active scenario, see Table 'Transmission scheme
		overview'. \n
			:param mode: TM1 | TM2 | TM3 | TM4 | TM6 | TM7 | TM8 | TM9 Transmission mode 1, 2, 3, 4, 6, 7, 8, 9
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TransmissionMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TRANsmission {param}')

	# noinspection PyTypeChecker
	def get_dci_format(self) -> enums.DciFormat:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:DCIFormat \n
		Snippet: value: enums.DciFormat = driver.configure.connection.pcc.get_dci_format() \n
		Selects the DCI format. The value must be compatible to the transmission mode, see Table 'Transmission scheme overview'. \n
			:return: dci: D1 | D1A | D1B | D2 | D2A | D2B | D2C | D61 Format 1, 1A, 1B, 2, 2A, 2B, 2C, 6-1A/B
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:DCIFormat?')
		return Conversions.str_to_scalar_enum(response, enums.DciFormat)

	def set_dci_format(self, dci: enums.DciFormat) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:DCIFormat \n
		Snippet: driver.configure.connection.pcc.set_dci_format(dci = enums.DciFormat.D1) \n
		Selects the DCI format. The value must be compatible to the transmission mode, see Table 'Transmission scheme overview'. \n
			:param dci: D1 | D1A | D1B | D2 | D2A | D2B | D2C | D61 Format 1, 1A, 1B, 2, 2A, 2B, 2C, 6-1A/B
		"""
		param = Conversions.enum_scalar_to_str(dci, enums.DciFormat)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:DCIFormat {param}')

	# noinspection PyTypeChecker
	def get_nenb_antennas(self) -> enums.AntennasTxA:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:NENBantennas \n
		Snippet: value: enums.AntennasTxA = driver.configure.connection.pcc.get_nenb_antennas() \n
		Selects the number of downlink TX antennas for transmission mode 1 to 6. The value must be compatible to the active
		scenario and transmission mode, see Table 'Transmission scheme overview'. \n
			:return: antennas: ONE | TWO | FOUR
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:NENBantennas?')
		return Conversions.str_to_scalar_enum(response, enums.AntennasTxA)

	def set_nenb_antennas(self, antennas: enums.AntennasTxA) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:NENBantennas \n
		Snippet: driver.configure.connection.pcc.set_nenb_antennas(antennas = enums.AntennasTxA.FOUR) \n
		Selects the number of downlink TX antennas for transmission mode 1 to 6. The value must be compatible to the active
		scenario and transmission mode, see Table 'Transmission scheme overview'. \n
			:param antennas: ONE | TWO | FOUR
		"""
		param = Conversions.enum_scalar_to_str(antennas, enums.AntennasTxA)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:NENBantennas {param}')

	# noinspection PyTypeChecker
	def get_no_layers(self) -> enums.NoOfLayers:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:NOLayers \n
		Snippet: value: enums.NoOfLayers = driver.configure.connection.pcc.get_no_layers() \n
		Selects the number of layers for MIMO 4x4 with spatial multiplexing (TM 3 and 4) . \n
			:return: number: L2 | L4 Two layers or four layers
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:NOLayers?')
		return Conversions.str_to_scalar_enum(response, enums.NoOfLayers)

	def set_no_layers(self, number: enums.NoOfLayers) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:NOLayers \n
		Snippet: driver.configure.connection.pcc.set_no_layers(number = enums.NoOfLayers.L2) \n
		Selects the number of layers for MIMO 4x4 with spatial multiplexing (TM 3 and 4) . \n
			:param number: L2 | L4 Two layers or four layers
		"""
		param = Conversions.enum_scalar_to_str(number, enums.NoOfLayers)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:NOLayers {param}')

	# noinspection PyTypeChecker
	def get_pmatrix(self) -> enums.PrecodingMatrixMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:PMATrix \n
		Snippet: value: enums.PrecodingMatrixMode = driver.configure.connection.pcc.get_pmatrix() \n
		Selects the precoding matrix. The value must be compatible to the active scenario and transmission mode, see Table
		'Transmission scheme overview'. For TM 8 and TM 9, the matrix is used as beamforming matrix, not for precoding. \n
			:return: mode: PMI0 | PMI1 | PMI2 | PMI3 | PMI4 | PMI5 | PMI6 | PMI7 | PMI8 | PMI9 | PMI10 | PMI11 | PMI12 | PMI13 | PMI14 | PMI15 | RANDom_pmi Matrix according to PMI 0, PMI 1, ... PMI15. RANDom_pmi: The PMI value is selected randomly as defined in 3GPP TS 36.521, annex B.4.1 and B.4.2.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:PMATrix?')
		return Conversions.str_to_scalar_enum(response, enums.PrecodingMatrixMode)

	def set_pmatrix(self, mode: enums.PrecodingMatrixMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:PMATrix \n
		Snippet: driver.configure.connection.pcc.set_pmatrix(mode = enums.PrecodingMatrixMode.PMI0) \n
		Selects the precoding matrix. The value must be compatible to the active scenario and transmission mode, see Table
		'Transmission scheme overview'. For TM 8 and TM 9, the matrix is used as beamforming matrix, not for precoding. \n
			:param mode: PMI0 | PMI1 | PMI2 | PMI3 | PMI4 | PMI5 | PMI6 | PMI7 | PMI8 | PMI9 | PMI10 | PMI11 | PMI12 | PMI13 | PMI14 | PMI15 | RANDom_pmi Matrix according to PMI 0, PMI 1, ... PMI15. RANDom_pmi: The PMI value is selected randomly as defined in 3GPP TS 36.521, annex B.4.1 and B.4.2.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PrecodingMatrixMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:PMATrix {param}')

	def clone(self) -> 'PccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
