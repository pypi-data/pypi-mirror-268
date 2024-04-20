from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UfieldCls:
	"""Ufield commands group definition. 10 total commands, 10 Subgroups, 0 group commands
	Repeated Capability: UserIx, default value after init: UserIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ufield", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_userIx_get', 'repcap_userIx_set', repcap.UserIx.Nr1)

	def repcap_userIx_set(self, userIx: repcap.UserIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UserIx.Default
		Default value after init: UserIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(userIx)

	def repcap_userIx_get(self) -> repcap.UserIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def staId(self):
		"""staId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_staId'):
			from .StaId import StaIdCls
			self._staId = StaIdCls(self._core, self._cmd_group)
		return self._staId

	@property
	def nsts(self):
		"""nsts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsts'):
			from .Nsts import NstsCls
			self._nsts = NstsCls(self._core, self._cmd_group)
		return self._nsts

	@property
	def txBeamforming(self):
		"""txBeamforming commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txBeamforming'):
			from .TxBeamforming import TxBeamformingCls
			self._txBeamforming = TxBeamformingCls(self._core, self._cmd_group)
		return self._txBeamforming

	@property
	def spaConfig(self):
		"""spaConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spaConfig'):
			from .SpaConfig import SpaConfigCls
			self._spaConfig = SpaConfigCls(self._core, self._cmd_group)
		return self._spaConfig

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import McsCls
			self._mcs = McsCls(self._core, self._cmd_group)
		return self._mcs

	@property
	def dcm(self):
		"""dcm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcm'):
			from .Dcm import DcmCls
			self._dcm = DcmCls(self._core, self._cmd_group)
		return self._dcm

	@property
	def reserved(self):
		"""reserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reserved'):
			from .Reserved import ReservedCls
			self._reserved = ReservedCls(self._core, self._cmd_group)
		return self._reserved

	@property
	def coding(self):
		"""coding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coding'):
			from .Coding import CodingCls
			self._coding = CodingCls(self._core, self._cmd_group)
		return self._coding

	@property
	def crc(self):
		"""crc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crc'):
			from .Crc import CrcCls
			self._crc = CrcCls(self._core, self._cmd_group)
		return self._crc

	@property
	def tail(self):
		"""tail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tail'):
			from .Tail import TailCls
			self._tail = TailCls(self._core, self._cmd_group)
		return self._tail

	def clone(self) -> 'UfieldCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UfieldCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
