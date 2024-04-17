from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDevCls:
	"""StandardDev commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Evm_All_Carr_Seg_1: float: No parameter help available
			- Evm_All_Carr_Seg_2: float: No parameter help available
			- Evm_Data_Carr_Seg_1: float: No parameter help available
			- Evm_Data_Carr_Seg_2: float: No parameter help available
			- Evm_Pilot_Carr_Seg_1: float: No parameter help available
			- Evm_Pilot_Carr_Seg_2: float: No parameter help available
			- Power_Backoff_Seg_1: float: No parameter help available
			- Power_Backoff_Seg_2: float: No parameter help available
			- Burst_Power_Seg_1: float: No parameter help available
			- Burst_Power_Seg_2: float: No parameter help available
			- Peak_Power_Seg_1: float: No parameter help available
			- Peak_Power_Seg_2: float: No parameter help available
			- Crest_Factor_Seg_1: float: No parameter help available
			- Crest_Factor_Seg_2: float: No parameter help available
			- Iq_Offset_Seg_1: float: No parameter help available
			- Iq_Offset_Seg_2: float: No parameter help available
			- Dc_Power_Seg_1: float: No parameter help available
			- Dc_Power_Seg_2: float: No parameter help available
			- Ltf_Power_Seg_1: float: No parameter help available
			- Ltf_Power_Seg_2: float: No parameter help available
			- Data_Power_Seg_1: float: No parameter help available
			- Data_Power_Seg_2: float: No parameter help available
			- Preamble_Power_Seg_1: float: No parameter help available
			- Preamble_Power_Seg_2: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Evm_All_Carr_Seg_1'),
			ArgStruct.scalar_float('Evm_All_Carr_Seg_2'),
			ArgStruct.scalar_float('Evm_Data_Carr_Seg_1'),
			ArgStruct.scalar_float('Evm_Data_Carr_Seg_2'),
			ArgStruct.scalar_float('Evm_Pilot_Carr_Seg_1'),
			ArgStruct.scalar_float('Evm_Pilot_Carr_Seg_2'),
			ArgStruct.scalar_float('Power_Backoff_Seg_1'),
			ArgStruct.scalar_float('Power_Backoff_Seg_2'),
			ArgStruct.scalar_float('Burst_Power_Seg_1'),
			ArgStruct.scalar_float('Burst_Power_Seg_2'),
			ArgStruct.scalar_float('Peak_Power_Seg_1'),
			ArgStruct.scalar_float('Peak_Power_Seg_2'),
			ArgStruct.scalar_float('Crest_Factor_Seg_1'),
			ArgStruct.scalar_float('Crest_Factor_Seg_2'),
			ArgStruct.scalar_float('Iq_Offset_Seg_1'),
			ArgStruct.scalar_float('Iq_Offset_Seg_2'),
			ArgStruct.scalar_float('Dc_Power_Seg_1'),
			ArgStruct.scalar_float('Dc_Power_Seg_2'),
			ArgStruct.scalar_float('Ltf_Power_Seg_1'),
			ArgStruct.scalar_float('Ltf_Power_Seg_2'),
			ArgStruct.scalar_float('Data_Power_Seg_1'),
			ArgStruct.scalar_float('Data_Power_Seg_2'),
			ArgStruct.scalar_float('Preamble_Power_Seg_1'),
			ArgStruct.scalar_float('Preamble_Power_Seg_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Evm_All_Carr_Seg_1: float = None
			self.Evm_All_Carr_Seg_2: float = None
			self.Evm_Data_Carr_Seg_1: float = None
			self.Evm_Data_Carr_Seg_2: float = None
			self.Evm_Pilot_Carr_Seg_1: float = None
			self.Evm_Pilot_Carr_Seg_2: float = None
			self.Power_Backoff_Seg_1: float = None
			self.Power_Backoff_Seg_2: float = None
			self.Burst_Power_Seg_1: float = None
			self.Burst_Power_Seg_2: float = None
			self.Peak_Power_Seg_1: float = None
			self.Peak_Power_Seg_2: float = None
			self.Crest_Factor_Seg_1: float = None
			self.Crest_Factor_Seg_2: float = None
			self.Iq_Offset_Seg_1: float = None
			self.Iq_Offset_Seg_2: float = None
			self.Dc_Power_Seg_1: float = None
			self.Dc_Power_Seg_2: float = None
			self.Ltf_Power_Seg_1: float = None
			self.Ltf_Power_Seg_2: float = None
			self.Data_Power_Seg_1: float = None
			self.Data_Power_Seg_2: float = None
			self.Preamble_Power_Seg_1: float = None
			self.Preamble_Power_Seg_2: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<instance>:MEValuation:MODulation:SEGMents:SDEViation \n
		Snippet: value: ResultData = driver.multiEval.modulation.segments.standardDev.read() \n
		Return the segment-specific single value results for 80+80 MHz SISO measurements. There are current, average, minimum,
		maximum and standard deviation results. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:SEGMents:SDEViation?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:MODulation:SEGMents:SDEViation \n
		Snippet: value: ResultData = driver.multiEval.modulation.segments.standardDev.fetch() \n
		Return the segment-specific single value results for 80+80 MHz SISO measurements. There are current, average, minimum,
		maximum and standard deviation results. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:SEGMents:SDEViation?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Evm_All_Carr_Seg_1: enums.ResultStatus2: No parameter help available
			- Evm_All_Carr_Seg_2: enums.ResultStatus2: No parameter help available
			- Evm_Data_Carr_Seg_1: enums.ResultStatus2: No parameter help available
			- Evm_Data_Carr_Seg_2: enums.ResultStatus2: No parameter help available
			- Evm_Pilot_Carr_Seg_1: enums.ResultStatus2: No parameter help available
			- Evm_Pilot_Carr_Seg_2: enums.ResultStatus2: No parameter help available
			- Power_Backoff_Seg_1: enums.ResultStatus2: No parameter help available
			- Power_Backoff_Seg_2: enums.ResultStatus2: No parameter help available
			- Burst_Power_Seg_1: enums.ResultStatus2: No parameter help available
			- Burst_Power_Seg_2: enums.ResultStatus2: No parameter help available
			- Peak_Power_Seg_1: enums.ResultStatus2: No parameter help available
			- Peak_Power_Seg_2: enums.ResultStatus2: No parameter help available
			- Crest_Factor_Seg_1: enums.ResultStatus2: No parameter help available
			- Crest_Factor_Seg_2: enums.ResultStatus2: No parameter help available
			- Iq_Offset_Seg_1: enums.ResultStatus2: No parameter help available
			- Iq_Offset_Seg_2: enums.ResultStatus2: No parameter help available
			- Dc_Power_Seg_1: enums.ResultStatus2: No parameter help available
			- Dc_Power_Seg_2: enums.ResultStatus2: No parameter help available
			- Ltf_Power_Seg_1: enums.ResultStatus2: No parameter help available
			- Ltf_Power_Seg_2: enums.ResultStatus2: No parameter help available
			- Data_Power_Seg_1: enums.ResultStatus2: No parameter help available
			- Data_Power_Seg_2: enums.ResultStatus2: No parameter help available
			- Preamble_Power_Seg_1: enums.ResultStatus2: No parameter help available
			- Preamble_Power_Seg_2: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Evm_All_Carr_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_All_Carr_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Data_Carr_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Data_Carr_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Pilot_Carr_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Pilot_Carr_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Power_Backoff_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Power_Backoff_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Power_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Power_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Peak_Power_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Peak_Power_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Crest_Factor_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Crest_Factor_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dc_Power_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dc_Power_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ltf_Power_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ltf_Power_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Data_Power_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Data_Power_Seg_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Preamble_Power_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Preamble_Power_Seg_2', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Evm_All_Carr_Seg_1: enums.ResultStatus2 = None
			self.Evm_All_Carr_Seg_2: enums.ResultStatus2 = None
			self.Evm_Data_Carr_Seg_1: enums.ResultStatus2 = None
			self.Evm_Data_Carr_Seg_2: enums.ResultStatus2 = None
			self.Evm_Pilot_Carr_Seg_1: enums.ResultStatus2 = None
			self.Evm_Pilot_Carr_Seg_2: enums.ResultStatus2 = None
			self.Power_Backoff_Seg_1: enums.ResultStatus2 = None
			self.Power_Backoff_Seg_2: enums.ResultStatus2 = None
			self.Burst_Power_Seg_1: enums.ResultStatus2 = None
			self.Burst_Power_Seg_2: enums.ResultStatus2 = None
			self.Peak_Power_Seg_1: enums.ResultStatus2 = None
			self.Peak_Power_Seg_2: enums.ResultStatus2 = None
			self.Crest_Factor_Seg_1: enums.ResultStatus2 = None
			self.Crest_Factor_Seg_2: enums.ResultStatus2 = None
			self.Iq_Offset_Seg_1: enums.ResultStatus2 = None
			self.Iq_Offset_Seg_2: enums.ResultStatus2 = None
			self.Dc_Power_Seg_1: enums.ResultStatus2 = None
			self.Dc_Power_Seg_2: enums.ResultStatus2 = None
			self.Ltf_Power_Seg_1: enums.ResultStatus2 = None
			self.Ltf_Power_Seg_2: enums.ResultStatus2 = None
			self.Data_Power_Seg_1: enums.ResultStatus2 = None
			self.Data_Power_Seg_2: enums.ResultStatus2 = None
			self.Preamble_Power_Seg_1: enums.ResultStatus2 = None
			self.Preamble_Power_Seg_2: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<instance>:MEValuation:MODulation:SEGMents:SDEViation \n
		Snippet: value: CalculateStruct = driver.multiEval.modulation.segments.standardDev.calculate() \n
		Return the segment-specific single value results for 80+80 MHz SISO measurements. There are current, average, minimum,
		maximum and standard deviation results. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:SEGMents:SDEViation?', self.__class__.CalculateStruct())
