from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowerCls:
	"""Lower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lower", core, parent)

	def set(self, center: float, side: float, bandwidthB=repcap.BandwidthB.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW<bandwidth>:LOWer \n
		Snippet: driver.configure.multiEval.limit.spectrFlatness.pofdm.bw.lower.set(center = 1.0, side = 1.0, bandwidthB = repcap.BandwidthB.Default) \n
		Defines lower limits for the spectrum flatness of the center subcarriers and the side subcarriers of 802.11p OFDM signals
		with the specified <bandwidth>. The lower limits must be smaller than the upper limit. \n
			:param center: numeric Range: -20 dB to 4 dB
			:param side: numeric Range: -20 dB to 4 dB
			:param bandwidthB: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('center', center, DataType.Float), ArgSingle('side', side, DataType.Float))
		bandwidthB_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthB, repcap.BandwidthB)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW{bandwidthB_cmd_val}:LOWer {param}'.rstrip())

	# noinspection PyTypeChecker
	class LowerStruct(StructBase):
		"""Response structure. Fields: \n
			- Center: float: numeric Range: -20 dB to 4 dB
			- Side: float: numeric Range: -20 dB to 4 dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Center'),
			ArgStruct.scalar_float('Side')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Center: float = None
			self.Side: float = None

	def get(self, bandwidthB=repcap.BandwidthB.Default) -> LowerStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW<bandwidth>:LOWer \n
		Snippet: value: LowerStruct = driver.configure.multiEval.limit.spectrFlatness.pofdm.bw.lower.get(bandwidthB = repcap.BandwidthB.Default) \n
		Defines lower limits for the spectrum flatness of the center subcarriers and the side subcarriers of 802.11p OFDM signals
		with the specified <bandwidth>. The lower limits must be smaller than the upper limit. \n
			:param bandwidthB: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: structure: for return value, see the help for LowerStruct structure arguments."""
		bandwidthB_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthB, repcap.BandwidthB)
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:POFDm:BW{bandwidthB_cmd_val}:LOWer?', self.__class__.LowerStruct())
