from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DedBearerCls:
	"""DedBearer commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dedBearer", core, parent)

	# noinspection PyTypeChecker
	class SeparateStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Def_Bearer_Id: str: string Bearer ID, selecting the default bearer, to which the dedicated bearer is mapped. Example: '5 (cmw500.rohde-schwarz.com) ' To query a list of IDs for all established default bearers, see [CMDLINKRESOLVED Catalog.Connection#DefBearer CMDLINKRESOLVED].
			- Profile: enums.DedBearerProfile: VOICe | VIDeo | DRAM | DRUM Selects a dedicated bearer profile VOICe: for voice connections VIDeo: for video connections DRAM: for data connections with RLC acknowledged mode DRUM: for data connections with RLC unacknowledged mode Range: DRUM
			- Tft_Port_Low_Dl: int: numeric Selects the lower end of the port range for downlink traffic Range: 1 to 65535
			- Tft_Port_High_Dl: int: numeric Selects the upper end of the port range for downlink traffic Range: 1 to 65535
			- Tft_Port_Low_Ul: int: numeric Selects the lower end of the port range for uplink traffic Range: 1 to 65535
			- Tft_Port_High_Ul: int: numeric Selects the upper end of the port range for uplink traffic Range: 1 to 65535"""
		__meta_args_list = [
			ArgStruct.scalar_str('Def_Bearer_Id'),
			ArgStruct.scalar_enum('Profile', enums.DedBearerProfile),
			ArgStruct.scalar_int('Tft_Port_Low_Dl'),
			ArgStruct.scalar_int('Tft_Port_High_Dl'),
			ArgStruct.scalar_int('Tft_Port_Low_Ul'),
			ArgStruct.scalar_int('Tft_Port_High_Ul')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Def_Bearer_Id: str = None
			self.Profile: enums.DedBearerProfile = None
			self.Tft_Port_Low_Dl: int = None
			self.Tft_Port_High_Dl: int = None
			self.Tft_Port_Low_Ul: int = None
			self.Tft_Port_High_Ul: int = None

	def get_separate(self) -> SeparateStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:CONNection:DEDBearer:SEParate \n
		Snippet: value: SeparateStruct = driver.prepare.connection.dedBearer.get_separate() \n
		Configures dedicated bearer settings as a preparation for a bearer setup via CALL:LTE:SIGN:PSWitched:ACTion CONNect.
		Different port ranges can be set for the uplink and for the downlink. \n
			:return: structure: for return value, see the help for SeparateStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:CONNection:DEDBearer:SEParate?', self.__class__.SeparateStruct())

	def set_separate(self, value: SeparateStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:CONNection:DEDBearer:SEParate \n
		Snippet with structure: \n
		structure = driver.prepare.connection.dedBearer.SeparateStruct() \n
		structure.Def_Bearer_Id: str = 'abc' \n
		structure.Profile: enums.DedBearerProfile = enums.DedBearerProfile.DRAM \n
		structure.Tft_Port_Low_Dl: int = 1 \n
		structure.Tft_Port_High_Dl: int = 1 \n
		structure.Tft_Port_Low_Ul: int = 1 \n
		structure.Tft_Port_High_Ul: int = 1 \n
		driver.prepare.connection.dedBearer.set_separate(value = structure) \n
		Configures dedicated bearer settings as a preparation for a bearer setup via CALL:LTE:SIGN:PSWitched:ACTion CONNect.
		Different port ranges can be set for the uplink and for the downlink. \n
			:param value: see the help for SeparateStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:CONNection:DEDBearer:SEParate', value)

	def set(self, def_bearer_id: str, profile: enums.DedBearerProfile, tft_port_low: int, tft_port_high: int) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:CONNection:DEDBearer \n
		Snippet: driver.prepare.connection.dedBearer.set(def_bearer_id = 'abc', profile = enums.DedBearerProfile.DRAM, tft_port_low = 1, tft_port_high = 1) \n
		Configures dedicated bearer settings as a preparation for a bearer setup via CALL:LTE:SIGN:PSWitched:ACTion CONNect. The
		same port range is used for the uplink and for the downlink. \n
			:param def_bearer_id: string Bearer ID, selecting the default bearer, to which the dedicated bearer is mapped. Example: '5 (cmw500.rohde-schwarz.com) ' To query a list of IDs for all established default bearers, see method RsCmwLteSig.Catalog.Connection.defBearer.
			:param profile: VOICe | VIDeo | DRAM | DRUM Selects a dedicated bearer profile VOICe: for voice connections VIDeo: for video connections DRAM: for data connections with RLC acknowledged mode DRUM: for data connections with RLC unacknowledged mode
			:param tft_port_low: numeric Selects the lower end of the port range, for which traffic is routed to the dedicated bearer Range: 1 to 65535
			:param tft_port_high: numeric Selects the upper end of the port range Range: 1 to 65535
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('def_bearer_id', def_bearer_id, DataType.String), ArgSingle('profile', profile, DataType.Enum, enums.DedBearerProfile), ArgSingle('tft_port_low', tft_port_low, DataType.Integer), ArgSingle('tft_port_high', tft_port_high, DataType.Integer))
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:CONNection:DEDBearer {param}'.rstrip())

	# noinspection PyTypeChecker
	class DedBearerStruct(StructBase):
		"""Response structure. Fields: \n
			- Def_Bearer_Id: str: string Bearer ID, selecting the default bearer, to which the dedicated bearer is mapped. Example: '5 (cmw500.rohde-schwarz.com) ' To query a list of IDs for all established default bearers, see [CMDLINKRESOLVED Catalog.Connection#DefBearer CMDLINKRESOLVED].
			- Profile: enums.DedBearerProfile: VOICe | VIDeo | DRAM | DRUM Selects a dedicated bearer profile VOICe: for voice connections VIDeo: for video connections DRAM: for data connections with RLC acknowledged mode DRUM: for data connections with RLC unacknowledged mode
			- Tft_Port_Low: int: numeric Selects the lower end of the port range, for which traffic is routed to the dedicated bearer Range: 1 to 65535
			- Tft_Port_High: int: numeric Selects the upper end of the port range Range: 1 to 65535"""
		__meta_args_list = [
			ArgStruct.scalar_str('Def_Bearer_Id'),
			ArgStruct.scalar_enum('Profile', enums.DedBearerProfile),
			ArgStruct.scalar_int('Tft_Port_Low'),
			ArgStruct.scalar_int('Tft_Port_High')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Def_Bearer_Id: str = None
			self.Profile: enums.DedBearerProfile = None
			self.Tft_Port_Low: int = None
			self.Tft_Port_High: int = None

	def get(self) -> DedBearerStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:CONNection:DEDBearer \n
		Snippet: value: DedBearerStruct = driver.prepare.connection.dedBearer.get() \n
		Configures dedicated bearer settings as a preparation for a bearer setup via CALL:LTE:SIGN:PSWitched:ACTion CONNect. The
		same port range is used for the uplink and for the downlink. \n
			:return: structure: for return value, see the help for DedBearerStruct structure arguments."""
		return self._core.io.query_struct(f'PREPare:LTE:SIGNaling<Instance>:CONNection:DEDBearer?', self.__class__.DedBearerStruct())
