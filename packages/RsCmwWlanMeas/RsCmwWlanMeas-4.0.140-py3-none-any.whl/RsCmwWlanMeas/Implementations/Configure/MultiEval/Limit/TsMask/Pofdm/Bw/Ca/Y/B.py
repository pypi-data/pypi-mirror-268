from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BCls:
	"""B commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("b", core, parent)

	def set(self, tsm_lim_yrel_lev_b: float, bandwidthB=repcap.BandwidthB.Bw5) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW<bandwidth>:CA:Y:B \n
		Snippet: driver.configure.multiEval.limit.tsMask.pofdm.bw.ca.y.b.set(tsm_lim_yrel_lev_b = 1.0, bandwidthB = repcap.BandwidthB.Bw5) \n
		Defines the Y-value of point B (Δf = 1.5 <bandwidth>) on the 802.11p spectrum mask for power class A and the specified
		<bandwidth>. For background information, see 'Transmit spectrum mask OFDM, by regulation'. \n
			:param tsm_lim_yrel_lev_b: numeric Range: -90 dB to 10 dB
			:param bandwidthB: optional repeated capability selector. Default value: Bw5
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_b)
		bandwidthB_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthB, repcap.BandwidthB)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW{bandwidthB_cmd_val}:CA:Y:B {param}')

	def get(self, bandwidthB=repcap.BandwidthB.Bw5) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW<bandwidth>:CA:Y:B \n
		Snippet: value: float = driver.configure.multiEval.limit.tsMask.pofdm.bw.ca.y.b.get(bandwidthB = repcap.BandwidthB.Bw5) \n
		Defines the Y-value of point B (Δf = 1.5 <bandwidth>) on the 802.11p spectrum mask for power class A and the specified
		<bandwidth>. For background information, see 'Transmit spectrum mask OFDM, by regulation'. \n
			:param bandwidthB: optional repeated capability selector. Default value: Bw5
			:return: tsm_lim_yrel_lev_b: numeric Range: -90 dB to 10 dB"""
		bandwidthB_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthB, repcap.BandwidthB)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW{bandwidthB_cmd_val}:CA:Y:B?')
		return Conversions.str_to_float(response)
