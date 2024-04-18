from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScenarioCls:
	"""Scenario commands group definition. 112 total commands, 105 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scenario", core, parent)

	@property
	def scell(self):
		"""scell commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scell'):
			from .Scell import ScellCls
			self._scell = ScellCls(self._core, self._cmd_group)
		return self._scell

	@property
	def tro(self):
		"""tro commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tro'):
			from .Tro import TroCls
			self._tro = TroCls(self._core, self._cmd_group)
		return self._tro

	@property
	def ad(self):
		"""ad commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ad'):
			from .Ad import AdCls
			self._ad = AdCls(self._core, self._cmd_group)
		return self._ad

	@property
	def scFading(self):
		"""scFading commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scFading'):
			from .ScFading import ScFadingCls
			self._scFading = ScFadingCls(self._core, self._cmd_group)
		return self._scFading

	@property
	def troFading(self):
		"""troFading commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_troFading'):
			from .TroFading import TroFadingCls
			self._troFading = TroFadingCls(self._core, self._cmd_group)
		return self._troFading

	@property
	def adf(self):
		"""adf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adf'):
			from .Adf import AdfCls
			self._adf = AdfCls(self._core, self._cmd_group)
		return self._adf

	@property
	def catRfOut(self):
		"""catRfOut commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catRfOut'):
			from .CatRfOut import CatRfOutCls
			self._catRfOut = CatRfOutCls(self._core, self._cmd_group)
		return self._catRfOut

	@property
	def cafrfOut(self):
		"""cafrfOut commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cafrfOut'):
			from .CafrfOut import CafrfOutCls
			self._cafrfOut = CafrfOutCls(self._core, self._cmd_group)
		return self._cafrfOut

	@property
	def bf(self):
		"""bf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bf'):
			from .Bf import BfCls
			self._bf = BfCls(self._core, self._cmd_group)
		return self._bf

	@property
	def bfsm(self):
		"""bfsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bfsm'):
			from .Bfsm import BfsmCls
			self._bfsm = BfsmCls(self._core, self._cmd_group)
		return self._bfsm

	@property
	def bh(self):
		"""bh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bh'):
			from .Bh import BhCls
			self._bh = BhCls(self._core, self._cmd_group)
		return self._bh

	@property
	def catf(self):
		"""catf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_catf'):
			from .Catf import CatfCls
			self._catf = CatfCls(self._core, self._cmd_group)
		return self._catf

	@property
	def caff(self):
		"""caff commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_caff'):
			from .Caff import CaffCls
			self._caff = CaffCls(self._core, self._cmd_group)
		return self._caff

	@property
	def bff(self):
		"""bff commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bff'):
			from .Bff import BffCls
			self._bff = BffCls(self._core, self._cmd_group)
		return self._bff

	@property
	def bhf(self):
		"""bhf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bhf'):
			from .Bhf import BhfCls
			self._bhf = BhfCls(self._core, self._cmd_group)
		return self._bhf

	@property
	def cc(self):
		"""cc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import CcCls
			self._cc = CcCls(self._core, self._cmd_group)
		return self._cc

	@property
	def ccmp(self):
		"""ccmp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccmp'):
			from .Ccmp import CcmpCls
			self._ccmp = CcmpCls(self._core, self._cmd_group)
		return self._ccmp

	@property
	def ccms(self):
		"""ccms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccms'):
			from .Ccms import CcmsCls
			self._ccms = CcmsCls(self._core, self._cmd_group)
		return self._ccms

	@property
	def cf(self):
		"""cf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cf'):
			from .Cf import CfCls
			self._cf = CfCls(self._core, self._cmd_group)
		return self._cf

	@property
	def ch(self):
		"""ch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ch'):
			from .Ch import ChCls
			self._ch = ChCls(self._core, self._cmd_group)
		return self._ch

	@property
	def chsm(self):
		"""chsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chsm'):
			from .Chsm import ChsmCls
			self._chsm = ChsmCls(self._core, self._cmd_group)
		return self._chsm

	@property
	def cj(self):
		"""cj commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cj'):
			from .Cj import CjCls
			self._cj = CjCls(self._core, self._cmd_group)
		return self._cj

	@property
	def cjsm(self):
		"""cjsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cjsm'):
			from .Cjsm import CjsmCls
			self._cjsm = CjsmCls(self._core, self._cmd_group)
		return self._cjsm

	@property
	def cl(self):
		"""cl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl'):
			from .Cl import ClCls
			self._cl = ClCls(self._core, self._cmd_group)
		return self._cl

	@property
	def cff(self):
		"""cff commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cff'):
			from .Cff import CffCls
			self._cff = CffCls(self._core, self._cmd_group)
		return self._cff

	@property
	def chf(self):
		"""chf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_chf'):
			from .Chf import ChfCls
			self._chf = ChfCls(self._core, self._cmd_group)
		return self._chf

	@property
	def cjf(self):
		"""cjf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cjf'):
			from .Cjf import CjfCls
			self._cjf = CjfCls(self._core, self._cmd_group)
		return self._cjf

	@property
	def cjfs(self):
		"""cjfs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cjfs'):
			from .Cjfs import CjfsCls
			self._cjfs = CjfsCls(self._core, self._cmd_group)
		return self._cjfs

	@property
	def dd(self):
		"""dd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dd'):
			from .Dd import DdCls
			self._dd = DdCls(self._core, self._cmd_group)
		return self._dd

	@property
	def dh(self):
		"""dh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dh'):
			from .Dh import DhCls
			self._dh = DhCls(self._core, self._cmd_group)
		return self._dh

	@property
	def dj(self):
		"""dj commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dj'):
			from .Dj import DjCls
			self._dj = DjCls(self._core, self._cmd_group)
		return self._dj

	@property
	def djsm(self):
		"""djsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_djsm'):
			from .Djsm import DjsmCls
			self._djsm = DjsmCls(self._core, self._cmd_group)
		return self._djsm

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def dlsm(self):
		"""dlsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlsm'):
			from .Dlsm import DlsmCls
			self._dlsm = DlsmCls(self._core, self._cmd_group)
		return self._dlsm

	@property
	def dn(self):
		"""dn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dn'):
			from .Dn import DnCls
			self._dn = DnCls(self._core, self._cmd_group)
		return self._dn

	@property
	def dnsm(self):
		"""dnsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dnsm'):
			from .Dnsm import DnsmCls
			self._dnsm = DnsmCls(self._core, self._cmd_group)
		return self._dnsm

	@property
	def dp(self):
		"""dp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dp'):
			from .Dp import DpCls
			self._dp = DpCls(self._core, self._cmd_group)
		return self._dp

	@property
	def dhf(self):
		"""dhf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dhf'):
			from .Dhf import DhfCls
			self._dhf = DhfCls(self._core, self._cmd_group)
		return self._dhf

	@property
	def dpf(self):
		"""dpf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpf'):
			from .Dpf import DpfCls
			self._dpf = DpfCls(self._core, self._cmd_group)
		return self._dpf

	@property
	def ee(self):
		"""ee commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ee'):
			from .Ee import EeCls
			self._ee = EeCls(self._core, self._cmd_group)
		return self._ee

	@property
	def ej(self):
		"""ej commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ej'):
			from .Ej import EjCls
			self._ej = EjCls(self._core, self._cmd_group)
		return self._ej

	@property
	def ejf(self):
		"""ejf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ejf'):
			from .Ejf import EjfCls
			self._ejf = EjfCls(self._core, self._cmd_group)
		return self._ejf

	@property
	def el(self):
		"""el commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_el'):
			from .El import ElCls
			self._el = ElCls(self._core, self._cmd_group)
		return self._el

	@property
	def elsm(self):
		"""elsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_elsm'):
			from .Elsm import ElsmCls
			self._elsm = ElsmCls(self._core, self._cmd_group)
		return self._elsm

	@property
	def en(self):
		"""en commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_en'):
			from .En import EnCls
			self._en = EnCls(self._core, self._cmd_group)
		return self._en

	@property
	def ensm(self):
		"""ensm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ensm'):
			from .Ensm import EnsmCls
			self._ensm = EnsmCls(self._core, self._cmd_group)
		return self._ensm

	@property
	def ep(self):
		"""ep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ep'):
			from .Ep import EpCls
			self._ep = EpCls(self._core, self._cmd_group)
		return self._ep

	@property
	def epsm(self):
		"""epsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_epsm'):
			from .Epsm import EpsmCls
			self._epsm = EpsmCls(self._core, self._cmd_group)
		return self._epsm

	@property
	def epf(self):
		"""epf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_epf'):
			from .Epf import EpfCls
			self._epf = EpfCls(self._core, self._cmd_group)
		return self._epf

	@property
	def epfs(self):
		"""epfs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_epfs'):
			from .Epfs import EpfsCls
			self._epfs = EpfsCls(self._core, self._cmd_group)
		return self._epfs

	@property
	def er(self):
		"""er commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_er'):
			from .Er import ErCls
			self._er = ErCls(self._core, self._cmd_group)
		return self._er

	@property
	def ersm(self):
		"""ersm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ersm'):
			from .Ersm import ErsmCls
			self._ersm = ErsmCls(self._core, self._cmd_group)
		return self._ersm

	@property
	def et(self):
		"""et commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_et'):
			from .Et import EtCls
			self._et = EtCls(self._core, self._cmd_group)
		return self._et

	@property
	def frsm(self):
		"""frsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frsm'):
			from .Frsm import FrsmCls
			self._frsm = FrsmCls(self._core, self._cmd_group)
		return self._frsm

	@property
	def fr(self):
		"""fr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fr'):
			from .Fr import FrCls
			self._fr = FrCls(self._core, self._cmd_group)
		return self._fr

	@property
	def fnsm(self):
		"""fnsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fnsm'):
			from .Fnsm import FnsmCls
			self._fnsm = FnsmCls(self._core, self._cmd_group)
		return self._fnsm

	@property
	def fn(self):
		"""fn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fn'):
			from .Fn import FnCls
			self._fn = FnCls(self._core, self._cmd_group)
		return self._fn

	@property
	def ftsm(self):
		"""ftsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ftsm'):
			from .Ftsm import FtsmCls
			self._ftsm = FtsmCls(self._core, self._cmd_group)
		return self._ftsm

	@property
	def ft(self):
		"""ft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ft'):
			from .Ft import FtCls
			self._ft = FtCls(self._core, self._cmd_group)
		return self._ft

	@property
	def fp(self):
		"""fp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fp'):
			from .Fp import FpCls
			self._fp = FpCls(self._core, self._cmd_group)
		return self._fp

	@property
	def fpsm(self):
		"""fpsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fpsm'):
			from .Fpsm import FpsmCls
			self._fpsm = FpsmCls(self._core, self._cmd_group)
		return self._fpsm

	@property
	def fv(self):
		"""fv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fv'):
			from .Fv import FvCls
			self._fv = FvCls(self._core, self._cmd_group)
		return self._fv

	@property
	def fvsm(self):
		"""fvsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fvsm'):
			from .Fvsm import FvsmCls
			self._fvsm = FvsmCls(self._core, self._cmd_group)
		return self._fvsm

	@property
	def fx(self):
		"""fx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fx'):
			from .Fx import FxCls
			self._fx = FxCls(self._core, self._cmd_group)
		return self._fx

	@property
	def ff(self):
		"""ff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ff'):
			from .Ff import FfCls
			self._ff = FfCls(self._core, self._cmd_group)
		return self._ff

	@property
	def fl(self):
		"""fl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fl'):
			from .Fl import FlCls
			self._fl = FlCls(self._core, self._cmd_group)
		return self._fl

	@property
	def flf(self):
		"""flf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_flf'):
			from .Flf import FlfCls
			self._flf = FlfCls(self._core, self._cmd_group)
		return self._flf

	@property
	def fpf(self):
		"""fpf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fpf'):
			from .Fpf import FpfCls
			self._fpf = FpfCls(self._core, self._cmd_group)
		return self._fpf

	@property
	def fpfs(self):
		"""fpfs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fpfs'):
			from .Fpfs import FpfsCls
			self._fpfs = FpfsCls(self._core, self._cmd_group)
		return self._fpfs

	@property
	def grsm(self):
		"""grsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_grsm'):
			from .Grsm import GrsmCls
			self._grsm = GrsmCls(self._core, self._cmd_group)
		return self._grsm

	@property
	def gr(self):
		"""gr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gr'):
			from .Gr import GrCls
			self._gr = GrCls(self._core, self._cmd_group)
		return self._gr

	@property
	def gtsm(self):
		"""gtsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gtsm'):
			from .Gtsm import GtsmCls
			self._gtsm = GtsmCls(self._core, self._cmd_group)
		return self._gtsm

	@property
	def gt(self):
		"""gt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gt'):
			from .Gt import GtCls
			self._gt = GtCls(self._core, self._cmd_group)
		return self._gt

	@property
	def gg(self):
		"""gg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gg'):
			from .Gg import GgCls
			self._gg = GgCls(self._core, self._cmd_group)
		return self._gg

	@property
	def gn(self):
		"""gn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gn'):
			from .Gn import GnCls
			self._gn = GnCls(self._core, self._cmd_group)
		return self._gn

	@property
	def gnf(self):
		"""gnf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gnf'):
			from .Gnf import GnfCls
			self._gnf = GnfCls(self._core, self._cmd_group)
		return self._gnf

	@property
	def gpsm(self):
		"""gpsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gpsm'):
			from .Gpsm import GpsmCls
			self._gpsm = GpsmCls(self._core, self._cmd_group)
		return self._gpsm

	@property
	def gpfs(self):
		"""gpfs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gpfs'):
			from .Gpfs import GpfsCls
			self._gpfs = GpfsCls(self._core, self._cmd_group)
		return self._gpfs

	@property
	def gp(self):
		"""gp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gp'):
			from .Gp import GpCls
			self._gp = GpCls(self._core, self._cmd_group)
		return self._gp

	@property
	def gpf(self):
		"""gpf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gpf'):
			from .Gpf import GpfCls
			self._gpf = GpfCls(self._core, self._cmd_group)
		return self._gpf

	@property
	def gv(self):
		"""gv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gv'):
			from .Gv import GvCls
			self._gv = GvCls(self._core, self._cmd_group)
		return self._gv

	@property
	def gvsm(self):
		"""gvsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gvsm'):
			from .Gvsm import GvsmCls
			self._gvsm = GvsmCls(self._core, self._cmd_group)
		return self._gvsm

	@property
	def gx(self):
		"""gx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gx'):
			from .Gx import GxCls
			self._gx = GxCls(self._core, self._cmd_group)
		return self._gx

	@property
	def gxsm(self):
		"""gxsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gxsm'):
			from .Gxsm import GxsmCls
			self._gxsm = GxsmCls(self._core, self._cmd_group)
		return self._gxsm

	@property
	def gya(self):
		"""gya commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gya'):
			from .Gya import GyaCls
			self._gya = GyaCls(self._core, self._cmd_group)
		return self._gya

	@property
	def gyas(self):
		"""gyas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gyas'):
			from .Gyas import GyasCls
			self._gyas = GyasCls(self._core, self._cmd_group)
		return self._gyas

	@property
	def gyc(self):
		"""gyc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gyc'):
			from .Gyc import GycCls
			self._gyc = GycCls(self._core, self._cmd_group)
		return self._gyc

	@property
	def htsm(self):
		"""htsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_htsm'):
			from .Htsm import HtsmCls
			self._htsm = HtsmCls(self._core, self._cmd_group)
		return self._htsm

	@property
	def ht(self):
		"""ht commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ht'):
			from .Ht import HtCls
			self._ht = HtCls(self._core, self._cmd_group)
		return self._ht

	@property
	def hh(self):
		"""hh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hh'):
			from .Hh import HhCls
			self._hh = HhCls(self._core, self._cmd_group)
		return self._hh

	@property
	def hp(self):
		"""hp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hp'):
			from .Hp import HpCls
			self._hp = HpCls(self._core, self._cmd_group)
		return self._hp

	@property
	def hr(self):
		"""hr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hr'):
			from .Hr import HrCls
			self._hr = HrCls(self._core, self._cmd_group)
		return self._hr

	@property
	def hrsm(self):
		"""hrsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hrsm'):
			from .Hrsm import HrsmCls
			self._hrsm = HrsmCls(self._core, self._cmd_group)
		return self._hrsm

	@property
	def hv(self):
		"""hv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hv'):
			from .Hv import HvCls
			self._hv = HvCls(self._core, self._cmd_group)
		return self._hv

	@property
	def hvsm(self):
		"""hvsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hvsm'):
			from .Hvsm import HvsmCls
			self._hvsm = HvsmCls(self._core, self._cmd_group)
		return self._hvsm

	@property
	def hx(self):
		"""hx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hx'):
			from .Hx import HxCls
			self._hx = HxCls(self._core, self._cmd_group)
		return self._hx

	@property
	def hxsm(self):
		"""hxsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hxsm'):
			from .Hxsm import HxsmCls
			self._hxsm = HxsmCls(self._core, self._cmd_group)
		return self._hxsm

	@property
	def hya(self):
		"""hya commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hya'):
			from .Hya import HyaCls
			self._hya = HyaCls(self._core, self._cmd_group)
		return self._hya

	@property
	def hyas(self):
		"""hyas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hyas'):
			from .Hyas import HyasCls
			self._hyas = HyasCls(self._core, self._cmd_group)
		return self._hyas

	@property
	def hyc(self):
		"""hyc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hyc'):
			from .Hyc import HycCls
			self._hyc = HycCls(self._core, self._cmd_group)
		return self._hyc

	@property
	def hycs(self):
		"""hycs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hycs'):
			from .Hycs import HycsCls
			self._hycs = HycsCls(self._core, self._cmd_group)
		return self._hycs

	@property
	def hye(self):
		"""hye commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hye'):
			from .Hye import HyeCls
			self._hye = HyeCls(self._core, self._cmd_group)
		return self._hye

	@property
	def hyes(self):
		"""hyes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hyes'):
			from .Hyes import HyesCls
			self._hyes = HyesCls(self._core, self._cmd_group)
		return self._hyes

	@property
	def hyg(self):
		"""hyg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hyg'):
			from .Hyg import HygCls
			self._hyg = HygCls(self._core, self._cmd_group)
		return self._hyg

	@property
	def hpf(self):
		"""hpf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hpf'):
			from .Hpf import HpfCls
			self._hpf = HpfCls(self._core, self._cmd_group)
		return self._hpf

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: NAV | SCEL | TRO | AD | SCF | TROF | ADF | CATR | CAFR | BF | BFSM4 | BH | CATF | CAFF | BFF | BHF | CC | CCMP | CCMS1 | CF | CH | CHSM4 | CJ | CJSM4 | CL | CFF | CHF | CJF | CJFS4 | DD | DH | DJ | DJSM4 | DL | DLSM4 | DN | DNSM4 | DP | DHF | DPF | EE | EJ | EL | ELSM4 | EN | ENSM4 | EP | EPSM4 | ER | ERSM4 | ET | EJF | EPF | EPFS4 | FF | FL | FN | FNSM4 | FP | FPSM4 | FR | FRSM4 | FT | FTSM4 | FV | FVSM4 | FX | FLF | FPF | FPFS4 | GG | GN | GP | GPSM4 | GR | GRSM4 | GT | GTSM4 | GV | GVSM4 | GX | GXSM4 | GYA | GYAS4 | GYC | GNF | GPF | GPFS4 | HH | HP | HR | HRSM4 | HT | HTSM4 | HV | HVSM4 | HX | HXSM4 | HYA | HYAS4 | HYC | HYCS4 | HYE | HYES4 | HYG | HPF For mapping of the values to scenario names, see Table 'Mapping of Scenario to scenario names'.
			- Fader: enums.SourceInt: EXTernal | INTernal Only returned for fading scenarios Indicates whether internal or external fading is active."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_enum('Fader', enums.SourceInt)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Fader: enums.SourceInt = None

	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario \n
		Snippet: value: ValueStruct = driver.route.scenario.get_value() \n
		Returns the active scenario. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario?', self.__class__.ValueStruct())

	def clone(self) -> 'ScenarioCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScenarioCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
