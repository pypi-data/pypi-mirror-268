from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


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
			- Out_Of_Tol_Seg_1: float: float Out of tolerance result, segment 1 Range: 0 % to 100 % , Unit: %
			- Out_Of_Tol_Seg_2: float: float Out of tolerance result, segment 2 Range: 0 % to 100 % , Unit: %
			- Margin_Xvals_Seg_1: List[float]: No parameter help available
			- Margin_Xvals_Seg_2: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol_Seg_1'),
			ArgStruct.scalar_float('Out_Of_Tol_Seg_2'),
			ArgStruct('Margin_Xvals_Seg_1', DataType.FloatList, None, False, True, 1),
			ArgStruct('Margin_Xvals_Seg_2', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol_Seg_1: float = None
			self.Out_Of_Tol_Seg_2: float = None
			self.Margin_Xvals_Seg_1: List[float] = None
			self.Margin_Xvals_Seg_2: List[float] = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:SEGMents:FREQuency:MINimum \n
		Snippet: value: ResultData = driver.multiEval.tsMask.segments.frequency.minimum.read() \n
		Return the X-positions of the limit line margins of the transmit spectrum mask, for SISO measurements, for bandwidths
		with two segments. Positions for the current, average, minimum and maximum traces are returned. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:SEGMents:FREQuency:MINimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:SEGMents:FREQuency:MINimum \n
		Snippet: value: ResultData = driver.multiEval.tsMask.segments.frequency.minimum.fetch() \n
		Return the X-positions of the limit line margins of the transmit spectrum mask, for SISO measurements, for bandwidths
		with two segments. Positions for the current, average, minimum and maximum traces are returned. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:SEGMents:FREQuency:MINimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol_Seg_1: enums.ResultStatus2: float Out of tolerance result, segment 1 Range: 0 % to 100 % , Unit: %
			- Out_Of_Tol_Seg_2: enums.ResultStatus2: float Out of tolerance result, segment 2 Range: 0 % to 100 % , Unit: %
			- Margin_Xvals_Seg_1: List[enums.ResultStatus2]: No parameter help available
			- Margin_Xvals_Seg_2: List[enums.ResultStatus2]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Out_Of_Tol_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol_Seg_2', enums.ResultStatus2),
			ArgStruct('Margin_Xvals_Seg_1', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Margin_Xvals_Seg_2', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol_Seg_1: enums.ResultStatus2 = None
			self.Out_Of_Tol_Seg_2: enums.ResultStatus2 = None
			self.Margin_Xvals_Seg_1: List[enums.ResultStatus2] = None
			self.Margin_Xvals_Seg_2: List[enums.ResultStatus2] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:SEGMents:FREQuency:MINimum \n
		Snippet: value: CalculateStruct = driver.multiEval.tsMask.segments.frequency.minimum.calculate() \n
		Return the X-positions of the limit line margins of the transmit spectrum mask, for SISO measurements, for bandwidths
		with two segments. Positions for the current, average, minimum and maximum traces are returned. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:SEGMents:FREQuency:MINimum?', self.__class__.CalculateStruct())
