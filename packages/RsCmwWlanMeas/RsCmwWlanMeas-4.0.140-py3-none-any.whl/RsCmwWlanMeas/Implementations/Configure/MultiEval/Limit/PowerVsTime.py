from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTimeCls:
	"""PowerVsTime commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("powerVsTime", core, parent)

	def get_rising_edge(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:REDGe \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.powerVsTime.get_rising_edge() \n
		Sets the upper limit for the rise time (transmit power-on ramp) of a DSSS signal. \n
			:return: rising_limit: (float or boolean) numeric | ON | OFF Range: 0 s to 5E-6 s Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous limit values)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:REDGe?')
		return Conversions.str_to_float_or_bool(response)

	def set_rising_edge(self, rising_limit: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:REDGe \n
		Snippet: driver.configure.multiEval.limit.powerVsTime.set_rising_edge(rising_limit = 1.0) \n
		Sets the upper limit for the rise time (transmit power-on ramp) of a DSSS signal. \n
			:param rising_limit: (float or boolean) numeric | ON | OFF Range: 0 s to 5E-6 s Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(rising_limit)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:REDGe {param}')

	def get_falling_edge(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:FEDGe \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.powerVsTime.get_falling_edge() \n
		Sets the upper limit for the fall time (transmit power-down ramp) of a DSSS signal. \n
			:return: falling_limit: (float or boolean) numeric | ON | OFF Range: 0 s to 5E-6 s Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous limit values)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:FEDGe?')
		return Conversions.str_to_float_or_bool(response)

	def set_falling_edge(self, falling_limit: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:FEDGe \n
		Snippet: driver.configure.multiEval.limit.powerVsTime.set_falling_edge(falling_limit = 1.0) \n
		Sets the upper limit for the fall time (transmit power-down ramp) of a DSSS signal. \n
			:param falling_limit: (float or boolean) numeric | ON | OFF Range: 0 s to 5E-6 s Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(falling_limit)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:FEDGe {param}')

	def get_terror(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:TERRor \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.powerVsTime.get_terror() \n
		Sets the upper limit for timing error for OFDM standards. \n
			:return: timing_error: (float or boolean) numeric | ON | OFF Range: 0 s to 100E-6 s Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous limit values)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:TERRor?')
		return Conversions.str_to_float_or_bool(response)

	def set_terror(self, timing_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:TERRor \n
		Snippet: driver.configure.multiEval.limit.powerVsTime.set_terror(timing_error = 1.0) \n
		Sets the upper limit for timing error for OFDM standards. \n
			:param timing_error: (float or boolean) numeric | ON | OFF Range: 0 s to 100E-6 s Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(timing_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:TERRor {param}')

	def get_te_distribution(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:TEDistrib \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.powerVsTime.get_te_distribution() \n
		Configure the limit of timing error distribution for power vs time measurements for OFDM standards. Exceeding the limit
		has no impact on the stop 'On Limit Failure' condition or out-of-tolerance counter. \n
			:return: te_percentage: (float or boolean) numeric | ON | OFF Unit: % Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:TEDistrib?')
		return Conversions.str_to_float_or_bool(response)

	def set_te_distribution(self, te_percentage: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:TEDistrib \n
		Snippet: driver.configure.multiEval.limit.powerVsTime.set_te_distribution(te_percentage = 1.0) \n
		Configure the limit of timing error distribution for power vs time measurements for OFDM standards. Exceeding the limit
		has no impact on the stop 'On Limit Failure' condition or out-of-tolerance counter. \n
			:param te_percentage: (float or boolean) numeric | ON | OFF Unit: % Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(te_percentage)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:PVTime:TEDistrib {param}')
