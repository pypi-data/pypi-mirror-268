from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 42 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	@property
	def dsss(self):
		"""dsss commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_dsss'):
			from .Dsss import DsssCls
			self._dsss = DsssCls(self._core, self._cmd_group)
		return self._dsss

	@property
	def lofdm(self):
		"""lofdm commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_lofdm'):
			from .Lofdm import LofdmCls
			self._lofdm = LofdmCls(self._core, self._cmd_group)
		return self._lofdm

	@property
	def pofdm(self):
		"""pofdm commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_pofdm'):
			from .Pofdm import PofdmCls
			self._pofdm = PofdmCls(self._core, self._cmd_group)
		return self._pofdm

	@property
	def htOfdm(self):
		"""htOfdm commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_htOfdm'):
			from .HtOfdm import HtOfdmCls
			self._htOfdm = HtOfdmCls(self._core, self._cmd_group)
		return self._htOfdm

	@property
	def vhtOfdm(self):
		"""vhtOfdm commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_vhtOfdm'):
			from .VhtOfdm import VhtOfdmCls
			self._vhtOfdm = VhtOfdmCls(self._core, self._cmd_group)
		return self._vhtOfdm

	@property
	def heOfdm(self):
		"""heOfdm commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_heOfdm'):
			from .HeOfdm import HeOfdmCls
			self._heOfdm = HeOfdmCls(self._core, self._cmd_group)
		return self._heOfdm

	@property
	def ehtOfdm(self):
		"""ehtOfdm commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_ehtOfdm'):
			from .EhtOfdm import EhtOfdmCls
			self._ehtOfdm = EhtOfdmCls(self._core, self._cmd_group)
		return self._ehtOfdm

	def clone(self) -> 'ModulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
