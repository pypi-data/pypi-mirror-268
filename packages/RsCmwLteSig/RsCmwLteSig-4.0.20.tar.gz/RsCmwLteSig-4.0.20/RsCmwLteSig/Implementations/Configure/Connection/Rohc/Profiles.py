from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProfilesCls:
	"""Profiles commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("profiles", core, parent)

	def set(self, profile_0_x_0001: bool, profile_0_x_0002: bool, profile_0_x_0004: bool, profile_0_x_0006: bool = None) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:PROFiles \n
		Snippet: driver.configure.connection.rohc.profiles.set(profile_0_x_0001 = False, profile_0_x_0002 = False, profile_0_x_0004 = False, profile_0_x_0006 = False) \n
		Enables header compression profiles for bidirectional header compression. \n
			:param profile_0_x_0001: OFF | ON Profile 1, for IP/UDP/RTP
			:param profile_0_x_0002: OFF | ON Profile 2, for IP/UDP/...
			:param profile_0_x_0004: OFF | ON Profile 4, for IP/...
			:param profile_0_x_0006: OFF | ON Profile 6, for IP/TCP/...
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('profile_0_x_0001', profile_0_x_0001, DataType.Boolean), ArgSingle('profile_0_x_0002', profile_0_x_0002, DataType.Boolean), ArgSingle('profile_0_x_0004', profile_0_x_0004, DataType.Boolean), ArgSingle('profile_0_x_0006', profile_0_x_0006, DataType.Boolean, None, is_optional=True))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:PROFiles {param}'.rstrip())

	# noinspection PyTypeChecker
	class ProfilesStruct(StructBase):
		"""Response structure. Fields: \n
			- Profile_0_X_0001: bool: OFF | ON Profile 1, for IP/UDP/RTP
			- Profile_0_X_0002: bool: OFF | ON Profile 2, for IP/UDP/...
			- Profile_0_X_0004: bool: OFF | ON Profile 4, for IP/...
			- Profile_0_X_0006: bool: OFF | ON Profile 6, for IP/TCP/..."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Profile_0_X_0001'),
			ArgStruct.scalar_bool('Profile_0_X_0002'),
			ArgStruct.scalar_bool('Profile_0_X_0004'),
			ArgStruct.scalar_bool('Profile_0_X_0006')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Profile_0_X_0001: bool = None
			self.Profile_0_X_0002: bool = None
			self.Profile_0_X_0004: bool = None
			self.Profile_0_X_0006: bool = None

	def get(self) -> ProfilesStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:PROFiles \n
		Snippet: value: ProfilesStruct = driver.configure.connection.rohc.profiles.get() \n
		Enables header compression profiles for bidirectional header compression. \n
			:return: structure: for return value, see the help for ProfilesStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:PROFiles?', self.__class__.ProfilesStruct())
