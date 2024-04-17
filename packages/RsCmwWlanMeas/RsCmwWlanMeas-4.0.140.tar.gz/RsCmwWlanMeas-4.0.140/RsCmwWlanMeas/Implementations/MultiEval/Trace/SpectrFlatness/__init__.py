from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrFlatnessCls:
	"""SpectrFlatness commands group definition. 104 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrFlatness", core, parent)

	@property
	def acarrier(self):
		"""acarrier commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_acarrier'):
			from .Acarrier import AcarrierCls
			self._acarrier = AcarrierCls(self._core, self._cmd_group)
		return self._acarrier

	@property
	def mimo(self):
		"""mimo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	@property
	def ofdm(self):
		"""ofdm commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ofdm'):
			from .Ofdm import OfdmCls
			self._ofdm = OfdmCls(self._core, self._cmd_group)
		return self._ofdm

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import CurrentCls
			self._current = CurrentCls(self._core, self._cmd_group)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	@property
	def segment(self):
		"""segment commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import SegmentCls
			self._segment = SegmentCls(self._core, self._cmd_group)
		return self._segment

	@property
	def acsiso(self):
		"""acsiso commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_acsiso'):
			from .Acsiso import AcsisoCls
			self._acsiso = AcsisoCls(self._core, self._cmd_group)
		return self._acsiso

	def clone(self) -> 'SpectrFlatnessCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpectrFlatnessCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
