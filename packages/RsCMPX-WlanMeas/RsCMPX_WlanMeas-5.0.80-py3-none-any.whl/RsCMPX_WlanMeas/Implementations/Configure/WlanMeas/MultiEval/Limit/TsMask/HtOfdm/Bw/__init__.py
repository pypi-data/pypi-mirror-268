from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwCls:
	"""Bw commands group definition. 6 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: BandwidthC, default value after init: BandwidthC.Bw5"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bw", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_bandwidthC_get', 'repcap_bandwidthC_set', repcap.BandwidthC.Bw5)

	def repcap_bandwidthC_set(self, bandwidthC: repcap.BandwidthC) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BandwidthC.Default
		Default value after init: BandwidthC.Bw5"""
		self._cmd_group.set_repcap_enum_value(bandwidthC)

	def repcap_bandwidthC_get(self) -> repcap.BandwidthC:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def band(self):
		"""band commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_band'):
			from .Band import BandCls
			self._band = BandCls(self._core, self._cmd_group)
		return self._band

	@property
	def absLimit(self):
		"""absLimit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absLimit'):
			from .AbsLimit import AbsLimitCls
			self._absLimit = AbsLimitCls(self._core, self._cmd_group)
		return self._absLimit

	def clone(self) -> 'BwCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BwCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
