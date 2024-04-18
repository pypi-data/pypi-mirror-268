from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability indicator'
			- Xvalue: List[float]: float Subframe label, 0 = last processed subframe, -1 = previously processed subframe, and so on
			- Yvalue: List[float]: float Throughput value calculated from the BLER result of 200 processed subframes (the labeled subframe and the previous 199 subframes) Unit: kbit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Xvalue', DataType.FloatList, None, False, True, 1),
			ArgStruct('Yvalue', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Xvalue: List[float] = None
			self.Yvalue: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer:TRACe:THRoughput:ALL \n
		Snippet: value: FetchStruct = driver.ebler.trace.throughput.all.fetch() \n
		Returns the throughput trace for the sum of all downlink streams of all carriers. Each value is returned as a pair of
		X-value and Y-value. The number of result pairs n equals the number of subframes to be processed per measurement cycle,
		divided by 200. Returned results: <Reliability>, <XValue>1, <YValue>1, ..., <XValue>n, <YValue>n \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:EBLer:TRACe:THRoughput:ALL?', self.__class__.FetchStruct())
