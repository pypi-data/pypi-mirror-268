from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwCls:
	"""Bw commands group definition. 1 total commands, 0 Subgroups, 1 group commands
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

	def set(self, offset_value_rel: float or bool, offset_value_abs: float or bool = None, bandwidthE=repcap.BandwidthE.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:IQOFfset:BW<BW> \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.iqOffset.bw.set(offset_value_rel = 1.0, offset_value_abs = 1.0, bandwidthE = repcap.BandwidthE.Default) \n
		Defines and activates upper limits for the I/Q origin offset for 802.11ax and channel bandwidth <BW>. \n
			:param offset_value_rel: (float or boolean) Relative limit
			:param offset_value_abs: (float or boolean) Absolute limit
			:param bandwidthE: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('offset_value_rel', offset_value_rel, DataType.FloatExt), ArgSingle('offset_value_abs', offset_value_abs, DataType.FloatExt, None, is_optional=True))
		bandwidthE_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthE, repcap.BandwidthE)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:IQOFfset:BW{bandwidthE_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class BwStruct(StructBase):
		"""Response structure. Fields: \n
			- Offset_Value_Rel: float or bool: Relative limit
			- Offset_Value_Abs: float or bool: Absolute limit"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Offset_Value_Rel'),
			ArgStruct.scalar_float_ext('Offset_Value_Abs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Offset_Value_Rel: float or bool = None
			self.Offset_Value_Abs: float or bool = None

	def get(self, bandwidthE=repcap.BandwidthE.Default) -> BwStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:IQOFfset:BW<BW> \n
		Snippet: value: BwStruct = driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.iqOffset.bw.get(bandwidthE = repcap.BandwidthE.Default) \n
		Defines and activates upper limits for the I/Q origin offset for 802.11ax and channel bandwidth <BW>. \n
			:param bandwidthE: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: structure: for return value, see the help for BwStruct structure arguments."""
		bandwidthE_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthE, repcap.BandwidthE)
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:IQOFfset:BW{bandwidthE_cmd_val}?', self.__class__.BwStruct())

	def clone(self) -> 'BwCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BwCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
