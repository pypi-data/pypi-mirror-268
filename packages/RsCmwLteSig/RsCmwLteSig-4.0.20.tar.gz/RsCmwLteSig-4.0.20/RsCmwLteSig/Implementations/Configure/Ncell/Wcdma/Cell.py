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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:WCDMa:CELL<n> \n
		Snippet: driver.configure.ncell.wcdma.cell.set(enable = False, band = enums.OperatingBandB.OB1, channel = 1, scrambling_code = rawAbc, measurement = False, cellNo = repcap.CellNo.Default) \n
		Configures the entry number <n> of the neighbor cell list for WCDMA. \n
			:param enable: OFF | ON Enables or disables the entry
			:param band: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB19 | OB20 | OB21 | OB22 | OB25 | OBS1 | OBS2 | OBS3 | OBL1 | OB26 OB1, ..., OB14: band I to XIV OB19, ..., OB22: band XIX to XXII OB25, OB26: band XXV, XXVI OBS1: band S OBS2: band S 170 MHz OBS3: band S 190 MHz OBL1: band L
			:param channel: integer Downlink channel number Range: 412 to 11000, depending on operating band, see table below
			:param scrambling_code: hex Primary scrambling code Range: #H0 to #H1FF
			:param measurement: OFF | ON Disables / enables neighbor cell measurements for the entry ON is only allowed if also Enable = ON
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('band', band, DataType.Enum, enums.OperatingBandB), ArgSingle('channel', channel, DataType.Integer), ArgSingle('scrambling_code', scrambling_code, DataType.RawString), ArgSingle('measurement', measurement, DataType.Boolean, None, is_optional=True))
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:WCDMa:CELL{cellNo_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF | ON Enables or disables the entry
			- Band: enums.OperatingBandB: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB19 | OB20 | OB21 | OB22 | OB25 | OBS1 | OBS2 | OBS3 | OBL1 | OB26 OB1, ..., OB14: band I to XIV OB19, ..., OB22: band XIX to XXII OB25, OB26: band XXV, XXVI OBS1: band S OBS2: band S 170 MHz OBS3: band S 190 MHz OBL1: band L
			- Channel: int: integer Downlink channel number Range: 412 to 11000, depending on operating band, see table below
			- Scrambling_Code: str: hex Primary scrambling code Range: #H0 to #H1FF
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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:WCDMa:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.wcdma.cell.get(cellNo = repcap.CellNo.Default) \n
		Configures the entry number <n> of the neighbor cell list for WCDMA. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:WCDMa:CELL{cellNo_cmd_val}?', self.__class__.CellStruct())
