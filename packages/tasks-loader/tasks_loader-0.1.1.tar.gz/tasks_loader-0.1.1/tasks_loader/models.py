
class Patterns:
    """
    Contains regular expressions for validating various types of data inputs.

    Class Attributes:
        MAIL (str): Pattern to validate email addresses.
        PHONE (str): Pattern to validate phone numbers.
        CREDIT_CARD (str): Pattern to validate credit card numbers.
        MONTH (str): Pattern to validate month names.
        YEAR (str): Pattern to validate year (four digits).
        DISCORD_WEBHOOK (str): Pattern to validate Discord webhook URLs.
        URL (str): Pattern to validate general URLs.
        IPV4 (str): Pattern to validate IPv4 addresses.
        ZIP_CODE_US (str): Pattern to validate US zip codes.
    """

    # Email pattern
    MAIL = r"[^@]+@[^@]+\.[^@]+"

    # Phone number pattern, simple version for international format
    PHONE = r"\+?[1-9]\d{1,14}"

    # Credit card number pattern (simplified, typically used for visual validation)
    CREDIT_CARD = r"\d{4}-\d{4}-\d{4}-\d{4}"

    # Month names pattern (case-insensitive)
    MONTH = r"^(?i)(January|February|March|April|May|June|July|August|September|October|November|December)$"

    # Year pattern (four digits)
    YEAR = r"^\d{4}$"

    # Discord webhook URL pattern
    DISCORD_WEBHOOK = r"https://discord(app)?\.com/api/webhooks/\d+/.+"

    # General URL pattern
    URL = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

    # IPv4 address pattern
    IPV4 = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

    # U.S. Zip code pattern
    ZIP_CODE_US = r"^\d{5}(-\d{4})?$"

class Task:
    """
    Represents a single task, dynamically creating attributes based on input keyword arguments.
    
    Attributes:
        id (str): A unique identifier for the task, formatted as a zero-padded string.
    
    Parameters:
        **kwargs: Arbitrary keyword arguments representing task attributes and their values.
    """
    _id_counter = 1  # Class variable to keep track of the next id

    def __init__(self, **kwargs):
        self.id = str(Task._id_counter).zfill(3)  # Format the id as '001', '002',...
        Task._id_counter += 1  # Increment for the next task
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """Return the task id as a string representation of the Task object."""
        return self.id

    def to_dict(self):
        """
        Convert the Task instance into a dictionary.
        
        Returns:
            dict: A dictionary representation of the Task instance, including its id and all dynamically added attributes.
        """
        return {**self.__dict__}
