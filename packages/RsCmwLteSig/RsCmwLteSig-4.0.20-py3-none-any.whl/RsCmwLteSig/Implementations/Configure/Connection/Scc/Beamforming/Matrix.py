from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MatrixCls:
	"""Matrix commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("matrix", core, parent)

	# noinspection PyTypeChecker
	class MatrixStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- B_11_Phi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- B_12_Phi: int: Optional setting parameter. numeric Range: 0 deg to 345 deg, Unit: deg
			- B_11_Abs: float: Optional setting parameter. numeric Range: 0 to 1
			- B_12_Abs: float: Optional setting parameter. numeric Range: 0 to 1
			- B_21_Phi: int: Optional setting parameter. numeric Range: 0 deg to 345 deg, Unit: deg
			- B_22_Phi: int: Optional setting parameter. numeric Range: 0 deg to 345 deg, Unit: deg
			- B_13_Phi: int: Optional setting parameter. numeric Range: 0 deg to 345 deg, Unit: deg
			- B_14_Phi: int: Optional setting parameter. numeric Range: 0 deg to 345 deg, Unit: deg
			- B_13_Abs: float: Optional setting parameter. numeric Range: 0 to 1
			- B_14_Abs: float: Optional setting parameter. numeric Range: 0 to 1
			- B_23_Phi: int: Optional setting parameter. numeric Range: 0 deg to 345 deg, Unit: deg
			- B_24_Phi: int: Optional setting parameter. numeric Range: 0 deg to 345 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_int('B_11_Phi'),
			ArgStruct.scalar_int_optional('B_12_Phi'),
			ArgStruct.scalar_float_optional('B_11_Abs'),
			ArgStruct.scalar_float_optional('B_12_Abs'),
			ArgStruct.scalar_int_optional('B_21_Phi'),
			ArgStruct.scalar_int_optional('B_22_Phi'),
			ArgStruct.scalar_int_optional('B_13_Phi'),
			ArgStruct.scalar_int_optional('B_14_Phi'),
			ArgStruct.scalar_float_optional('B_13_Abs'),
			ArgStruct.scalar_float_optional('B_14_Abs'),
			ArgStruct.scalar_int_optional('B_23_Phi'),
			ArgStruct.scalar_int_optional('B_24_Phi')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.B_11_Phi: int = None
			self.B_12_Phi: int = None
			self.B_11_Abs: float = None
			self.B_12_Abs: float = None
			self.B_21_Phi: int = None
			self.B_22_Phi: int = None
			self.B_13_Phi: int = None
			self.B_14_Phi: int = None
			self.B_13_Abs: float = None
			self.B_14_Abs: float = None
			self.B_23_Phi: int = None
			self.B_24_Phi: int = None

	def set(self, structure: MatrixStruct, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:BEAMforming:MATRix \n
		Snippet with structure: \n
		structure = driver.configure.connection.scc.beamforming.matrix.MatrixStruct() \n
		structure.B_11_Phi: int = 1 \n
		structure.B_12_Phi: int = 1 \n
		structure.B_11_Abs: float = 1.0 \n
		structure.B_12_Abs: float = 1.0 \n
		structure.B_21_Phi: int = 1 \n
		structure.B_22_Phi: int = 1 \n
		structure.B_13_Phi: int = 1 \n
		structure.B_14_Phi: int = 1 \n
		structure.B_13_Abs: float = 1.0 \n
		structure.B_14_Abs: float = 1.0 \n
		structure.B_23_Phi: int = 1 \n
		structure.B_24_Phi: int = 1 \n
		driver.configure.connection.scc.beamforming.matrix.set(structure, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the beamforming matrix coefficients for TM 7 and TM 8.
			INTRO_CMD_HELP: There are two types of parameters: \n
			- <bnmabs> defines the square of the magnitude of the coefficient nm: <bnmabs> = (bnm) 2
			- <bnmphi> defines the phase of the coefficient nm: <bnmphi> = φ(bnm) The phase can be entered in steps of 15 degrees. The setting is rounded, if necessary.
			INTRO_CMD_HELP: Depending on the size of your matrix, use the following parameters: \n
			- 1x1: <b11phi>
			- 1x2: <b11phi>, <b12phi>
			- 2x2: <b11phi>, <b12phi>, <b11abs>, <b12abs>, <b21phi>, <b22phi>
		The last six parameters are for future use and can always be omitted. \n
			:param structure: for set value, see the help for MatrixStruct structure arguments.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:BEAMforming:MATRix', structure)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> MatrixStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:BEAMforming:MATRix \n
		Snippet: value: MatrixStruct = driver.configure.connection.scc.beamforming.matrix.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the beamforming matrix coefficients for TM 7 and TM 8.
			INTRO_CMD_HELP: There are two types of parameters: \n
			- <bnmabs> defines the square of the magnitude of the coefficient nm: <bnmabs> = (bnm) 2
			- <bnmphi> defines the phase of the coefficient nm: <bnmphi> = φ(bnm) The phase can be entered in steps of 15 degrees. The setting is rounded, if necessary.
			INTRO_CMD_HELP: Depending on the size of your matrix, use the following parameters: \n
			- 1x1: <b11phi>
			- 1x2: <b11phi>, <b12phi>
			- 2x2: <b11phi>, <b12phi>, <b11abs>, <b12abs>, <b21phi>, <b22phi>
		The last six parameters are for future use and can always be omitted. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for MatrixStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:BEAMforming:MATRix?', self.__class__.MatrixStruct())
