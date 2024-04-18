from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EightCls:
	"""Eight commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: MatrixEightLine, default value after init: MatrixEightLine.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eight", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_matrixEightLine_get', 'repcap_matrixEightLine_set', repcap.MatrixEightLine.Nr1)

	def repcap_matrixEightLine_set(self, matrixEightLine: repcap.MatrixEightLine) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MatrixEightLine.Default
		Default value after init: MatrixEightLine.Nr1"""
		self._cmd_group.set_repcap_enum_value(matrixEightLine)

	def repcap_matrixEightLine_get(self) -> repcap.MatrixEightLine:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- H_1_Xabs: float: numeric Range: 0 to 1
			- H_1_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_2_Xabs: float: numeric Range: 0 to 1
			- H_2_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_3_Xabs: float: numeric Range: 0 to 1
			- H_3_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_4_Xabs: float: numeric Range: 0 to 1
			- H_4_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_5_Xabs: float: numeric Range: 0 to 1
			- H_5_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_6_Xabs: float: numeric Range: 0 to 1
			- H_6_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_7_Xabs: float: numeric Range: 0 to 1
			- H_7_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_8_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_float('H_1_Xabs'),
			ArgStruct.scalar_int('H_1_Xphi'),
			ArgStruct.scalar_float('H_2_Xabs'),
			ArgStruct.scalar_int('H_2_Xphi'),
			ArgStruct.scalar_float('H_3_Xabs'),
			ArgStruct.scalar_int('H_3_Xphi'),
			ArgStruct.scalar_float('H_4_Xabs'),
			ArgStruct.scalar_int('H_4_Xphi'),
			ArgStruct.scalar_float('H_5_Xabs'),
			ArgStruct.scalar_int('H_5_Xphi'),
			ArgStruct.scalar_float('H_6_Xabs'),
			ArgStruct.scalar_int('H_6_Xphi'),
			ArgStruct.scalar_float('H_7_Xabs'),
			ArgStruct.scalar_int('H_7_Xphi'),
			ArgStruct.scalar_int('H_8_Xphi')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.H_1_Xabs: float = None
			self.H_1_Xphi: int = None
			self.H_2_Xabs: float = None
			self.H_2_Xphi: int = None
			self.H_3_Xabs: float = None
			self.H_3_Xphi: int = None
			self.H_4_Xabs: float = None
			self.H_4_Xphi: int = None
			self.H_5_Xabs: float = None
			self.H_5_Xphi: int = None
			self.H_6_Xabs: float = None
			self.H_6_Xphi: int = None
			self.H_7_Xabs: float = None
			self.H_7_Xphi: int = None
			self.H_8_Xphi: int = None

	def set(self, structure: SetStruct, matrixEightLine=repcap.MatrixEightLine.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CMATrix:EIGHt<line> \n
		Snippet with structure: \n
		structure = driver.configure.connection.pcc.tm.cmatrix.eight.SetStruct() \n
		structure.H_1_Xabs: float = 1.0 \n
		structure.H_1_Xphi: int = 1 \n
		structure.H_2_Xabs: float = 1.0 \n
		structure.H_2_Xphi: int = 1 \n
		structure.H_3_Xabs: float = 1.0 \n
		structure.H_3_Xphi: int = 1 \n
		structure.H_4_Xabs: float = 1.0 \n
		structure.H_4_Xphi: int = 1 \n
		structure.H_5_Xabs: float = 1.0 \n
		structure.H_5_Xphi: int = 1 \n
		structure.H_6_Xabs: float = 1.0 \n
		structure.H_6_Xphi: int = 1 \n
		structure.H_7_Xabs: float = 1.0 \n
		structure.H_7_Xphi: int = 1 \n
		structure.H_8_Xphi: int = 1 \n
		driver.configure.connection.pcc.tm.cmatrix.eight.set(structure, matrixEightLine = repcap.MatrixEightLine.Default) \n
		Configures the 8x2 channel coefficients for TM 9.
			INTRO_CMD_HELP: There are two types of parameters: \n
			- <hnmabs> defines the square of the magnitude of the channel coefficient nm: <hnmabs> = (hnm) 2 The sum of all values in one matrix line must not be greater than 1. <h8xabs> is calculated automatically, so that the sum equals 1.
			- <hnmphi> defines the phase of the channel coefficient nm: <hnmphi> = φ(hnm)
		A query returns <h1xabs>, <h1xphi>, <h2xabs>, ..., <h8xabs>, <h8xphi>. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
			:param matrixEightLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eight')
		"""
		matrixEightLine_cmd_val = self._cmd_group.get_repcap_cmd_value(matrixEightLine, repcap.MatrixEightLine)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CMATrix:EIGHt{matrixEightLine_cmd_val}', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- H_1_Xabs: float: numeric Range: 0 to 1
			- H_1_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_2_Xabs: float: numeric Range: 0 to 1
			- H_2_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_3_Xabs: float: numeric Range: 0 to 1
			- H_3_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_4_Xabs: float: numeric Range: 0 to 1
			- H_4_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_5_Xabs: float: numeric Range: 0 to 1
			- H_5_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_6_Xabs: float: numeric Range: 0 to 1
			- H_6_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_7_Xabs: float: numeric Range: 0 to 1
			- H_7_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg
			- H_8_Xabs: float: float Range: 0 to 1
			- H_8_Xphi: int: numeric Range: 0 deg to 345 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_float('H_1_Xabs'),
			ArgStruct.scalar_int('H_1_Xphi'),
			ArgStruct.scalar_float('H_2_Xabs'),
			ArgStruct.scalar_int('H_2_Xphi'),
			ArgStruct.scalar_float('H_3_Xabs'),
			ArgStruct.scalar_int('H_3_Xphi'),
			ArgStruct.scalar_float('H_4_Xabs'),
			ArgStruct.scalar_int('H_4_Xphi'),
			ArgStruct.scalar_float('H_5_Xabs'),
			ArgStruct.scalar_int('H_5_Xphi'),
			ArgStruct.scalar_float('H_6_Xabs'),
			ArgStruct.scalar_int('H_6_Xphi'),
			ArgStruct.scalar_float('H_7_Xabs'),
			ArgStruct.scalar_int('H_7_Xphi'),
			ArgStruct.scalar_float('H_8_Xabs'),
			ArgStruct.scalar_int('H_8_Xphi')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.H_1_Xabs: float = None
			self.H_1_Xphi: int = None
			self.H_2_Xabs: float = None
			self.H_2_Xphi: int = None
			self.H_3_Xabs: float = None
			self.H_3_Xphi: int = None
			self.H_4_Xabs: float = None
			self.H_4_Xphi: int = None
			self.H_5_Xabs: float = None
			self.H_5_Xphi: int = None
			self.H_6_Xabs: float = None
			self.H_6_Xphi: int = None
			self.H_7_Xabs: float = None
			self.H_7_Xphi: int = None
			self.H_8_Xabs: float = None
			self.H_8_Xphi: int = None

	def get(self, matrixEightLine=repcap.MatrixEightLine.Default) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CMATrix:EIGHt<line> \n
		Snippet: value: GetStruct = driver.configure.connection.pcc.tm.cmatrix.eight.get(matrixEightLine = repcap.MatrixEightLine.Default) \n
		Configures the 8x2 channel coefficients for TM 9.
			INTRO_CMD_HELP: There are two types of parameters: \n
			- <hnmabs> defines the square of the magnitude of the channel coefficient nm: <hnmabs> = (hnm) 2 The sum of all values in one matrix line must not be greater than 1. <h8xabs> is calculated automatically, so that the sum equals 1.
			- <hnmphi> defines the phase of the channel coefficient nm: <hnmphi> = φ(hnm)
		A query returns <h1xabs>, <h1xphi>, <h2xabs>, ..., <h8xabs>, <h8xphi>. \n
			:param matrixEightLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eight')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		matrixEightLine_cmd_val = self._cmd_group.get_repcap_cmd_value(matrixEightLine, repcap.MatrixEightLine)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CMATrix:EIGHt{matrixEightLine_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'EightCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EightCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
