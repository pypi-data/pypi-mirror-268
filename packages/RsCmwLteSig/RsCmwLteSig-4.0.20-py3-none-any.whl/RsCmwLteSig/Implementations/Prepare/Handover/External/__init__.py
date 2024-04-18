from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExternalCls:
	"""External commands group definition. 7 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	@property
	def lte(self):
		"""lte commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def gsm(self):
		"""gsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gsm'):
			from .Gsm import GsmCls
			self._gsm = GsmCls(self._core, self._cmd_group)
		return self._gsm

	@property
	def cdma(self):
		"""cdma commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdma'):
			from .Cdma import CdmaCls
			self._cdma = CdmaCls(self._core, self._cmd_group)
		return self._cdma

	@property
	def evdo(self):
		"""evdo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evdo'):
			from .Evdo import EvdoCls
			self._evdo = EvdoCls(self._core, self._cmd_group)
		return self._evdo

	@property
	def wcdma(self):
		"""wcdma commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wcdma'):
			from .Wcdma import WcdmaCls
			self._wcdma = WcdmaCls(self._core, self._cmd_group)
		return self._wcdma

	@property
	def tdscdma(self):
		"""tdscdma commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdscdma'):
			from .Tdscdma import TdscdmaCls
			self._tdscdma = TdscdmaCls(self._core, self._cmd_group)
		return self._tdscdma

	# noinspection PyTypeChecker
	def get_destination(self) -> enums.HandoverDestination:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:DESTination \n
		Snippet: value: enums.HandoverDestination = driver.prepare.handover.external.get_destination() \n
		Selects the target radio access technology for handover to another instrument. \n
			:return: destination: LTE | EVDO | CDMA | GSM | WCDMa | TDSCdma
		"""
		response = self._core.io.query_str('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.HandoverDestination)

	def set_destination(self, destination: enums.HandoverDestination) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:DESTination \n
		Snippet: driver.prepare.handover.external.set_destination(destination = enums.HandoverDestination.CDMA) \n
		Selects the target radio access technology for handover to another instrument. \n
			:param destination: LTE | EVDO | CDMA | GSM | WCDMa | TDSCdma
		"""
		param = Conversions.enum_scalar_to_str(destination, enums.HandoverDestination)
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:DESTination {param}')

	def clone(self) -> 'ExternalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ExternalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
