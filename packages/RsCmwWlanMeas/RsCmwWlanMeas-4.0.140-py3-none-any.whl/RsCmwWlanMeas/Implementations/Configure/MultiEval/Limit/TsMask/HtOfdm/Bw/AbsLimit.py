from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AbsLimitCls:
	"""AbsLimit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absLimit", core, parent)

	def set(self, tsm_lim_abs: float, bandwidthC=repcap.BandwidthC.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW<bandwidth>:ABSLimit \n
		Snippet: driver.configure.multiEval.limit.tsMask.htOfdm.bw.absLimit.set(tsm_lim_abs = 1.0, bandwidthC = repcap.BandwidthC.Default) \n
		Defines an absolute power limit for 802.11n signals with the specified <bandwidth>. See 'Transmit spectrum mask OFDM,
		absolute limits' for background information. \n
			:param tsm_lim_abs: numeric Limit value, applies to frequency offsets greater than 3/2*bandwidth, measured at 100 kHz RBW. Range: -90 dBm to 10 dBm
			:param bandwidthC: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_abs)
		bandwidthC_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthC, repcap.BandwidthC)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW{bandwidthC_cmd_val}:ABSLimit {param}')

	def get(self, bandwidthC=repcap.BandwidthC.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW<bandwidth>:ABSLimit \n
		Snippet: value: float = driver.configure.multiEval.limit.tsMask.htOfdm.bw.absLimit.get(bandwidthC = repcap.BandwidthC.Default) \n
		Defines an absolute power limit for 802.11n signals with the specified <bandwidth>. See 'Transmit spectrum mask OFDM,
		absolute limits' for background information. \n
			:param bandwidthC: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: tsm_lim_abs: numeric Limit value, applies to frequency offsets greater than 3/2*bandwidth, measured at 100 kHz RBW. Range: -90 dBm to 10 dBm"""
		bandwidthC_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthC, repcap.BandwidthC)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW{bandwidthC_cmd_val}:ABSLimit?')
		return Conversions.str_to_float(response)
