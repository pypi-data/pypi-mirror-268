from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SingleCls:
	"""Single commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("single", core, parent)

	def set(self, no_of_steps: int, step_direction: enums.UpDownDirection) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:SINGle \n
		Snippet: driver.configure.uplink.setc.pusch.tpc.single.set(no_of_steps = 1, step_direction = enums.UpDownDirection.DOWN) \n
		Defines a pattern for power control of the PUSCH with the TPC setup SINGle. The pattern consists of 1 to 35 up (+1 dB) or
		down (-1 dB) commands, followed by 'constant power' commands (0 dB) . \n
			:param no_of_steps: numeric Range: 1 to 35
			:param step_direction: UP | DOWN
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('no_of_steps', no_of_steps, DataType.Integer), ArgSingle('step_direction', step_direction, DataType.Enum, enums.UpDownDirection))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:SINGle {param}'.rstrip())

	# noinspection PyTypeChecker
	class SingleStruct(StructBase):
		"""Response structure. Fields: \n
			- No_Of_Steps: int: numeric Range: 1 to 35
			- Step_Direction: enums.UpDownDirection: UP | DOWN"""
		__meta_args_list = [
			ArgStruct.scalar_int('No_Of_Steps'),
			ArgStruct.scalar_enum('Step_Direction', enums.UpDownDirection)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.No_Of_Steps: int = None
			self.Step_Direction: enums.UpDownDirection = None

	def get(self) -> SingleStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:SINGle \n
		Snippet: value: SingleStruct = driver.configure.uplink.setc.pusch.tpc.single.get() \n
		Defines a pattern for power control of the PUSCH with the TPC setup SINGle. The pattern consists of 1 to 35 up (+1 dB) or
		down (-1 dB) commands, followed by 'constant power' commands (0 dB) . \n
			:return: structure: for return value, see the help for SingleStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:SINGle?', self.__class__.SingleStruct())
