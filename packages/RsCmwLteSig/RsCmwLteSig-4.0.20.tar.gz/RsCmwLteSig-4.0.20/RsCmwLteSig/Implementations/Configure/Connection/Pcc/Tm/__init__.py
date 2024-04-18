from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TmCls:
	"""Tm commands group definition. 15 total commands, 3 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tm", core, parent)

	@property
	def cmatrix(self):
		"""cmatrix commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmatrix'):
			from .Cmatrix import CmatrixCls
			self._cmatrix = CmatrixCls(self._core, self._cmd_group)
		return self._cmatrix

	@property
	def zp(self):
		"""zp commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_zp'):
			from .Zp import ZpCls
			self._zp = ZpCls(self._core, self._cmd_group)
		return self._zp

	@property
	def csirs(self):
		"""csirs commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_csirs'):
			from .Csirs import CsirsCls
			self._csirs = CsirsCls(self._core, self._cmd_group)
		return self._csirs

	# noinspection PyTypeChecker
	class ChMatrixStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
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

	def get_ch_matrix(self) -> ChMatrixStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<8>:CHMatrix \n
		Snippet: value: ChMatrixStruct = driver.configure.connection.pcc.tm.get_ch_matrix() \n
		Configures the channel coefficients, characterizing the radio channel for TM 8. \n
			:return: structure: for return value, see the help for ChMatrixStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM8:CHMatrix?', self.__class__.ChMatrixStruct())

	def set_ch_matrix(self, value: ChMatrixStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<8>:CHMatrix \n
		Snippet with structure: \n
		structure = driver.configure.connection.pcc.tm.ChMatrixStruct() \n
		structure.Abs_11: float = 1.0 \n
		structure.Phase_11: int = 1 \n
		structure.Abs_12: float = 1.0 \n
		structure.Phase_12: int = 1 \n
		structure.Abs_21: float = 1.0 \n
		structure.Phase_21: int = 1 \n
		structure.Abs_22: float = 1.0 \n
		structure.Phase_22: int = 1 \n
		driver.configure.connection.pcc.tm.set_ch_matrix(value = structure) \n
		Configures the channel coefficients, characterizing the radio channel for TM 8. \n
			:param value: see the help for ChMatrixStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM8:CHMatrix', value)

	# noinspection PyTypeChecker
	def get_pmatrix(self) -> enums.PrecodingMatrixMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:PMATrix \n
		Snippet: value: enums.PrecodingMatrixMode = driver.configure.connection.pcc.tm.get_pmatrix() \n
		Selects the second precoding matrix for TM 9. \n
			:return: mode: PMI0 | PMI1 | PMI2 | PMI3 | PMI4 | PMI5 | PMI6 | PMI7 | PMI8 | PMI9 | PMI10 | PMI11 | PMI12 | PMI13 | PMI14 | PMI15 Matrix according to PMI 0, PMI 1, ... PMI 15.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:PMATrix?')
		return Conversions.str_to_scalar_enum(response, enums.PrecodingMatrixMode)

	def set_pmatrix(self, mode: enums.PrecodingMatrixMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:PMATrix \n
		Snippet: driver.configure.connection.pcc.tm.set_pmatrix(mode = enums.PrecodingMatrixMode.PMI0) \n
		Selects the second precoding matrix for TM 9. \n
			:param mode: PMI0 | PMI1 | PMI2 | PMI3 | PMI4 | PMI5 | PMI6 | PMI7 | PMI8 | PMI9 | PMI10 | PMI11 | PMI12 | PMI13 | PMI14 | PMI15 Matrix according to PMI 0, PMI 1, ... PMI 15.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PrecodingMatrixMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:PMATrix {param}')

	# noinspection PyTypeChecker
	def get_codewords(self) -> enums.AntennasTxA:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CODewords \n
		Snippet: value: enums.AntennasTxA = driver.configure.connection.pcc.tm.get_codewords() \n
		Selects the number of code words for TM 9. \n
			:return: codewords: ONE | TWO | FOUR
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CODewords?')
		return Conversions.str_to_scalar_enum(response, enums.AntennasTxA)

	def set_codewords(self, codewords: enums.AntennasTxA) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CODewords \n
		Snippet: driver.configure.connection.pcc.tm.set_codewords(codewords = enums.AntennasTxA.FOUR) \n
		Selects the number of code words for TM 9. \n
			:param codewords: ONE | TWO | FOUR
		"""
		param = Conversions.enum_scalar_to_str(codewords, enums.AntennasTxA)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CODewords {param}')

	# noinspection PyTypeChecker
	def get_ntx_antennas(self) -> enums.AntennasTxB:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:NTXantennas \n
		Snippet: value: enums.AntennasTxB = driver.configure.connection.pcc.tm.get_ntx_antennas() \n
		Selects the number of downlink TX antennas for TM 9. \n
			:return: antennas: TWO | FOUR | EIGHt
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:NTXantennas?')
		return Conversions.str_to_scalar_enum(response, enums.AntennasTxB)

	def set_ntx_antennas(self, antennas: enums.AntennasTxB) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:NTXantennas \n
		Snippet: driver.configure.connection.pcc.tm.set_ntx_antennas(antennas = enums.AntennasTxB.EIGHt) \n
		Selects the number of downlink TX antennas for TM 9. \n
			:param antennas: TWO | FOUR | EIGHt
		"""
		param = Conversions.enum_scalar_to_str(antennas, enums.AntennasTxB)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:NTXantennas {param}')

	def clone(self) -> 'TmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
