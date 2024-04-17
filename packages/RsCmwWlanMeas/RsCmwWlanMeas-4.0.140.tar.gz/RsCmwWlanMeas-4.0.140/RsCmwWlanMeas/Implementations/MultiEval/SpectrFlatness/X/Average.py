from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def read(self) -> List[int]:
		"""SCPI: READ:WLAN:MEASurement<instance>:MEValuation:SFLatness:X:AVERage \n
		Snippet: value: List[int] = driver.multiEval.spectrFlatness.x.average.read() \n
		Return the subcarrier indices for the current, average, minimum and maximum margin values. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: margins: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:SFLatness:X:AVERage?', suppressed)
		return response

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:SFLatness:X:AVERage \n
		Snippet: value: List[int] = driver.multiEval.spectrFlatness.x.average.fetch() \n
		Return the subcarrier indices for the current, average, minimum and maximum margin values. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: margins: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:SFLatness:X:AVERage?', suppressed)
		return response
