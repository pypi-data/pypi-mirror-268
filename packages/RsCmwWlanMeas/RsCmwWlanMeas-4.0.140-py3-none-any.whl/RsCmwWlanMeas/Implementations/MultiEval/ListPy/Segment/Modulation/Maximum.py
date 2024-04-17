from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Out_Of_Tol: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits. Range: 0 % to 100 %, Unit: %
			- Mcs_Index: int: decimal Modulation and coding scheme index Range: 0 to 76
			- Mod_Type: enums.ModulationTypeD: UNSPecified | BPSK14 | BPSK12 | BPSK34 | QPSK14 | QPSK12 | QPSK34 | 16Q14 | 16Q38 | 16Q12 | 16Q34 | 64Q12 | 64Q23 | 64Q34 | 64Q56 | 256Q34 | 256Q56 | 1KQ34 | 1KQ56 | BPSK | QPSK | 16Q | 64Q | 256Q | 1KQ Modulation scheme and coding rate UNSPecified: modulation unknown BPSK: BPSK, coding rate unknown BPSK12, BPSK34 (BPSKab) : BPSK, coding rate a/b BPSK14: BPSK, coding rate 1/2 DCM QPSK: QPSK, coding rate unknown QPSK12, QPSK34 (QPSKab) : QPSK, coding rate a/b QPSK14: QPSK, coding rate 1/2 DCM 16Q: 16-QAM, coding rate unknown 16Q12, 16Q34 (16Qab) : 16-QAM, coding rate a/b 16Q14: 16-QAM, coding rate 1/2 DCM 16Q38: 16-QAM, coding rate 3/4 DCM 64Q: 64-QAM, coding rate unknown 64Q12, 64Q23, 64Q34, 64Q56 (64Qab) : 64-QAM, coding rate a/b 256Q: 256-QAM, coding rate unknown 256Q34, 256Q56 (256Qab) : 256-QAM, coding rate a/b 1KQ: 1024-QAM, coding rate unknown 1KQ34, 1KQ56 (1KQab) : 1024-QAM, coding rate a/b
			- Payload_Sym: int: decimal Number of OFDM symbols in the payload of the measured burst Range: 1 symbol to 1366 symbols, Unit: symbol
			- Measured_Sym: int: decimal Number of OFDM symbols in the payload to be measured Range: 1 symbol to 1366 symbols, Unit: symbol
			- Payload_Bytes: int: decimal Number of bytes in the payload of the measured burst. The results are only available for the standards up to Wi-Fi 4 (802.11n) , for Wi-Fi 5 standard (802.11ac) and later, NCAP is returned. Range: 1 byte to 4095 bytes, Unit: byte
			- Guard_Interval: enums.GuardInterval: SHORt | LONG | GI08 | GI16 | GI32 SHORt, LONG: short or long guard interval (up to 802.11ac) GI08, GI16, GI32: 0.8 μs, 1.6 μs, and 3.2 μs guard interval durations (for 802.11ax)
			- Nof_Ss: int: decimal Number of spatial streams Range: 1 to 8
			- No_Of_Sts: int: decimal Number of space-time streams Range: 1 to 8
			- Burst_Rate: float: float Indicates the share of bursts of the selected modulation type 5_ModType in the bursts received. Unit: %
			- Power_Backoff: float: float Minimum distance of signal power to reference level since the start of the measurement Range: -100 dB to 0 dB, Unit: dB
			- Burst_Power: float: float RMS power of the measured burst Range: -100 dBm to 30 dBm, Unit: dBm
			- Peak_Power: float: float Peak power of the measured burst Range: -100 dBm to 30 dBm, Unit: dBm
			- Crest_Factor: float: float Range: 0 dB to 60 dB, Unit: dB
			- Evm_All_Carr: float: float EVM for all, data, and pilot carriers Range: -100 dB to 0 dB, Unit: dB
			- Evm_Data_Carr: float: float EVM for all, data, and pilot carriers Range: -100 dB to 0 dB, Unit: dB
			- Evm_Pilot_Carr: float: float EVM for all, data, and pilot carriers Range: -100 dB to 0 dB, Unit: dB
			- Freq_Error: float: float Center frequency error Range: -150 MHz to 150 MHz, Unit: Hz
			- Clock_Error: float: float Symbol clock error Range: -125 ppm to 125 ppm, Unit: ppm
			- Iq_Offset: float: float Range: -100 dB to 0 dB, Unit: dB
			- Dc_Power: float: float Range: -100 dBm to 30 dBm, Unit: dBm
			- Gain_Imbalance: float: float Range: -100 dB to 100 dB, Unit: dB
			- Quad_Error: float: float Quadrature error Range: -180 deg to 180 deg, Unit: deg
			- Ltf_Power: float: float Power of long training fields (LTF) portion Unit: dBm
			- Data_Power: float: float Power of data portion Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_int('Mcs_Index'),
			ArgStruct.scalar_enum('Mod_Type', enums.ModulationTypeD),
			ArgStruct.scalar_int('Payload_Sym'),
			ArgStruct.scalar_int('Measured_Sym'),
			ArgStruct.scalar_int('Payload_Bytes'),
			ArgStruct.scalar_enum('Guard_Interval', enums.GuardInterval),
			ArgStruct.scalar_int('Nof_Ss'),
			ArgStruct.scalar_int('No_Of_Sts'),
			ArgStruct.scalar_float('Burst_Rate'),
			ArgStruct.scalar_float('Power_Backoff'),
			ArgStruct.scalar_float('Burst_Power'),
			ArgStruct.scalar_float('Peak_Power'),
			ArgStruct.scalar_float('Crest_Factor'),
			ArgStruct.scalar_float('Evm_All_Carr'),
			ArgStruct.scalar_float('Evm_Data_Carr'),
			ArgStruct.scalar_float('Evm_Pilot_Carr'),
			ArgStruct.scalar_float('Freq_Error'),
			ArgStruct.scalar_float('Clock_Error'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Dc_Power'),
			ArgStruct.scalar_float('Gain_Imbalance'),
			ArgStruct.scalar_float('Quad_Error'),
			ArgStruct.scalar_float('Ltf_Power'),
			ArgStruct.scalar_float('Data_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Mcs_Index: int = None
			self.Mod_Type: enums.ModulationTypeD = None
			self.Payload_Sym: int = None
			self.Measured_Sym: int = None
			self.Payload_Bytes: int = None
			self.Guard_Interval: enums.GuardInterval = None
			self.Nof_Ss: int = None
			self.No_Of_Sts: int = None
			self.Burst_Rate: float = None
			self.Power_Backoff: float = None
			self.Burst_Power: float = None
			self.Peak_Power: float = None
			self.Crest_Factor: float = None
			self.Evm_All_Carr: float = None
			self.Evm_Data_Carr: float = None
			self.Evm_Pilot_Carr: float = None
			self.Freq_Error: float = None
			self.Clock_Error: float = None
			self.Iq_Offset: float = None
			self.Dc_Power: float = None
			self.Gain_Imbalance: float = None
			self.Quad_Error: float = None
			self.Ltf_Power: float = None
			self.Data_Power: float = None

	def fetch(self, segmentB=repcap.SegmentB.Default) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:MODulation:MAXimum \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.modulation.maximum.fetch(segmentB = repcap.SegmentB.Default) \n
		Return OFDM/OFDMA modulation single value results for segment <no> in list mode. \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:MODulation:MAXimum?', self.__class__.FetchStruct())
