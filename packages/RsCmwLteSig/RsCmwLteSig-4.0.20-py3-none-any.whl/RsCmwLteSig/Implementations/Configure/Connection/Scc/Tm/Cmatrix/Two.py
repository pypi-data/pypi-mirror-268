from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TwoCls:
	"""Two commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: MatrixTwoLine, default value after init: MatrixTwoLine.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("two", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_matrixTwoLine_get', 'repcap_matrixTwoLine_set', repcap.MatrixTwoLine.Nr1)

	def repcap_matrixTwoLine_set(self, matrixTwoLine: repcap.MatrixTwoLine) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MatrixTwoLine.Default
		Default value after init: MatrixTwoLine.Nr1"""
		self._cmd_group.set_repcap_enum_value(matrixTwoLine)

	def repcap_matrixTwoLine_get(self) -> repcap.MatrixTwoLine:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, h_1_xabs: float, h_1_xphi: int, h_2_xphi: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, matrixTwoLine=repcap.MatrixTwoLine.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:CMATrix:TWO<line> \n
		Snippet: driver.configure.connection.scc.tm.cmatrix.two.set(h_1_xabs = 1.0, h_1_xphi = 1, h_2_xphi = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, matrixTwoLine = repcap.MatrixTwoLine.Default) \n
		Configures the 2x2 channel coefficients for TM 9. The value <h2xabs> is calculated automatically from <h1xabs>, so that
		the sum of the values equals 1. A query returns <h1xabs>, <h1xphi>, <h2xabs>, <h2xphi>. \n
			:param h_1_xabs: numeric Square of magnitude of h1x Range: 0 to 1
			:param h_1_xphi: numeric Phase of h1x Range: 0 deg to 345 deg, Unit: deg
			:param h_2_xphi: numeric Phase of h2x Range: 0 deg to 345 deg, Unit: deg
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param matrixTwoLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Two')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('h_1_xabs', h_1_xabs, DataType.Float), ArgSingle('h_1_xphi', h_1_xphi, DataType.Integer), ArgSingle('h_2_xphi', h_2_xphi, DataType.Integer))
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		matrixTwoLine_cmd_val = self._cmd_group.get_repcap_cmd_value(matrixTwoLine, repcap.MatrixTwoLine)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CMATrix:TWO{matrixTwoLine_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- H_1_Xabs: float: numeric Square of magnitude of h1x Range: 0 to 1
			- H_1_Xphi: int: numeric Phase of h1x Range: 0 deg to 345 deg, Unit: deg
			- H_2_Xabs: float: float Square of magnitude of h2x Range: 0 to 1
			- H_2_Xphi: int: numeric Phase of h2x Range: 0 deg to 345 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_float('H_1_Xabs'),
			ArgStruct.scalar_int('H_1_Xphi'),
			ArgStruct.scalar_float('H_2_Xabs'),
			ArgStruct.scalar_int('H_2_Xphi')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.H_1_Xabs: float = None
			self.H_1_Xphi: int = None
			self.H_2_Xabs: float = None
			self.H_2_Xphi: int = None

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, matrixTwoLine=repcap.MatrixTwoLine.Default) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:CMATrix:TWO<line> \n
		Snippet: value: GetStruct = driver.configure.connection.scc.tm.cmatrix.two.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, matrixTwoLine = repcap.MatrixTwoLine.Default) \n
		Configures the 2x2 channel coefficients for TM 9. The value <h2xabs> is calculated automatically from <h1xabs>, so that
		the sum of the values equals 1. A query returns <h1xabs>, <h1xphi>, <h2xabs>, <h2xphi>. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param matrixTwoLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Two')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		matrixTwoLine_cmd_val = self._cmd_group.get_repcap_cmd_value(matrixTwoLine, repcap.MatrixTwoLine)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CMATrix:TWO{matrixTwoLine_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'TwoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TwoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
