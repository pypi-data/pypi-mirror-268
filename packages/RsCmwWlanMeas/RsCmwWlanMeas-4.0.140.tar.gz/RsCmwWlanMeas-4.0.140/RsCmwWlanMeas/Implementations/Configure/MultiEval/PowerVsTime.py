from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTimeCls:
	"""PowerVsTime commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("powerVsTime", core, parent)

	# noinspection PyTypeChecker
	def get_rpower(self) -> enums.RefPower:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:PVTime:RPOWer \n
		Snippet: value: enums.RefPower = driver.configure.multiEval.powerVsTime.get_rpower() \n
		Sets the reference power to the maximum power or to the mean power of the burst. In DSSS, the thresholds for rising and
		falling edge results are defined as percentage values of the reference power. \n
			:return: ref_power: MAXimum | MEAN
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:RPOWer?')
		return Conversions.str_to_scalar_enum(response, enums.RefPower)

	def set_rpower(self, ref_power: enums.RefPower) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:PVTime:RPOWer \n
		Snippet: driver.configure.multiEval.powerVsTime.set_rpower(ref_power = enums.RefPower.MAXimum) \n
		Sets the reference power to the maximum power or to the mean power of the burst. In DSSS, the thresholds for rising and
		falling edge results are defined as percentage values of the reference power. \n
			:param ref_power: MAXimum | MEAN
		"""
		param = Conversions.enum_scalar_to_str(ref_power, enums.RefPower)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:RPOWer {param}')

	def get_alength(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:PVTime:ALENgth \n
		Snippet: value: float = driver.configure.multiEval.powerVsTime.get_alength() \n
		Sets the length of the moving average filter, which smoothes the power trace and thus eliminates the modulation. \n
			:return: avg_lenth: numeric Range: 1 to 199
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:ALENgth?')
		return Conversions.str_to_float(response)

	def set_alength(self, avg_lenth: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:PVTime:ALENgth \n
		Snippet: driver.configure.multiEval.powerVsTime.set_alength(avg_lenth = 1.0) \n
		Sets the length of the moving average filter, which smoothes the power trace and thus eliminates the modulation. \n
			:param avg_lenth: numeric Range: 1 to 199
		"""
		param = Conversions.decimal_value_to_str(avg_lenth)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:ALENgth {param}')

	def get_rising_edge(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:REDGe \n
		Snippet: value: bool = driver.configure.multiEval.powerVsTime.get_rising_edge() \n
		Enables or disables the evaluation of rising edge results (transmit power-on ramp) in the power vs time view for DSSS
		signals. \n
			:return: rising: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:REDGe?')
		return Conversions.str_to_bool(response)

	def set_rising_edge(self, rising: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:REDGe \n
		Snippet: driver.configure.multiEval.powerVsTime.set_rising_edge(rising = False) \n
		Enables or disables the evaluation of rising edge results (transmit power-on ramp) in the power vs time view for DSSS
		signals. \n
			:param rising: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(rising)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:REDGe {param}')

	def get_falling_edge(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:FEDGe \n
		Snippet: value: bool = driver.configure.multiEval.powerVsTime.get_falling_edge() \n
		Enables or disables the evaluation of falling edge results (transmit power-down ramp) in the power vs time view for DSSS
		signals. \n
			:return: fall: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:FEDGe?')
		return Conversions.str_to_bool(response)

	def set_falling_edge(self, fall: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:FEDGe \n
		Snippet: driver.configure.multiEval.powerVsTime.set_falling_edge(fall = False) \n
		Enables or disables the evaluation of falling edge results (transmit power-down ramp) in the power vs time view for DSSS
		signals. \n
			:param fall: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(fall)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:FEDGe {param}')

	def get_burst(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:BURSt \n
		Snippet: value: bool = driver.configure.multiEval.powerVsTime.get_burst() \n
		Enables or disables the evaluation of burst power results in the power vs time view. \n
			:return: burst: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:BURSt?')
		return Conversions.str_to_bool(response)

	def set_burst(self, burst: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:BURSt \n
		Snippet: driver.configure.multiEval.powerVsTime.set_burst(burst = False) \n
		Enables or disables the evaluation of burst power results in the power vs time view. \n
			:param burst: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(burst)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:PVTime:BURSt {param}')
