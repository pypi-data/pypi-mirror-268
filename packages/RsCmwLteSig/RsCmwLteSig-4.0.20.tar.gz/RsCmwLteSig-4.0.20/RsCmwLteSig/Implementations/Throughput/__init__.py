from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ThroughputCls:
	"""Throughput commands group definition. 15 total commands, 2 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("throughput", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	def stop(self) -> None:
		"""SCPI: STOP:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:LTE:SIGNaling<Instance>:THRoughput')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:LTE:SIGNaling<Instance>:THRoughput', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:LTE:SIGNaling<Instance>:THRoughput', opc_timeout_ms)

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:LTE:SIGNaling<Instance>:THRoughput', opc_timeout_ms)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability indicator'
			- Curr_Dl_Pdu: float: float Current downlink throughput Unit: bit/s
			- Avg_Dl_Pdu: float: float Average downlink throughput Unit: bit/s
			- Max_Dl_Pdu: float: float Maximum downlink throughput Unit: bit/s
			- Min_Dl_Pdu: float: float Minimum downlink throughput Unit: bit/s
			- Bytes_Dl_Pdu: int: decimal Number of bytes transmitted in the downlink
			- Curr_Ul_Pdu: float: float Current uplink throughput Unit: bit/s
			- Avg_Ul_Pdu: float: float Average uplink throughput Unit: bit/s
			- Max_Ul_Pdu: float: float Maximum uplink throughput Unit: bit/s
			- Min_Ul_Pdu: float: float Minimum uplink throughput Unit: bit/s
			- Bytes_Ul_Pdu: float: float Number of bytes received in the uplink"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Curr_Dl_Pdu'),
			ArgStruct.scalar_float('Avg_Dl_Pdu'),
			ArgStruct.scalar_float('Max_Dl_Pdu'),
			ArgStruct.scalar_float('Min_Dl_Pdu'),
			ArgStruct.scalar_int('Bytes_Dl_Pdu'),
			ArgStruct.scalar_float('Curr_Ul_Pdu'),
			ArgStruct.scalar_float('Avg_Ul_Pdu'),
			ArgStruct.scalar_float('Max_Ul_Pdu'),
			ArgStruct.scalar_float('Min_Ul_Pdu'),
			ArgStruct.scalar_float('Bytes_Ul_Pdu')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Curr_Dl_Pdu: float = None
			self.Avg_Dl_Pdu: float = None
			self.Max_Dl_Pdu: float = None
			self.Min_Dl_Pdu: float = None
			self.Bytes_Dl_Pdu: int = None
			self.Curr_Ul_Pdu: float = None
			self.Avg_Ul_Pdu: float = None
			self.Max_Ul_Pdu: float = None
			self.Min_Ul_Pdu: float = None
			self.Bytes_Ul_Pdu: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: value: ResultData = driver.throughput.fetch() \n
		Returns the contents of the RLC throughput result table. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:THRoughput?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: value: ResultData = driver.throughput.read() \n
		Returns the contents of the RLC throughput result table. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:LTE:SIGNaling<Instance>:THRoughput?', self.__class__.ResultData())

	def clone(self) -> 'ThroughputCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ThroughputCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
