from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDevCls:
	"""StandardDev commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Out_Of_Tol: float: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Mod_Type: enums.ModulationTypeC: Modulation scheme and coding rate DBPSk1: 1 Mbit/s DBPSK DQPSk2: 2 Mbit/s DQPSK CCK5: 5.5 Mbit/s CCK CCK11: 11 Mbit/s CCK
			- Plcp_Type: enums.PlcpType: Short or long PLCP
			- Payload_Length: int: Number of bytes in the payload of the measured burst
			- Burst_Power: float: RMS power of the measured burst
			- Evm_Peak: float: Error vector magnitude peak value
			- Evm_Rms: float: Error vector magnitude RMS value
			- Freq_Error: float: Center frequency error
			- Clock_Error: float: Chip clock error
			- Iq_Offset: float: No parameter help available
			- Gain_Imbalance: float: Gain imbalance
			- Quad_Error: float: Quadrature error"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_enum('Mod_Type', enums.ModulationTypeC),
			ArgStruct.scalar_enum('Plcp_Type', enums.PlcpType),
			ArgStruct.scalar_int('Payload_Length'),
			ArgStruct.scalar_float('Burst_Power'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Freq_Error'),
			ArgStruct.scalar_float('Clock_Error'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Gain_Imbalance'),
			ArgStruct.scalar_float('Quad_Error')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Mod_Type: enums.ModulationTypeC = None
			self.Plcp_Type: enums.PlcpType = None
			self.Payload_Length: int = None
			self.Burst_Power: float = None
			self.Evm_Peak: float = None
			self.Evm_Rms: float = None
			self.Freq_Error: float = None
			self.Clock_Error: float = None
			self.Iq_Offset: float = None
			self.Gain_Imbalance: float = None
			self.Quad_Error: float = None

	def fetch(self, segmentB=repcap.SegmentB.Default) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:MODulation:DSSS:SDEViation \n
		Snippet: value: FetchStruct = driver.wlanMeas.multiEval.listPy.segment.modulation.dsss.standardDev.fetch(segmentB = repcap.SegmentB.Default) \n
		Return the current, average, minimum, maximum and standard deviation single value results for DSSS signals for segment
		<no> in list mode. \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:MODulation:DSSS:SDEViation?', self.__class__.FetchStruct())
