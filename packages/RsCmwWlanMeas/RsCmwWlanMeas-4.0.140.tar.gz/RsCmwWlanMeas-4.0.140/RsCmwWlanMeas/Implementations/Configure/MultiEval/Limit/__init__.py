from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 120 total commands, 4 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def spectrFlatness(self):
		"""spectrFlatness commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrFlatness'):
			from .SpectrFlatness import SpectrFlatnessCls
			self._spectrFlatness = SpectrFlatnessCls(self._core, self._cmd_group)
		return self._spectrFlatness

	@property
	def tsMask(self):
		"""tsMask commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsMask'):
			from .TsMask import TsMaskCls
			self._tsMask = TsMaskCls(self._core, self._cmd_group)
		return self._tsMask

	@property
	def modulation(self):
		"""modulation commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	# noinspection PyTypeChecker
	def get_ute_power(self) -> enums.LowHigh:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:UTEPower \n
		Snippet: value: enums.LowHigh = driver.configure.multiEval.limit.get_ute_power() \n
		No command help available \n
			:return: ute_power: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:UTEPower?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)

	def set_ute_power(self, ute_power: enums.LowHigh) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:UTEPower \n
		Snippet: driver.configure.multiEval.limit.set_ute_power(ute_power = enums.LowHigh.HIGH) \n
		No command help available \n
			:param ute_power: No help available
		"""
		param = Conversions.enum_scalar_to_str(ute_power, enums.LowHigh)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:UTEPower {param}')

	def get_ut_error(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:UTERror \n
		Snippet: value: bool = driver.configure.multiEval.limit.get_ut_error() \n
		No command help available \n
			:return: ute_limits: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:UTERror?')
		return Conversions.str_to_bool(response)

	def set_ut_error(self, ute_limits: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:UTERror \n
		Snippet: driver.configure.multiEval.limit.set_ut_error(ute_limits = False) \n
		No command help available \n
			:param ute_limits: No help available
		"""
		param = Conversions.bool_to_str(ute_limits)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:UTERror {param}')

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
