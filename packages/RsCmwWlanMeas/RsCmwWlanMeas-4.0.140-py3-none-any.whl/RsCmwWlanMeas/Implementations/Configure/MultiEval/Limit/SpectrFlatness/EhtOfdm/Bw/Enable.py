from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, bandwidthF=repcap.BandwidthF.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:EHTofdm:BW<bandwidth>:ENABle \n
		Snippet: driver.configure.multiEval.limit.spectrFlatness.ehtOfdm.bw.enable.set(enable = False, bandwidthF = repcap.BandwidthF.Default) \n
		No command help available \n
			:param enable: No help available
			:param bandwidthF: optional repeated capability selector. Default value: Bw20 (settable in the interface 'Bw')
		"""
		param = Conversions.bool_to_str(enable)
		bandwidthF_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthF, repcap.BandwidthF)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:EHTofdm:BW{bandwidthF_cmd_val}:ENABle {param}')

	def get(self, bandwidthF=repcap.BandwidthF.Default) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:EHTofdm:BW<bandwidth>:ENABle \n
		Snippet: value: bool = driver.configure.multiEval.limit.spectrFlatness.ehtOfdm.bw.enable.get(bandwidthF = repcap.BandwidthF.Default) \n
		No command help available \n
			:param bandwidthF: optional repeated capability selector. Default value: Bw20 (settable in the interface 'Bw')
			:return: enable: No help available"""
		bandwidthF_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthF, repcap.BandwidthF)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:EHTofdm:BW{bandwidthF_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
