from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MclusterCls:
	"""Mcluster commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcluster", core, parent)

	# noinspection PyTypeChecker
	class UplinkStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Number_Rb_1: enums.NumberRb: ZERO | N1 | N2 | N3 | N4 | N5 | N6 | N7 | N8 | N9 | N10 | N12 | N15 | N16 | N17 | N18 | N20 | N21 | N24 | N25 | N27 | N30 | N32 | N36 | N40 | N42 | N45 | N48 | N50 | N54 | N60 | N64 | N72 | N75 | N80 | N81 | N83 | N90 | N92 | N96 | N100 Number of allocated resource blocks, cluster 1
			- Position_Rb_1: enums.RbPosition: FULL | LOW | HIGH | MID | P0 | P1 | P2 | P3 | P4 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | P13 | P14 | P15 | P16 | P19 | P20 | P21 | P22 | P24 | P25 | P28 | P30 | P31 | P33 | P36 | P37 | P39 | P40 | P43 | P44 | P45 | P48 | P49 | P50 | P51 | P52 | P54 | P56 | P57 | P58 | P62 | P63 | P66 | P68 | P70 | P74 | P75 | P83 | P96 | P99 Position of first RB, cluster 1
			- Number_Rb_2: enums.NumberRb: ZERO | N1 | N2 | N3 | N4 | N5 | N6 | N7 | N8 | N9 | N10 | N12 | N15 | N16 | N17 | N18 | N20 | N21 | N24 | N25 | N27 | N30 | N32 | N36 | N40 | N42 | N45 | N48 | N50 | N54 | N60 | N64 | N72 | N75 | N80 | N81 | N83 | N90 | N92 | N96 | N100 Number of allocated resource blocks, cluster 2
			- Position_Rb_2: enums.RbPosition: FULL | LOW | HIGH | MID | P0 | P1 | P2 | P3 | P4 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | P13 | P14 | P15 | P16 | P19 | P20 | P21 | P22 | P24 | P25 | P28 | P30 | P31 | P33 | P36 | P37 | P39 | P40 | P43 | P44 | P45 | P48 | P49 | P50 | P51 | P52 | P54 | P56 | P57 | P58 | P62 | P63 | P66 | P68 | P70 | P74 | P75 | P83 | P96 | P99 Position of first RB, cluster 2
			- Modulation: enums.Modulation: Q16 | Q64 Modulation type 16-QAM | 64-QAM
			- Trans_Block_Size_Idx: enums.TransBlockSizeIdx: ZERO | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 | T13 | T14 | T15 | T16 | T17 | T18 | T19 | T20 | T21 | T22 | T23 | T24 | T25 | T26 | T27 | T28 | T29 | T30 | T31 | T32 | T33 | T34 | T35 | T36 | T37 Transport block size index. Use KEEP to select a compatible value."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Number_Rb_1', enums.NumberRb),
			ArgStruct.scalar_enum('Position_Rb_1', enums.RbPosition),
			ArgStruct.scalar_enum('Number_Rb_2', enums.NumberRb),
			ArgStruct.scalar_enum('Position_Rb_2', enums.RbPosition),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_enum('Trans_Block_Size_Idx', enums.TransBlockSizeIdx)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb_1: enums.NumberRb = None
			self.Position_Rb_1: enums.RbPosition = None
			self.Number_Rb_2: enums.NumberRb = None
			self.Position_Rb_2: enums.RbPosition = None
			self.Modulation: enums.Modulation = None
			self.Trans_Block_Size_Idx: enums.TransBlockSizeIdx = None

	def get_uplink(self) -> UplinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:MCLuster:UL \n
		Snippet: value: UplinkStruct = driver.configure.connection.pcc.rmc.mcluster.get_uplink() \n
		Configures an uplink reference measurement channel (RMC) with multi-cluster allocation. Only certain value combinations
		are accepted, see 'Scheduling type RMC'. \n
			:return: structure: for return value, see the help for UplinkStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:MCLuster:UL?', self.__class__.UplinkStruct())

	def set_uplink(self, value: UplinkStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:MCLuster:UL \n
		Snippet with structure: \n
		structure = driver.configure.connection.pcc.rmc.mcluster.UplinkStruct() \n
		structure.Number_Rb_1: enums.NumberRb = enums.NumberRb.N1 \n
		structure.Position_Rb_1: enums.RbPosition = enums.RbPosition.FULL \n
		structure.Number_Rb_2: enums.NumberRb = enums.NumberRb.N1 \n
		structure.Position_Rb_2: enums.RbPosition = enums.RbPosition.FULL \n
		structure.Modulation: enums.Modulation = enums.Modulation.Q1024 \n
		structure.Trans_Block_Size_Idx: enums.TransBlockSizeIdx = enums.TransBlockSizeIdx.T1 \n
		driver.configure.connection.pcc.rmc.mcluster.set_uplink(value = structure) \n
		Configures an uplink reference measurement channel (RMC) with multi-cluster allocation. Only certain value combinations
		are accepted, see 'Scheduling type RMC'. \n
			:param value: see the help for UplinkStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:MCLuster:UL', value)
