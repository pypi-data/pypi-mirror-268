from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddressCls:
	"""IpAddress commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipAddress", core, parent)

	def set(self, index: enums.IpAddress) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:MMONitor:IPADdress \n
		Snippet: driver.configure.mmonitor.ipAddress.set(index = enums.IpAddress.IP1) \n
		Selects the IP address to which signaling messages are sent for message monitoring. The address pool is configured
		globally via CONFigure:BASE:MMONitor:IPADdress<n>. A query returns both the current index and the resulting IP address. \n
			:param index: IP1 | IP2 | IP3 Address pool index
		"""
		param = Conversions.enum_scalar_to_str(index, enums.IpAddress)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:MMONitor:IPADdress {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Index: enums.IpAddress: IP1 | IP2 | IP3 Address pool index
			- Ip_Address: str: string Used IP address"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Index', enums.IpAddress),
			ArgStruct.scalar_str('Ip_Address')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Index: enums.IpAddress = None
			self.Ip_Address: str = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:MMONitor:IPADdress \n
		Snippet: value: GetStruct = driver.configure.mmonitor.ipAddress.get() \n
		Selects the IP address to which signaling messages are sent for message monitoring. The address pool is configured
		globally via CONFigure:BASE:MMONitor:IPADdress<n>. A query returns both the current index and the resulting IP address. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:MMONitor:IPADdress?', self.__class__.GetStruct())
