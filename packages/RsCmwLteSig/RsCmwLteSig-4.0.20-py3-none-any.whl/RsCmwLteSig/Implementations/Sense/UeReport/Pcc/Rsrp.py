from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsrpCls:
	"""Rsrp commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsrp", core, parent)

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Lower: int: decimal Range: -140 dBm to -44 dBm, Unit: dBm
			- Upper: int: decimal Range: -140 dBm to -44 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Lower'),
			ArgStruct.scalar_int('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower: int = None
			self.Upper: int = None

	def get_range(self) -> RangeStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport[:PCC]:RSRP:RANGe \n
		Snippet: value: RangeStruct = driver.sense.ueReport.pcc.rsrp.get_range() \n
		Returns the RSRP value range, corresponding to the RSRP index reported by the UE. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:LTE:SIGNaling<Instance>:UEReport:PCC:RSRP:RANGe?', self.__class__.RangeStruct())

	def get_value(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport[:PCC]:RSRP \n
		Snippet: value: int = driver.sense.ueReport.pcc.rsrp.get_value() \n
		Returns the RSRP reported by the UE as dimensionless index. \n
			:return: rsrp: decimal Range: 0 to 97
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UEReport:PCC:RSRP?')
		return Conversions.str_to_int(response)
