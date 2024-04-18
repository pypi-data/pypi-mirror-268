from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsrqCls:
	"""Rsrq commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsrq", core, parent)

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Lower: float: float Range: -34 dB to 2.5 dB, Unit: dB
			- Upper: float: float Range: -34 dB to 2.5 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower: float = None
			self.Upper: float = None

	def get_range(self) -> RangeStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport[:PCC]:RSRQ:RANGe \n
		Snippet: value: RangeStruct = driver.sense.ueReport.pcc.rsrq.get_range() \n
		Returns the RSRQ value range, corresponding to the RSRQ index reported by the UE. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:LTE:SIGNaling<Instance>:UEReport:PCC:RSRQ:RANGe?', self.__class__.RangeStruct())

	def get_value(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport[:PCC]:RSRQ \n
		Snippet: value: int = driver.sense.ueReport.pcc.rsrq.get_value() \n
		Returns the RSRQ reported by the UE as dimensionless index. \n
			:return: rsrq: decimal Range: -30 to 46
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UEReport:PCC:RSRQ?')
		return Conversions.str_to_int(response)
