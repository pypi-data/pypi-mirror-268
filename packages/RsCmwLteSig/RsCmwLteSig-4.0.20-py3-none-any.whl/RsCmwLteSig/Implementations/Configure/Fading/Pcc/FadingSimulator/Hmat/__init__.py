from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HmatCls:
	"""Hmat commands group definition. 5 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hmat", core, parent)

	@property
	def rst(self):
		"""rst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rst'):
			from .Rst import RstCls
			self._rst = RstCls(self._core, self._cmd_group)
		return self._rst

	@property
	def row(self):
		"""row commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_row'):
			from .Row import RowCls
			self._row = RowCls(self._core, self._cmd_group)
		return self._row

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FadingMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:HMAT:MODE \n
		Snippet: value: enums.FadingMode = driver.configure.fading.pcc.fadingSimulator.hmat.get_mode() \n
		No command help available \n
			:return: hdef_matrix_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:HMAT:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadingMode)

	def set_mode(self, hdef_matrix_mode: enums.FadingMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:HMAT:MODE \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.hmat.set_mode(hdef_matrix_mode = enums.FadingMode.NORMal) \n
		No command help available \n
			:param hdef_matrix_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(hdef_matrix_mode, enums.FadingMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:HMAT:MODE {param}')

	def get_value(self) -> List[float]:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:HMAT \n
		Snippet: value: List[float] = driver.configure.fading.pcc.fadingSimulator.hmat.get_value() \n
		No command help available \n
			:return: hdef_matrix_mode: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:HMAT?')
		return response

	def clone(self) -> 'HmatCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HmatCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
