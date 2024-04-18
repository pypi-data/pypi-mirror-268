from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScellCls:
	"""Scell commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scell", core, parent)

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Rsrp_Lower: int: decimal RSRP minimum value Range: -140 dBm to -44 dBm, Unit: dBm
			- Rsrp_Upper: int: decimal RSRP maximum value Range: -140 dBm to -44 dBm, Unit: dBm
			- Rsrq_Lower: float: float RSRQ minimum value Range: -34 dB to 2.5 dB, Unit: dB
			- Rsrq_Upper: float: float RSRQ maximum value Range: -34 dB to 2.5 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rsrp_Lower'),
			ArgStruct.scalar_int('Rsrp_Upper'),
			ArgStruct.scalar_float('Rsrq_Lower'),
			ArgStruct.scalar_float('Rsrq_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rsrp_Lower: int = None
			self.Rsrp_Upper: int = None
			self.Rsrq_Lower: float = None
			self.Rsrq_Upper: float = None

	def get_range(self) -> RangeStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport[:PCC]:SCELl:RANGe \n
		Snippet: value: RangeStruct = driver.sense.ueReport.pcc.scell.get_range() \n
		Returns the value ranges corresponding to the dimensionless index values reported for the serving LTE cell. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:LTE:SIGNaling<Instance>:UEReport:PCC:SCELl:RANGe?', self.__class__.RangeStruct())

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Rsrp: int: decimal RSRP as dimensionless index Range: 0 to 97
			- Rsrq: int: decimal RSRQ as dimensionless index Range: -30 to 46"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rsrp'),
			ArgStruct.scalar_int('Rsrq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rsrp: int = None
			self.Rsrq: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport[:PCC]:SCELl \n
		Snippet: value: ValueStruct = driver.sense.ueReport.pcc.scell.get_value() \n
		Returns measurement report values for the serving LTE cell. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:LTE:SIGNaling<Instance>:UEReport:PCC:SCELl?', self.__class__.ValueStruct())
