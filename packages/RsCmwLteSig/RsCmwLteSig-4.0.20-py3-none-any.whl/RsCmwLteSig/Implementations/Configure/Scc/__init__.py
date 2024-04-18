from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SccCls:
	"""Scc commands group definition. 6 total commands, 5 Subgroups, 1 group commands
	Repeated Capability: SecondaryCompCarrier, default value after init: SecondaryCompCarrier.CC1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_secondaryCompCarrier_get', 'repcap_secondaryCompCarrier_set', repcap.SecondaryCompCarrier.CC1)

	def repcap_secondaryCompCarrier_set(self, secondaryCompCarrier: repcap.SecondaryCompCarrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondaryCompCarrier.Default
		Default value after init: SecondaryCompCarrier.CC1"""
		self._cmd_group.set_repcap_enum_value(secondaryCompCarrier)

	def repcap_secondaryCompCarrier_get(self) -> repcap.SecondaryCompCarrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def uul(self):
		"""uul commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uul'):
			from .Uul import UulCls
			self._uul = UulCls(self._core, self._cmd_group)
		return self._uul

	@property
	def dmode(self):
		"""dmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmode'):
			from .Dmode import DmodeCls
			self._dmode = DmodeCls(self._core, self._cmd_group)
		return self._dmode

	@property
	def band(self):
		"""band commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_band'):
			from .Band import BandCls
			self._band = BandCls(self._core, self._cmd_group)
		return self._band

	@property
	def fstructure(self):
		"""fstructure commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fstructure'):
			from .Fstructure import FstructureCls
			self._fstructure = FstructureCls(self._core, self._cmd_group)
		return self._fstructure

	@property
	def caggregation(self):
		"""caggregation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_caggregation'):
			from .Caggregation import CaggregationCls
			self._caggregation = CaggregationCls(self._core, self._cmd_group)
		return self._caggregation

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.AutoManualModeExt:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC:AMODe \n
		Snippet: value: enums.AutoManualModeExt = driver.configure.scc.get_amode() \n
		Selects the SCC activation mode. For manual triggering of a state transition, see method RsCmwLteSig.Call.Scc.Action.set. \n
			:return: mode: AUTO | MANual | SEMiauto AUTO All SCCs are activated automatically at RRC connection establishment, so that the state 'MAC Activated' is reached. MANual Each state transition step must be initiated separately for each SCC. So several actions are required to reach the state 'MAC Activated'. SEMiauto The activation must be initiated manually for each SCC. As a result, all state transitions required to reach the state 'MAC Activated' are performed.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SCC:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualModeExt)

	def set_amode(self, mode: enums.AutoManualModeExt) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC:AMODe \n
		Snippet: driver.configure.scc.set_amode(mode = enums.AutoManualModeExt.AUTO) \n
		Selects the SCC activation mode. For manual triggering of a state transition, see method RsCmwLteSig.Call.Scc.Action.set. \n
			:param mode: AUTO | MANual | SEMiauto AUTO All SCCs are activated automatically at RRC connection establishment, so that the state 'MAC Activated' is reached. MANual Each state transition step must be initiated separately for each SCC. So several actions are required to reach the state 'MAC Activated'. SEMiauto The activation must be initiated manually for each SCC. As a result, all state transitions required to reach the state 'MAC Activated' are performed.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualModeExt)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SCC:AMODe {param}')

	def clone(self) -> 'SccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
