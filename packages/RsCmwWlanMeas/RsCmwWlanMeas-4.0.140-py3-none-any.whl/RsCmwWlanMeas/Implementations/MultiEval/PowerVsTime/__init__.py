from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTimeCls:
	"""PowerVsTime commands group definition. 54 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("powerVsTime", core, parent)

	@property
	def terror(self):
		"""terror commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_terror'):
			from .Terror import TerrorCls
			self._terror = TerrorCls(self._core, self._cmd_group)
		return self._terror

	@property
	def risingEdge(self):
		"""risingEdge commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_risingEdge'):
			from .RisingEdge import RisingEdgeCls
			self._risingEdge = RisingEdgeCls(self._core, self._cmd_group)
		return self._risingEdge

	@property
	def fallingEdge(self):
		"""fallingEdge commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallingEdge'):
			from .FallingEdge import FallingEdgeCls
			self._fallingEdge = FallingEdgeCls(self._core, self._cmd_group)
		return self._fallingEdge

	@property
	def teDistribution(self):
		"""teDistribution commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_teDistribution'):
			from .TeDistribution import TeDistributionCls
			self._teDistribution = TeDistributionCls(self._core, self._cmd_group)
		return self._teDistribution

	@property
	def mimo(self):
		"""mimo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	def clone(self) -> 'PowerVsTimeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerVsTimeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
