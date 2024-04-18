from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScellCls:
	"""Scell commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scell", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import RangeCls
			self._range = RangeCls(self._core, self._cmd_group)
		return self._range

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Rsrp: int: decimal RSRP as dimensionless index Range: 0 to 97
			- Rsrq: int: decimal RSRQ as dimensionless index Range: -30 to 46"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rsrp'),
			ArgStruct.scalar_int('Rsrq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rsrp: int = None
			self.Rsrq: int = None

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:SCELl \n
		Snippet: value: GetStruct = driver.sense.ueReport.scc.scell.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns measurement report values for the serving LTE cell. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:SCELl?', self.__class__.GetStruct())

	def clone(self) -> 'ScellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
