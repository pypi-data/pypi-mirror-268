from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsrqCls:
	"""Rsrq commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsrq", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import RangeCls
			self._range = RangeCls(self._core, self._cmd_group)
		return self._range

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RSRQ \n
		Snippet: value: int = driver.sense.ueReport.scc.rsrq.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns the RSRQ reported by the UE as dimensionless index. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: rsrq: decimal Range: -30 to 46"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RSRQ?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'RsrqCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RsrqCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
