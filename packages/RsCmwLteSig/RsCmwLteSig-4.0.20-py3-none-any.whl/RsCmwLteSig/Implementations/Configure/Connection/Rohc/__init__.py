from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RohcCls:
	"""Rohc commands group definition. 5 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rohc", core, parent)

	@property
	def ulOnly(self):
		"""ulOnly commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ulOnly'):
			from .UlOnly import UlOnlyCls
			self._ulOnly = UlOnlyCls(self._core, self._cmd_group)
		return self._ulOnly

	@property
	def profiles(self):
		"""profiles commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_profiles'):
			from .Profiles import ProfilesCls
			self._profiles = ProfilesCls(self._core, self._cmd_group)
		return self._profiles

	# noinspection PyTypeChecker
	def get_efor(self) -> enums.HeaderCompression:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:EFOR \n
		Snippet: value: enums.HeaderCompression = driver.configure.connection.rohc.get_efor() \n
		Selects for which types of dedicated bearers header compression is enabled. \n
			:return: for_py: VVB | ADB VVB: voice and video bearers ADB: all dedicated bearers
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:EFOR?')
		return Conversions.str_to_scalar_enum(response, enums.HeaderCompression)

	def set_efor(self, for_py: enums.HeaderCompression) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:EFOR \n
		Snippet: driver.configure.connection.rohc.set_efor(for_py = enums.HeaderCompression.ADB) \n
		Selects for which types of dedicated bearers header compression is enabled. \n
			:param for_py: VVB | ADB VVB: voice and video bearers ADB: all dedicated bearers
		"""
		param = Conversions.enum_scalar_to_str(for_py, enums.HeaderCompression)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:EFOR {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:ENABle \n
		Snippet: value: bool = driver.configure.connection.rohc.get_enable() \n
		Enables or disables bidirectional header compression. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:ENABle \n
		Snippet: driver.configure.connection.rohc.set_enable(enable = False) \n
		Enables or disables bidirectional header compression. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:ENABle {param}')

	def clone(self) -> 'RohcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RohcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
