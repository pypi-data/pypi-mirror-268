from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CschedulingCls:
	"""Cscheduling commands group definition. 6 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cscheduling", core, parent)

	@property
	def b(self):
		"""b commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_b'):
			from .B import BCls
			self._b = BCls(self._core, self._cmd_group)
		return self._b

	@property
	def a(self):
		"""a commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_a'):
			from .A import ACls
			self._a = ACls(self._core, self._cmd_group)
		return self._a

	# noinspection PyTypeChecker
	def get_sf_pattern(self) -> enums.SubFramePattern:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:CSCHeduling:SFPattern \n
		Snippet: value: enums.SubFramePattern = driver.configure.connection.pcc.cscheduling.get_sf_pattern() \n
		Selects the subframe pattern for eMTC compact scheduling, half-duplex. There are patterns with and without PDSCH HARQ-ACK
		bundling. \n
			:return: pattern: STANdard | HAB8 | HAB10 STANdard: no bundling HAB8: bundling, 8 HARQ processes HAB10: bundling, 10 HARQ processes
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:CSCHeduling:SFPattern?')
		return Conversions.str_to_scalar_enum(response, enums.SubFramePattern)

	def set_sf_pattern(self, pattern: enums.SubFramePattern) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:CSCHeduling:SFPattern \n
		Snippet: driver.configure.connection.pcc.cscheduling.set_sf_pattern(pattern = enums.SubFramePattern.HAB10) \n
		Selects the subframe pattern for eMTC compact scheduling, half-duplex. There are patterns with and without PDSCH HARQ-ACK
		bundling. \n
			:param pattern: STANdard | HAB8 | HAB10 STANdard: no bundling HAB8: bundling, 8 HARQ processes HAB10: bundling, 10 HARQ processes
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.SubFramePattern)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:CSCHeduling:SFPattern {param}')

	def clone(self) -> 'CschedulingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CschedulingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
