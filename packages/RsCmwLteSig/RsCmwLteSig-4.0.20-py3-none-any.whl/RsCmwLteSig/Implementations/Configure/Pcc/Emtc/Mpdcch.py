from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MpdcchCls:
	"""Mpdcch commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mpdcch", core, parent)

	# noinspection PyTypeChecker
	def get_sspace(self) -> enums.SearchSpace:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MPDCch:SSPace \n
		Snippet: value: enums.SearchSpace = driver.configure.pcc.emtc.mpdcch.get_sspace() \n
		Selects where the signaling application puts the MPDCCH. \n
			:return: search_space: COMM | UESP COMM: common search space UESP: UE-specific search space
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MPDCch:SSPace?')
		return Conversions.str_to_scalar_enum(response, enums.SearchSpace)

	def set_sspace(self, search_space: enums.SearchSpace) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MPDCch:SSPace \n
		Snippet: driver.configure.pcc.emtc.mpdcch.set_sspace(search_space = enums.SearchSpace.COMM) \n
		Selects where the signaling application puts the MPDCCH. \n
			:param search_space: COMM | UESP COMM: common search space UESP: UE-specific search space
		"""
		param = Conversions.enum_scalar_to_str(search_space, enums.SearchSpace)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MPDCch:SSPace {param}')

	# noinspection PyTypeChecker
	def get_rlevel(self) -> enums.RepetitionLevel:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MPDCch:RLEVel \n
		Snippet: value: enums.RepetitionLevel = driver.configure.pcc.emtc.mpdcch.get_rlevel() \n
		Configures the repetition level for MPDCCH repetitions. \n
			:return: rep_level: RL1 | RL2 | RL3 | RL4
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MPDCch:RLEVel?')
		return Conversions.str_to_scalar_enum(response, enums.RepetitionLevel)

	def set_rlevel(self, rep_level: enums.RepetitionLevel) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MPDCch:RLEVel \n
		Snippet: driver.configure.pcc.emtc.mpdcch.set_rlevel(rep_level = enums.RepetitionLevel.RL1) \n
		Configures the repetition level for MPDCCH repetitions. \n
			:param rep_level: RL1 | RL2 | RL3 | RL4
		"""
		param = Conversions.enum_scalar_to_str(rep_level, enums.RepetitionLevel)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MPDCch:RLEVel {param}')

	# noinspection PyTypeChecker
	def get_mrepetitions(self) -> enums.MpdcchRepetitions:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MPDCch:MREPetitions \n
		Snippet: value: enums.MpdcchRepetitions = driver.configure.pcc.emtc.mpdcch.get_mrepetitions() \n
		Configures the maximum number of MPDCCH repetitions (no paging) . \n
			:return: max_repetitions: MR1 | MR2 | MR4 | MR8 | MR16 | MR32 | MR64 | MR128 | MR256 1, 2, 4, ..., 128, 256 repetitions
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MPDCch:MREPetitions?')
		return Conversions.str_to_scalar_enum(response, enums.MpdcchRepetitions)

	def set_mrepetitions(self, max_repetitions: enums.MpdcchRepetitions) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MPDCch:MREPetitions \n
		Snippet: driver.configure.pcc.emtc.mpdcch.set_mrepetitions(max_repetitions = enums.MpdcchRepetitions.MR1) \n
		Configures the maximum number of MPDCCH repetitions (no paging) . \n
			:param max_repetitions: MR1 | MR2 | MR4 | MR8 | MR16 | MR32 | MR64 | MR128 | MR256 1, 2, 4, ..., 128, 256 repetitions
		"""
		param = Conversions.enum_scalar_to_str(max_repetitions, enums.MpdcchRepetitions)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MPDCch:MREPetitions {param}')

	# noinspection PyTypeChecker
	def get_mr_paging(self) -> enums.MpdcchRepetitions:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MPDCch:MRPaging \n
		Snippet: value: enums.MpdcchRepetitions = driver.configure.pcc.emtc.mpdcch.get_mr_paging() \n
		Configures the maximum number of MPDCCH repetitions for paging. \n
			:return: max_repetitions: MR1 | MR2 | MR4 | MR8 | MR16 | MR32 | MR64 | MR128 | MR256 1, 2, 4, ..., 128, 256 repetitions
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MPDCch:MRPaging?')
		return Conversions.str_to_scalar_enum(response, enums.MpdcchRepetitions)

	def set_mr_paging(self, max_repetitions: enums.MpdcchRepetitions) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MPDCch:MRPaging \n
		Snippet: driver.configure.pcc.emtc.mpdcch.set_mr_paging(max_repetitions = enums.MpdcchRepetitions.MR1) \n
		Configures the maximum number of MPDCCH repetitions for paging. \n
			:param max_repetitions: MR1 | MR2 | MR4 | MR8 | MR16 | MR32 | MR64 | MR128 | MR256 1, 2, 4, ..., 128, 256 repetitions
		"""
		param = Conversions.enum_scalar_to_str(max_repetitions, enums.MpdcchRepetitions)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MPDCch:MRPaging {param}')
