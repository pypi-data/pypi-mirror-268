from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsfbCls:
	"""Csfb commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csfb", core, parent)

	@property
	def gsm(self):
		"""gsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gsm'):
			from .Gsm import GsmCls
			self._gsm = GsmCls(self._core, self._cmd_group)
		return self._gsm

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
	def get_destination(self) -> enums.CsbfDestination:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:DESTination \n
		Snippet: value: enums.CsbfDestination = driver.configure.connection.csfb.get_destination() \n
		Selects the target radio access technology for MO CSFB. \n
			:return: destination: GSM | WCDMa | TDSCdma | NONE
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.CsbfDestination)

	def set_destination(self, destination: enums.CsbfDestination) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:DESTination \n
		Snippet: driver.configure.connection.csfb.set_destination(destination = enums.CsbfDestination.CDMA) \n
		Selects the target radio access technology for MO CSFB. \n
			:param destination: GSM | WCDMa | TDSCdma | NONE
		"""
		param = Conversions.enum_scalar_to_str(destination, enums.CsbfDestination)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:DESTination {param}')

	def clone(self) -> 'CsfbCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CsfbCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
