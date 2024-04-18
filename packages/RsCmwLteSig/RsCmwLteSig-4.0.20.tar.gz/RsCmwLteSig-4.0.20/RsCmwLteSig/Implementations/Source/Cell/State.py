from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Main_State: enums.MainState: OFF | ON | RFHandover OFF: generator switched off ON: generator switched on RFHandover: ready to receive a handover from another signaling application
			- Sync_State: enums.SignalingGeneratorState: PENDing | ADJusted PENDing: generator turned on (off) but signal not yet (still) available ADJusted: physical output signal corresponds to main generator state"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Main_State', enums.MainState),
			ArgStruct.scalar_enum('Sync_State', enums.SignalingGeneratorState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Main_State: enums.MainState = None
			self.Sync_State: enums.SignalingGeneratorState = None

	def get_all(self) -> AllStruct:
		"""SCPI: SOURce:LTE:SIGNaling<instance>:CELL:STATe:ALL \n
		Snippet: value: AllStruct = driver.source.cell.state.get_all() \n
		Returns detailed information about the signaling generator state. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:LTE:SIGNaling<Instance>:CELL:STATe:ALL?', self.__class__.AllStruct())

	def get_value(self) -> bool:
		"""SCPI: SOURce:LTE:SIGNaling<instance>:CELL:STATe \n
		Snippet: value: bool = driver.source.cell.state.get_value() \n
		Turns the generator (the cell) on or off. \n
			:return: main_state: No help available
		"""
		response = self._core.io.query_str_with_opc('SOURce:LTE:SIGNaling<Instance>:CELL:STATe?')
		return Conversions.str_to_bool(response)

	def set_value(self, main_state: bool) -> None:
		"""SCPI: SOURce:LTE:SIGNaling<instance>:CELL:STATe \n
		Snippet: driver.source.cell.state.set_value(main_state = False) \n
		Turns the generator (the cell) on or off. \n
			:param main_state: No help available
		"""
		param = Conversions.bool_to_str(main_state)
		self._core.io.write_with_opc(f'SOURce:LTE:SIGNaling<Instance>:CELL:STATe {param}')
