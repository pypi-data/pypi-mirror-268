from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self, start: float = None, count: float = None, decimation: float = None, mimo=repcap.Mimo.Default, segment=repcap.Segment.Default) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:PVTime:REDGe:MIMO<n>:SEGMent<seg>:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.powerVsTime.risingEdge.mimo.segment.current.read(start = 1.0, count = 1.0, decimation = 1.0, mimo = repcap.Mimo.Default, segment = repcap.Segment.Default) \n
		Return the values of the power vs time ramp traces (for 80+80 MHz, MIMO) , rising edge (REDGe) and falling edge (FEDGe) .
		The results of the current, average, maximum and minimum traces can be retrieved. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:param start: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param count: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param decimation: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: power_curr: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:PVTime:REDGe:MIMO{mimo_cmd_val}:SEGMent{segment_cmd_val}:CURRent? {param}'.rstrip(), suppressed)
		return response

	def fetch(self, start: float = None, count: float = None, decimation: float = None, mimo=repcap.Mimo.Default, segment=repcap.Segment.Default) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:PVTime:REDGe:MIMO<n>:SEGMent<seg>:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.powerVsTime.risingEdge.mimo.segment.current.fetch(start = 1.0, count = 1.0, decimation = 1.0, mimo = repcap.Mimo.Default, segment = repcap.Segment.Default) \n
		Return the values of the power vs time ramp traces (for 80+80 MHz, MIMO) , rising edge (REDGe) and falling edge (FEDGe) .
		The results of the current, average, maximum and minimum traces can be retrieved. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:param start: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param count: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param decimation: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: power_curr: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:PVTime:REDGe:MIMO{mimo_cmd_val}:SEGMent{segment_cmd_val}:CURRent? {param}'.rstrip(), suppressed)
		return response
