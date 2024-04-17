from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 3 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: Mimo, default value after init: Mimo.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_mimo_get', 'repcap_mimo_set', repcap.Mimo.Nr1)

	def repcap_mimo_set(self, mimo: repcap.Mimo) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Mimo.Default
		Default value after init: Mimo.Nr1"""
		self._cmd_group.set_repcap_enum_value(mimo)

	def repcap_mimo_get(self) -> repcap.Mimo:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def teDistribution(self):
		"""teDistribution commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_teDistribution'):
			from .TeDistribution import TeDistributionCls
			self._teDistribution = TeDistributionCls(self._core, self._cmd_group)
		return self._teDistribution

	def clone(self) -> 'MimoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MimoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
