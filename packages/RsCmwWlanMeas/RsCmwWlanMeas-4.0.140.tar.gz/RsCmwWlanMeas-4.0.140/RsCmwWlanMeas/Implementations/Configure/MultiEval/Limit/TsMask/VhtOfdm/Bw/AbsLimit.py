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

	def set(self, tsm_lim_abs: float, bandwidthE=repcap.BandwidthE.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:VHTofdm:BW<bandwidth>:ABSLimit \n
		Snippet: driver.configure.multiEval.limit.tsMask.vhtOfdm.bw.absLimit.set(tsm_lim_abs = 1.0, bandwidthE = repcap.BandwidthE.Default) \n
		Defines an absolute power limit for 802.11ac signals with the specified <bandwidth>. See 'Transmit spectrum mask OFDM,
		absolute limits' for background information. \n
			:param tsm_lim_abs: numeric Limit value, applies to frequency offsets greater than 3/2*bandwidth, measured at 100 kHz RBW Range: -90 dBm to 10 dBm
			:param bandwidthE: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_abs)
		bandwidthE_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthE, repcap.BandwidthE)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:VHTofdm:BW{bandwidthE_cmd_val}:ABSLimit {param}')

	def get(self, bandwidthE=repcap.BandwidthE.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:VHTofdm:BW<bandwidth>:ABSLimit \n
		Snippet: value: float = driver.configure.multiEval.limit.tsMask.vhtOfdm.bw.absLimit.get(bandwidthE = repcap.BandwidthE.Default) \n
		Defines an absolute power limit for 802.11ac signals with the specified <bandwidth>. See 'Transmit spectrum mask OFDM,
		absolute limits' for background information. \n
			:param bandwidthE: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: tsm_lim_abs: numeric Limit value, applies to frequency offsets greater than 3/2*bandwidth, measured at 100 kHz RBW Range: -90 dBm to 10 dBm"""
		bandwidthE_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthE, repcap.BandwidthE)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:VHTofdm:BW{bandwidthE_cmd_val}:ABSLimit?')
		return Conversions.str_to_float(response)
