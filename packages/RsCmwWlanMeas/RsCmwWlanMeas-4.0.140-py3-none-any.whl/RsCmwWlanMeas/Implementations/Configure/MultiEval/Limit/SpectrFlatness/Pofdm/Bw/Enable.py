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

	def set(self, enable: bool, bandwidthB=repcap.BandwidthB.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW<bandwidth>:ENABle \n
		Snippet: driver.configure.multiEval.limit.spectrFlatness.pofdm.bw.enable.set(enable = False, bandwidthB = repcap.BandwidthB.Default) \n
		Enables or disables the spectrum flatness limit check for 802.11p OFDM signals with the specified <bandwidth>. \n
			:param enable: OFF | ON
			:param bandwidthB: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = Conversions.bool_to_str(enable)
		bandwidthB_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthB, repcap.BandwidthB)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW{bandwidthB_cmd_val}:ENABle {param}')

	def get(self, bandwidthB=repcap.BandwidthB.Default) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW<bandwidth>:ENABle \n
		Snippet: value: bool = driver.configure.multiEval.limit.spectrFlatness.pofdm.bw.enable.get(bandwidthB = repcap.BandwidthB.Default) \n
		Enables or disables the spectrum flatness limit check for 802.11p OFDM signals with the specified <bandwidth>. \n
			:param bandwidthB: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: enable: OFF | ON"""
		bandwidthB_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthB, repcap.BandwidthB)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW{bandwidthB_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
