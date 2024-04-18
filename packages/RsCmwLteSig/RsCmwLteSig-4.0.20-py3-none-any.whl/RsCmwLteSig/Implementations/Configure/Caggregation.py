from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaggregationCls:
	"""Caggregation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caggregation", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Set_Apos_1: enums.SetPosition: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Primary carrier of set A
			- Set_Apos_2: enums.SetPosition: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Second carrier of set A
			- Set_Apos_3: enums.SetPosition: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Third carrier of set A
			- Set_Apos_4: enums.SetPosition: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Fourth carrier of set A
			- Set_Bpos_1: enums.SetPosition: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Primary carrier of set B
			- Set_Bpos_2: enums.SetPosition: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Second carrier of set B
			- Set_Bpos_3: enums.SetPosition: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Third carrier of set B
			- Set_Bpos_4: enums.SetPosition: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Fourth carrier of set B
			- Set_Cpos_1: enums.SetPosition: Optional setting parameter. INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Primary carrier of set C
			- Set_Cpos_2: enums.SetPosition: Optional setting parameter. INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Second carrier of set C
			- Set_Cpos_3: enums.SetPosition: Optional setting parameter. INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Third carrier of set C
			- Set_Cpos_4: enums.SetPosition: Optional setting parameter. INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Fourth carrier of set C"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Set_Apos_1', enums.SetPosition),
			ArgStruct.scalar_enum('Set_Apos_2', enums.SetPosition),
			ArgStruct.scalar_enum('Set_Apos_3', enums.SetPosition),
			ArgStruct.scalar_enum('Set_Apos_4', enums.SetPosition),
			ArgStruct.scalar_enum('Set_Bpos_1', enums.SetPosition),
			ArgStruct.scalar_enum('Set_Bpos_2', enums.SetPosition),
			ArgStruct.scalar_enum('Set_Bpos_3', enums.SetPosition),
			ArgStruct.scalar_enum('Set_Bpos_4', enums.SetPosition),
			ArgStruct.scalar_enum_optional('Set_Cpos_1', enums.SetPosition),
			ArgStruct.scalar_enum_optional('Set_Cpos_2', enums.SetPosition),
			ArgStruct.scalar_enum_optional('Set_Cpos_3', enums.SetPosition),
			ArgStruct.scalar_enum_optional('Set_Cpos_4', enums.SetPosition)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Set_Apos_1: enums.SetPosition = None
			self.Set_Apos_2: enums.SetPosition = None
			self.Set_Apos_3: enums.SetPosition = None
			self.Set_Apos_4: enums.SetPosition = None
			self.Set_Bpos_1: enums.SetPosition = None
			self.Set_Bpos_2: enums.SetPosition = None
			self.Set_Bpos_3: enums.SetPosition = None
			self.Set_Bpos_4: enums.SetPosition = None
			self.Set_Cpos_1: enums.SetPosition = None
			self.Set_Cpos_2: enums.SetPosition = None
			self.Set_Cpos_3: enums.SetPosition = None
			self.Set_Cpos_4: enums.SetPosition = None

	def get_set(self) -> SetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CAGGregation:SET \n
		Snippet: value: SetStruct = driver.configure.caggregation.get_set() \n
		Configures the alignment of uplink component carriers for intraband contiguous uplink carrier aggregation. The command
		configures set A, set B and set C. It aligns all component carriers of a set for contiguous UL CA.
			INTRO_CMD_HELP: Rules for valid parameter combinations: \n
			- Enable the uplink of a component carrier before adding it to a set.
			- Use set C only for scenarios with at least 6 carriers. Use set B only for scenarios with at least 4 carriers.
			- To disable a set, select INV for all four parameters of the set. If you omit the <SetC...> settings, set C is disabled (all four set to INV) .
			- To use a set, select the primary carrier for <...pos1> and a second carrier for <...pos2>. To align only two carriers, set <...pos3> and <...pos4> to INV. To align three carriers, select <...pos3> and set <...pos4> to INV. To align four carriers, select <...pos3> and <...pos4>.
			- All carriers of a set must fit into the band of the primary carrier, without changing the frequency of the primary carrier. \n
			:return: structure: for return value, see the help for SetStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CAGGregation:SET?', self.__class__.SetStruct())

	def set_set(self, value: SetStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CAGGregation:SET \n
		Snippet with structure: \n
		structure = driver.configure.caggregation.SetStruct() \n
		structure.Set_Apos_1: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Apos_2: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Apos_3: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Apos_4: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Bpos_1: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Bpos_2: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Bpos_3: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Bpos_4: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Cpos_1: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Cpos_2: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Cpos_3: enums.SetPosition = enums.SetPosition.INV \n
		structure.Set_Cpos_4: enums.SetPosition = enums.SetPosition.INV \n
		driver.configure.caggregation.set_set(value = structure) \n
		Configures the alignment of uplink component carriers for intraband contiguous uplink carrier aggregation. The command
		configures set A, set B and set C. It aligns all component carriers of a set for contiguous UL CA.
			INTRO_CMD_HELP: Rules for valid parameter combinations: \n
			- Enable the uplink of a component carrier before adding it to a set.
			- Use set C only for scenarios with at least 6 carriers. Use set B only for scenarios with at least 4 carriers.
			- To disable a set, select INV for all four parameters of the set. If you omit the <SetC...> settings, set C is disabled (all four set to INV) .
			- To use a set, select the primary carrier for <...pos1> and a second carrier for <...pos2>. To align only two carriers, set <...pos3> and <...pos4> to INV. To align three carriers, select <...pos3> and set <...pos4> to INV. To align four carriers, select <...pos3> and <...pos4>.
			- All carriers of a set must fit into the band of the primary carrier, without changing the frequency of the primary carrier. \n
			:param value: see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CAGGregation:SET', value)
