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

	def set(self, enable: bool, band_class: enums.BandClass, channel: int, cell_id: int, measurement: bool = None, cellNo=repcap.CellNo.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:CDMA:CELL<n> \n
		Snippet: driver.configure.ncell.cdma.cell.set(enable = False, band_class = enums.BandClass.AWS, channel = 1, cell_id = 1, measurement = False, cellNo = repcap.CellNo.Default) \n
		Configures the entry number <n> of the neighbor cell list for CDMA2000 (1xRTT) or 1xEV-DO (HRPD) . \n
			:param enable: OFF | ON Enables or disables the entry
			:param band_class: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | U25F | NA9C | PS7C | LO7C USC: BC 0, US cellular KCEL: BC 0, Korean cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS band JTAC: BC 3, JTACS band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, upper 700 MHz B18M: BC 8, 1800-MHz band NA9C: BC 9, North American 900 MHz NA8S: BC 10, secondary 800 MHz PA4M: BC 11, European 400-MHz PAMR PA8M: BC 12, 800-MHz PAMR IEXT: BC 13, IMT-2000 2.5-GHz extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS band U25B: BC 16, US 2.5-GHz band U25F: BC 17, US 2.5 GHz forward PS7C: BC 18, public safety band 700 MHz LO7C: BC 19, lower 700 MHz
			:param channel: integer Channel number Range: 0 to 2108, depending on band class, see table below
			:param cell_id: integer Physical cell ID Range: 0 to 511
			:param measurement: OFF | ON Disables / enables neighbor cell measurements for the entry ON is only allowed if also Enable = ON
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('band_class', band_class, DataType.Enum, enums.BandClass), ArgSingle('channel', channel, DataType.Integer), ArgSingle('cell_id', cell_id, DataType.Integer), ArgSingle('measurement', measurement, DataType.Boolean, None, is_optional=True))
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:CDMA:CELL{cellNo_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF | ON Enables or disables the entry
			- Band_Class: enums.BandClass: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | U25F | NA9C | PS7C | LO7C USC: BC 0, US cellular KCEL: BC 0, Korean cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS band JTAC: BC 3, JTACS band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, upper 700 MHz B18M: BC 8, 1800-MHz band NA9C: BC 9, North American 900 MHz NA8S: BC 10, secondary 800 MHz PA4M: BC 11, European 400-MHz PAMR PA8M: BC 12, 800-MHz PAMR IEXT: BC 13, IMT-2000 2.5-GHz extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS band U25B: BC 16, US 2.5-GHz band U25F: BC 17, US 2.5 GHz forward PS7C: BC 18, public safety band 700 MHz LO7C: BC 19, lower 700 MHz
			- Channel: int: integer Channel number Range: 0 to 2108, depending on band class, see table below
			- Cell_Id: int: integer Physical cell ID Range: 0 to 511
			- Measurement: bool: OFF | ON Disables / enables neighbor cell measurements for the entry ON is only allowed if also Enable = ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Band_Class', enums.BandClass),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_int('Cell_Id'),
			ArgStruct.scalar_bool('Measurement')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Band_Class: enums.BandClass = None
			self.Channel: int = None
			self.Cell_Id: int = None
			self.Measurement: bool = None

	def get(self, cellNo=repcap.CellNo.Default) -> CellStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:CDMA:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.cdma.cell.get(cellNo = repcap.CellNo.Default) \n
		Configures the entry number <n> of the neighbor cell list for CDMA2000 (1xRTT) or 1xEV-DO (HRPD) . \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:CDMA:CELL{cellNo_cmd_val}?', self.__class__.CellStruct())
