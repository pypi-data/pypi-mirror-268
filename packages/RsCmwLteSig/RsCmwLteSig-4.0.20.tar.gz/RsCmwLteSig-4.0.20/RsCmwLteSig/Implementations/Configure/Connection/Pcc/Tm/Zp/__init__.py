from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ZpCls:
	"""Zp commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zp", core, parent)

	@property
	def csirs(self):
		"""csirs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csirs'):
			from .Csirs import CsirsCls
			self._csirs = CsirsCls(self._core, self._cmd_group)
		return self._csirs

	def get_bits(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:ZP:BITS \n
		Snippet: value: str = driver.configure.connection.pcc.tm.zp.get_bits() \n
		Specifies the bitmap 'ZeroPowerCSI-RS'. \n
			:return: bits: binary 16-bit value Range: #B0000000000000000 to #B1111111111111111
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:ZP:BITS?')
		return trim_str_response(response)

	def set_bits(self, bits: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:ZP:BITS \n
		Snippet: driver.configure.connection.pcc.tm.zp.set_bits(bits = rawAbc) \n
		Specifies the bitmap 'ZeroPowerCSI-RS'. \n
			:param bits: binary 16-bit value Range: #B0000000000000000 to #B1111111111111111
		"""
		param = Conversions.value_to_str(bits)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:ZP:BITS {param}')

	def clone(self) -> 'ZpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ZpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
