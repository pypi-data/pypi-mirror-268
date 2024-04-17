from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsMaskCls:
	"""TsMask commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsMask", core, parent)

	def get_afft_num(self) -> int:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:AFFTnum \n
		Snippet: value: int = driver.configure.multiEval.tsMask.get_afft_num() \n
		Specifies the number of FFT operations per burst. \n
			:return: aver_fft_num: numeric Range: 1 to 16
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:AFFTnum?')
		return Conversions.str_to_int(response)

	def set_afft_num(self, aver_fft_num: int) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:AFFTnum \n
		Snippet: driver.configure.multiEval.tsMask.set_afft_num(aver_fft_num = 1) \n
		Specifies the number of FFT operations per burst. \n
			:param aver_fft_num: numeric Range: 1 to 16
		"""
		param = Conversions.decimal_value_to_str(aver_fft_num)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:AFFTnum {param}')

	def get_tro_time(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:TROTime \n
		Snippet: value: float = driver.configure.multiEval.tsMask.get_tro_time() \n
		Specifies the trigger offset between trigger event and FFT operation. \n
			:return: trigger_off_time: numeric Range: 0 s to 0.1E-3 s
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:TROTime?')
		return Conversions.str_to_float(response)

	def set_tro_time(self, trigger_off_time: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:TROTime \n
		Snippet: driver.configure.multiEval.tsMask.set_tro_time(trigger_off_time = 1.0) \n
		Specifies the trigger offset between trigger event and FFT operation. \n
			:param trigger_off_time: numeric Range: 0 s to 0.1E-3 s
		"""
		param = Conversions.decimal_value_to_str(trigger_off_time)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:TROTime {param}')

	def get_obw_percent(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBWPercent \n
		Snippet: value: float or bool = driver.configure.multiEval.tsMask.get_obw_percent() \n
		Enables/disables OBW measurement and sets the OBW percentage. \n
			:return: obw_power: (float or boolean) numeric | ON | OFF Range: 50 % to 100 % Additional values: ON | OFF (disables | enables OBW measurement)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBWPercent?')
		return Conversions.str_to_float_or_bool(response)

	def set_obw_percent(self, obw_power: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBWPercent \n
		Snippet: driver.configure.multiEval.tsMask.set_obw_percent(obw_power = 1.0) \n
		Enables/disables OBW measurement and sets the OBW percentage. \n
			:param obw_power: (float or boolean) numeric | ON | OFF Range: 50 % to 100 % Additional values: ON | OFF (disables | enables OBW measurement)
		"""
		param = Conversions.decimal_or_bool_value_to_str(obw_power)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBWPercent {param}')

	def get_mselection(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:MSELection \n
		Snippet: value: float = driver.configure.multiEval.tsMask.get_mselection() \n
		Selects the spectrum limit mask to be applied to 802.11p signals. See 'Transmit spectrum mask OFDM, by regulation' \n
			:return: mask_selection: IEEE | ETSI | ARIB IEEE: Relative spectral density limits, IEEE 802.11 ETSI: Absolute emission limits, ETSI EN 302 571 V1.1.1 (2008-09) ARIB: Absolute emission limits, ARIB STD-T109, only for 10 MHz bandwidth
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:MSELection?')
		return Conversions.str_to_float(response)

	def set_mselection(self, mask_selection: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:MSELection \n
		Snippet: driver.configure.multiEval.tsMask.set_mselection(mask_selection = 1.0) \n
		Selects the spectrum limit mask to be applied to 802.11p signals. See 'Transmit spectrum mask OFDM, by regulation' \n
			:param mask_selection: IEEE | ETSI | ARIB IEEE: Relative spectral density limits, IEEE 802.11 ETSI: Absolute emission limits, ETSI EN 302 571 V1.1.1 (2008-09) ARIB: Absolute emission limits, ARIB STD-T109, only for 10 MHz bandwidth
		"""
		param = Conversions.decimal_value_to_str(mask_selection)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:MSELection {param}')

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.DisplayMode:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:DMODe \n
		Snippet: value: enums.DisplayMode = driver.configure.multiEval.tsMask.get_dmode() \n
		Selects the display mode of 'Spectrum Flatness' and 'Transmit Spectrum Mask' results to switch between relative and
		absolute result values (dB vs dBm) . \n
			:return: disp_mode: RELative | ABSolute
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.DisplayMode)

	def set_dmode(self, disp_mode: enums.DisplayMode) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:DMODe \n
		Snippet: driver.configure.multiEval.tsMask.set_dmode(disp_mode = enums.DisplayMode.ABSolute) \n
		Selects the display mode of 'Spectrum Flatness' and 'Transmit Spectrum Mask' results to switch between relative and
		absolute result values (dB vs dBm) . \n
			:param disp_mode: RELative | ABSolute
		"""
		param = Conversions.enum_scalar_to_str(disp_mode, enums.DisplayMode)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:TSMask:DMODe {param}')
