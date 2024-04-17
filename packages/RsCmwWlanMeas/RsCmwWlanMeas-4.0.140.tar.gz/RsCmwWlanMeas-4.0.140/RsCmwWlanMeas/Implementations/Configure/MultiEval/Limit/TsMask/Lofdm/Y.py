from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class YCls:
	"""Y commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def get_a(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:A \n
		Snippet: value: float = driver.configure.multiEval.limit.tsMask.lofdm.y.get_a() \n
		Defines the Y-value for point A of the spectrum mask (802.11a/g, OFDM) . See also 'Transmit spectrum mask OFDM, default
		masks'. \n
			:return: tsm_lim_yrel_lev_a: numeric Range: -90 dB to 10 dB
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:A?')
		return Conversions.str_to_float(response)

	def set_a(self, tsm_lim_yrel_lev_a: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:A \n
		Snippet: driver.configure.multiEval.limit.tsMask.lofdm.y.set_a(tsm_lim_yrel_lev_a = 1.0) \n
		Defines the Y-value for point A of the spectrum mask (802.11a/g, OFDM) . See also 'Transmit spectrum mask OFDM, default
		masks'. \n
			:param tsm_lim_yrel_lev_a: numeric Range: -90 dB to 10 dB
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_a)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:A {param}')

	def get_b(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:B \n
		Snippet: value: float = driver.configure.multiEval.limit.tsMask.lofdm.y.get_b() \n
		Defines the Y-value for point B of the spectrum mask (802.11a/g, OFDM) . See also 'Transmit spectrum mask OFDM, default
		masks'. \n
			:return: tsm_lim_yrel_lev_b: numeric Range: -90 dB to 10 dB
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:B?')
		return Conversions.str_to_float(response)

	def set_b(self, tsm_lim_yrel_lev_b: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:B \n
		Snippet: driver.configure.multiEval.limit.tsMask.lofdm.y.set_b(tsm_lim_yrel_lev_b = 1.0) \n
		Defines the Y-value for point B of the spectrum mask (802.11a/g, OFDM) . See also 'Transmit spectrum mask OFDM, default
		masks'. \n
			:param tsm_lim_yrel_lev_b: numeric Range: -90 dB to 10 dB
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_b)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:B {param}')

	def get_c(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:C \n
		Snippet: value: float = driver.configure.multiEval.limit.tsMask.lofdm.y.get_c() \n
		Defines the Y-value for point C of the spectrum mask (802.11a/g, OFDM) . See also 'Transmit spectrum mask OFDM, default
		masks'. \n
			:return: tsm_lim_yrel_lev_c: numeric Range: -90 dB to 10 dB
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:C?')
		return Conversions.str_to_float(response)

	def set_c(self, tsm_lim_yrel_lev_c: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:C \n
		Snippet: driver.configure.multiEval.limit.tsMask.lofdm.y.set_c(tsm_lim_yrel_lev_c = 1.0) \n
		Defines the Y-value for point C of the spectrum mask (802.11a/g, OFDM) . See also 'Transmit spectrum mask OFDM, default
		masks'. \n
			:param tsm_lim_yrel_lev_c: numeric Range: -90 dB to 10 dB
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_c)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:C {param}')

	def get_d(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:D \n
		Snippet: value: float = driver.configure.multiEval.limit.tsMask.lofdm.y.get_d() \n
		Defines the Y-value for point D of the spectrum mask (802.11a/g, OFDM) . See also 'Transmit spectrum mask OFDM, default
		masks'. \n
			:return: tsm_lim_yrel_lev_d: numeric Range: -90 dB to 10 dB
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:D?')
		return Conversions.str_to_float(response)

	def set_d(self, tsm_lim_yrel_lev_d: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:D \n
		Snippet: driver.configure.multiEval.limit.tsMask.lofdm.y.set_d(tsm_lim_yrel_lev_d = 1.0) \n
		Defines the Y-value for point D of the spectrum mask (802.11a/g, OFDM) . See also 'Transmit spectrum mask OFDM, default
		masks'. \n
			:param tsm_lim_yrel_lev_d: numeric Range: -90 dB to 10 dB
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_d)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:Y:D {param}')
