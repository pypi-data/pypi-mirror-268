from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CCls:
	"""C commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("c", core, parent)

	def set(self, tsm_lim_yrel_lev_c: float, bandwidthF=repcap.BandwidthF.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:EHTofdm:BW<bandwidth>:Y:C \n
		Snippet: driver.configure.multiEval.limit.tsMask.ehtOfdm.bw.y.c.set(tsm_lim_yrel_lev_c = 1.0, bandwidthF = repcap.BandwidthF.Default) \n
		No command help available \n
			:param tsm_lim_yrel_lev_c: No help available
			:param bandwidthF: optional repeated capability selector. Default value: Bw20 (settable in the interface 'Bw')
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_c)
		bandwidthF_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthF, repcap.BandwidthF)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:EHTofdm:BW{bandwidthF_cmd_val}:Y:C {param}')

	def get(self, bandwidthF=repcap.BandwidthF.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:EHTofdm:BW<bandwidth>:Y:C \n
		Snippet: value: float = driver.configure.multiEval.limit.tsMask.ehtOfdm.bw.y.c.get(bandwidthF = repcap.BandwidthF.Default) \n
		No command help available \n
			:param bandwidthF: optional repeated capability selector. Default value: Bw20 (settable in the interface 'Bw')
			:return: tsm_lim_yrel_lev_c: No help available"""
		bandwidthF_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthF, repcap.BandwidthF)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:EHTofdm:BW{bandwidthF_cmd_val}:Y:C?')
		return Conversions.str_to_float(response)
