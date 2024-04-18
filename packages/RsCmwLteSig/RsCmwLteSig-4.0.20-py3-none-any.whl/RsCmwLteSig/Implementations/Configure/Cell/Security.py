from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SecurityCls:
	"""Security commands group definition. 9 total commands, 0 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("security", core, parent)

	def get_authenticate(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:AUTHenticat \n
		Snippet: value: bool = driver.configure.cell.security.get_authenticate() \n
		Enables or disables authentication, to be performed during the attach procedure. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:AUTHenticat?')
		return Conversions.str_to_bool(response)

	def set_authenticate(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:AUTHenticat \n
		Snippet: driver.configure.cell.security.set_authenticate(enable = False) \n
		Enables or disables authentication, to be performed during the attach procedure. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:AUTHenticat {param}')

	def get_nas(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:NAS \n
		Snippet: value: bool = driver.configure.cell.security.get_nas() \n
		Enables or disables the NAS security mode. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:NAS?')
		return Conversions.str_to_bool(response)

	def set_nas(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:NAS \n
		Snippet: driver.configure.cell.security.set_nas(enable = False) \n
		Enables or disables the NAS security mode. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:NAS {param}')

	def get_as_py(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:AS \n
		Snippet: value: bool = driver.configure.cell.security.get_as_py() \n
		Enables or disables the AS security mode. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:AS?')
		return Conversions.str_to_bool(response)

	def set_as_py(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:AS \n
		Snippet: driver.configure.cell.security.set_as_py(enable = False) \n
		Enables or disables the AS security mode. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:AS {param}')

	# noinspection PyTypeChecker
	def get_ialgorithm(self) -> enums.SecurityAlgorithm:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:IALGorithm \n
		Snippet: value: enums.SecurityAlgorithm = driver.configure.cell.security.get_ialgorithm() \n
		Selects an algorithm for integrity protection. \n
			:return: algorithm: NULL | S3G NULL: no integrity protection S3G: SNOW3G (EIA1) algorithm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:IALGorithm?')
		return Conversions.str_to_scalar_enum(response, enums.SecurityAlgorithm)

	def set_ialgorithm(self, algorithm: enums.SecurityAlgorithm) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:IALGorithm \n
		Snippet: driver.configure.cell.security.set_ialgorithm(algorithm = enums.SecurityAlgorithm.NULL) \n
		Selects an algorithm for integrity protection. \n
			:param algorithm: NULL | S3G NULL: no integrity protection S3G: SNOW3G (EIA1) algorithm
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.SecurityAlgorithm)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:IALGorithm {param}')

	# noinspection PyTypeChecker
	def get_nc_algorithm(self) -> enums.SecurityAlgorithm:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:NCALgorithm \n
		Snippet: value: enums.SecurityAlgorithm = driver.configure.cell.security.get_nc_algorithm() \n
		Selects an algorithm for ciphering of NAS signaling. \n
			:return: algorithm: NULL | S3G NULL: no ciphering S3G: SNOW3G (EIA1) algorithm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:NCALgorithm?')
		return Conversions.str_to_scalar_enum(response, enums.SecurityAlgorithm)

	def set_nc_algorithm(self, algorithm: enums.SecurityAlgorithm) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:NCALgorithm \n
		Snippet: driver.configure.cell.security.set_nc_algorithm(algorithm = enums.SecurityAlgorithm.NULL) \n
		Selects an algorithm for ciphering of NAS signaling. \n
			:param algorithm: NULL | S3G NULL: no ciphering S3G: SNOW3G (EIA1) algorithm
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.SecurityAlgorithm)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:NCALgorithm {param}')

	def get_milenage(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:MILenage \n
		Snippet: value: bool = driver.configure.cell.security.get_milenage() \n
		Enables or disables using the MILENAGE algorithm set instead of the standard algorithms. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:MILenage?')
		return Conversions.str_to_bool(response)

	def set_milenage(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:MILenage \n
		Snippet: driver.configure.cell.security.set_milenage(enable = False) \n
		Enables or disables using the MILENAGE algorithm set instead of the standard algorithms. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:MILenage {param}')

	def get_skey(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:SKEY \n
		Snippet: value: str = driver.configure.cell.security.get_skey() \n
		Defines the secret key K as 32-digit hexadecimal number. You can omit leading zeros. K is used for the authentication
		procedure including a possible integrity check. \n
			:return: secret_key: hex Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:SKEY?')
		return trim_str_response(response)

	def set_skey(self, secret_key: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:SKEY \n
		Snippet: driver.configure.cell.security.set_skey(secret_key = rawAbc) \n
		Defines the secret key K as 32-digit hexadecimal number. You can omit leading zeros. K is used for the authentication
		procedure including a possible integrity check. \n
			:param secret_key: hex Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		param = Conversions.value_to_str(secret_key)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:SKEY {param}')

	def get_opc(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:OPC \n
		Snippet: value: str = driver.configure.cell.security.get_opc() \n
		Specifies the key OPc as 32-digit hexadecimal number. \n
			:return: opc: hex Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:OPC?')
		return trim_str_response(response)

	def set_opc(self, opc: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:OPC \n
		Snippet: driver.configure.cell.security.set_opc(opc = rawAbc) \n
		Specifies the key OPc as 32-digit hexadecimal number. \n
			:param opc: hex Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		param = Conversions.value_to_str(opc)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:OPC {param}')

	# noinspection PyTypeChecker
	def get_rvalue(self) -> enums.RandomValueMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:RVALue \n
		Snippet: value: enums.RandomValueMode = driver.configure.cell.security.get_rvalue() \n
		Selects whether an even or odd RAND value is used. \n
			:return: mode: EVEN | ODD
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:RVALue?')
		return Conversions.str_to_scalar_enum(response, enums.RandomValueMode)

	def set_rvalue(self, mode: enums.RandomValueMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SECurity:RVALue \n
		Snippet: driver.configure.cell.security.set_rvalue(mode = enums.RandomValueMode.EVEN) \n
		Selects whether an even or odd RAND value is used. \n
			:param mode: EVEN | ODD
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.RandomValueMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SECurity:RVALue {param}')
