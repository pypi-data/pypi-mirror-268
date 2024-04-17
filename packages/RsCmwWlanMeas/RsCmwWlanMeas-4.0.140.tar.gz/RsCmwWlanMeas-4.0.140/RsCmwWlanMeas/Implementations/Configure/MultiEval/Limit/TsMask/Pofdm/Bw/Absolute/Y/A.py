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

	def set(self, tsm_lim_yabs_lev_a: float, bandwidthA=repcap.BandwidthA.Bw10) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW<bandwidth>:ABSolute:Y:A \n
		Snippet: driver.configure.multiEval.limit.tsMask.pofdm.bw.absolute.y.a.set(tsm_lim_yabs_lev_a = 1.0, bandwidthA = repcap.BandwidthA.Bw10) \n
		Defines the Y-value of point A (Δf = 2 <BW>) on the ETSI ITS absolute emission mask for the specified <bandwidth>.
		For background information, see 'Transmit spectrum mask OFDM, absolute limits'. \n
			:param tsm_lim_yabs_lev_a: numeric Range: -150 dBm to 30 dBm
			:param bandwidthA: optional repeated capability selector. Default value: Bw10
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yabs_lev_a)
		bandwidthA_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthA, repcap.BandwidthA)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW{bandwidthA_cmd_val}:ABSolute:Y:A {param}')

	def get(self, bandwidthA=repcap.BandwidthA.Bw10) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW<bandwidth>:ABSolute:Y:A \n
		Snippet: value: float = driver.configure.multiEval.limit.tsMask.pofdm.bw.absolute.y.a.get(bandwidthA = repcap.BandwidthA.Bw10) \n
		Defines the Y-value of point A (Δf = 2 <BW>) on the ETSI ITS absolute emission mask for the specified <bandwidth>.
		For background information, see 'Transmit spectrum mask OFDM, absolute limits'. \n
			:param bandwidthA: optional repeated capability selector. Default value: Bw10
			:return: tsm_lim_yabs_lev_a: numeric Range: -150 dBm to 30 dBm"""
		bandwidthA_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthA, repcap.BandwidthA)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:POFDm:BW{bandwidthA_cmd_val}:ABSolute:Y:A?')
		return Conversions.str_to_float(response)
