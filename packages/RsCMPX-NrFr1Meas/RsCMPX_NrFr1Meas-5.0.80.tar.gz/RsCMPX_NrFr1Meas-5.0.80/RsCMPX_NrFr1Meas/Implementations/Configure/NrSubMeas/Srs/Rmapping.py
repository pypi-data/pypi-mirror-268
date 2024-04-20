from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmappingCls:
	"""Rmapping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmapping", core, parent)

	def set(self, number_symbols: enums.NumberSymbols, start_position: int = None) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:RMAPping \n
		Snippet: driver.configure.nrSubMeas.srs.rmapping.set(number_symbols = enums.NumberSymbols.N1, start_position = 1) \n
		Defines the position of the SRS resource within a slot. \n
			:param number_symbols: Number of OFDM symbols per SRS transmission.
			:param start_position: Start position of the SRS resource (0 = last symbol of slot) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_symbols', number_symbols, DataType.Enum, enums.NumberSymbols), ArgSingle('start_position', start_position, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:RMAPping {param}'.rstrip())

	# noinspection PyTypeChecker
	class RmappingStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Symbols: enums.NumberSymbols: Number of OFDM symbols per SRS transmission.
			- Start_Position: int: Start position of the SRS resource (0 = last symbol of slot) ."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Number_Symbols', enums.NumberSymbols),
			ArgStruct.scalar_int('Start_Position')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Symbols: enums.NumberSymbols = None
			self.Start_Position: int = None

	def get(self) -> RmappingStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:RMAPping \n
		Snippet: value: RmappingStruct = driver.configure.nrSubMeas.srs.rmapping.get() \n
		Defines the position of the SRS resource within a slot. \n
			:return: structure: for return value, see the help for RmappingStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:SRS:RMAPping?', self.__class__.RmappingStruct())
