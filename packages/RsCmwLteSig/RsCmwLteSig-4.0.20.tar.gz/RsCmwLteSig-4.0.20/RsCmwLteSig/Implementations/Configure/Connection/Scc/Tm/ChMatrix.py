from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChMatrixCls:
	"""ChMatrix commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chMatrix", core, parent)

	# noinspection PyTypeChecker
	class ChMatrixStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Abs_11: float: numeric Square of magnitude of h11 abs11 + abs12 must equal 1 Range: 0 to 1
			- Phase_11: int: numeric Phase of h11 Range: 0 deg to 345 deg, Unit: deg
			- Abs_12: float: numeric Square of magnitude of h12 Range: 0 to 1
			- Phase_12: int: numeric Phase of h12 Range: 0 deg to 345 deg, Unit: deg
			- Abs_21: float: numeric Square of magnitude of h21 abs21 + abs22 must equal 1 Range: 0 to 1
			- Phase_21: int: numeric Phase of h21 Range: 0 deg to 345 deg, Unit: deg
			- Abs_22: float: numeric Square of magnitude of h22 Range: 0 to 1
			- Phase_22: int: numeric Phase of h22 Range: 0 deg to 345 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_float('Abs_11'),
			ArgStruct.scalar_int('Phase_11'),
			ArgStruct.scalar_float('Abs_12'),
			ArgStruct.scalar_int('Phase_12'),
			ArgStruct.scalar_float('Abs_21'),
			ArgStruct.scalar_int('Phase_21'),
			ArgStruct.scalar_float('Abs_22'),
			ArgStruct.scalar_int('Phase_22')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Abs_11: float = None
			self.Phase_11: int = None
			self.Abs_12: float = None
			self.Phase_12: int = None
			self.Abs_21: float = None
			self.Phase_21: int = None
			self.Abs_22: float = None
			self.Phase_22: int = None

	def set(self, structure: ChMatrixStruct, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<8>:CHMatrix \n
		Snippet with structure: \n
		structure = driver.configure.connection.scc.tm.chMatrix.ChMatrixStruct() \n
		structure.Abs_11: float = 1.0 \n
		structure.Phase_11: int = 1 \n
		structure.Abs_12: float = 1.0 \n
		structure.Phase_12: int = 1 \n
		structure.Abs_21: float = 1.0 \n
		structure.Phase_21: int = 1 \n
		structure.Abs_22: float = 1.0 \n
		structure.Phase_22: int = 1 \n
		driver.configure.connection.scc.tm.chMatrix.set(structure, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the channel coefficients, characterizing the radio channel for TM 8. \n
			:param structure: for set value, see the help for ChMatrixStruct structure arguments.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM8:CHMatrix', structure)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> ChMatrixStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<8>:CHMatrix \n
		Snippet: value: ChMatrixStruct = driver.configure.connection.scc.tm.chMatrix.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the channel coefficients, characterizing the radio channel for TM 8. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for ChMatrixStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM8:CHMatrix?', self.__class__.ChMatrixStruct())
