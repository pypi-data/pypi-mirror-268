from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	def set(self, enable: bool, band: enums.OperatingBandB, channel: int, scrambling_code: str, measurement: bool = None, cellNo=repcap.CellNo.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:TDSCdma:CELL<n> \n
		Snippet: driver.configure.ncell.tdscdma.cell.set(enable = False, band = enums.OperatingBandB.OB1, channel = 1, scrambling_code = rawAbc, measurement = False, cellNo = repcap.CellNo.Default) \n
		Configures the entry number <n> of the neighbor cell list for TD-SCDMA. \n
			:param enable: OFF | ON Enables or disables the entry
			:param band: OB1 | OB2 | OB3 OB1: Band 1 (F) , channel 9400 to 9600 OB2: Band 2 (A) , channel 10050 to 10125 OB3: Band 3 (E) , channel 11500 to 12000
			:param channel: integer Channel number Range: 9400 to 12000, depending on operating band
			:param scrambling_code: hex Cell parameter ID Range: #H0 to #H7F
			:param measurement: OFF | ON Disables / enables neighbor cell measurements for the entry ON is only allowed if also Enable = ON
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('band', band, DataType.Enum, enums.OperatingBandB), ArgSingle('channel', channel, DataType.Integer), ArgSingle('scrambling_code', scrambling_code, DataType.RawString), ArgSingle('measurement', measurement, DataType.Boolean, None, is_optional=True))
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:TDSCdma:CELL{cellNo_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF | ON Enables or disables the entry
			- Band: enums.OperatingBandB: OB1 | OB2 | OB3 OB1: Band 1 (F) , channel 9400 to 9600 OB2: Band 2 (A) , channel 10050 to 10125 OB3: Band 3 (E) , channel 11500 to 12000
			- Channel: int: integer Channel number Range: 9400 to 12000, depending on operating band
			- Scrambling_Code: str: hex Cell parameter ID Range: #H0 to #H7F
			- Measurement: bool: OFF | ON Disables / enables neighbor cell measurements for the entry ON is only allowed if also Enable = ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Band', enums.OperatingBandB),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_raw_str('Scrambling_Code'),
			ArgStruct.scalar_bool('Measurement')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Band: enums.OperatingBandB = None
			self.Channel: int = None
			self.Scrambling_Code: str = None
			self.Measurement: bool = None

	def get(self, cellNo=repcap.CellNo.Default) -> CellStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:TDSCdma:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.tdscdma.cell.get(cellNo = repcap.CellNo.Default) \n
		Configures the entry number <n> of the neighbor cell list for TD-SCDMA. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:TDSCdma:CELL{cellNo_cmd_val}?', self.__class__.CellStruct())
