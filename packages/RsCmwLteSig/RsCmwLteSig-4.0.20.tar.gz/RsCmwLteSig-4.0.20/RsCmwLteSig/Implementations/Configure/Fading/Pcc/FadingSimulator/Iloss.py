from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IlossCls:
	"""Iloss commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iloss", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.InsertLossMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:ILOSs:MODE \n
		Snippet: value: enums.InsertLossMode = driver.configure.fading.pcc.fadingSimulator.iloss.get_mode() \n
		Sets the insertion loss mode. \n
			:return: insert_loss_mode: NORMal | USER NORMal: The insertion loss is determined by the fading profile. USER: The insertion loss is configurable.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:ILOSs:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.InsertLossMode)

	def set_mode(self, insert_loss_mode: enums.InsertLossMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:ILOSs:MODE \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.iloss.set_mode(insert_loss_mode = enums.InsertLossMode.LACP) \n
		Sets the insertion loss mode. \n
			:param insert_loss_mode: NORMal | USER NORMal: The insertion loss is determined by the fading profile. USER: The insertion loss is configurable.
		"""
		param = Conversions.enum_scalar_to_str(insert_loss_mode, enums.InsertLossMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:ILOSs:MODE {param}')

	def get_loss(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:ILOSs:LOSS \n
		Snippet: value: float = driver.configure.fading.pcc.fadingSimulator.iloss.get_loss() \n
		Sets the insertion loss for the fading simulator. A setting is only allowed in USER mode (see CONFigure:...
		:FSIMulator:ILOSs:MODE) . \n
			:return: insertion_loss: numeric Range: 0 dB to 30 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:ILOSs:LOSS?')
		return Conversions.str_to_float(response)

	def set_loss(self, insertion_loss: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:ILOSs:LOSS \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.iloss.set_loss(insertion_loss = 1.0) \n
		Sets the insertion loss for the fading simulator. A setting is only allowed in USER mode (see CONFigure:...
		:FSIMulator:ILOSs:MODE) . \n
			:param insertion_loss: numeric Range: 0 dB to 30 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(insertion_loss)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:ILOSs:LOSS {param}')
