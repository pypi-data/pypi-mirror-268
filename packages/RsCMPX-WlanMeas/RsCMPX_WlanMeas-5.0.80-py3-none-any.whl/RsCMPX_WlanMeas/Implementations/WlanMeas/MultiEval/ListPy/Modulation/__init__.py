from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 112 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def pbackoff(self):
		"""pbackoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pbackoff'):
			from .Pbackoff import PbackoffCls
			self._pbackoff = PbackoffCls(self._core, self._cmd_group)
		return self._pbackoff

	@property
	def bpower(self):
		"""bpower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_bpower'):
			from .Bpower import BpowerCls
			self._bpower = BpowerCls(self._core, self._cmd_group)
		return self._bpower

	@property
	def ppower(self):
		"""ppower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppower'):
			from .Ppower import PpowerCls
			self._ppower = PpowerCls(self._core, self._cmd_group)
		return self._ppower

	@property
	def cfactor(self):
		"""cfactor commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfactor'):
			from .Cfactor import CfactorCls
			self._cfactor = CfactorCls(self._core, self._cmd_group)
		return self._cfactor

	@property
	def evmAll(self):
		"""evmAll commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_evmAll'):
			from .EvmAll import EvmAllCls
			self._evmAll = EvmAllCls(self._core, self._cmd_group)
		return self._evmAll

	@property
	def evmData(self):
		"""evmData commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_evmData'):
			from .EvmData import EvmDataCls
			self._evmData = EvmDataCls(self._core, self._cmd_group)
		return self._evmData

	@property
	def evmPilot(self):
		"""evmPilot commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_evmPilot'):
			from .EvmPilot import EvmPilotCls
			self._evmPilot = EvmPilotCls(self._core, self._cmd_group)
		return self._evmPilot

	@property
	def cfError(self):
		"""cfError commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfError'):
			from .CfError import CfErrorCls
			self._cfError = CfErrorCls(self._core, self._cmd_group)
		return self._cfError

	@property
	def scError(self):
		"""scError commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_scError'):
			from .ScError import ScErrorCls
			self._scError = ScErrorCls(self._core, self._cmd_group)
		return self._scError

	@property
	def iqOffset(self):
		"""iqOffset commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def dcPower(self):
		"""dcPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_dcPower'):
			from .DcPower import DcPowerCls
			self._dcPower = DcPowerCls(self._core, self._cmd_group)
		return self._dcPower

	@property
	def gimbalance(self):
		"""gimbalance commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import GimbalanceCls
			self._gimbalance = GimbalanceCls(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def qerror(self):
		"""qerror commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_qerror'):
			from .Qerror import QerrorCls
			self._qerror = QerrorCls(self._core, self._cmd_group)
		return self._qerror

	@property
	def ltfPower(self):
		"""ltfPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ltfPower'):
			from .LtfPower import LtfPowerCls
			self._ltfPower = LtfPowerCls(self._core, self._cmd_group)
		return self._ltfPower

	@property
	def dpower(self):
		"""dpower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpower'):
			from .Dpower import DpowerCls
			self._dpower = DpowerCls(self._core, self._cmd_group)
		return self._dpower

	@property
	def dsss(self):
		"""dsss commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsss'):
			from .Dsss import DsssCls
			self._dsss = DsssCls(self._core, self._cmd_group)
		return self._dsss

	def clone(self) -> 'ModulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
