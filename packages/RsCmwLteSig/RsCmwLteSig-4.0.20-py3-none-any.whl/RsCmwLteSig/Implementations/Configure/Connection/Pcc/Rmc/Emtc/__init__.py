from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EmtcCls:
	"""Emtc commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emtc", core, parent)

	@property
	def nbPosition(self):
		"""nbPosition commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_nbPosition'):
			from .NbPosition import NbPositionCls
			self._nbPosition = NbPositionCls(self._core, self._cmd_group)
		return self._nbPosition

	# noinspection PyTypeChecker
	def get_sf_pattern(self) -> enums.EmtcRmcPattern:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:EMTC:SFPattern \n
		Snippet: value: enums.EmtcRmcPattern = driver.configure.connection.pcc.rmc.emtc.get_sf_pattern() \n
		Determines the subframe pattern for eMTC RMCs. \n
			:return: pattern: P1 | P2 | P3 | P4 | P5 P1: standard P2: chapter 6.3.4EA P3: chapter 6.3.5EA.3 P4: chapter 6.5.2.1EA.2-A P5: chapter 6.5.2.1EA.2-B
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:EMTC:SFPattern?')
		return Conversions.str_to_scalar_enum(response, enums.EmtcRmcPattern)

	def set_sf_pattern(self, pattern: enums.EmtcRmcPattern) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:EMTC:SFPattern \n
		Snippet: driver.configure.connection.pcc.rmc.emtc.set_sf_pattern(pattern = enums.EmtcRmcPattern.P1) \n
		Determines the subframe pattern for eMTC RMCs. \n
			:param pattern: P1 | P2 | P3 | P4 | P5 P1: standard P2: chapter 6.3.4EA P3: chapter 6.3.5EA.3 P4: chapter 6.5.2.1EA.2-A P5: chapter 6.5.2.1EA.2-B
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.EmtcRmcPattern)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:EMTC:SFPattern {param}')

	def clone(self) -> 'EmtcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EmtcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
