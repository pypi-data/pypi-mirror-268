from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FcoefficientCls:
	"""Fcoefficient commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fcoefficient", core, parent)

	# noinspection PyTypeChecker
	def get_rsrp(self) -> enums.FilterRsrpqCoefficient:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:FCOefficient:RSRP \n
		Snippet: value: enums.FilterRsrpqCoefficient = driver.configure.ueReport.fcoefficient.get_rsrp() \n
		Selects the value to be sent to the UE as 'filterCoefficientRSRP'. It is used by the UE to measure the reference signal
		received power (RSRP) . \n
			:return: filter_py: FC0 | FC4
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UEReport:FCOefficient:RSRP?')
		return Conversions.str_to_scalar_enum(response, enums.FilterRsrpqCoefficient)

	def set_rsrp(self, filter_py: enums.FilterRsrpqCoefficient) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:FCOefficient:RSRP \n
		Snippet: driver.configure.ueReport.fcoefficient.set_rsrp(filter_py = enums.FilterRsrpqCoefficient.FC0) \n
		Selects the value to be sent to the UE as 'filterCoefficientRSRP'. It is used by the UE to measure the reference signal
		received power (RSRP) . \n
			:param filter_py: FC0 | FC4
		"""
		param = Conversions.enum_scalar_to_str(filter_py, enums.FilterRsrpqCoefficient)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:FCOefficient:RSRP {param}')

	# noinspection PyTypeChecker
	def get_rsrq(self) -> enums.FilterRsrpqCoefficient:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:FCOefficient:RSRQ \n
		Snippet: value: enums.FilterRsrpqCoefficient = driver.configure.ueReport.fcoefficient.get_rsrq() \n
		Selects the value to be sent to the UE as 'filterCoefficientRSRQ'. It is used by the UE to measure the reference signal
		received quality (RSRQ) . \n
			:return: filter_py: FC0 | FC4
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UEReport:FCOefficient:RSRQ?')
		return Conversions.str_to_scalar_enum(response, enums.FilterRsrpqCoefficient)

	def set_rsrq(self, filter_py: enums.FilterRsrpqCoefficient) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:FCOefficient:RSRQ \n
		Snippet: driver.configure.ueReport.fcoefficient.set_rsrq(filter_py = enums.FilterRsrpqCoefficient.FC0) \n
		Selects the value to be sent to the UE as 'filterCoefficientRSRQ'. It is used by the UE to measure the reference signal
		received quality (RSRQ) . \n
			:param filter_py: FC0 | FC4
		"""
		param = Conversions.enum_scalar_to_str(filter_py, enums.FilterRsrpqCoefficient)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:FCOefficient:RSRQ {param}')
