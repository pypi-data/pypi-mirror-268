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

	def set(self, enable: bool, band: enums.GsmBand, channel: int, measurement: bool = None, cellNo=repcap.CellNo.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:GSM:CELL<n> \n
		Snippet: driver.configure.ncell.gsm.cell.set(enable = False, band = enums.GsmBand.G04, channel = 1, measurement = False, cellNo = repcap.CellNo.Default) \n
		Configures the entry number <n> of the neighbor cell list for GSM. \n
			:param enable: OFF | ON Enables or disables the entry
			:param band: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
			:param channel: integer Channel number used for the broadcast control channel (BCCH) Range: 0 to 1023, depending on GSM band, see table below
			:param measurement: OFF | ON Disables / enables neighbor cell measurements for the entry ON is only allowed if also Enable = ON
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('band', band, DataType.Enum, enums.GsmBand), ArgSingle('channel', channel, DataType.Integer), ArgSingle('measurement', measurement, DataType.Boolean, None, is_optional=True))
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:GSM:CELL{cellNo_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF | ON Enables or disables the entry
			- Band: enums.GsmBand: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
			- Channel: int: integer Channel number used for the broadcast control channel (BCCH) Range: 0 to 1023, depending on GSM band, see table below
			- Measurement: bool: OFF | ON Disables / enables neighbor cell measurements for the entry ON is only allowed if also Enable = ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Band', enums.GsmBand),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_bool('Measurement')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Band: enums.GsmBand = None
			self.Channel: int = None
			self.Measurement: bool = None

	def get(self, cellNo=repcap.CellNo.Default) -> CellStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:GSM:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.gsm.cell.get(cellNo = repcap.CellNo.Default) \n
		Configures the entry number <n> of the neighbor cell list for GSM. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:GSM:CELL{cellNo_cmd_val}?', self.__class__.CellStruct())
