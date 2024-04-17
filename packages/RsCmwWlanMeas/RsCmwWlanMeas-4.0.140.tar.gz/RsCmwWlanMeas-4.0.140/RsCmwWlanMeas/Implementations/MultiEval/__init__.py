from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 1011 total commands, 11 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def modulation(self):
		"""modulation commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def listPy(self):
		"""listPy commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def ofdma(self):
		"""ofdma commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ofdma'):
			from .Ofdma import OfdmaCls
			self._ofdma = OfdmaCls(self._core, self._cmd_group)
		return self._ofdma

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def sinfo(self):
		"""sinfo commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_sinfo'):
			from .Sinfo import SinfoCls
			self._sinfo = SinfoCls(self._core, self._cmd_group)
		return self._sinfo

	@property
	def utError(self):
		"""utError commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_utError'):
			from .UtError import UtErrorCls
			self._utError = UtErrorCls(self._core, self._cmd_group)
		return self._utError

	@property
	def spectrFlatness(self):
		"""spectrFlatness commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrFlatness'):
			from .SpectrFlatness import SpectrFlatnessCls
			self._spectrFlatness = SpectrFlatnessCls(self._core, self._cmd_group)
		return self._spectrFlatness

	@property
	def tsMask(self):
		"""tsMask commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsMask'):
			from .TsMask import TsMaskCls
			self._tsMask = TsMaskCls(self._core, self._cmd_group)
		return self._tsMask

	@property
	def trace(self):
		"""trace commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:WLAN:MEASurement<Instance>:MEValuation \n
		Snippet: driver.multiEval.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:WLAN:MEASurement<Instance>:MEValuation', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:WLAN:MEASurement<Instance>:MEValuation \n
		Snippet: driver.multiEval.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:WLAN:MEASurement<Instance>:MEValuation', opc_timeout_ms)

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:WLAN:MEASurement<Instance>:MEValuation \n
		Snippet: driver.multiEval.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:WLAN:MEASurement<Instance>:MEValuation', opc_timeout_ms)

	def clone(self) -> 'MultiEvalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEvalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
