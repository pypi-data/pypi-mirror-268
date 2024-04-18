from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MessageCls:
	"""Message commands group definition. 19 total commands, 5 Subgroups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("message", core, parent)

	@property
	def serial(self):
		"""serial commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_serial'):
			from .Serial import SerialCls
			self._serial = SerialCls(self._core, self._cmd_group)
		return self._serial

	@property
	def dcScheme(self):
		"""dcScheme commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dcScheme'):
			from .DcScheme import DcSchemeCls
			self._dcScheme = DcSchemeCls(self._core, self._cmd_group)
		return self._dcScheme

	@property
	def language(self):
		"""language commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_language'):
			from .Language import LanguageCls
			self._language = LanguageCls(self._core, self._cmd_group)
		return self._language

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_file'):
			from .File import FileCls
			self._file = FileCls(self._core, self._cmd_group)
		return self._file

	@property
	def etws(self):
		"""etws commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_etws'):
			from .Etws import EtwsCls
			self._etws = EtwsCls(self._core, self._cmd_group)
		return self._etws

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:ENABle \n
		Snippet: value: bool = driver.configure.cbs.message.get_enable() \n
		Enables the transmission of cell broadcast messages. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:ENABle \n
		Snippet: driver.configure.cbs.message.set_enable(enable = False) \n
		Enables the transmission of cell broadcast messages. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:ENABle {param}')

	def get_id(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:ID \n
		Snippet: value: int = driver.configure.cbs.message.get_id() \n
		Specifies the message ID as decimal value. The related message type is set automatically. \n
			:return: idn: numeric Range: 0 to 65535
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:ID?')
		return Conversions.str_to_int(response)

	def set_id(self, idn: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:ID \n
		Snippet: driver.configure.cbs.message.set_id(idn = 1) \n
		Specifies the message ID as decimal value. The related message type is set automatically. \n
			:param idn: numeric Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(idn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:ID {param}')

	# noinspection PyTypeChecker
	def get_id_type(self) -> enums.MessageType:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:IDTYpe \n
		Snippet: value: enums.MessageType = driver.configure.cbs.message.get_id_type() \n
		Selects the message type. The related message ID is set automatically. For user-defined CMAS/ETWS, specify the message ID
		via method RsCmwLteSig.Configure.Cbs.Message.id. \n
			:return: type_py: APResidentia | AEXTreme | ASEVere | AAMBer | EARThquake | TSUNami | ETWarning | ETWTest | UDCMas | UDETws | GFENcing APResidentia: presidential alert AEXTreme: extreme alert ASEVere: severe alert AAMBer: amber alert EARThquake: earthquake TSUNami: tsunami ETWarning: earthquake + tsunami ETWTest: ETWS test UDCMas: user-defined CMAS UDETws: user-defined ETWS GFENcing: geo fencing
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:IDTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.MessageType)

	def set_id_type(self, type_py: enums.MessageType) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:IDTYpe \n
		Snippet: driver.configure.cbs.message.set_id_type(type_py = enums.MessageType.AAMBer) \n
		Selects the message type. The related message ID is set automatically. For user-defined CMAS/ETWS, specify the message ID
		via method RsCmwLteSig.Configure.Cbs.Message.id. \n
			:param type_py: APResidentia | AEXTreme | ASEVere | AAMBer | EARThquake | TSUNami | ETWarning | ETWTest | UDCMas | UDETws | GFENcing APResidentia: presidential alert AEXTreme: extreme alert ASEVere: severe alert AAMBer: amber alert EARThquake: earthquake TSUNami: tsunami ETWarning: earthquake + tsunami ETWTest: ETWS test UDCMas: user-defined CMAS UDETws: user-defined ETWS GFENcing: geo fencing
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.MessageType)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:IDTYpe {param}')

	def get_cgroup(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:CGRoup \n
		Snippet: value: int = driver.configure.cbs.message.get_cgroup() \n
		Queries the coding group of the message, for the data sources INTernal and FILE. \n
			:return: coding_group: 0 | 1 0: coding group bits 0000, used for internal data source 1: coding group bits 0001, used for file data source
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:CGRoup?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_category(self) -> enums.Priority:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:CATegory \n
		Snippet: value: enums.Priority = driver.configure.cbs.message.get_category() \n
		No command help available \n
			:return: category: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:CATegory?')
		return Conversions.str_to_scalar_enum(response, enums.Priority)

	def set_category(self, category: enums.Priority) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:CATegory \n
		Snippet: driver.configure.cbs.message.set_category(category = enums.Priority.BACKground) \n
		No command help available \n
			:param category: No help available
		"""
		param = Conversions.enum_scalar_to_str(category, enums.Priority)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:CATegory {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.MessageHandling:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:SOURce \n
		Snippet: value: enums.MessageHandling = driver.configure.cbs.message.get_source() \n
		Selects the source of the message text. \n
			:return: message_handling: INTernal | FILE | UCODed INTernal The message text is defined via method RsCmwLteSig.Configure.Cbs.Message.data. FILE The message text is read from a file, selected via method RsCmwLteSig.Configure.Cbs.Message.File.value. UCODed The message contents are defined via method RsCmwLteSig.Configure.Cbs.Message.ucoded
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.MessageHandling)

	def set_source(self, message_handling: enums.MessageHandling) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:SOURce \n
		Snippet: driver.configure.cbs.message.set_source(message_handling = enums.MessageHandling.FILE) \n
		Selects the source of the message text. \n
			:param message_handling: INTernal | FILE | UCODed INTernal The message text is defined via method RsCmwLteSig.Configure.Cbs.Message.data. FILE The message text is read from a file, selected via method RsCmwLteSig.Configure.Cbs.Message.File.value. UCODed The message contents are defined via method RsCmwLteSig.Configure.Cbs.Message.ucoded
		"""
		param = Conversions.enum_scalar_to_str(message_handling, enums.MessageHandling)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:SOURce {param}')

	def get_data(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:DATA \n
		Snippet: value: str = driver.configure.cbs.message.get_data() \n
		Defines the message text for the data source INTernal. \n
			:return: data: string Up to 1395 characters
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:DATA?')
		return trim_str_response(response)

	def set_data(self, data: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:DATA \n
		Snippet: driver.configure.cbs.message.set_data(data = 'abc') \n
		Defines the message text for the data source INTernal. \n
			:param data: string Up to 1395 characters
		"""
		param = Conversions.value_to_quoted_str(data)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:DATA {param}')

	def get_ucoded(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:UCODed \n
		Snippet: value: float = driver.configure.cbs.message.get_ucoded() \n
		Defines the message contents for the data source UCODed. \n
			:return: user_coded: numeric 0 to 56 binary octets, as hexadecimal or binary number Only complete octets are allowed (binary n*8 bits or hexadecimal n*2 digits) .
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:UCODed?')
		return Conversions.str_to_float(response)

	def set_ucoded(self, user_coded: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:UCODed \n
		Snippet: driver.configure.cbs.message.set_ucoded(user_coded = 1.0) \n
		Defines the message contents for the data source UCODed. \n
			:param user_coded: numeric 0 to 56 binary octets, as hexadecimal or binary number Only complete octets are allowed (binary n*8 bits or hexadecimal n*2 digits) .
		"""
		param = Conversions.decimal_value_to_str(user_coded)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:UCODed {param}')

	def get_wa_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:WAENable \n
		Snippet: value: bool = driver.configure.cbs.message.get_wa_enable() \n
		Enables or disables the transmission of the warning area coordinates to the UE. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WAENable?')
		return Conversions.str_to_bool(response)

	def set_wa_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:WAENable \n
		Snippet: driver.configure.cbs.message.set_wa_enable(enable = False) \n
		Enables or disables the transmission of the warning area coordinates to the UE. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WAENable {param}')

	def get_wa_coordinate(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WACoordinate \n
		Snippet: value: float = driver.configure.cbs.message.get_wa_coordinate() \n
		Defines the contents of the warning area coordinates field. \n
			:return: wa_coordinates: numeric 0 to 56 binary octets, as hexadecimal or binary number Only complete octets are allowed (binary n*8 bits or hexadecimal n*2 digits) .
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WACoordinate?')
		return Conversions.str_to_float(response)

	def set_wa_coordinate(self, wa_coordinates: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WACoordinate \n
		Snippet: driver.configure.cbs.message.set_wa_coordinate(wa_coordinates = 1.0) \n
		Defines the contents of the warning area coordinates field. \n
			:param wa_coordinates: numeric 0 to 56 binary octets, as hexadecimal or binary number Only complete octets are allowed (binary n*8 bits or hexadecimal n*2 digits) .
		"""
		param = Conversions.decimal_value_to_str(wa_coordinates)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WACoordinate {param}')

	def get_period(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:PERiod \n
		Snippet: value: float = driver.configure.cbs.message.get_period() \n
		No command help available \n
			:return: interval: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:PERiod?')
		return Conversions.str_to_float(response)

	def set_period(self, interval: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:PERiod \n
		Snippet: driver.configure.cbs.message.set_period(interval = 1.0) \n
		No command help available \n
			:param interval: No help available
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:PERiod {param}')

	def clone(self) -> 'MessageCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MessageCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
