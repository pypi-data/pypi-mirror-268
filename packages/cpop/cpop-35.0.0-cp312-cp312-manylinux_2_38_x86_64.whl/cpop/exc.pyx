"""
Pop related exceptions
"""


cdef class PopBaseException(Exception):
    """
    Base exception where all of Pop's exceptions derive
    """


cdef class PopError(PopBaseException):
    """
    General purpose cpop.exception to signal an error
    """


cdef class PopLoadError(PopBaseException):
    """
    Exception raised when a pop module fails to load
    """


cdef class PopLookupError(PopBaseException):
    """
    Exception raised when a pop module lookup fails
    """


cdef class ContractModuleException(PopBaseException):
    """
    Exception raised when a function specified in a contract as required
    to exist is not found in the loaded module
    """


cdef class ContractFuncException(PopBaseException):
    """
    Exception raised when a function specified in a contract as required
    to exist is found on the module but it's not function
    """


cdef class ContractSigException(PopBaseException):
    """
    Exception raised when a function signature is not compatible with the
    coresponding function signature found in the contract.
    """


cdef class ProcessNotStarted(PopBaseException):
    """
    Exception raised when failing to start a process on the process manager
    """


cdef class BindError(PopBaseException):
    """
    Exception raised when arguments for a function in a ContractedContext cannot be bound
    Indicates invalid function arguments.
    """


cdef class PreContractFailed(PopBaseException):
    """
    Exception raised when a pre contract returns False or False and a message.
    Indicates that the corresponding function could not be called.
    """
