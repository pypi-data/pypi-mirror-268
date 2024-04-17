from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 190 total commands, 9 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def listPy(self):
		"""listPy commands group. 4 Sub-classes, 12 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	@property
	def compensation(self):
		"""compensation commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_compensation'):
			from .Compensation import CompensationCls
			self._compensation = CompensationCls(self._core, self._cmd_group)
		return self._compensation

	@property
	def demod(self):
		"""demod commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_demod'):
			from .Demod import DemodCls
			self._demod = DemodCls(self._core, self._cmd_group)
		return self._demod

	@property
	def tsMask(self):
		"""tsMask commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_tsMask'):
			from .TsMask import TsMaskCls
			self._tsMask = TsMaskCls(self._core, self._cmd_group)
		return self._tsMask

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 10 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def spectrFlatness(self):
		"""spectrFlatness commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spectrFlatness'):
			from .SpectrFlatness import SpectrFlatnessCls
			self._spectrFlatness = SpectrFlatnessCls(self._core, self._cmd_group)
		return self._spectrFlatness

	@property
	def limit(self):
		"""limit commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: value: float = driver.configure.multiEval.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout.
		The measurement of a DSSS signal with low data rate and large payload sizes can take up to 40 s. Set the measurement
		timeout to an adequate value, e.g. to 60 s. \n
			:return: tcd_timeout: numeric Unit: s
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: driver.configure.multiEval.set_timeout(tcd_timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout.
		The measurement of a DSSS signal with low data rate and large payload sizes can take up to 40 s. Set the measurement
		timeout to an adequate value, e.g. to 60 s. \n
			:param tcd_timeout: numeric Unit: s
		"""
		param = Conversions.decimal_value_to_str(tcd_timeout)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:TOUT {param}')

	# noinspection PyTypeChecker
	def get_cfo_estimate(self) -> enums.CfoEstimation:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:CFOestimate \n
		Snippet: value: enums.CfoEstimation = driver.configure.multiEval.get_cfo_estimate() \n
		No command help available \n
			:return: cfo_est: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:CFOestimate?')
		return Conversions.str_to_scalar_enum(response, enums.CfoEstimation)

	def set_cfo_estimate(self, cfo_est: enums.CfoEstimation) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:CFOestimate \n
		Snippet: driver.configure.multiEval.set_cfo_estimate(cfo_est = enums.CfoEstimation.FULLpacket) \n
		No command help available \n
			:param cfo_est: No help available
		"""
		param = Conversions.enum_scalar_to_str(cfo_est, enums.CfoEstimation)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:CFOestimate {param}')

	# noinspection PyTypeChecker
	def get_emethod(self) -> enums.EvmMethod:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:EMEThod \n
		Snippet: value: enums.EvmMethod = driver.configure.multiEval.get_emethod() \n
		This parameter is relevant for 802.11b signals only. It selects the EVM measurement method - according to standard IEEE
		Std 802.11-2007, IEEE Std 802.11b-1999, or according to standard IEEE Std 802.11-2016. \n
			:return: evm_method_11_b: ST2007 | ST1999 | ST2016
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:EMEThod?')
		return Conversions.str_to_scalar_enum(response, enums.EvmMethod)

	def set_emethod(self, evm_method_11_b: enums.EvmMethod) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:EMEThod \n
		Snippet: driver.configure.multiEval.set_emethod(evm_method_11_b = enums.EvmMethod.ST1999) \n
		This parameter is relevant for 802.11b signals only. It selects the EVM measurement method - according to standard IEEE
		Std 802.11-2007, IEEE Std 802.11b-1999, or according to standard IEEE Std 802.11-2016. \n
			:param evm_method_11_b: ST2007 | ST1999 | ST2016
		"""
		param = Conversions.enum_scalar_to_str(evm_method_11_b, enums.EvmMethod)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:EMEThod {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.multiEval.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE | SLFail NONE: Continue measurement irrespective of the limit check. SLFail: Stop measurement on limit failure.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: driver.configure.multiEval.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE | SLFail NONE: Continue measurement irrespective of the limit check. SLFail: Stop measurement on limit failure.
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:SCONdition {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.multiEval.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: driver.configure.multiEval.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:REPetition {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: value: bool = driver.configure.multiEval.get_mo_exception() \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF | ON OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: driver.configure.multiEval.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF | ON OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:MOEXception {param}')

	# noinspection PyTypeChecker
	def get_smode(self) -> enums.SynchroMode:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SMODe \n
		Snippet: value: enums.SynchroMode = driver.configure.multiEval.get_smode() \n
			INTRO_CMD_HELP: Sets the synchronization mode: \n
			- Normal: synchronization according to preamble detection
			- Tolerant: synchronization with the second part of preamble when the first part cannot be detected \n
			:return: synchronization_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:SMODe?')
		return Conversions.str_to_scalar_enum(response, enums.SynchroMode)

	def set_smode(self, synchronization_mode: enums.SynchroMode) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SMODe \n
		Snippet: driver.configure.multiEval.set_smode(synchronization_mode = enums.SynchroMode.NORMal) \n
			INTRO_CMD_HELP: Sets the synchronization mode: \n
			- Normal: synchronization according to preamble detection
			- Tolerant: synchronization with the second part of preamble when the first part cannot be detected \n
			:param synchronization_mode: NORMal | TOLerant
		"""
		param = Conversions.enum_scalar_to_str(synchronization_mode, enums.SynchroMode)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:SMODe {param}')

	def clone(self) -> 'MultiEvalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEvalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
