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
			- Rsrp_Lower: int: decimal RSRP minimum value Range: -140 dBm to -44 dBm, Unit: dBm
			- Rsrp_Upper: int: decimal RSRP maximum value Range: -140 dBm to -44 dBm, Unit: dBm
			- Rsrq_Lower: float: float RSRQ minimum value Range: -34 dB to 2.5 dB, Unit: dB
			- Rsrq_Upper: float: float RSRQ maximum value Range: -34 dB to 2.5 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rsrp_Lower'),
			ArgStruct.scalar_int('Rsrp_Upper'),
			ArgStruct.scalar_float('Rsrq_Lower'),
			ArgStruct.scalar_float('Rsrq_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rsrp_Lower: int = None
			self.Rsrp_Upper: int = None
			self.Rsrq_Lower: float = None
			self.Rsrq_Upper: float = None

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:SCELl:RANGe \n
		Snippet: value: GetStruct = driver.sense.ueReport.scc.scell.range.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns the value ranges corresponding to the dimensionless index values reported for the serving LTE cell. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:SCELl:RANGe?', self.__class__.GetStruct())
