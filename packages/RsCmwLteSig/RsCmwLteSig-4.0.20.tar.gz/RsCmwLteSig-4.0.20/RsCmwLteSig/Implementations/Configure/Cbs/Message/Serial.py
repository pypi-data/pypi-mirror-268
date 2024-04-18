from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SerialCls:
	"""Serial commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("serial", core, parent)

	def set(self, geo_scope: enums.GeoScope, message_code: int, auto_incr: bool, update_number: int = None) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:SERial \n
		Snippet: driver.configure.cbs.message.serial.set(geo_scope = enums.GeoScope.CIMMediate, message_code = 1, auto_incr = False, update_number = 1) \n
		Specifies the serial number, consisting of the geographical scope, the message code and the update number. \n
			:param geo_scope: CIMMediate | PLMN | LOCation | CNORmal Geographical scope CIMMediate: cell immediate PLMN: PLMN normal LOCation: tracking area normal CNORmal: cell normal
			:param message_code: numeric Range: 0 to 1023
			:param auto_incr: OFF | ON OFF: UpdateNumber is not changed automatically ON: UpdateNumber is increased if message is changed
			:param update_number: numeric Range: 0 to 15
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('geo_scope', geo_scope, DataType.Enum, enums.GeoScope), ArgSingle('message_code', message_code, DataType.Integer), ArgSingle('auto_incr', auto_incr, DataType.Boolean), ArgSingle('update_number', update_number, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:SERial {param}'.rstrip())

	# noinspection PyTypeChecker
	class SerialStruct(StructBase):
		"""Response structure. Fields: \n
			- Geo_Scope: enums.GeoScope: CIMMediate | PLMN | LOCation | CNORmal Geographical scope CIMMediate: cell immediate PLMN: PLMN normal LOCation: tracking area normal CNORmal: cell normal
			- Message_Code: int: numeric Range: 0 to 1023
			- Auto_Incr: bool: OFF | ON OFF: UpdateNumber is not changed automatically ON: UpdateNumber is increased if message is changed
			- Update_Number: int: numeric Range: 0 to 15"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Geo_Scope', enums.GeoScope),
			ArgStruct.scalar_int('Message_Code'),
			ArgStruct.scalar_bool('Auto_Incr'),
			ArgStruct.scalar_int('Update_Number')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Geo_Scope: enums.GeoScope = None
			self.Message_Code: int = None
			self.Auto_Incr: bool = None
			self.Update_Number: int = None

	def get(self) -> SerialStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:SERial \n
		Snippet: value: SerialStruct = driver.configure.cbs.message.serial.get() \n
		Specifies the serial number, consisting of the geographical scope, the message code and the update number. \n
			:return: structure: for return value, see the help for SerialStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:SERial?', self.__class__.SerialStruct())
