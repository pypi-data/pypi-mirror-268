from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SccCls:
	"""Scc commands group definition. 3 total commands, 2 Subgroups, 1 group commands
	Repeated Capability: SecondaryCompCarrier, default value after init: SecondaryCompCarrier.CC1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_secondaryCompCarrier_get', 'repcap_secondaryCompCarrier_set', repcap.SecondaryCompCarrier.CC1)

	def repcap_secondaryCompCarrier_set(self, secondaryCompCarrier: repcap.SecondaryCompCarrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondaryCompCarrier.Default
		Default value after init: SecondaryCompCarrier.CC1"""
		self._cmd_group.set_repcap_enum_value(secondaryCompCarrier)

	def repcap_secondaryCompCarrier_get(self) -> repcap.SecondaryCompCarrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def stream(self):
		"""stream commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stream'):
			from .Stream import StreamCls
			self._stream = StreamCls(self._core, self._cmd_group)
		return self._stream

	@property
	def mcqi(self):
		"""mcqi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcqi'):
			from .Mcqi import McqiCls
			self._mcqi = McqiCls(self._core, self._cmd_group)
		return self._mcqi

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

	def fetch(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> FetchStruct:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer:TRACe:THRoughput:SCC<Carrier> \n
		Snippet: value: FetchStruct = driver.ebler.trace.throughput.scc.fetch(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns the throughput trace for the sum of all DL streams of one carrier. Each value is returned as a pair of X-value
		and Y-value. The number of result pairs n equals the number of subframes to be processed per measurement cycle, divided
		by 200. Returned results: <Reliability>, <XValue>1, <YValue>1, ..., <XValue>n, <YValue>n \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:EBLer:TRACe:THRoughput:SCC{secondaryCompCarrier_cmd_val}?', self.__class__.FetchStruct())

	def clone(self) -> 'SccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
