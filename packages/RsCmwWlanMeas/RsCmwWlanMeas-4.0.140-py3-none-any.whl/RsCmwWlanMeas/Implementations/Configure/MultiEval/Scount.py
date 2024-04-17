from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScountCls:
	"""Scount commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scount", core, parent)

	def get_ts_mask(self) -> int:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:TSMask \n
		Snippet: value: int = driver.configure.multiEval.scount.get_ts_mask() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: numeric Number of measurement intervals for the transmit spectrum mask measurement Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:TSMask?')
		return Conversions.str_to_int(response)

	def set_ts_mask(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:TSMask \n
		Snippet: driver.configure.multiEval.scount.set_ts_mask(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: numeric Number of measurement intervals for the transmit spectrum mask measurement Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:TSMask {param}')

	def get_power_vs_time(self) -> int:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:PVTime \n
		Snippet: value: int = driver.configure.multiEval.scount.get_power_vs_time() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: numeric Number of measurement intervals for the power vs time measurement Range: 1 to 2000
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:PVTime?')
		return Conversions.str_to_int(response)

	def set_power_vs_time(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:PVTime \n
		Snippet: driver.configure.multiEval.scount.set_power_vs_time(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: numeric Number of measurement intervals for the power vs time measurement Range: 1 to 2000
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:PVTime {param}')

	def get_modulation(self) -> int:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:MODulation \n
		Snippet: value: int = driver.configure.multiEval.scount.get_modulation() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: numeric Number of measurement intervals for modulation measurements Range: 1 to 2000
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:MODulation?')
		return Conversions.str_to_int(response)

	def set_modulation(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:MODulation \n
		Snippet: driver.configure.multiEval.scount.set_modulation(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: numeric Number of measurement intervals for modulation measurements Range: 1 to 2000
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCOunt:MODulation {param}')
