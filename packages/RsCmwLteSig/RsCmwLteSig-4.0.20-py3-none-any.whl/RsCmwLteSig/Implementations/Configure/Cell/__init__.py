from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 89 total commands, 15 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def pcc(self):
		"""pcc commands group. 4 Sub-classes, 3 commands."""
		if not hasattr(self, '_pcc'):
			from .Pcc import PccCls
			self._pcc = PccCls(self._core, self._cmd_group)
		return self._pcc

	@property
	def scc(self):
		"""scc commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .Scc import SccCls
			self._scc = SccCls(self._core, self._cmd_group)
		return self._scc

	@property
	def tdd(self):
		"""tdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdd'):
			from .Tdd import TddCls
			self._tdd = TddCls(self._core, self._cmd_group)
		return self._tdd

	@property
	def prach(self):
		"""prach commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import PrachCls
			self._prach = PrachCls(self._core, self._cmd_group)
		return self._prach

	@property
	def rar(self):
		"""rar commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rar'):
			from .Rar import RarCls
			self._rar = RarCls(self._core, self._cmd_group)
		return self._rar

	@property
	def mnc(self):
		"""mnc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mnc'):
			from .Mnc import MncCls
			self._mnc = MncCls(self._core, self._cmd_group)
		return self._mnc

	@property
	def security(self):
		"""security commands group. 0 Sub-classes, 9 commands."""
		if not hasattr(self, '_security'):
			from .Security import SecurityCls
			self._security = SecurityCls(self._core, self._cmd_group)
		return self._security

	@property
	def ueIdentity(self):
		"""ueIdentity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueIdentity'):
			from .UeIdentity import UeIdentityCls
			self._ueIdentity = UeIdentityCls(self._core, self._cmd_group)
		return self._ueIdentity

	@property
	def timeout(self):
		"""timeout commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_timeout'):
			from .Timeout import TimeoutCls
			self._timeout = TimeoutCls(self._core, self._cmd_group)
		return self._timeout

	@property
	def reSelection(self):
		"""reSelection commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_reSelection'):
			from .ReSelection import ReSelectionCls
			self._reSelection = ReSelectionCls(self._core, self._cmd_group)
		return self._reSelection

	@property
	def time(self):
		"""time commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_time'):
			from .Time import TimeCls
			self._time = TimeCls(self._core, self._cmd_group)
		return self._time

	@property
	def nas(self):
		"""nas commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_nas'):
			from .Nas import NasCls
			self._nas = NasCls(self._core, self._cmd_group)
		return self._nas

	@property
	def acause(self):
		"""acause commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acause'):
			from .Acause import AcauseCls
			self._acause = AcauseCls(self._core, self._cmd_group)
		return self._acause

	@property
	def rcause(self):
		"""rcause commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rcause'):
			from .Rcause import RcauseCls
			self._rcause = RcauseCls(self._core, self._cmd_group)
		return self._rcause

	# noinspection PyTypeChecker
	def get_cprefix(self) -> enums.CyclicPrefix:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:CPRefix \n
		Snippet: value: enums.CyclicPrefix = driver.configure.cell.get_cprefix() \n
		Defines whether a normal or extended cyclic prefix (CP) is used. \n
			:return: cyclic_prefix: NORMal | EXTended
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:CPRefix?')
		return Conversions.str_to_scalar_enum(response, enums.CyclicPrefix)

	def set_cprefix(self, cyclic_prefix: enums.CyclicPrefix) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:CPRefix \n
		Snippet: driver.configure.cell.set_cprefix(cyclic_prefix = enums.CyclicPrefix.EXTended) \n
		Defines whether a normal or extended cyclic prefix (CP) is used. \n
			:param cyclic_prefix: NORMal | EXTended
		"""
		param = Conversions.enum_scalar_to_str(cyclic_prefix, enums.CyclicPrefix)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:CPRefix {param}')

	def get_mcc(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:MCC \n
		Snippet: value: int = driver.configure.cell.get_mcc() \n
		Specifies the three-digit mobile country code (MCC) . You can omit leading zeros. \n
			:return: mcc: decimal Range: 0 to 999
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:MCC?')
		return Conversions.str_to_int(response)

	def set_mcc(self, mcc: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:MCC \n
		Snippet: driver.configure.cell.set_mcc(mcc = 1) \n
		Specifies the three-digit mobile country code (MCC) . You can omit leading zeros. \n
			:param mcc: decimal Range: 0 to 999
		"""
		param = Conversions.decimal_value_to_str(mcc)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:MCC {param}')

	def get_tac(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TAC \n
		Snippet: value: int = driver.configure.cell.get_tac() \n
		Specifies the tracking area code. \n
			:return: tac: decimal Range: 0 to 65535
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:TAC?')
		return Conversions.str_to_int(response)

	def set_tac(self, tac: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TAC \n
		Snippet: driver.configure.cell.set_tac(tac = 1) \n
		Specifies the tracking area code. \n
			:param tac: decimal Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(tac)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:TAC {param}')

	def clone(self) -> 'CellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
