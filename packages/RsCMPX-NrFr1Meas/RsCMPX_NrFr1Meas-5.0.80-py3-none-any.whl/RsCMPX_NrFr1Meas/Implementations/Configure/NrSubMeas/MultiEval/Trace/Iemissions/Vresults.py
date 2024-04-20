from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VresultsCls:
	"""Vresults commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vresults", core, parent)

	def set(self, cc_1_start: int, cc_1_length: int, cc_2_start: int, cc_2_length: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:TRACe:IEMissions:VRESults \n
		Snippet: driver.configure.nrSubMeas.multiEval.trace.iemissions.vresults.set(cc_1_start = 1, cc_1_length = 1, cc_2_start = 1, cc_2_length = 1) \n
		No command help available \n
			:param cc_1_start: No help available
			:param cc_1_length: No help available
			:param cc_2_start: No help available
			:param cc_2_length: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cc_1_start', cc_1_start, DataType.Integer), ArgSingle('cc_1_length', cc_1_length, DataType.Integer), ArgSingle('cc_2_start', cc_2_start, DataType.Integer), ArgSingle('cc_2_length', cc_2_length, DataType.Integer))
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:TRACe:IEMissions:VRESults {param}'.rstrip())

	# noinspection PyTypeChecker
	class VresultsStruct(StructBase):
		"""Response structure. Fields: \n
			- Cc_1_Start: int: No parameter help available
			- Cc_1_Length: int: No parameter help available
			- Cc_2_Start: int: No parameter help available
			- Cc_2_Length: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Cc_1_Start'),
			ArgStruct.scalar_int('Cc_1_Length'),
			ArgStruct.scalar_int('Cc_2_Start'),
			ArgStruct.scalar_int('Cc_2_Length')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cc_1_Start: int = None
			self.Cc_1_Length: int = None
			self.Cc_2_Start: int = None
			self.Cc_2_Length: int = None

	def get(self) -> VresultsStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:TRACe:IEMissions:VRESults \n
		Snippet: value: VresultsStruct = driver.configure.nrSubMeas.multiEval.trace.iemissions.vresults.get() \n
		No command help available \n
			:return: structure: for return value, see the help for VresultsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:TRACe:IEMissions:VRESults?', self.__class__.VresultsStruct())
