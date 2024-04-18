from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReportedCls:
	"""Reported commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reported", core, parent)

	@property
	def enhanced(self):
		"""enhanced commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enhanced'):
			from .Enhanced import EnhancedCls
			self._enhanced = EnhancedCls(self._core, self._cmd_group)
		return self._enhanced

	def set(self, use_reported: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:REPorted \n
		Snippet: driver.configure.connection.ueCategory.reported.set(use_reported = False) \n
		No command help available \n
			:param use_reported: No help available
		"""
		param = Conversions.bool_to_str(use_reported)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:REPorted {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Use_Reported: bool: No parameter help available
			- Ue_Cat_Reported: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Use_Reported'),
			ArgStruct.scalar_int('Ue_Cat_Reported')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Use_Reported: bool = None
			self.Ue_Cat_Reported: int = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:REPorted \n
		Snippet: value: GetStruct = driver.configure.connection.ueCategory.reported.get() \n
		No command help available \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:REPorted?', self.__class__.GetStruct())

	def clone(self) -> 'ReportedCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ReportedCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
