from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvdoCls:
	"""Evdo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evdo", core, parent)

	def set(self, band_class: enums.BandClass, dl_channel: int) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:EVDO \n
		Snippet: driver.prepare.handover.external.evdo.set(band_class = enums.BandClass.AWS, dl_channel = 1) \n
		Configures the destination parameters for handover to a CDMA2000 or 1xEV-DO destination at another instrument. \n
			:param band_class: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | U25F | NA9C | PS7C | LO7C USC: BC 0, US cellular KCEL: BC 0, Korean cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS band JTAC: BC 3, JTACS band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, upper 700 MHz B18M: BC 8, 1800-MHz band NA9C: BC 9, North American 900 MHz NA8S: BC 10, secondary 800 MHz PA4M: BC 11, European 400-MHz PAMR PA8M: BC 12, 800-MHz PAMR IEXT: BC 13, IMT-2000 2.5-GHz extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS band U25B: BC 16, US 2.5-GHz band U25F: BC 17, US 2.5 GHz forward PS7C: BC 18, public safety band 700 MHz LO7C: BC 19, lower 700 MHz
			:param dl_channel: decimal Channel number Range: depends on the band class, see table below
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('band_class', band_class, DataType.Enum, enums.BandClass), ArgSingle('dl_channel', dl_channel, DataType.Integer))
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:EVDO {param}'.rstrip())

	# noinspection PyTypeChecker
	class EvdoStruct(StructBase):
		"""Response structure. Fields: \n
			- Band_Class: enums.BandClass: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | U25F | NA9C | PS7C | LO7C USC: BC 0, US cellular KCEL: BC 0, Korean cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS band JTAC: BC 3, JTACS band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, upper 700 MHz B18M: BC 8, 1800-MHz band NA9C: BC 9, North American 900 MHz NA8S: BC 10, secondary 800 MHz PA4M: BC 11, European 400-MHz PAMR PA8M: BC 12, 800-MHz PAMR IEXT: BC 13, IMT-2000 2.5-GHz extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS band U25B: BC 16, US 2.5-GHz band U25F: BC 17, US 2.5 GHz forward PS7C: BC 18, public safety band 700 MHz LO7C: BC 19, lower 700 MHz
			- Dl_Channel: int: decimal Channel number Range: depends on the band class, see table below"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band_Class', enums.BandClass),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band_Class: enums.BandClass = None
			self.Dl_Channel: int = None

	def get(self) -> EvdoStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:EVDO \n
		Snippet: value: EvdoStruct = driver.prepare.handover.external.evdo.get() \n
		Configures the destination parameters for handover to a CDMA2000 or 1xEV-DO destination at another instrument. \n
			:return: structure: for return value, see the help for EvdoStruct structure arguments."""
		return self._core.io.query_struct(f'PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:EVDO?', self.__class__.EvdoStruct())
