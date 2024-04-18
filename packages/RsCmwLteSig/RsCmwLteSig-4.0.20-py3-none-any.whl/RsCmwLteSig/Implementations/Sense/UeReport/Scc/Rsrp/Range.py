from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RangeCls:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Lower: int: decimal Range: -140 dBm to -44 dBm, Unit: dBm
			- Upper: int: decimal Range: -140 dBm to -44 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Lower'),
			ArgStruct.scalar_int('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower: int = None
			self.Upper: int = None

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RSRP:RANGe \n
		Snippet: value: GetStruct = driver.sense.ueReport.scc.rsrp.range.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns the RSRP value range, corresponding to the RSRP index reported by the UE. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RSRP:RANGe?', self.__class__.GetStruct())
