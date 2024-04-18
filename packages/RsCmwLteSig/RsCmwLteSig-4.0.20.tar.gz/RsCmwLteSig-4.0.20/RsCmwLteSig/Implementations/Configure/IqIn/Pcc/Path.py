from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PathCls:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Path, default value after init: Path.Path1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_path_get', 'repcap_path_set', repcap.Path.Path1)

	def repcap_path_set(self, path: repcap.Path) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Path.Default
		Default value after init: Path.Path1"""
		self._cmd_group.set_repcap_enum_value(path)

	def repcap_path_get(self) -> repcap.Path:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, pep: float, level: float, path=repcap.Path.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:IQIN[:PCC]:PATH<n> \n
		Snippet: driver.configure.iqIn.pcc.path.set(pep = 1.0, level = 1.0, path = repcap.Path.Default) \n
		No command help available \n
			:param pep: No help available
			:param level: No help available
			:param path: optional repeated capability selector. Default value: Path1 (settable in the interface 'Path')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('pep', pep, DataType.Float), ArgSingle('level', level, DataType.Float))
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:IQIN:PCC:PATH{path_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class PathStruct(StructBase):
		"""Response structure. Fields: \n
			- Pep: float: No parameter help available
			- Level: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Pep'),
			ArgStruct.scalar_float('Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pep: float = None
			self.Level: float = None

	def get(self, path=repcap.Path.Default) -> PathStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:IQIN[:PCC]:PATH<n> \n
		Snippet: value: PathStruct = driver.configure.iqIn.pcc.path.get(path = repcap.Path.Default) \n
		No command help available \n
			:param path: optional repeated capability selector. Default value: Path1 (settable in the interface 'Path')
			:return: structure: for return value, see the help for PathStruct structure arguments."""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:IQIN:PCC:PATH{path_cmd_val}?', self.__class__.PathStruct())

	def clone(self) -> 'PathCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PathCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
