from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AbsoluteCls:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability indicator'
			- Ack: int: decimal Number of received acknowledgments (sum of all downlink streams)
			- Nack: int: decimal Number of received negative acknowledgments (sum of all downlink streams)
			- Expired_Subframes: int: No parameter help available
			- Throughput: List[float]: No parameter help available
			- Dtx: int: decimal Number of sent scheduled subframes for which no ACK and no NACK has been received (sum of all downlink streams)
			- Scheduled: int: decimal Number of already sent scheduled subframes (per downlink stream)
			- Median_Cqi: int: decimal Median value of received CQI indices"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Ack'),
			ArgStruct.scalar_int('Nack'),
			ArgStruct.scalar_int('Expired_Subframes'),
			ArgStruct('Throughput', DataType.FloatList, None, False, False, 3),
			ArgStruct.scalar_int('Dtx'),
			ArgStruct.scalar_int('Scheduled'),
			ArgStruct.scalar_int('Median_Cqi')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ack: int = None
			self.Nack: int = None
			self.Expired_Subframes: int = None
			self.Throughput: List[float] = None
			self.Dtx: int = None
			self.Scheduled: int = None
			self.Median_Cqi: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:INTermediate:LTE:SIGNaling<instance>:EBLer[:PCC]:ABSolute \n
		Snippet: value: FetchStruct = driver.intermediate.ebler.pcc.absolute.fetch() \n
		Returns the absolute overall results of the BLER measurement for the sum of all DL streams of one carrier. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:INTermediate:LTE:SIGNaling<Instance>:EBLer:PCC:ABSolute?', self.__class__.FetchStruct())
