from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:MODulation:BPOWer:AVERage \n
		Snippet: value: List[float] = driver.multiEval.listPy.modulation.bpower.average.fetch() \n
		Return the burst power results for OFDM/OFDMA signals in list mode. The values in curly brackets {} are specified for
		each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments n is determined by method
		RsCmwWlanMeas.Configure.MultiEval.ListPy.count. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: burst_power: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:MODulation:BPOWer:AVERage?', suppressed)
		return response
