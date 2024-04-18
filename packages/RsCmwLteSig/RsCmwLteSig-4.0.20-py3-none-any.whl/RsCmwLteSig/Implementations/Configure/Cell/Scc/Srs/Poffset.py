from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoffsetCls:
	"""Poffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	def set(self, offset: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:SRS:POFFset \n
		Snippet: driver.configure.cell.scc.srs.poffset.set(offset = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'pSRS-Offset' value. The setting is only used if manual configuration is enabled, see method RsCmwLteSig.
		Configure.Cell.Pcc.Srs.mcEnable. A query returns <Offset>, <Value>. \n
			:param offset: decimal 'pSRS-Offset' value Range: 0 to 15
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SRS:POFFset {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Offset: int: decimal 'pSRS-Offset' value Range: 0 to 15
			- Value: float: float Offset in dB, corresponding to the configured 'pSRS-Offset' value Range: -10.5 dB to 12 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Offset'),
			ArgStruct.scalar_float('Value')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Offset: int = None
			self.Value: float = None

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:SRS:POFFset \n
		Snippet: value: GetStruct = driver.configure.cell.scc.srs.poffset.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'pSRS-Offset' value. The setting is only used if manual configuration is enabled, see method RsCmwLteSig.
		Configure.Cell.Pcc.Srs.mcEnable. A query returns <Offset>, <Value>. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SRS:POFFset?', self.__class__.GetStruct())
