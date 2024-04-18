from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PccCls:
	"""Pcc commands group definition. 37 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcc", core, parent)

	@property
	def dmode(self):
		"""dmode commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dmode'):
			from .Dmode import DmodeCls
			self._dmode = DmodeCls(self._core, self._cmd_group)
		return self._dmode

	@property
	def emtc(self):
		"""emtc commands group. 6 Sub-classes, 2 commands."""
		if not hasattr(self, '_emtc'):
			from .Emtc import EmtcCls
			self._emtc = EmtcCls(self._core, self._cmd_group)
		return self._emtc

	# noinspection PyTypeChecker
	def get_band(self) -> enums.OperatingBandC:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:BAND \n
		Snippet: value: enums.OperatingBandC = driver.configure.pcc.get_band() \n
		Selects the operating band (OB) . The allowed input range depends on the duplex mode (FDD or TDD) . \n
			:return: band: FDD: UDEFined | OB1 | ... | OB32 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB252 | OB255 (OB29/32/67/69/75/76/252/255 only for SCC DL) TDD: UDEFined | OB33 | ... | OB46 | OB48 | ... | OB53 | OB250 (OB46/49 only for SCC DL)
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.OperatingBandC)

	def set_band(self, band: enums.OperatingBandC) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:BAND \n
		Snippet: driver.configure.pcc.set_band(band = enums.OperatingBandC.OB1) \n
		Selects the operating band (OB) . The allowed input range depends on the duplex mode (FDD or TDD) . \n
			:param band: FDD: UDEFined | OB1 | ... | OB32 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB252 | OB255 (OB29/32/67/69/75/76/252/255 only for SCC DL) TDD: UDEFined | OB33 | ... | OB46 | OB48 | ... | OB53 | OB250 (OB46/49 only for SCC DL)
		"""
		param = Conversions.enum_scalar_to_str(band, enums.OperatingBandC)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:BAND {param}')

	# noinspection PyTypeChecker
	def get_fstructure(self) -> enums.FrameStructure:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:FSTRucture \n
		Snippet: value: enums.FrameStructure = driver.configure.pcc.get_fstructure() \n
		No command help available \n
			:return: structure: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:FSTRucture?')
		return Conversions.str_to_scalar_enum(response, enums.FrameStructure)

	def set_fstructure(self, structure: enums.FrameStructure) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:FSTRucture \n
		Snippet: driver.configure.pcc.set_fstructure(structure = enums.FrameStructure.T1) \n
		No command help available \n
			:param structure: No help available
		"""
		param = Conversions.enum_scalar_to_str(structure, enums.FrameStructure)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:FSTRucture {param}')

	def clone(self) -> 'PccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
