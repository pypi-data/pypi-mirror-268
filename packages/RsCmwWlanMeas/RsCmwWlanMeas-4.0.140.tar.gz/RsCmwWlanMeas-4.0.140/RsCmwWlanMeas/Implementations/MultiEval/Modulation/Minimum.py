from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits. Range: 0 % to 100 %, Unit: %
			- Mcs_Index: int: decimal Modulation and coding scheme index Range: 0 to 76
			- Mod_Type: enums.ModulationTypeD: No parameter help available
			- Payload_Sym: int: decimal Number of OFDM symbols in the payload of the measured burst Range: 1 symbol to 1366 symbols, Unit: symbol
			- Measured_Sym: int: decimal Number of measured payload OFDM symbols Range: 1 symbol to 1366 symbols, Unit: symbol
			- Payload_Bytes: int: decimal Number of bytes in the payload of the measured burst. The results are only available for the standards up to Wi-Fi 4 (802.11n) , for Wi-Fi 5 standard (802.11ac) and later, NCAP is returned. Range: 1 byte to 4095 bytes, Unit: byte
			- Guard_Interval: enums.GuardInterval: SHORt | LONG | GI08 | GI16 | GI32 SHORt, LONG: short or long guard interval (up to 802.11ac) GI08, GI16, GI32: 0.8 μs, 1.6 μs, and 3.2 μs guard interval durations (for 802.11ax)
			- Nof_Ss: int: decimal Number of spatial streams Range: 1 to 8
			- No_Of_Sts: int: decimal Number of space-time streams Range: 1 to 8
			- Burst_Rate: float: float If a modulation filter is used, the burst rate indicates the share of bursts of the selected modulation type in the bursts received. Otherwise, it returns 1. See also [CMDLINKRESOLVED Configure.Isignal#Modfilter CMDLINKRESOLVED]. Unit: %
			- Power_Backoff: float: float Minimum distance of signal power to reference level since the start of the measurement Range: -100 dB to 0 dB, Unit: dB
			- Burst_Power: float: float RMS power of the measured burst Range: -100 dBm to 30 dBm, Unit: dBm
			- Peak_Power: float: float Peak power of the measured burst Range: -100 dBm to 30 dBm, Unit: dBm
			- Crest_Factor: float: float Range: 0 dB to 60 dB, Unit: dB
			- Evm_All_Carr: float: float EVM for all carriers Range: -100 dB to 0 dB, Unit: dB
			- Evm_Data_Carr: float: float EVM for data carriers Range: -100 dB to 0 dB, Unit: dB
			- Evm_Pilot_Carr: float: float EVM for pilot carriers Range: -100 dB to 0 dB, Unit: dB
			- Freq_Error: float: float Center frequency error Range: -150 MHz to 150 MHz, Unit: Hz
			- Clock_Error: float: float Symbol clock error Range: -125 ppm to 125 ppm, Unit: ppm
			- Iq_Offset: float: float Range: -100 dB to 0 dB, Unit: dB
			- Dc_Power: float: float Power of the DC subcarriers Range: -100 dBm to 30 dBm, Unit: dBm
			- Gain_Imbalance: float: float Gain imbalance cannot be calculated if the spectrum is not symmetrical, e.g. for HT_TB and HE_MU. Range: -100 dB to 100 dB, Unit: dB
			- Quad_Error: float: float Quadrature error cannot be calculated if the spectrum is not symmetrical, e.g. for HT_TB and HE_MU. Range: -180 deg to 180 deg, Unit: deg
			- Ltf_Power: float: float Power of long training fields (LTF) portion Unit: dBm
			- Data_Power: float: float Power of data portion Unit: dBm
			- Preamble_Power: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
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
			ArgStruct.scalar_float('Data_Power'),
			ArgStruct.scalar_float('Preamble_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
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
			self.Preamble_Power: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:MINimum \n
		Snippet: value: ResultData = driver.multiEval.modulation.minimum.read() \n
		Return the single value results for OFDM SISO measurements. For MIMO measurements, the stream/antenna-independent values
		are returned. For 80+80 MHz signals, the segment-independent values are returned. There are current, average, minimum,
		maximum and standard deviation results. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:MINimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:MINimum \n
		Snippet: value: ResultData = driver.multiEval.modulation.minimum.fetch() \n
		Return the single value results for OFDM SISO measurements. For MIMO measurements, the stream/antenna-independent values
		are returned. For 80+80 MHz signals, the segment-independent values are returned. There are current, average, minimum,
		maximum and standard deviation results. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:MINimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: enums.ResultStatus2: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits. Range: 0 % to 100 %, Unit: %
			- Mcs_Index: enums.ResultStatus2: decimal Modulation and coding scheme index Range: 0 to 76
			- Mod_Type: enums.ResultStatus2: No parameter help available
			- Payload_Sym: enums.ResultStatus2: decimal Number of OFDM symbols in the payload of the measured burst Range: 1 symbol to 1366 symbols, Unit: symbol
			- Measured_Sym: enums.ResultStatus2: decimal Number of measured payload OFDM symbols Range: 1 symbol to 1366 symbols, Unit: symbol
			- Payload_Bytes: enums.ResultStatus2: decimal Number of bytes in the payload of the measured burst. The results are only available for the standards up to Wi-Fi 4 (802.11n) , for Wi-Fi 5 standard (802.11ac) and later, NCAP is returned. Range: 1 byte to 4095 bytes, Unit: byte
			- Guard_Interval: enums.ResultStatus2: SHORt | LONG | GI08 | GI16 | GI32 SHORt, LONG: short or long guard interval (up to 802.11ac) GI08, GI16, GI32: 0.8 μs, 1.6 μs, and 3.2 μs guard interval durations (for 802.11ax)
			- Nof_Ss: enums.ResultStatus2: decimal Number of spatial streams Range: 1 to 8
			- No_Of_Sts: enums.ResultStatus2: decimal Number of space-time streams Range: 1 to 8
			- Burst_Rate: enums.ResultStatus2: float If a modulation filter is used, the burst rate indicates the share of bursts of the selected modulation type in the bursts received. Otherwise, it returns 1. See also [CMDLINKRESOLVED Configure.Isignal#Modfilter CMDLINKRESOLVED]. Unit: %
			- Power_Backoff: enums.ResultStatus2: float Minimum distance of signal power to reference level since the start of the measurement Range: -100 dB to 0 dB, Unit: dB
			- Burst_Power: enums.ResultStatus2: float RMS power of the measured burst Range: -100 dBm to 30 dBm, Unit: dBm
			- Peak_Power: enums.ResultStatus2: float Peak power of the measured burst Range: -100 dBm to 30 dBm, Unit: dBm
			- Crest_Factor: enums.ResultStatus2: float Range: 0 dB to 60 dB, Unit: dB
			- Evm_All_Carr: enums.ResultStatus2: float EVM for all carriers Range: -100 dB to 0 dB, Unit: dB
			- Evm_Data_Carr: enums.ResultStatus2: float EVM for data carriers Range: -100 dB to 0 dB, Unit: dB
			- Evm_Pilot_Carr: enums.ResultStatus2: float EVM for pilot carriers Range: -100 dB to 0 dB, Unit: dB
			- Freq_Error: enums.ResultStatus2: float Center frequency error Range: -150 MHz to 150 MHz, Unit: Hz
			- Clock_Error: enums.ResultStatus2: float Symbol clock error Range: -125 ppm to 125 ppm, Unit: ppm
			- Iq_Offset: enums.ResultStatus2: float Range: -100 dB to 0 dB, Unit: dB
			- Dc_Power: enums.ResultStatus2: float Power of the DC subcarriers Range: -100 dBm to 30 dBm, Unit: dBm
			- Gain_Imbalance: enums.ResultStatus2: float Gain imbalance cannot be calculated if the spectrum is not symmetrical, e.g. for HT_TB and HE_MU. Range: -100 dB to 100 dB, Unit: dB
			- Quad_Error: enums.ResultStatus2: float Quadrature error cannot be calculated if the spectrum is not symmetrical, e.g. for HT_TB and HE_MU. Range: -180 deg to 180 deg, Unit: deg
			- Ltf_Power: enums.ResultStatus2: float Power of long training fields (LTF) portion Unit: dBm
			- Data_Power: enums.ResultStatus2: float Power of data portion Unit: dBm
			- Preamble_Power: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2),
			ArgStruct.scalar_enum('Mcs_Index', enums.ResultStatus2),
			ArgStruct.scalar_enum('Mod_Type', enums.ResultStatus2),
			ArgStruct.scalar_enum('Payload_Sym', enums.ResultStatus2),
			ArgStruct.scalar_enum('Measured_Sym', enums.ResultStatus2),
			ArgStruct.scalar_enum('Payload_Bytes', enums.ResultStatus2),
			ArgStruct.scalar_enum('Guard_Interval', enums.ResultStatus2),
			ArgStruct.scalar_enum('Nof_Ss', enums.ResultStatus2),
			ArgStruct.scalar_enum('No_Of_Sts', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Rate', enums.ResultStatus2),
			ArgStruct.scalar_enum('Power_Backoff', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Peak_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Crest_Factor', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_All_Carr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Data_Carr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Pilot_Carr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Freq_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Clock_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dc_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Gain_Imbalance', enums.ResultStatus2),
			ArgStruct.scalar_enum('Quad_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ltf_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Data_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Preamble_Power', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: enums.ResultStatus2 = None
			self.Mcs_Index: enums.ResultStatus2 = None
			self.Mod_Type: enums.ResultStatus2 = None
			self.Payload_Sym: enums.ResultStatus2 = None
			self.Measured_Sym: enums.ResultStatus2 = None
			self.Payload_Bytes: enums.ResultStatus2 = None
			self.Guard_Interval: enums.ResultStatus2 = None
			self.Nof_Ss: enums.ResultStatus2 = None
			self.No_Of_Sts: enums.ResultStatus2 = None
			self.Burst_Rate: enums.ResultStatus2 = None
			self.Power_Backoff: enums.ResultStatus2 = None
			self.Burst_Power: enums.ResultStatus2 = None
			self.Peak_Power: enums.ResultStatus2 = None
			self.Crest_Factor: enums.ResultStatus2 = None
			self.Evm_All_Carr: enums.ResultStatus2 = None
			self.Evm_Data_Carr: enums.ResultStatus2 = None
			self.Evm_Pilot_Carr: enums.ResultStatus2 = None
			self.Freq_Error: enums.ResultStatus2 = None
			self.Clock_Error: enums.ResultStatus2 = None
			self.Iq_Offset: enums.ResultStatus2 = None
			self.Dc_Power: enums.ResultStatus2 = None
			self.Gain_Imbalance: enums.ResultStatus2 = None
			self.Quad_Error: enums.ResultStatus2 = None
			self.Ltf_Power: enums.ResultStatus2 = None
			self.Data_Power: enums.ResultStatus2 = None
			self.Preamble_Power: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:MINimum \n
		Snippet: value: CalculateStruct = driver.multiEval.modulation.minimum.calculate() \n
		Return the single value results for OFDM SISO measurements. For MIMO measurements, the stream/antenna-independent values
		are returned. For 80+80 MHz signals, the segment-independent values are returned. There are current, average, minimum,
		maximum and standard deviation results. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:MINimum?', self.__class__.CalculateStruct())
