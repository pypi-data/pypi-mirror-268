from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, enable: List[bool] = None, bands: List[enums.OperatingBandC] = None) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:AFBands:ALL \n
		Snippet: driver.configure.rfSettings.pcc.afBands.all.set(enable = [True, False, True], bands = [OperatingBandC.OB1, OperatingBandC.UDEFined]) \n
		Configures additional frequency bands supported by the cell ('multiBandInfoList') . There are eight entries.
		You can enable/disable each entry and assign a band to each entry. \n
			:param enable: OFF | ON Enables/disables the entry.
			:param bands: OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB250 | OB252 | OB255
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.BooleanList, None, True, True, 1), ArgSingle('bands', bands, DataType.EnumList, enums.OperatingBandC, True, True, 1))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:AFBands:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: List[bool]: OFF | ON Enables/disables the entry.
			- Bands: List[enums.OperatingBandC]: OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB250 | OB252 | OB255"""
		__meta_args_list = [
			ArgStruct('Enable', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Bands', DataType.EnumList, enums.OperatingBandC, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: List[bool] = None
			self.Bands: List[enums.OperatingBandC] = None

	def get(self) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:AFBands:ALL \n
		Snippet: value: AllStruct = driver.configure.rfSettings.pcc.afBands.all.get() \n
		Configures additional frequency bands supported by the cell ('multiBandInfoList') . There are eight entries.
		You can enable/disable each entry and assign a band to each entry. \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:AFBands:ALL?', self.__class__.AllStruct())
