from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UpperCls:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, upper: float, bandwidthB=repcap.BandwidthB.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW<bandwidth>:UPPer \n
		Snippet: driver.configure.multiEval.limit.spectrFlatness.pofdm.bw.upper.set(upper = 1.0, bandwidthB = repcap.BandwidthB.Default) \n
		Defines an upper limit for the spectrum flatness of 802.11p OFDM signals with the specified <bandwidth>. The upper limit
		must be larger than the lower limits. \n
			:param upper: numeric Range: -4 dB to 20 dB
			:param bandwidthB: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = Conversions.decimal_value_to_str(upper)
		bandwidthB_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthB, repcap.BandwidthB)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW{bandwidthB_cmd_val}:UPPer {param}')

	def get(self, bandwidthB=repcap.BandwidthB.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW<bandwidth>:UPPer \n
		Snippet: value: float = driver.configure.multiEval.limit.spectrFlatness.pofdm.bw.upper.get(bandwidthB = repcap.BandwidthB.Default) \n
		Defines an upper limit for the spectrum flatness of 802.11p OFDM signals with the specified <bandwidth>. The upper limit
		must be larger than the lower limits. \n
			:param bandwidthB: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: upper: numeric Range: -4 dB to 20 dB"""
		bandwidthB_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthB, repcap.BandwidthB)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW{bandwidthB_cmd_val}:UPPer?')
		return Conversions.str_to_float(response)
