from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PccCls:
	"""Pcc commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcc", core, parent)

	@property
	def stream(self):
		"""stream commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stream'):
			from .Stream import StreamCls
			self._stream = StreamCls(self._core, self._cmd_group)
		return self._stream

	def get_value(self) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection:ETHRoughput:DL[:PCC] \n
		Snippet: value: float = driver.sense.connection.ethroughput.downlink.pcc.get_value() \n
		Returns the expected maximum throughput (averaged over one frame) for the sum of all DL streams of one component carrier.
		The throughput is calculated for the currently selected scheduling type. \n
			:return: throughput: float Unit: Mbit/s
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:CONNection:ETHRoughput:DL:PCC?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'PccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
