from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Low: List[float]: No parameter help available
			- High: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Low', DataType.FloatList, None, False, True, 1),
			ArgStruct('High', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Low: List[float] = None
			self.High: List[float] = None

	def read(self) -> ResultData:
		"""SCPI: READ:NRSub:MEASurement<Instance>:SRS:EVMSymbol:AVERage \n
		Snippet: value: ResultData = driver.nrSubMeas.srs.evmSymbol.average.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NRSub:MEASurement<Instance>:SRS:EVMSymbol:AVERage?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:SRS:EVMSymbol:AVERage \n
		Snippet: value: ResultData = driver.nrSubMeas.srs.evmSymbol.average.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRSub:MEASurement<Instance>:SRS:EVMSymbol:AVERage?', self.__class__.ResultData())
