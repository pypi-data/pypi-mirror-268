from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SegmentCls:
	"""Segment commands group definition. 18 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: SegmentB, default value after init: SegmentB.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segment", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_segmentB_get', 'repcap_segmentB_set', repcap.SegmentB.Nr1)

	def repcap_segmentB_set(self, segmentB: repcap.SegmentB) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SegmentB.Default
		Default value after init: SegmentB.Nr1"""
		self._cmd_group.set_repcap_enum_value(segmentB)

	def repcap_segmentB_get(self) -> repcap.SegmentB:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def modulation(self):
		"""modulation commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def tsMask(self):
		"""tsMask commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsMask'):
			from .TsMask import TsMaskCls
			self._tsMask = TsMaskCls(self._core, self._cmd_group)
		return self._tsMask

	def clone(self) -> 'SegmentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SegmentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
