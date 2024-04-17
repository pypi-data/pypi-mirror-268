from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Mod_Type: enums.ModulationTypeC: DBPSk1 | DQPSk2 | CCK5 | CCK11 DBPSk1: 1 Mbps DBPSK DQPSk2: 2 Mbps DQPSK CCK5: 5.5 Mbps CCK CCK11: 11 Mbps CCK
			- Plcp_Type: enums.PlcpType: SHORtplcp | LONGplcp Short or long PLCP
			- Payload_Length: int: decimal Range: 1 byte to 4095 bytes, Unit: byte
			- Burst_Power: float: float Range: -100 dBm to 30 dBm, Unit: dBm
			- Evm_Peak: float: float Error vector magnitude peak value Range: 0 % to 100 %, Unit: %
			- Evm: float: float Error vector magnitude RMS value Range: 0 % to 100 %, Unit: %
			- Freq_Error: float: float Center frequency error Range: -150 MHz to 150 MHz Hz
			- Clock_Error: float: float Chip clock error Range: -125 ppm to 125 ppm, Unit: ppm
			- Iq_Offset: float: float Range: -100 dB to 0 dB, Unit: dB
			- Gain_Imbalance: float: float Gain imbalance Range: -100 dB to 100 dB, Unit: dB
			- Quad_Error: float: float Quadrature error Range: -180 deg to 180 deg, Unit: deg
			- Out_Of_Tol: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits. Range: 0 % to 100 % , Unit: %
			- Burst_Rate: float: float If a modulation filter is used, the burst rate indicates the share of bursts of the selected modulation type in the bursts received. Otherwise, it returns 1. See [CMDLINKRESOLVED Configure.Isignal#Modfilter CMDLINKRESOLVED]. Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Mod_Type', enums.ModulationTypeC),
			ArgStruct.scalar_enum('Plcp_Type', enums.PlcpType),
			ArgStruct.scalar_int('Payload_Length'),
			ArgStruct.scalar_float('Burst_Power'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Evm'),
			ArgStruct.scalar_float('Freq_Error'),
			ArgStruct.scalar_float('Clock_Error'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Gain_Imbalance'),
			ArgStruct.scalar_float('Quad_Error'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Burst_Rate')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Mod_Type: enums.ModulationTypeC = None
			self.Plcp_Type: enums.PlcpType = None
			self.Payload_Length: int = None
			self.Burst_Power: float = None
			self.Evm_Peak: float = None
			self.Evm: float = None
			self.Freq_Error: float = None
			self.Clock_Error: float = None
			self.Iq_Offset: float = None
			self.Gain_Imbalance: float = None
			self.Quad_Error: float = None
			self.Out_Of_Tol: float = None
			self.Burst_Rate: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:AVERage \n
		Snippet: value: ResultData = driver.multiEval.modulation.dsss.average.read() \n
		Return the current, average, minimum, maximum and standard deviation single value results for DSSS signals. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:AVERage?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:AVERage \n
		Snippet: value: ResultData = driver.multiEval.modulation.dsss.average.fetch() \n
		Return the current, average, minimum, maximum and standard deviation single value results for DSSS signals. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:AVERage?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: str: decimal 'Reliability indicator'
			- Mod_Type: enums.ResultStatus2: DBPSk1 | DQPSk2 | CCK5 | CCK11 DBPSk1: 1 Mbps DBPSK DQPSk2: 2 Mbps DQPSK CCK5: 5.5 Mbps CCK CCK11: 11 Mbps CCK
			- Plcp_Type: enums.ResultStatus2: SHORtplcp | LONGplcp Short or long PLCP
			- Payload_Length: enums.ResultStatus2: decimal Range: 1 byte to 4095 bytes, Unit: byte
			- Burst_Power: enums.ResultStatus2: float Range: -100 dBm to 30 dBm, Unit: dBm
			- Evm_Peak: enums.ResultStatus2: float Error vector magnitude peak value Range: 0 % to 100 %, Unit: %
			- Evm: enums.ResultStatus2: float Error vector magnitude RMS value Range: 0 % to 100 %, Unit: %
			- Freq_Error: enums.ResultStatus2: float Center frequency error Range: -150 MHz to 150 MHz Hz
			- Clock_Error: enums.ResultStatus2: float Chip clock error Range: -125 ppm to 125 ppm, Unit: ppm
			- Iq_Offset: enums.ResultStatus2: float Range: -100 dB to 0 dB, Unit: dB
			- Gain_Imbalance: enums.ResultStatus2: float Gain imbalance Range: -100 dB to 100 dB, Unit: dB
			- Quad_Error: enums.ResultStatus2: float Quadrature error Range: -180 deg to 180 deg, Unit: deg
			- Out_Of_Tol: enums.ResultStatus2: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits. Range: 0 % to 100 % , Unit: %
			- Burst_Rate: enums.ResultStatus2: float If a modulation filter is used, the burst rate indicates the share of bursts of the selected modulation type in the bursts received. Otherwise, it returns 1. See [CMDLINKRESOLVED Configure.Isignal#Modfilter CMDLINKRESOLVED]. Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Reliability'),
			ArgStruct.scalar_enum('Mod_Type', enums.ResultStatus2),
			ArgStruct.scalar_enum('Plcp_Type', enums.ResultStatus2),
			ArgStruct.scalar_enum('Payload_Length', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Peak', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm', enums.ResultStatus2),
			ArgStruct.scalar_enum('Freq_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Clock_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset', enums.ResultStatus2),
			ArgStruct.scalar_enum('Gain_Imbalance', enums.ResultStatus2),
			ArgStruct.scalar_enum('Quad_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Rate', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: str = None
			self.Mod_Type: enums.ResultStatus2 = None
			self.Plcp_Type: enums.ResultStatus2 = None
			self.Payload_Length: enums.ResultStatus2 = None
			self.Burst_Power: enums.ResultStatus2 = None
			self.Evm_Peak: enums.ResultStatus2 = None
			self.Evm: enums.ResultStatus2 = None
			self.Freq_Error: enums.ResultStatus2 = None
			self.Clock_Error: enums.ResultStatus2 = None
			self.Iq_Offset: enums.ResultStatus2 = None
			self.Gain_Imbalance: enums.ResultStatus2 = None
			self.Quad_Error: enums.ResultStatus2 = None
			self.Out_Of_Tol: enums.ResultStatus2 = None
			self.Burst_Rate: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:AVERage \n
		Snippet: value: CalculateStruct = driver.multiEval.modulation.dsss.average.calculate() \n
		Return the current, average, minimum, maximum and standard deviation single value results for DSSS signals. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:AVERage?', self.__class__.CalculateStruct())
