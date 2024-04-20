from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Ab_Max: float: No parameter help available
			- Bc_Max: float: No parameter help available
			- Cd_Max: float: No parameter help available
			- De_Max: float: No parameter help available
			- Ed_Max: float: No parameter help available
			- Dcmax: float: No parameter help available
			- Cb_Max: float: No parameter help available
			- Ba_Max: float: No parameter help available
			- Out_Of_Tol: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ab_Max'),
			ArgStruct.scalar_float('Bc_Max'),
			ArgStruct.scalar_float('Cd_Max'),
			ArgStruct.scalar_float('De_Max'),
			ArgStruct.scalar_float('Ed_Max'),
			ArgStruct.scalar_float('Dcmax'),
			ArgStruct.scalar_float('Cb_Max'),
			ArgStruct.scalar_float('Ba_Max'),
			ArgStruct.scalar_float('Out_Of_Tol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ab_Max: float = None
			self.Bc_Max: float = None
			self.Cd_Max: float = None
			self.De_Max: float = None
			self.Ed_Max: float = None
			self.Dcmax: float = None
			self.Cb_Max: float = None
			self.Ba_Max: float = None
			self.Out_Of_Tol: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:MAXimum \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.acsiso.maximum.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:MAXimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:MAXimum \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.acsiso.maximum.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:MAXimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Ab_Max: enums.ResultStatus2: No parameter help available
			- Bc_Max: enums.ResultStatus2: No parameter help available
			- Cd_Max: enums.ResultStatus2: No parameter help available
			- De_Max: enums.ResultStatus2: No parameter help available
			- Ed_Max: enums.ResultStatus2: No parameter help available
			- Dcmax: enums.ResultStatus2: No parameter help available
			- Cb_Max: enums.ResultStatus2: No parameter help available
			- Ba_Max: enums.ResultStatus2: No parameter help available
			- Out_Of_Tol: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Ab_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Bc_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Cd_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('De_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ed_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dcmax', enums.ResultStatus2),
			ArgStruct.scalar_enum('Cb_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ba_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ab_Max: enums.ResultStatus2 = None
			self.Bc_Max: enums.ResultStatus2 = None
			self.Cd_Max: enums.ResultStatus2 = None
			self.De_Max: enums.ResultStatus2 = None
			self.Ed_Max: enums.ResultStatus2 = None
			self.Dcmax: enums.ResultStatus2 = None
			self.Cb_Max: enums.ResultStatus2 = None
			self.Ba_Max: enums.ResultStatus2 = None
			self.Out_Of_Tol: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:MAXimum \n
		Snippet: value: CalculateStruct = driver.wlanMeas.multiEval.tsMask.acsiso.maximum.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:MAXimum?', self.__class__.CalculateStruct())
