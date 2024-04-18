from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	# noinspection PyTypeChecker
	class UplinkStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Number_Rb_1: int: numeric Number of allocated resource blocks, cluster 1
			- Start_Rb_1: int: numeric Position of first RB, cluster 1
			- Number_Rb_2: int: numeric Number of allocated resource blocks, cluster 2
			- Start_Rb_2: int: numeric Position of first RB, cluster 2
			- Modulation: enums.Modulation: QPSK | Q16 | Q64 | Q256 Modulation type QPSK | 16-QAM | 64-QAM | 256-QAM
			- Trans_Block_Size_Idx: int: numeric Transport block size index"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number_Rb_1'),
			ArgStruct.scalar_int('Start_Rb_1'),
			ArgStruct.scalar_int('Number_Rb_2'),
			ArgStruct.scalar_int('Start_Rb_2'),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_int('Trans_Block_Size_Idx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb_1: int = None
			self.Start_Rb_1: int = None
			self.Number_Rb_2: int = None
			self.Start_Rb_2: int = None
			self.Modulation: enums.Modulation = None
			self.Trans_Block_Size_Idx: int = None

	def set(self, structure: UplinkStruct, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:UDCHannels:MCLuster:UL \n
		Snippet with structure: \n
		structure = driver.configure.connection.scc.udChannels.mcluster.uplink.UplinkStruct() \n
		structure.Number_Rb_1: int = 1 \n
		structure.Start_Rb_1: int = 1 \n
		structure.Number_Rb_2: int = 1 \n
		structure.Start_Rb_2: int = 1 \n
		structure.Modulation: enums.Modulation = enums.Modulation.Q1024 \n
		structure.Trans_Block_Size_Idx: int = 1 \n
		driver.configure.connection.scc.udChannels.mcluster.uplink.set(structure, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures a user-defined uplink channel with multi-cluster allocation. The allowed input ranges have dependencies and
		are described in the background information, see 'User-defined channels'. \n
			:param structure: for set value, see the help for UplinkStruct structure arguments.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDCHannels:MCLuster:UL', structure)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> UplinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:UDCHannels:MCLuster:UL \n
		Snippet: value: UplinkStruct = driver.configure.connection.scc.udChannels.mcluster.uplink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures a user-defined uplink channel with multi-cluster allocation. The allowed input ranges have dependencies and
		are described in the background information, see 'User-defined channels'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for UplinkStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDCHannels:MCLuster:UL?', self.__class__.UplinkStruct())
