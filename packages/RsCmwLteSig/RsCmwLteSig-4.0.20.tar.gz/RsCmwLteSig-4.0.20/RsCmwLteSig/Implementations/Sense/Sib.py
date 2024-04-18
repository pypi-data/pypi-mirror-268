from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SibCls:
	"""Sib commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sib", core, parent)

	# noinspection PyTypeChecker
	class TtimingStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Lst_High: int: No parameter help available
			- Lst_Low: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Lst_High'),
			ArgStruct.scalar_int('Lst_Low')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lst_High: int = None
			self.Lst_Low: int = None

	def get_ttiming(self) -> TtimingStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:SIB<n>:TTIMing \n
		Snippet: value: TtimingStruct = driver.sense.sib.get_ttiming() \n
		No command help available \n
			:return: structure: for return value, see the help for TtimingStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:LTE:SIGNaling<Instance>:SIB1:TTIMing?', self.__class__.TtimingStruct())
