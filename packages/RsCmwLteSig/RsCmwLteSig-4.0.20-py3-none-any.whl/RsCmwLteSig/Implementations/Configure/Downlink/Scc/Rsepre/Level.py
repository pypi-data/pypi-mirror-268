from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:RSEPre:LEVel \n
		Snippet: driver.configure.downlink.scc.rsepre.level.set(level = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the energy per resource element (EPRE) of the cell-specific reference signal (C-RS) . The power levels of
		resource elements used for other channels/signals are defined relative to this power level. The allowed value range
		depends basically on the used connector, the number of allocated resource blocks (specified via the cell bandwidth) and
		the external attenuation in the output path. levelRS EPRE, min = levelconnector, min - 10*log10(12*NRB) - ext attout
		levelRS EPRE, max = levelconnector, max - 10*log10(12*NRB) - ext attout - 15 dB With levelconnector, min = -130 dBm (-120
		dBm) , levelconnector, max = -5 dBm (8 dBm) for [RF COM] ([RF OUT]) . Notice also the ranges quoted in the data sheet.
		The range is also affected by active AWGN ('Downlink Power Levels' parameter) , internal fading (insertion loss value) ,
		CSI-RS power, number of MIMO transmit antennas. \n
			:param level: numeric Range: see above , Unit: dBm/15kHz
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(level)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:RSEPre:LEVel {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:RSEPre:LEVel \n
		Snippet: value: float = driver.configure.downlink.scc.rsepre.level.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the energy per resource element (EPRE) of the cell-specific reference signal (C-RS) . The power levels of
		resource elements used for other channels/signals are defined relative to this power level. The allowed value range
		depends basically on the used connector, the number of allocated resource blocks (specified via the cell bandwidth) and
		the external attenuation in the output path. levelRS EPRE, min = levelconnector, min - 10*log10(12*NRB) - ext attout
		levelRS EPRE, max = levelconnector, max - 10*log10(12*NRB) - ext attout - 15 dB With levelconnector, min = -130 dBm (-120
		dBm) , levelconnector, max = -5 dBm (8 dBm) for [RF COM] ([RF OUT]) . Notice also the ranges quoted in the data sheet.
		The range is also affected by active AWGN ('Downlink Power Levels' parameter) , internal fading (insertion loss value) ,
		CSI-RS power, number of MIMO transmit antennas. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: level: numeric Range: see above , Unit: dBm/15kHz"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:RSEPre:LEVel?')
		return Conversions.str_to_float(response)
