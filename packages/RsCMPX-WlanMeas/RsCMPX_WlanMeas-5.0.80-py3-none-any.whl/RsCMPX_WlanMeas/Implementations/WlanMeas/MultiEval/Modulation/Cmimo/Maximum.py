from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Mcs_Index: int: No parameter help available
			- Nof_Ss: int: No parameter help available
			- No_Of_Sts: int: No parameter help available
			- Payload_Length: int: No parameter help available
			- Evm_All_Carr: float: No parameter help available
			- Evm_Data_Carr: float: No parameter help available
			- Evm_Pilot_Carr: float: No parameter help available
			- Power_Total: float: No parameter help available
			- Power_Total_Peak: float: No parameter help available
			- Power_Sts_1: float: No parameter help available
			- Power_Sts_2: float: No parameter help available
			- Power_Sts_3: float: No parameter help available
			- Power_Sts_4: float: No parameter help available
			- Freq_Error: float: No parameter help available
			- Out_Of_Tol: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Mcs_Index'),
			ArgStruct.scalar_int('Nof_Ss'),
			ArgStruct.scalar_int('No_Of_Sts'),
			ArgStruct.scalar_int('Payload_Length'),
			ArgStruct.scalar_float('Evm_All_Carr'),
			ArgStruct.scalar_float('Evm_Data_Carr'),
			ArgStruct.scalar_float('Evm_Pilot_Carr'),
			ArgStruct.scalar_float('Power_Total'),
			ArgStruct.scalar_float('Power_Total_Peak'),
			ArgStruct.scalar_float('Power_Sts_1'),
			ArgStruct.scalar_float('Power_Sts_2'),
			ArgStruct.scalar_float('Power_Sts_3'),
			ArgStruct.scalar_float('Power_Sts_4'),
			ArgStruct.scalar_float('Freq_Error'),
			ArgStruct.scalar_float('Out_Of_Tol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Mcs_Index: int = None
			self.Nof_Ss: int = None
			self.No_Of_Sts: int = None
			self.Payload_Length: int = None
			self.Evm_All_Carr: float = None
			self.Evm_Data_Carr: float = None
			self.Evm_Pilot_Carr: float = None
			self.Power_Total: float = None
			self.Power_Total_Peak: float = None
			self.Power_Sts_1: float = None
			self.Power_Sts_2: float = None
			self.Power_Sts_3: float = None
			self.Power_Sts_4: float = None
			self.Freq_Error: float = None
			self.Out_Of_Tol: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:CMIMo:MAXimum \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.modulation.cmimo.maximum.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:CMIMo:MAXimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:CMIMo:MAXimum \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.modulation.cmimo.maximum.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:CMIMo:MAXimum?', self.__class__.ResultData())
