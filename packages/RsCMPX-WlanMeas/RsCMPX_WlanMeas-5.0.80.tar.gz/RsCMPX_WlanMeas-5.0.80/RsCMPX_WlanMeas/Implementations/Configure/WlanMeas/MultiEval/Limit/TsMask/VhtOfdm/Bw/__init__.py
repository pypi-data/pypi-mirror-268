from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwCls:
	"""Bw commands group definition. 6 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: BandwidthE, default value after init: BandwidthE.Bw5"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bw", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_bandwidthE_get', 'repcap_bandwidthE_set', repcap.BandwidthE.Bw5)

	def repcap_bandwidthE_set(self, bandwidthE: repcap.BandwidthE) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BandwidthE.Default
		Default value after init: BandwidthE.Bw5"""
		self._cmd_group.set_repcap_enum_value(bandwidthE)

	def repcap_bandwidthE_get(self) -> repcap.BandwidthE:
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
	def y(self):
		"""y commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_y'):
			from .Y import YCls
			self._y = YCls(self._core, self._cmd_group)
		return self._y

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
