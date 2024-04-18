from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NcellCls:
	"""Ncell commands group definition. 10 total commands, 6 Subgroups, 0 group commands
	Repeated Capability: CellNo, default value after init: CellNo.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncell", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cellNo_get', 'repcap_cellNo_set', repcap.CellNo.Nr1)

	def repcap_cellNo_set(self, cellNo: repcap.CellNo) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CellNo.Default
		Default value after init: CellNo.Nr1"""
		self._cmd_group.set_repcap_enum_value(cellNo)

	def repcap_cellNo_get(self) -> repcap.CellNo:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def gsm(self):
		"""gsm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gsm'):
			from .Gsm import GsmCls
			self._gsm = GsmCls(self._core, self._cmd_group)
		return self._gsm

	@property
	def wcdma(self):
		"""wcdma commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wcdma'):
			from .Wcdma import WcdmaCls
			self._wcdma = WcdmaCls(self._core, self._cmd_group)
		return self._wcdma

	@property
	def cdma(self):
		"""cdma commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdma'):
			from .Cdma import CdmaCls
			self._cdma = CdmaCls(self._core, self._cmd_group)
		return self._cdma

	@property
	def evdo(self):
		"""evdo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_evdo'):
			from .Evdo import EvdoCls
			self._evdo = EvdoCls(self._core, self._cmd_group)
		return self._evdo

	@property
	def tdscdma(self):
		"""tdscdma commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdscdma'):
			from .Tdscdma import TdscdmaCls
			self._tdscdma = TdscdmaCls(self._core, self._cmd_group)
		return self._tdscdma

	def clone(self) -> 'NcellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NcellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
