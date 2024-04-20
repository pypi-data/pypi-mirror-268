from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Seg_Reliability: int: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Out_Of_Tol: float: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Mcs_Index: int: Modulation and coding scheme index
			- Mod_Type: enums.ModulationTypeD: Modulation scheme and coding rate UNSPecified: modulation unknown BPSK: BPSK, coding rate unknown BPSK12, BPSK34 (BPSKab) : BPSK, coding rate a/b BPSK14: BPSK, coding rate 1/2 DCM QPSK: QPSK, coding rate unknown QPSK12, QPSK34 (QPSKab) : QPSK, coding rate a/b QPSK14: QPSK, coding rate 1/2 DCM 16Q: 16QAM, coding rate unknown 16Q12, 16Q34 (16Qab) : 16QAM, coding rate a/b 16Q14: 16QAM, coding rate 1/2 DCM 16Q38: 16QAM, coding rate 3/4 DCM 64Q: 64QAM, coding rate unknown 64Q12, 64Q23, 64Q34, 64Q56 (64Qab) : 64QAM, coding rate a/b 256Q: 256QAM, coding rate unknown 256Q34, 256Q56 (256Qab) : 256QAM, coding rate a/b 1KQ: 1024QAM, coding rate unknown 1KQ34, 1KQ56 (1KQab) : 1024QAM, coding rate a/b BMCS14: BPSK DCM DUP BMCS15: BPSK DCM 4KQ: 4096QAM, coding rate unknown 4KQ34, 4KQ56 (4KQab) : 4096QAM, coding rate a/b
			- Payload_Sym: int: Number of OFDM symbols in the payload of the measured burst
			- Measured_Sym: int: The number of OFDM payload symbols to be measured.
			- Payload_Bytes: int: Number of bytes in the payload of the measured burst.
			- Guard_Interval: enums.GuardInterval: SHORt, LONG: short or long guard interval (up to 802.11ac) GI08, GI16, GI32: 0.8 μs, 1.6 μs, and 3.2 μs guard interval durations (for 802.11ax)
			- Nof_Ss: int: Number of spatial streams
			- No_Of_Sts: int: Number of space-time streams
			- Burst_Rate: float: The rate of bursts of the selected modulation format 5_ModType in the bursts received.
			- Power_Backoff: float: Minimum distance of signal power to reference level since the start of the measurement.
			- Burst_Power: float: RMS power of the measured burst
			- Peak_Power: float: Peak power of the measured burst
			- Crest_Factor: float: No parameter help available
			- Evm_All_Carr: float: EVM for all, data, and pilot carriers
			- Evm_Data_Carr: float: EVM for all, data, and pilot carriers
			- Evm_Pilot_Carr: float: EVM for all, data, and pilot carriers
			- Freq_Error: float: Center frequency error
			- Clock_Error: float: Symbol clock error
			- Iq_Offset: float: No parameter help available
			- Dc_Power: float: No parameter help available
			- Gain_Imbalance: float: No parameter help available
			- Quad_Error: float: Quadrature error
			- Ltf_Power: float: Power of long training fields (LTF) portion
			- Data_Power: float: Power of data portion"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_int('Mcs_Index'),
			ArgStruct.scalar_enum('Mod_Type', enums.ModulationTypeD),
			ArgStruct.scalar_int('Payload_Sym'),
			ArgStruct.scalar_int('Measured_Sym'),
			ArgStruct.scalar_int('Payload_Bytes'),
			ArgStruct.scalar_enum('Guard_Interval', enums.GuardInterval),
			ArgStruct.scalar_int('Nof_Ss'),
			ArgStruct.scalar_int('No_Of_Sts'),
			ArgStruct.scalar_float('Burst_Rate'),
			ArgStruct.scalar_float('Power_Backoff'),
			ArgStruct.scalar_float('Burst_Power'),
			ArgStruct.scalar_float('Peak_Power'),
			ArgStruct.scalar_float('Crest_Factor'),
			ArgStruct.scalar_float('Evm_All_Carr'),
			ArgStruct.scalar_float('Evm_Data_Carr'),
			ArgStruct.scalar_float('Evm_Pilot_Carr'),
			ArgStruct.scalar_float('Freq_Error'),
			ArgStruct.scalar_float('Clock_Error'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Dc_Power'),
			ArgStruct.scalar_float('Gain_Imbalance'),
			ArgStruct.scalar_float('Quad_Error'),
			ArgStruct.scalar_float('Ltf_Power'),
			ArgStruct.scalar_float('Data_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Mcs_Index: int = None
			self.Mod_Type: enums.ModulationTypeD = None
			self.Payload_Sym: int = None
			self.Measured_Sym: int = None
			self.Payload_Bytes: int = None
			self.Guard_Interval: enums.GuardInterval = None
			self.Nof_Ss: int = None
			self.No_Of_Sts: int = None
			self.Burst_Rate: float = None
			self.Power_Backoff: float = None
			self.Burst_Power: float = None
			self.Peak_Power: float = None
			self.Crest_Factor: float = None
			self.Evm_All_Carr: float = None
			self.Evm_Data_Carr: float = None
			self.Evm_Pilot_Carr: float = None
			self.Freq_Error: float = None
			self.Clock_Error: float = None
			self.Iq_Offset: float = None
			self.Dc_Power: float = None
			self.Gain_Imbalance: float = None
			self.Quad_Error: float = None
			self.Ltf_Power: float = None
			self.Data_Power: float = None

	def fetch(self, segmentB=repcap.SegmentB.Default) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:MODulation:CURRent \n
		Snippet: value: FetchStruct = driver.wlanMeas.multiEval.listPy.segment.modulation.current.fetch(segmentB = repcap.SegmentB.Default) \n
		Return OFDM/OFDMA modulation single value results for segment <no> in list mode. \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:MODulation:CURRent?', self.__class__.FetchStruct())
