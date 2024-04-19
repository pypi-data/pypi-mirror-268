class Error(Exception):
    """Base class for other exceptions"""
    pass


class EmptyFileError(Error):
    message = "File doesn't have contents"
    pass


class FalseError(Error):
    message = "Error in API response"
    pass


class FileProcessError(Error):
    pass

class InvalidDatetimeInHl7Message(Error):
    def __init__(self,child):
        Error.__init__(self,("Datetime in not valid in child : "+child))
        self.message = "Datetime in not valid in child : "+child


class InvalidLoginToken(Error):
    message = "Invalid Login Token"
    pass

class LoginTokenExpired(Error):
    message = "Login Token Expired"
    pass

class LicenseHasExpired(Error):
    message = "License Has Expired..Please check domain name in headers.."
    pass

class DeadlockCondition(Error):
    message = "Deadlock found when trying to get lock; try restarting transaction"
    pass

class LockWaitTimeout(Error):
    message = "Lock wait timeout exceeded; try restarting transaction"
    pass

class LoginFailed(Error):
    def __init__(self,msg):
        Error.__init__(self,(msg))
        self.message=msg

class InvalidNumbers(Error):
    def __init__(self, num):
        Error.__init__(self,('","'.join(num))+" are not numbers")
        self.message = ",".join(num)+" are not numbers"

    def __str__(self):
        # return self.num+" not an integer value"
        return self.message

class InvalidNumber(Error):
    def __init__(self, num):
        Error.__init__(self, "'"+num+"' is not a number")
        # self.num=num
        self.message = "'"+num+"' is not a number"

    def __str__(self):
        # return self.num+" not an integer value"
        return self.message


class InvalidCalculation(Error):
    def __init__(self, num):
        Error.__init__(self, num+" invalid calculation")

    def __str__(self):
        return "invalid calculation"

class HL7ParserError(Error):
    def __init__(self):
        Error.__init__(self,"Error in HL7 message Parsing")

class EventHandlingError(Error):
    def __init__(self):
        Error.__init__(self,"Error in Event Handling")
class InvalidInput(Error):
    def __init__(self,message):
        Error.__init__(self, message)
        self.message=message
    def __str__(self):
        return self.message

class InvalidDateTime(Error):
    def __init__(self):
        Error.__init__(self,"invalid datetime")

    def __str__(self):
        return "invalid datetime"

class InvalidJob(Error):
    """
    Job body is not valid json or it doesn't have required fields
    """

    def __init__(self, jib, missing_parameters=None):
        self.message = "Invalid Job : [JID :(" + jib + ")" + ", Missing Parameters : (" + "".join(
            missing_parameters) + ")" + "]"


class MaxApiRetriesExceeded(Error):
    def __init__(self,message_details=None):
        self.message = "Max retries for a URL exceeded.There might be any exception. Please check."
        self.message_details = message_details

class BeanstalkConnectionFailed(Error):
    def __init__(self,message_details):
        self.message="Beanstalk Connection Failed"
        self.message_details=message_details


class RsysLogConnectionFailed(Error):
    def __init__(self,message_details):
        self.message="Rsyslog Connection Failed"
        self.message_details=message_details


class RedisConnectionFailed(Error):
    def __init__(self,message_details):
        self.message="Redis Connection Failed"
        self.message_details=message_details


class ResourceNotFound(Error):
    def __init__(self,message_details):
        self.message="Resource Not Found"
        self.message_details=message_details


class InternalServerError(Error):
    def __init__(self,message_details):
        self.message="Internal Server Error"
        self.message_details=message_details

class InvalidRequest(Error):
    def __init__(self,message_details):
        self.message="Invalid Request Sent"
        self.message_details=message_details