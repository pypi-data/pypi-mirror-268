from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DateCls:
	"""Date commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("date", core, parent)

	def set(self, day: int, month: int, year: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TIME:DATE \n
		Snippet: driver.configure.cell.time.date.set(day = 1, month = 1, year = 1) \n
		Specifies the UTC date for the time source DATE (see method RsCmwLteSig.Configure.Cell.Time.tsource) . \n
			:param day: integer Range: 1 to 31
			:param month: integer Range: 1 to 12
			:param year: integer Range: 2011 to 9999
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('day', day, DataType.Integer), ArgSingle('month', month, DataType.Integer), ArgSingle('year', year, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:TIME:DATE {param}'.rstrip())

	# noinspection PyTypeChecker
	class DateStruct(StructBase):
		"""Response structure. Fields: \n
			- Day: int: integer Range: 1 to 31
			- Month: int: integer Range: 1 to 12
			- Year: int: integer Range: 2011 to 9999"""
		__meta_args_list = [
			ArgStruct.scalar_int('Day'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Year')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Day: int = None
			self.Month: int = None
			self.Year: int = None

	def get(self) -> DateStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TIME:DATE \n
		Snippet: value: DateStruct = driver.configure.cell.time.date.get() \n
		Specifies the UTC date for the time source DATE (see method RsCmwLteSig.Configure.Cell.Time.tsource) . \n
			:return: structure: for return value, see the help for DateStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CELL:TIME:DATE?', self.__class__.DateStruct())
