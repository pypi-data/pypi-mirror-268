from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def read(self, start: float = None, count: float = None, decimation: float = None) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:ACARrier:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.trace.spectrFlatness.acarrier.maximum.read(start = 1.0, count = 1.0, decimation = 1.0) \n
		Return the results over all carriers (complete FFTSize) of the spectrum flatness traces for OFDM and OFDMA SISO signals.
		The results of the current, average, minimum and maximum traces can be retrieved. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:param start: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param count: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param decimation: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:return: sflat_all_carr_max: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:ACARrier:MAXimum? {param}'.rstrip(), suppressed)
		return response

	def fetch(self, start: float = None, count: float = None, decimation: float = None) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:ACARrier:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.trace.spectrFlatness.acarrier.maximum.fetch(start = 1.0, count = 1.0, decimation = 1.0) \n
		Return the results over all carriers (complete FFTSize) of the spectrum flatness traces for OFDM and OFDMA SISO signals.
		The results of the current, average, minimum and maximum traces can be retrieved. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:param start: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param count: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param decimation: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:return: sflat_all_carr_max: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:ACARrier:MAXimum? {param}'.rstrip(), suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self, start: float = None, count: float = None, decimation: float = None) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:ACARrier:MAXimum \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.trace.spectrFlatness.acarrier.maximum.calculate(start = 1.0, count = 1.0, decimation = 1.0) \n
		Return the results over all carriers (complete FFTSize) of the spectrum flatness traces for OFDM and OFDMA SISO signals.
		The results of the current, average, minimum and maximum traces can be retrieved. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:param start: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param count: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:param decimation: numeric For the optional query parameters start, count and decimation, see 'Trace sub-arrays'.
			:return: sflat_all_carr_max: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:ACARrier:MAXimum? {param}'.rstrip(), suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
