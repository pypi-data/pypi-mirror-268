from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: float: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Mcs_Index: int: Modulation and coding scheme index
			- Mod_Type: enums.ModulationTypeD: No parameter help available
			- Payload_Sym: int: Number of OFDM symbols in the payload of the measured burst
			- Measured_Sym: int: Number of measured payload OFDM symbols
			- Payload_Bytes: int: Number of bytes in the payload of the measured burst.
			- Guard_Interval: enums.GuardInterval: SHORt, LONG: short or long guard interval (up to 802.11ac) GI08, GI16, GI32: 0.8 μs, 1.6 μs, and 3.2 μs guard interval durations (for 802.11ax)
			- Nof_Ss: int: Number of spatial streams
			- No_Of_Sts: int: Number of space-time streams
			- Burst_Rate: float: If a modulation filter is used, the burst rate indicates the share of bursts of the selected modulation format in the bursts received. Otherwise, it returns 1.
			- Power_Backoff: float: Minimum distance of signal power to reference level since the start of the measurement.
			- Burst_Power: float: RMS power of the measured burst
			- Peak_Power: float: Peak power of the measured burst
			- Crest_Factor: float: No parameter help available
			- Evm_All_Carr: float: EVM for all carriers
			- Evm_Data_Carr: float: EVM for data carriers
			- Evm_Pilot_Carr: float: EVM for pilot carriers
			- Freq_Error: float: Center frequency error
			- Clock_Error: float: Symbol clock error
			- Iq_Offset: float: No parameter help available
			- Dc_Power: float: Power of the DC subcarriers
			- Gain_Imbalance: float: Gain imbalance cannot be calculated if the spectrum is not symmetrical, e.g. for HE_TB and HE_MU.
			- Quad_Error: float: Quadrature error cannot be calculated if the spectrum is not symmetrical, e.g. for HE_TB and HE_MU.
			- Ltf_Power: float: Power of long training fields (LTF) portion
			- Data_Power: float: Power of data portion
			- Preamble_Power: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
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
			ArgStruct.scalar_float('Data_Power'),
			ArgStruct.scalar_float('Preamble_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
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
			self.Preamble_Power: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:CURRent \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.modulation.current.read() \n
		Return the single value results for OFDM SISO measurements. For MIMO measurements, the stream/antenna-independent values
		are returned. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:CURRent \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.modulation.current.fetch() \n
		Return the single value results for OFDM SISO measurements. For MIMO measurements, the stream/antenna-independent values
		are returned. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: enums.ResultStatus2: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Mcs_Index: enums.ResultStatus2: Modulation and coding scheme index
			- Mod_Type: enums.ResultStatus2: No parameter help available
			- Payload_Sym: enums.ResultStatus2: Number of OFDM symbols in the payload of the measured burst
			- Measured_Sym: enums.ResultStatus2: Number of measured payload OFDM symbols
			- Payload_Bytes: enums.ResultStatus2: Number of bytes in the payload of the measured burst.
			- Guard_Interval: enums.ResultStatus2: SHORt, LONG: short or long guard interval (up to 802.11ac) GI08, GI16, GI32: 0.8 μs, 1.6 μs, and 3.2 μs guard interval durations (for 802.11ax)
			- Nof_Ss: enums.ResultStatus2: Number of spatial streams
			- No_Of_Sts: enums.ResultStatus2: Number of space-time streams
			- Burst_Rate: enums.ResultStatus2: If a modulation filter is used, the burst rate indicates the share of bursts of the selected modulation format in the bursts received. Otherwise, it returns 1.
			- Power_Backoff: enums.ResultStatus2: Minimum distance of signal power to reference level since the start of the measurement.
			- Burst_Power: enums.ResultStatus2: RMS power of the measured burst
			- Peak_Power: enums.ResultStatus2: Peak power of the measured burst
			- Crest_Factor: enums.ResultStatus2: No parameter help available
			- Evm_All_Carr: enums.ResultStatus2: EVM for all carriers
			- Evm_Data_Carr: enums.ResultStatus2: EVM for data carriers
			- Evm_Pilot_Carr: enums.ResultStatus2: EVM for pilot carriers
			- Freq_Error: enums.ResultStatus2: Center frequency error
			- Clock_Error: enums.ResultStatus2: Symbol clock error
			- Iq_Offset: enums.ResultStatus2: No parameter help available
			- Dc_Power: enums.ResultStatus2: Power of the DC subcarriers
			- Gain_Imbalance: enums.ResultStatus2: Gain imbalance cannot be calculated if the spectrum is not symmetrical, e.g. for HE_TB and HE_MU.
			- Quad_Error: enums.ResultStatus2: Quadrature error cannot be calculated if the spectrum is not symmetrical, e.g. for HE_TB and HE_MU.
			- Ltf_Power: enums.ResultStatus2: Power of long training fields (LTF) portion
			- Data_Power: enums.ResultStatus2: Power of data portion
			- Preamble_Power: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2),
			ArgStruct.scalar_enum('Mcs_Index', enums.ResultStatus2),
			ArgStruct.scalar_enum('Mod_Type', enums.ResultStatus2),
			ArgStruct.scalar_enum('Payload_Sym', enums.ResultStatus2),
			ArgStruct.scalar_enum('Measured_Sym', enums.ResultStatus2),
			ArgStruct.scalar_enum('Payload_Bytes', enums.ResultStatus2),
			ArgStruct.scalar_enum('Guard_Interval', enums.ResultStatus2),
			ArgStruct.scalar_enum('Nof_Ss', enums.ResultStatus2),
			ArgStruct.scalar_enum('No_Of_Sts', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Rate', enums.ResultStatus2),
			ArgStruct.scalar_enum('Power_Backoff', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Peak_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Crest_Factor', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_All_Carr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Data_Carr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Pilot_Carr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Freq_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Clock_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dc_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Gain_Imbalance', enums.ResultStatus2),
			ArgStruct.scalar_enum('Quad_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ltf_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Data_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Preamble_Power', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: enums.ResultStatus2 = None
			self.Mcs_Index: enums.ResultStatus2 = None
			self.Mod_Type: enums.ResultStatus2 = None
			self.Payload_Sym: enums.ResultStatus2 = None
			self.Measured_Sym: enums.ResultStatus2 = None
			self.Payload_Bytes: enums.ResultStatus2 = None
			self.Guard_Interval: enums.ResultStatus2 = None
			self.Nof_Ss: enums.ResultStatus2 = None
			self.No_Of_Sts: enums.ResultStatus2 = None
			self.Burst_Rate: enums.ResultStatus2 = None
			self.Power_Backoff: enums.ResultStatus2 = None
			self.Burst_Power: enums.ResultStatus2 = None
			self.Peak_Power: enums.ResultStatus2 = None
			self.Crest_Factor: enums.ResultStatus2 = None
			self.Evm_All_Carr: enums.ResultStatus2 = None
			self.Evm_Data_Carr: enums.ResultStatus2 = None
			self.Evm_Pilot_Carr: enums.ResultStatus2 = None
			self.Freq_Error: enums.ResultStatus2 = None
			self.Clock_Error: enums.ResultStatus2 = None
			self.Iq_Offset: enums.ResultStatus2 = None
			self.Dc_Power: enums.ResultStatus2 = None
			self.Gain_Imbalance: enums.ResultStatus2 = None
			self.Quad_Error: enums.ResultStatus2 = None
			self.Ltf_Power: enums.ResultStatus2 = None
			self.Data_Power: enums.ResultStatus2 = None
			self.Preamble_Power: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:CURRent \n
		Snippet: value: CalculateStruct = driver.wlanMeas.multiEval.modulation.current.calculate() \n
		Return the single value results for OFDM SISO measurements. For MIMO measurements, the stream/antenna-independent values
		are returned. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:CURRent?', self.__class__.CalculateStruct())
