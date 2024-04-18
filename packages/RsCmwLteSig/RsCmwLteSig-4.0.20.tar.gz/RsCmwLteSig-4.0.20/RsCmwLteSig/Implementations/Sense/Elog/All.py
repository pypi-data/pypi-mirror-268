from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Timestamp: List[str]: string Timestamp of the entry
			- Category: List[enums.LogCategory]: INFO | WARNing | ERRor | CONTinue Category of the entry, as indicated in the main view by an icon
			- Event: List[str]: string Describes the event, e.g. 'RRC Connection Established'"""
		__meta_args_list = [
			ArgStruct('Timestamp', DataType.StringList, None, False, True, 1),
			ArgStruct('Category', DataType.EnumList, enums.LogCategory, False, True, 1),
			ArgStruct('Event', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Timestamp: List[str] = None
			self.Category: List[enums.LogCategory] = None
			self.Event: List[str] = None

	def get(self, hres: enums.TimeResolution = None) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:ELOG:ALL \n
		Snippet: value: GetStruct = driver.sense.elog.all.get(hres = enums.TimeResolution.HRES) \n
		Queries all entries of the event log. For each entry, three parameters are returned, from oldest to latest entry:
		{<Timestamp>, <Category>, <Event>}entry 1, {<Timestamp>, <Category>, <Event>}entry 2, ... \n
			:param hres: HRES If you omit this parameter, the timestamp resolution is 1 s (format 'hh:mm:ss') . If you send the value HRES, the timestamp resolution is 1 ms (format 'hh:mm:ss.sss') .
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('hres', hres, DataType.Enum, enums.TimeResolution, is_optional=True))
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:ELOG:ALL? {param}'.rstrip(), self.__class__.GetStruct())
