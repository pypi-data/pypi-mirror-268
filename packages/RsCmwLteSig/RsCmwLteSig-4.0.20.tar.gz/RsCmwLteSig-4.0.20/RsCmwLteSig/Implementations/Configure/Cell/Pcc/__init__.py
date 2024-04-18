from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PccCls:
	"""Pcc commands group definition. 17 total commands, 4 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcc", core, parent)

	@property
	def ulSupport(self):
		"""ulSupport commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ulSupport'):
			from .UlSupport import UlSupportCls
			self._ulSupport = UlSupportCls(self._core, self._cmd_group)
		return self._ulSupport

	@property
	def srs(self):
		"""srs commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import SrsCls
			self._srs = SrsCls(self._core, self._cmd_group)
		return self._srs

	@property
	def cid(self):
		"""cid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cid'):
			from .Cid import CidCls
			self._cid = CidCls(self._core, self._cmd_group)
		return self._cid

	@property
	def sync(self):
		"""sync commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import SyncCls
			self._sync = SyncCls(self._core, self._cmd_group)
		return self._sync

	def get_pcid(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:PCID \n
		Snippet: value: int = driver.configure.cell.pcc.get_pcid() \n
		Defines the physical cell ID used for generation of the DL physical synchronization signals.
		If you use carrier aggregation, configure different values for the component carriers. \n
			:return: idn: decimal Range: 0 to 503
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:PCID?')
		return Conversions.str_to_int(response)

	def set_pcid(self, idn: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:PCID \n
		Snippet: driver.configure.cell.pcc.set_pcid(idn = 1) \n
		Defines the physical cell ID used for generation of the DL physical synchronization signals.
		If you use carrier aggregation, configure different values for the component carriers. \n
			:param idn: decimal Range: 0 to 503
		"""
		param = Conversions.decimal_value_to_str(idn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:PCID {param}')

	def get_ul_dl(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:ULDL \n
		Snippet: value: int = driver.configure.cell.pcc.get_ul_dl() \n
		Selects a UL-DL configuration, defining the combination of UL, DL and special subframes within a radio frame.
		This command is only relevant for duplex mode TDD. See also method RsCmwLteSig.Configure.Cell.Tdd.specific. \n
			:return: uplink_downlink: integer Range: 0 to 6
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:ULDL?')
		return Conversions.str_to_int(response)

	def set_ul_dl(self, uplink_downlink: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:ULDL \n
		Snippet: driver.configure.cell.pcc.set_ul_dl(uplink_downlink = 1) \n
		Selects a UL-DL configuration, defining the combination of UL, DL and special subframes within a radio frame.
		This command is only relevant for duplex mode TDD. See also method RsCmwLteSig.Configure.Cell.Tdd.specific. \n
			:param uplink_downlink: integer Range: 0 to 6
		"""
		param = Conversions.decimal_value_to_str(uplink_downlink)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:ULDL {param}')

	def get_ssubframe(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SSUBframe \n
		Snippet: value: int = driver.configure.cell.pcc.get_ssubframe() \n
		Selects a special subframe configuration, defining the inner structure of special subframes. This parameter is only
		relevant for TDD signals. The special subframe configurations are defined in 3GPP TS 36.211, chapter 4, 'Frame Structure'.
		See also method RsCmwLteSig.Configure.Cell.Tdd.specific. \n
			:return: special_subframe: integer Value 8 and 9 can only be used with normal cyclic prefix. Range: 0 to 9
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SSUBframe?')
		return Conversions.str_to_int(response)

	def set_ssubframe(self, special_subframe: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SSUBframe \n
		Snippet: driver.configure.cell.pcc.set_ssubframe(special_subframe = 1) \n
		Selects a special subframe configuration, defining the inner structure of special subframes. This parameter is only
		relevant for TDD signals. The special subframe configurations are defined in 3GPP TS 36.211, chapter 4, 'Frame Structure'.
		See also method RsCmwLteSig.Configure.Cell.Tdd.specific. \n
			:param special_subframe: integer Value 8 and 9 can only be used with normal cyclic prefix. Range: 0 to 9
		"""
		param = Conversions.decimal_value_to_str(special_subframe)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SSUBframe {param}')

	def clone(self) -> 'PccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
