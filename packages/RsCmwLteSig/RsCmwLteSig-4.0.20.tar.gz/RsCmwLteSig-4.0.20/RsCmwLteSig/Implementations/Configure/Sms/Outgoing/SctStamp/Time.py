from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimeCls:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, hour: int, minute: int, second: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TIME \n
		Snippet: driver.configure.sms.outgoing.sctStamp.time.set(hour = 1, minute = 1, second = 1) \n
		Specifies the time of the service center time stamp for the time source DATE (see method RsCmwLteSig.Configure.Sms.
		Outgoing.SctStamp.tsource) . \n
			:param hour: integer Range: 0 to 23
			:param minute: integer Range: 0 to 59
			:param second: integer Range: 0 to 59
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('hour', hour, DataType.Integer), ArgSingle('minute', minute, DataType.Integer), ArgSingle('second', second, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TIME {param}'.rstrip())

	# noinspection PyTypeChecker
	class TimeStruct(StructBase):
		"""Response structure. Fields: \n
			- Hour: int: integer Range: 0 to 23
			- Minute: int: integer Range: 0 to 59
			- Second: int: integer Range: 0 to 59"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute'),
			ArgStruct.scalar_int('Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Minute: int = None
			self.Second: int = None

	def get(self) -> TimeStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TIME \n
		Snippet: value: TimeStruct = driver.configure.sms.outgoing.sctStamp.time.get() \n
		Specifies the time of the service center time stamp for the time source DATE (see method RsCmwLteSig.Configure.Sms.
		Outgoing.SctStamp.tsource) . \n
			:return: structure: for return value, see the help for TimeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TIME?', self.__class__.TimeStruct())
