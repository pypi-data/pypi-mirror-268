from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Ab_Curr: float: No parameter help available
			- Bc_Curr: float: No parameter help available
			- Cd_Curr: float: No parameter help available
			- De_Curr: float: No parameter help available
			- Ed_Curr: float: No parameter help available
			- Dc_Curr: float: No parameter help available
			- Cb_Curr: float: No parameter help available
			- Ba_Curr: float: No parameter help available
			- Out_Of_Tol: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ab_Curr'),
			ArgStruct.scalar_float('Bc_Curr'),
			ArgStruct.scalar_float('Cd_Curr'),
			ArgStruct.scalar_float('De_Curr'),
			ArgStruct.scalar_float('Ed_Curr'),
			ArgStruct.scalar_float('Dc_Curr'),
			ArgStruct.scalar_float('Cb_Curr'),
			ArgStruct.scalar_float('Ba_Curr'),
			ArgStruct.scalar_float('Out_Of_Tol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ab_Curr: float = None
			self.Bc_Curr: float = None
			self.Cd_Curr: float = None
			self.De_Curr: float = None
			self.Ed_Curr: float = None
			self.Dc_Curr: float = None
			self.Cb_Curr: float = None
			self.Ba_Curr: float = None
			self.Out_Of_Tol: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:NSISo:CURRent \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.nsiso.current.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:NSISo:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:NSISo:CURRent \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.nsiso.current.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:NSISo:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Ab_Curr: enums.ResultStatus2: No parameter help available
			- Bc_Curr: enums.ResultStatus2: No parameter help available
			- Cd_Curr: enums.ResultStatus2: No parameter help available
			- De_Curr: enums.ResultStatus2: No parameter help available
			- Ed_Curr: enums.ResultStatus2: No parameter help available
			- Dc_Curr: enums.ResultStatus2: No parameter help available
			- Cb_Curr: enums.ResultStatus2: No parameter help available
			- Ba_Curr: enums.ResultStatus2: No parameter help available
			- Out_Of_Tol: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Ab_Curr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Bc_Curr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Cd_Curr', enums.ResultStatus2),
			ArgStruct.scalar_enum('De_Curr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ed_Curr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dc_Curr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Cb_Curr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ba_Curr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ab_Curr: enums.ResultStatus2 = None
			self.Bc_Curr: enums.ResultStatus2 = None
			self.Cd_Curr: enums.ResultStatus2 = None
			self.De_Curr: enums.ResultStatus2 = None
			self.Ed_Curr: enums.ResultStatus2 = None
			self.Dc_Curr: enums.ResultStatus2 = None
			self.Cb_Curr: enums.ResultStatus2 = None
			self.Ba_Curr: enums.ResultStatus2 = None
			self.Out_Of_Tol: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:NSISo:CURRent \n
		Snippet: value: CalculateStruct = driver.wlanMeas.multiEval.tsMask.nsiso.current.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:NSISo:CURRent?', self.__class__.CalculateStruct())
