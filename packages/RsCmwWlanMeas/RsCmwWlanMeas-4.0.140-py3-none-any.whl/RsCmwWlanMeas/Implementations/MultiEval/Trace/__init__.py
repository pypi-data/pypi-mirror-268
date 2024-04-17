from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TraceCls:
	"""Trace commands group definition. 360 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	@property
	def tsMask(self):
		"""tsMask commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsMask'):
			from .TsMask import TsMaskCls
			self._tsMask = TsMaskCls(self._core, self._cmd_group)
		return self._tsMask

	@property
	def cfError(self):
		"""cfError commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cfError'):
			from .CfError import CfErrorCls
			self._cfError = CfErrorCls(self._core, self._cmd_group)
		return self._cfError

	@property
	def terror(self):
		"""terror commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_terror'):
			from .Terror import TerrorCls
			self._terror = TerrorCls(self._core, self._cmd_group)
		return self._terror

	@property
	def spectrFlatness(self):
		"""spectrFlatness commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrFlatness'):
			from .SpectrFlatness import SpectrFlatnessCls
			self._spectrFlatness = SpectrFlatnessCls(self._core, self._cmd_group)
		return self._spectrFlatness

	@property
	def iqConstant(self):
		"""iqConstant commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqConstant'):
			from .IqConstant import IqConstantCls
			self._iqConstant = IqConstantCls(self._core, self._cmd_group)
		return self._iqConstant

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .EvMagnitude import EvMagnitudeCls
			self._evMagnitude = EvMagnitudeCls(self._core, self._cmd_group)
		return self._evMagnitude

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	def clone(self) -> 'TraceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TraceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
