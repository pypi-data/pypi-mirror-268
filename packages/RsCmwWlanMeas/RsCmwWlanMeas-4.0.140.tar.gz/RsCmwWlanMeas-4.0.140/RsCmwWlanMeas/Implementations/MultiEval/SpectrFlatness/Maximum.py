from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<instance>:MEValuation:SFLatness:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.spectrFlatness.maximum.read() \n
		Returns the margin values of the spectrum flatness measurement for the current, average, minimum and maximum traces.
		A positive margin indicates a violation of the spectrum flatness limit. The respective trace value is located above the
		upper or below the lower limit line. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: margins: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:SFLatness:MAXimum?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:SFLatness:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.spectrFlatness.maximum.fetch() \n
		Returns the margin values of the spectrum flatness measurement for the current, average, minimum and maximum traces.
		A positive margin indicates a violation of the spectrum flatness limit. The respective trace value is located above the
		upper or below the lower limit line. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: margins: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:SFLatness:MAXimum?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:WLAN:MEASurement<instance>:MEValuation:SFLatness:MAXimum \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.spectrFlatness.maximum.calculate() \n
		Returns the margin values of the spectrum flatness measurement for the current, average, minimum and maximum traces.
		A positive margin indicates a violation of the spectrum flatness limit. The respective trace value is located above the
		upper or below the lower limit line. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: margins: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:SFLatness:MAXimum?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
