from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnhancedCls:
	"""Enhanced commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enhanced", core, parent)

	def set(self, use_reported: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:REPorted:ENHanced \n
		Snippet: driver.configure.connection.ueCategory.reported.enhanced.set(use_reported = False) \n
		Enables or disables the usage of the UE category value reported by the UE. When disabled, the UE category must be set
		manually, see method RsCmwLteSig.Configure.Connection.UeCategory.Manual.enhanced. The manually set value is also used if
		no reported value is available.
			INTRO_CMD_HELP: A query returns two parameters. The second parameter depends on <UseReported> as follows: \n
			- If <UseReported> = ON: Query returns <UseReported>, <UECatReported>.
			- If <UseReported> = OFF: Query returns <UseReported>, <UECatManual>. \n
			:param use_reported: OFF | ON
		"""
		param = Conversions.bool_to_str(use_reported)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:REPorted:ENHanced {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Use_Reported: bool: OFF | ON
			- Ue_Cat_Reported: int: decimal UE category reported by the UE (NAV indicates that none has been reported) Range: 1 to 12
			- Ue_Cat_Manual: enums.UeCatManual: M1 | M2 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 UE category configured manually."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Use_Reported'),
			ArgStruct.scalar_int('Ue_Cat_Reported'),
			ArgStruct.scalar_enum('Ue_Cat_Manual', enums.UeCatManual)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Use_Reported: bool = None
			self.Ue_Cat_Reported: int = None
			self.Ue_Cat_Manual: enums.UeCatManual = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:REPorted:ENHanced \n
		Snippet: value: GetStruct = driver.configure.connection.ueCategory.reported.enhanced.get() \n
		Enables or disables the usage of the UE category value reported by the UE. When disabled, the UE category must be set
		manually, see method RsCmwLteSig.Configure.Connection.UeCategory.Manual.enhanced. The manually set value is also used if
		no reported value is available.
			INTRO_CMD_HELP: A query returns two parameters. The second parameter depends on <UseReported> as follows: \n
			- If <UseReported> = ON: Query returns <UseReported>, <UECatReported>.
			- If <UseReported> = OFF: Query returns <UseReported>, <UECatManual>. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:REPorted:ENHanced?', self.__class__.GetStruct())
