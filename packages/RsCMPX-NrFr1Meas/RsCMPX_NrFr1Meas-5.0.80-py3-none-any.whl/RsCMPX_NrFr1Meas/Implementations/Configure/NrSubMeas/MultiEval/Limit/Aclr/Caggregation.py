from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaggregationCls:
	"""Caggregation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caggregation", core, parent)

	def set(self, relative_level: float or bool, absolute_level: float or bool) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:CAGGregation \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.aclr.caggregation.set(relative_level = 1.0, absolute_level = 1.0) \n
		Defines relative and absolute limits for the ACLR measured in an adjacent aggregated channel bandwidth, for NR SA with
		carrier aggregation. \n
			:param relative_level: (float or boolean) Relative lower ACLR limit without test tolerance
			:param absolute_level: (float or boolean) No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('relative_level', relative_level, DataType.FloatExt), ArgSingle('absolute_level', absolute_level, DataType.FloatExt))
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:CAGGregation {param}'.rstrip())

	# noinspection PyTypeChecker
	class CaggregationStruct(StructBase):
		"""Response structure. Fields: \n
			- Relative_Level: float or bool: Relative lower ACLR limit without test tolerance
			- Absolute_Level: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Relative_Level'),
			ArgStruct.scalar_float_ext('Absolute_Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Relative_Level: float or bool = None
			self.Absolute_Level: float or bool = None

	def get(self) -> CaggregationStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:CAGGregation \n
		Snippet: value: CaggregationStruct = driver.configure.nrSubMeas.multiEval.limit.aclr.caggregation.get() \n
		Defines relative and absolute limits for the ACLR measured in an adjacent aggregated channel bandwidth, for NR SA with
		carrier aggregation. \n
			:return: structure: for return value, see the help for CaggregationStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:CAGGregation?', self.__class__.CaggregationStruct())
