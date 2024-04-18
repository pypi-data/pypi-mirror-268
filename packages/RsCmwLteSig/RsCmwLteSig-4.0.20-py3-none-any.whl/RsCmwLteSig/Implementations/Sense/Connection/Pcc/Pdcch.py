from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcchCls:
	"""Pdcch commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcch", core, parent)

	def get_psymbols(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection[:PCC]:PDCCh:PSYMbols \n
		Snippet: value: int = driver.sense.connection.pcc.pdcch.get_psymbols() \n
		Queries the number of PDCCH symbols per normal subframe. \n
			:return: pdcch_symbols: decimal Range: 1 to 4
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:CONNection:PCC:PDCCh:PSYMbols?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	class AlevelStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Dldci_Crnti: int: decimal DCI for DL with C-RNTI Range: 1 to 8
			- Uldci_Crnti: int: decimal DCI for UL with C-RNTI Range: 1 to 8
			- Dldci_Sirnti: int: decimal DCI for DL with SI-RNTI Range: 1 to 8"""
		__meta_args_list = [
			ArgStruct.scalar_int('Dldci_Crnti'),
			ArgStruct.scalar_int('Uldci_Crnti'),
			ArgStruct.scalar_int('Dldci_Sirnti')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dldci_Crnti: int = None
			self.Uldci_Crnti: int = None
			self.Dldci_Sirnti: int = None

	def get_alevel(self) -> AlevelStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection[:PCC]:PDCCh:ALEVel \n
		Snippet: value: AlevelStruct = driver.sense.connection.pcc.pdcch.get_alevel() \n
		Queries the used PDCCH aggregation levels. \n
			:return: structure: for return value, see the help for AlevelStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:LTE:SIGNaling<Instance>:CONNection:PCC:PDCCh:ALEVel?', self.__class__.AlevelStruct())
