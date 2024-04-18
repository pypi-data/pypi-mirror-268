from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcpCls:
	"""Pdcp commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcp", core, parent)

	# noinspection PyTypeChecker
	class SrprofilesStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Rohc_Rtp: bool: OFF | ON Support of profile 0x0001, ROHC RTP
			- Rohc_Udp: bool: OFF | ON Support of profile 0x0002, ROHC UDP
			- Rohc_Esp: bool: OFF | ON Support of profile 0x0003, ROHC ESP
			- Rohc_Ip: bool: OFF | ON Support of profile 0x0004, ROHC IP
			- Rohc_Tcp: bool: OFF | ON Support of profile 0x0006, ROHC TCP
			- Rohc_V_2_Rtp: bool: OFF | ON Support of profile 0x0101, ROHCv2 RTP
			- Rohc_V_2_Udp: bool: OFF | ON Support of profile 0x0102, ROHCv2 UDP
			- Rohc_V_2_Esp: bool: OFF | ON Support of profile 0x0103, ROHCv2 ESP
			- Rohc_V_2_Ip: bool: OFF | ON Support of profile 0x0104, ROHCv2 IP"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Rohc_Rtp'),
			ArgStruct.scalar_bool('Rohc_Udp'),
			ArgStruct.scalar_bool('Rohc_Esp'),
			ArgStruct.scalar_bool('Rohc_Ip'),
			ArgStruct.scalar_bool('Rohc_Tcp'),
			ArgStruct.scalar_bool('Rohc_V_2_Rtp'),
			ArgStruct.scalar_bool('Rohc_V_2_Udp'),
			ArgStruct.scalar_bool('Rohc_V_2_Esp'),
			ArgStruct.scalar_bool('Rohc_V_2_Ip')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rohc_Rtp: bool = None
			self.Rohc_Udp: bool = None
			self.Rohc_Esp: bool = None
			self.Rohc_Ip: bool = None
			self.Rohc_Tcp: bool = None
			self.Rohc_V_2_Rtp: bool = None
			self.Rohc_V_2_Udp: bool = None
			self.Rohc_V_2_Esp: bool = None
			self.Rohc_V_2_Ip: bool = None

	def get_srprofiles(self) -> SrprofilesStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PDCP:SRPRofiles \n
		Snippet: value: SrprofilesStruct = driver.sense.ueCapability.pdcp.get_srprofiles() \n
		Returns UE capability information indicating the support of the individual robust header compression (ROHC) profiles. \n
			:return: structure: for return value, see the help for SrprofilesStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:LTE:SIGNaling<Instance>:UECapability:PDCP:SRPRofiles?', self.__class__.SrprofilesStruct())

	# noinspection PyTypeChecker
	def get_mrc_sessions(self) -> enums.MaxNuRohcConSes:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PDCP:MRCSessions \n
		Snippet: value: enums.MaxNuRohcConSes = driver.sense.ueCapability.pdcp.get_mrc_sessions() \n
		Returns the maximum number of ROHC context sessions supported by the UE. \n
			:return: max_nu_rohc_con_ses: CS2 | CS4 | CS8 | CS12 | CS16 | CS24 | CS32 | CS48 | CS64 | CS128 | CS256 | CS512 | CS1024 | CS16384
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PDCP:MRCSessions?')
		return Conversions.str_to_scalar_enum(response, enums.MaxNuRohcConSes)

	def get_sn_extension(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PDCP:SNEXtension \n
		Snippet: value: bool = driver.sense.ueCapability.pdcp.get_sn_extension() \n
		Returns whether the UE supports PDCP SN extension. \n
			:return: extension: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PDCP:SNEXtension?')
		return Conversions.str_to_bool(response)

	def get_srccontinue(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:PDCP:SRCContinue \n
		Snippet: value: bool = driver.sense.ueCapability.pdcp.get_srccontinue() \n
		Returns whether the UE supports ROHC context continuation during handover. \n
			:return: support_rcc: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:PDCP:SRCContinue?')
		return Conversions.str_to_bool(response)
