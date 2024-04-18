from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Enable: bool: OFF | ON Enables or disables the entry
			- Band: enums.OperatingBandC: OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB250 | OB252 | OB255
			- Channel: int: integer Downlink channel number Range: depends on operating band
			- Cell_Id: int: integer Physical layer cell ID Range: 0 to 503
			- Qoffset: enums.Qoffset: N24 | N22 | N20 | N18 | N16 | N14 | N12 | N10 | N8 | N6 | N5 | N4 | N3 | N2 | N1 | ZERO | P1 | P2 | P3 | P4 | P5 | P6 | P8 | P10 | P12 | P14 | P16 | P18 | P20 | P22 | P24 Corresponds to value 'q-OffsetCell' in 3GPP TS 36.331 N24 to N1: -24 dB to -1 dB ZERO: 0 dB P1 to P24: 1 dB to 24 dB
			- Measurement: bool: Optional setting parameter. OFF | ON Disables / enables neighbor cell measurements for the entry ON is only allowed if also Enable = ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Band', enums.OperatingBandC),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_int('Cell_Id'),
			ArgStruct.scalar_enum('Qoffset', enums.Qoffset),
			ArgStruct.scalar_bool_optional('Measurement')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Band: enums.OperatingBandC = None
			self.Channel: int = None
			self.Cell_Id: int = None
			self.Qoffset: enums.Qoffset = None
			self.Measurement: bool = None

	def set(self, structure: CellStruct, cellNo=repcap.CellNo.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:LTE:CELL<n> \n
		Snippet with structure: \n
		structure = driver.configure.ncell.lte.cell.CellStruct() \n
		structure.Enable: bool = False \n
		structure.Band: enums.OperatingBandC = enums.OperatingBandC.OB1 \n
		structure.Channel: int = 1 \n
		structure.Cell_Id: int = 1 \n
		structure.Qoffset: enums.Qoffset = enums.Qoffset.N1 \n
		structure.Measurement: bool = False \n
		driver.configure.ncell.lte.cell.set(structure, cellNo = repcap.CellNo.Default) \n
		Configures the entry number <n> of the neighbor cell list for LTE. For channel number ranges depending on operating bands
		see 'Operating bands'. Note that only 5 entries with different channel numbers can be active at a time. Entries with the
		same channel number must have different cell IDs. \n
			:param structure: for set value, see the help for CellStruct structure arguments.
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
		"""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:LTE:CELL{cellNo_cmd_val}', structure)

	def get(self, cellNo=repcap.CellNo.Default) -> CellStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:LTE:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.lte.cell.get(cellNo = repcap.CellNo.Default) \n
		Configures the entry number <n> of the neighbor cell list for LTE. For channel number ranges depending on operating bands
		see 'Operating bands'. Note that only 5 entries with different channel numbers can be active at a time. Entries with the
		same channel number must have different cell IDs. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:LTE:CELL{cellNo_cmd_val}?', self.__class__.CellStruct())
