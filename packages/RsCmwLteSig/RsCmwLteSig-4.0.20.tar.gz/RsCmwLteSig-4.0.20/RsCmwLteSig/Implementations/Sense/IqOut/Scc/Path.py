from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
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

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Sample_Rate: enums.IqOutSampleRate: No parameter help available
			- Pep: float: No parameter help available
			- Crest_Factor: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Sample_Rate', enums.IqOutSampleRate),
			ArgStruct.scalar_float('Pep'),
			ArgStruct.scalar_float('Crest_Factor')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sample_Rate: enums.IqOutSampleRate = None
			self.Pep: float = None
			self.Crest_Factor: float = None

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, path=repcap.Path.Default) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:IQOut:SCC<Carrier>:PATH<n> \n
		Snippet: value: GetStruct = driver.sense.iqOut.scc.path.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, path = repcap.Path.Default) \n
		No command help available \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param path: optional repeated capability selector. Default value: Path1 (settable in the interface 'Path')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:IQOut:SCC{secondaryCompCarrier_cmd_val}:PATH{path_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'PathCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PathCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
