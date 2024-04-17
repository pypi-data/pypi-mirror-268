from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CompensationCls:
	"""Compensation commands group definition. 8 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("compensation", core, parent)

	@property
	def tracking(self):
		"""tracking commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_tracking'):
			from .Tracking import TrackingCls
			self._tracking = TrackingCls(self._core, self._cmd_group)
		return self._tracking

	@property
	def efTaps(self):
		"""efTaps commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_efTaps'):
			from .EfTaps import EfTapsCls
			self._efTaps = EfTapsCls(self._core, self._cmd_group)
		return self._efTaps

	@property
	def skipSymbols(self):
		"""skipSymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_skipSymbols'):
			from .SkipSymbols import SkipSymbolsCls
			self._skipSymbols = SkipSymbolsCls(self._core, self._cmd_group)
		return self._skipSymbols

	# noinspection PyTypeChecker
	def get_cestimation(self) -> enums.ChannelEstimation:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:CESTimation \n
		Snippet: value: enums.ChannelEstimation = driver.configure.multiEval.compensation.get_cestimation() \n
		Specifies whether the channel estimation is done in payload or preamble. \n
			:return: channel_estimation: PAYLoad | PREamble PAYLoad: Channel estimation in payload and preamble PREamble: Channel estimation in preamble only *RST: PRE
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:CESTimation?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelEstimation)

	def set_cestimation(self, channel_estimation: enums.ChannelEstimation) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:CESTimation \n
		Snippet: driver.configure.multiEval.compensation.set_cestimation(channel_estimation = enums.ChannelEstimation.PAYLoad) \n
		Specifies whether the channel estimation is done in payload or preamble. \n
			:param channel_estimation: PAYLoad | PREamble PAYLoad: Channel estimation in payload and preamble PREamble: Channel estimation in preamble only *RST: PRE
		"""
		param = Conversions.enum_scalar_to_str(channel_estimation, enums.ChannelEstimation)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:CESTimation {param}')

	def get_smoothing(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:SMOothing \n
		Snippet: value: bool = driver.configure.multiEval.compensation.get_smoothing() \n
		No command help available \n
			:return: smoothing: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:SMOothing?')
		return Conversions.str_to_bool(response)

	def set_smoothing(self, smoothing: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:SMOothing \n
		Snippet: driver.configure.multiEval.compensation.set_smoothing(smoothing = False) \n
		No command help available \n
			:param smoothing: No help available
		"""
		param = Conversions.bool_to_str(smoothing)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:SMOothing {param}')

	def get_ncancel(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:NCANcel \n
		Snippet: value: bool = driver.configure.multiEval.compensation.get_ncancel() \n
		No command help available \n
			:return: noise_cancel: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:NCANcel?')
		return Conversions.str_to_bool(response)

	def set_ncancel(self, noise_cancel: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:NCANcel \n
		Snippet: driver.configure.multiEval.compensation.set_ncancel(noise_cancel = False) \n
		No command help available \n
			:param noise_cancel: No help available
		"""
		param = Conversions.bool_to_str(noise_cancel)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:NCANcel {param}')

	def clone(self) -> 'CompensationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CompensationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
