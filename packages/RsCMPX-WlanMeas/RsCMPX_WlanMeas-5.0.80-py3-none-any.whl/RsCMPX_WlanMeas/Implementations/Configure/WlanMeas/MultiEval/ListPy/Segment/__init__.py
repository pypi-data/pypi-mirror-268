from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SegmentCls:
	"""Segment commands group definition. 13 total commands, 13 Subgroups, 0 group commands
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
	def setup(self):
		"""setup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_setup'):
			from .Setup import SetupCls
			self._setup = SetupCls(self._core, self._cmd_group)
		return self._setup

	@property
	def stime(self):
		"""stime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stime'):
			from .Stime import StimeCls
			self._stime = StimeCls(self._core, self._cmd_group)
		return self._stime

	@property
	def mtime(self):
		"""mtime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtime'):
			from .Mtime import MtimeCls
			self._mtime = MtimeCls(self._core, self._cmd_group)
		return self._mtime

	@property
	def moffset(self):
		"""moffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_moffset'):
			from .Moffset import MoffsetCls
			self._moffset = MoffsetCls(self._core, self._cmd_group)
		return self._moffset

	@property
	def envelopePower(self):
		"""envelopePower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_envelopePower'):
			from .EnvelopePower import EnvelopePowerCls
			self._envelopePower = EnvelopePowerCls(self._core, self._cmd_group)
		return self._envelopePower

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def standard(self):
		"""standard commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standard'):
			from .Standard import StandardCls
			self._standard = StandardCls(self._core, self._cmd_group)
		return self._standard

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def btype(self):
		"""btype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_btype'):
			from .Btype import BtypeCls
			self._btype = BtypeCls(self._core, self._cmd_group)
		return self._btype

	@property
	def rtrigger(self):
		"""rtrigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtrigger'):
			from .Rtrigger import RtriggerCls
			self._rtrigger = RtriggerCls(self._core, self._cmd_group)
		return self._rtrigger

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .SingleCmw import SingleCmwCls
			self._singleCmw = SingleCmwCls(self._core, self._cmd_group)
		return self._singleCmw

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	def clone(self) -> 'SegmentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SegmentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
