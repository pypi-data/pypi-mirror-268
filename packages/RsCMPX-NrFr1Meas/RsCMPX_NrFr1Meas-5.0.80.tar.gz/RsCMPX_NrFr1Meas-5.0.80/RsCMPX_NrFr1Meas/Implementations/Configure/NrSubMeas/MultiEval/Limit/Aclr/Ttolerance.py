from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TtoleranceCls:
	"""Ttolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttolerance", core, parent)

	def set(self, test_tol_sub_4_ghz: float, test_tol_sub_6_gh_z: float) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:TTOLerance \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.aclr.ttolerance.set(test_tol_sub_4_ghz = 1.0, test_tol_sub_6_gh_z = 1.0) \n
		Defines the test tolerance for relative ACLR limits, depending on the center frequency. \n
			:param test_tol_sub_4_ghz: Test tolerance for center frequencies ≤ 4 GHz
			:param test_tol_sub_6_gh_z: Test tolerance for center frequencies 4 GHz
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('test_tol_sub_4_ghz', test_tol_sub_4_ghz, DataType.Float), ArgSingle('test_tol_sub_6_gh_z', test_tol_sub_6_gh_z, DataType.Float))
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:TTOLerance {param}'.rstrip())

	# noinspection PyTypeChecker
	class TtoleranceStruct(StructBase):
		"""Response structure. Fields: \n
			- Test_Tol_Sub_4_Ghz: float: Test tolerance for center frequencies ≤ 4 GHz
			- Test_Tol_Sub_6_Gh_Z: float: Test tolerance for center frequencies 4 GHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Test_Tol_Sub_4_Ghz'),
			ArgStruct.scalar_float('Test_Tol_Sub_6_Gh_Z')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Test_Tol_Sub_4_Ghz: float = None
			self.Test_Tol_Sub_6_Gh_Z: float = None

	def get(self) -> TtoleranceStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:TTOLerance \n
		Snippet: value: TtoleranceStruct = driver.configure.nrSubMeas.multiEval.limit.aclr.ttolerance.get() \n
		Defines the test tolerance for relative ACLR limits, depending on the center frequency. \n
			:return: structure: for return value, see the help for TtoleranceStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:TTOLerance?', self.__class__.TtoleranceStruct())
