from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcombCls:
	"""Tcomb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcomb", core, parent)

	def set(self, ktc: enums.Ktc, offset: int = None, cyclic_shift: int = None) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:TCOMb \n
		Snippet: driver.configure.nrSubMeas.srs.tcomb.set(ktc = enums.Ktc.N2, offset = 1, cyclic_shift = 1) \n
		No command help available \n
			:param ktc: No help available
			:param offset: No help available
			:param cyclic_shift: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ktc', ktc, DataType.Enum, enums.Ktc), ArgSingle('offset', offset, DataType.Integer, None, is_optional=True), ArgSingle('cyclic_shift', cyclic_shift, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:TCOMb {param}'.rstrip())

	# noinspection PyTypeChecker
	class TcombStruct(StructBase):
		"""Response structure. Fields: \n
			- Ktc: enums.Ktc: No parameter help available
			- Offset: int: No parameter help available
			- Cyclic_Shift: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Ktc', enums.Ktc),
			ArgStruct.scalar_int('Offset'),
			ArgStruct.scalar_int('Cyclic_Shift')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ktc: enums.Ktc = None
			self.Offset: int = None
			self.Cyclic_Shift: int = None

	def get(self) -> TcombStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:TCOMb \n
		Snippet: value: TcombStruct = driver.configure.nrSubMeas.srs.tcomb.get() \n
		No command help available \n
			:return: structure: for return value, see the help for TcombStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:SRS:TCOMb?', self.__class__.TcombStruct())
