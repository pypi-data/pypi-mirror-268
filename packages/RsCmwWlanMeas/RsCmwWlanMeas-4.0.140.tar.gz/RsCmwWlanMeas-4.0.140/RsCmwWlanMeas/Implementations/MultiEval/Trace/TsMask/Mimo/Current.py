from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self, start: float = None, count: float = None, decimation: float = None, mimo=repcap.Mimo.Default) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:TSMask:MIMO<n>:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.tsMask.mimo.current.read(start = 1.0, count = 1.0, decimation = 1.0, mimo = repcap.Mimo.Default) \n
		Return the values of the transmit spectrum mask traces for MIMO measurements, antenna <n>, bandwidths with one segment.
		The results of the current, average, minimum and maximum traces can be retrieved. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:param start: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param count: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param decimation: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: spectrum_trace_tx: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:TSMask:MIMO{mimo_cmd_val}:CURRent? {param}'.rstrip(), suppressed)
		return response

	def fetch(self, start: float = None, count: float = None, decimation: float = None, mimo=repcap.Mimo.Default) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:TSMask:MIMO<n>:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.tsMask.mimo.current.fetch(start = 1.0, count = 1.0, decimation = 1.0, mimo = repcap.Mimo.Default) \n
		Return the values of the transmit spectrum mask traces for MIMO measurements, antenna <n>, bandwidths with one segment.
		The results of the current, average, minimum and maximum traces can be retrieved. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:param start: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param count: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param decimation: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: spectrum_trace_tx: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:TSMask:MIMO{mimo_cmd_val}:CURRent? {param}'.rstrip(), suppressed)
		return response
