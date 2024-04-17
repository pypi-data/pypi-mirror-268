from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Power: enums.ResultStatus2: float Range: 0 µs to 10 µs, Unit: μs
			- Out_Of_Tol: enums.ResultStatus2: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for PVT measurements exceeding the specified power limit Range: 0 % to 100 % , Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Power: enums.ResultStatus2 = None
			self.Out_Of_Tol: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:PVTime:REDGe:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.powerVsTime.risingEdge.maximum.calculate() \n
		Returns the current, average and maximum ramp durations of the power vs time measurement, for the falling edge (FEDGe)
		and rising edge (REDGe) . The values described below are returned by FETCh and READ commands. CALCulate commands return
		limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:PVTime:REDGe:MAXimum?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Power: float: float Range: 0 µs to 10 µs, Unit: μs
			- Out_Of_Tol: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for PVT measurements exceeding the specified power limit Range: 0 % to 100 % , Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Power'),
			ArgStruct.scalar_float('Out_Of_Tol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Power: float = None
			self.Out_Of_Tol: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:PVTime:REDGe:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.powerVsTime.risingEdge.maximum.read() \n
		Returns the current, average and maximum ramp durations of the power vs time measurement, for the falling edge (FEDGe)
		and rising edge (REDGe) . The values described below are returned by FETCh and READ commands. CALCulate commands return
		limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:PVTime:REDGe:MAXimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:PVTime:REDGe:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.powerVsTime.risingEdge.maximum.fetch() \n
		Returns the current, average and maximum ramp durations of the power vs time measurement, for the falling edge (FEDGe)
		and rising edge (REDGe) . The values described below are returned by FETCh and READ commands. CALCulate commands return
		limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:PVTime:REDGe:MAXimum?', self.__class__.ResultData())
