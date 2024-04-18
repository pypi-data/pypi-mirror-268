from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OutgoingCls:
	"""Outgoing commands group definition. 16 total commands, 2 Subgroups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("outgoing", core, parent)

	@property
	def sctStamp(self):
		"""sctStamp commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_sctStamp'):
			from .SctStamp import SctStampCls
			self._sctStamp = SctStampCls(self._core, self._cmd_group)
		return self._sctStamp

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_file'):
			from .File import FileCls
			self._file = FileCls(self._core, self._cmd_group)
		return self._file

	def get_udheader(self) -> float or bool:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:UDHeader \n
		Snippet: value: float or bool = driver.configure.sms.outgoing.get_udheader() \n
		Configures the TP user data header. \n
			:return: header: (float or boolean) hex | ON | OFF Up to 16 hexadecimal digits Range: #H0 to #HFFFFFFFFFFFFFFFF ON | OFF enables or disables sending the header.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:UDHeader?')
		return Conversions.str_to_float_or_bool(response)

	def set_udheader(self, header: float or bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:UDHeader \n
		Snippet: driver.configure.sms.outgoing.set_udheader(header = 1.0) \n
		Configures the TP user data header. \n
			:param header: (float or boolean) hex | ON | OFF Up to 16 hexadecimal digits Range: #H0 to #HFFFFFFFFFFFFFFFF ON | OFF enables or disables sending the header.
		"""
		param = Conversions.decimal_or_bool_value_to_str(header)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:UDHeader {param}')

	# noinspection PyTypeChecker
	def get_mes_handling(self) -> enums.MessageHandlingB:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:MESHandling \n
		Snippet: value: enums.MessageHandlingB = driver.configure.sms.outgoing.get_mes_handling() \n
		Selects whether an outgoing message is defined directly via the GUI/commands or read from a file. For file selection, see
		method RsCmwLteSig.Configure.Sms.Outgoing.File.value. \n
			:return: message_handling: INTernal | FILE INTernal: message defined directly FILE: message specified via a file
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:MESHandling?')
		return Conversions.str_to_scalar_enum(response, enums.MessageHandlingB)

	def set_mes_handling(self, message_handling: enums.MessageHandlingB) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:MESHandling \n
		Snippet: driver.configure.sms.outgoing.set_mes_handling(message_handling = enums.MessageHandlingB.FILE) \n
		Selects whether an outgoing message is defined directly via the GUI/commands or read from a file. For file selection, see
		method RsCmwLteSig.Configure.Sms.Outgoing.File.value. \n
			:param message_handling: INTernal | FILE INTernal: message defined directly FILE: message specified via a file
		"""
		param = Conversions.enum_scalar_to_str(message_handling, enums.MessageHandlingB)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:MESHandling {param}')

	def get_internal(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:INTernal \n
		Snippet: value: str = driver.configure.sms.outgoing.get_internal() \n
		Defines the message text for outgoing 7-bit ASCII messages. \n
			:return: sms_internal: string Message contents, up to 800 characters
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:INTernal?')
		return trim_str_response(response)

	def set_internal(self, sms_internal: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:INTernal \n
		Snippet: driver.configure.sms.outgoing.set_internal(sms_internal = 'abc') \n
		Defines the message text for outgoing 7-bit ASCII messages. \n
			:param sms_internal: string Message contents, up to 800 characters
		"""
		param = Conversions.value_to_quoted_str(sms_internal)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:INTernal {param}')

	def get_binary(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:BINary \n
		Snippet: value: float = driver.configure.sms.outgoing.get_binary() \n
		Defines the message contents for outgoing 8-bit binary messages. \n
			:return: sms_binary: hex Message contents, up to 1400 digits
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:BINary?')
		return Conversions.str_to_float(response)

	def set_binary(self, sms_binary: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:BINary \n
		Snippet: driver.configure.sms.outgoing.set_binary(sms_binary = 1.0) \n
		Defines the message contents for outgoing 8-bit binary messages. \n
			:param sms_binary: hex Message contents, up to 1400 digits
		"""
		param = Conversions.decimal_value_to_str(sms_binary)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:BINary {param}')

	def get_pidentifier(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:PIDentifier \n
		Snippet: value: float = driver.configure.sms.outgoing.get_pidentifier() \n
		Specifies the TP protocol identifier (TP-PID) value to be sent. \n
			:return: idn: numeric Range: #H0 to #HFF
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:PIDentifier?')
		return Conversions.str_to_float(response)

	def set_pidentifier(self, idn: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:PIDentifier \n
		Snippet: driver.configure.sms.outgoing.set_pidentifier(idn = 1.0) \n
		Specifies the TP protocol identifier (TP-PID) value to be sent. \n
			:param idn: numeric Range: #H0 to #HFF
		"""
		param = Conversions.decimal_value_to_str(idn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:PIDentifier {param}')

	# noinspection PyTypeChecker
	def get_dcoding(self) -> enums.SmsDataCoding:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:DCODing \n
		Snippet: value: enums.SmsDataCoding = driver.configure.sms.outgoing.get_dcoding() \n
		Selects the data coding for outgoing messages. \n
			:return: data_coding: BIT7 | BIT8 BIT7: 7-bit encoded ASCII message BIT8: 8-bit encoded binary message
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:DCODing?')
		return Conversions.str_to_scalar_enum(response, enums.SmsDataCoding)

	def set_dcoding(self, data_coding: enums.SmsDataCoding) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:DCODing \n
		Snippet: driver.configure.sms.outgoing.set_dcoding(data_coding = enums.SmsDataCoding.BIT7) \n
		Selects the data coding for outgoing messages. \n
			:param data_coding: BIT7 | BIT8 BIT7: 7-bit encoded ASCII message BIT8: 8-bit encoded binary message
		"""
		param = Conversions.enum_scalar_to_str(data_coding, enums.SmsDataCoding)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:DCODing {param}')

	# noinspection PyTypeChecker
	def get_cgroup(self) -> enums.SmsCodingGroup:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:CGRoup \n
		Snippet: value: enums.SmsCodingGroup = driver.configure.sms.outgoing.get_cgroup() \n
		Selects the coding group to be indicated to the message recipient in the TP-Data-Coding-Scheme field. \n
			:return: coding_group: GDCoding | DCMClass GDCoding: general data coding DCMClass: data coding / message class
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:CGRoup?')
		return Conversions.str_to_scalar_enum(response, enums.SmsCodingGroup)

	def set_cgroup(self, coding_group: enums.SmsCodingGroup) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:CGRoup \n
		Snippet: driver.configure.sms.outgoing.set_cgroup(coding_group = enums.SmsCodingGroup.DCMClass) \n
		Selects the coding group to be indicated to the message recipient in the TP-Data-Coding-Scheme field. \n
			:param coding_group: GDCoding | DCMClass GDCoding: general data coding DCMClass: data coding / message class
		"""
		param = Conversions.enum_scalar_to_str(coding_group, enums.SmsCodingGroup)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:CGRoup {param}')

	# noinspection PyTypeChecker
	def get_mclass(self) -> enums.MessageClass:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:MCLass \n
		Snippet: value: enums.MessageClass = driver.configure.sms.outgoing.get_mclass() \n
		Selects the message class to be indicated to the message recipient in the TP-Data-Coding-Scheme field. \n
			:return: message_class: CL0 | CL1 | CL2 | CL3 | NONE CL0, CL1, CL2, CL3: Class 0 to 3 NONE: Do not send message class
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:MCLass?')
		return Conversions.str_to_scalar_enum(response, enums.MessageClass)

	def set_mclass(self, message_class: enums.MessageClass) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:MCLass \n
		Snippet: driver.configure.sms.outgoing.set_mclass(message_class = enums.MessageClass.CL0) \n
		Selects the message class to be indicated to the message recipient in the TP-Data-Coding-Scheme field. \n
			:param message_class: CL0 | CL1 | CL2 | CL3 | NONE CL0, CL1, CL2, CL3: Class 0 to 3 NONE: Do not send message class
		"""
		param = Conversions.enum_scalar_to_str(message_class, enums.MessageClass)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:MCLass {param}')

	def get_os_address(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:OSADdress \n
		Snippet: value: str = driver.configure.sms.outgoing.get_os_address() \n
		Specifies the originator short message service center address to be sent to the recipient. \n
			:return: orig_smsca_ddress: string
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:OSADdress?')
		return trim_str_response(response)

	def set_os_address(self, orig_smsca_ddress: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:OSADdress \n
		Snippet: driver.configure.sms.outgoing.set_os_address(orig_smsca_ddress = 'abc') \n
		Specifies the originator short message service center address to be sent to the recipient. \n
			:param orig_smsca_ddress: string
		"""
		param = Conversions.value_to_quoted_str(orig_smsca_ddress)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:OSADdress {param}')

	def get_oaddress(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:OADDress \n
		Snippet: value: str = driver.configure.sms.outgoing.get_oaddress() \n
		Specifies the originating address to be sent to the message recipient. \n
			:return: orig_address: string
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:OADDress?')
		return trim_str_response(response)

	def set_oaddress(self, orig_address: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:OADDress \n
		Snippet: driver.configure.sms.outgoing.set_oaddress(orig_address = 'abc') \n
		Specifies the originating address to be sent to the message recipient. \n
			:param orig_address: string
		"""
		param = Conversions.value_to_quoted_str(orig_address)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:OADDress {param}')

	# noinspection PyTypeChecker
	def get_lhandling(self) -> enums.LongSmsHandling:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:LHANdling \n
		Snippet: value: enums.LongSmsHandling = driver.configure.sms.outgoing.get_lhandling() \n
		Selects the handling of messages exceeding 160 characters. \n
			:return: lsms_handling: TRUNcate | MSMS TRUNcate The SMS is truncated to 160 characters, the rest is discarded. MSMS Up to five concatenated messages are sent, consisting in sum of up to 800 characters.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:LHANdling?')
		return Conversions.str_to_scalar_enum(response, enums.LongSmsHandling)

	def set_lhandling(self, lsms_handling: enums.LongSmsHandling) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:OUTGoing:LHANdling \n
		Snippet: driver.configure.sms.outgoing.set_lhandling(lsms_handling = enums.LongSmsHandling.MSMS) \n
		Selects the handling of messages exceeding 160 characters. \n
			:param lsms_handling: TRUNcate | MSMS TRUNcate The SMS is truncated to 160 characters, the rest is discarded. MSMS Up to five concatenated messages are sent, consisting in sum of up to 800 characters.
		"""
		param = Conversions.enum_scalar_to_str(lsms_handling, enums.LongSmsHandling)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:LHANdling {param}')

	def clone(self) -> 'OutgoingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OutgoingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
