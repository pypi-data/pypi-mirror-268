from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ACls:
	"""A commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("a", core, parent)

	def set(self, tsm_lim_yrel_lev_a: float, bandwidthB=repcap.BandwidthB.Bw5) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW<bandwidth>:UDEFined:Y:A \n
		Snippet: driver.configure.multiEval.limit.tsMask.pofdm.bw.userDefined.y.a.set(tsm_lim_yrel_lev_a = 1.0, bandwidthB = repcap.BandwidthB.Bw5) \n
		Defines the Y-value of point A (Δf = 2 <bandwidth>) on the 802.11p spectrum mask for power class 'user defined' and the
		specified <bandwidth>. For background information, see 'Transmit spectrum mask OFDM, by regulation'. \n
			:param tsm_lim_yrel_lev_a: numeric Range: -90 dB to 10 dB
			:param bandwidthB: optional repeated capability selector. Default value: Bw5
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_a)
		bandwidthB_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthB, repcap.BandwidthB)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW{bandwidthB_cmd_val}:UDEFined:Y:A {param}')

	def get(self, bandwidthB=repcap.BandwidthB.Bw5) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW<bandwidth>:UDEFined:Y:A \n
		Snippet: value: float = driver.configure.multiEval.limit.tsMask.pofdm.bw.userDefined.y.a.get(bandwidthB = repcap.BandwidthB.Bw5) \n
		Defines the Y-value of point A (Δf = 2 <bandwidth>) on the 802.11p spectrum mask for power class 'user defined' and the
		specified <bandwidth>. For background information, see 'Transmit spectrum mask OFDM, by regulation'. \n
			:param bandwidthB: optional repeated capability selector. Default value: Bw5
			:return: tsm_lim_yrel_lev_a: numeric Range: -90 dB to 10 dB"""
		bandwidthB_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthB, repcap.BandwidthB)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW{bandwidthB_cmd_val}:UDEFined:Y:A?')
		return Conversions.str_to_float(response)
