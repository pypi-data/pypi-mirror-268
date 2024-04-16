import binascii
import re


def utf8_to_hex(text: str) -> str:
    """
  Converts a UTF-8 encoded string to its hexadecimal representation.

  Args:
      text: The UTF-8 encoded string to convert.

  Returns:
      The hexadecimal representation of the input string.
  """

    # Encode the string as bytes using UTF-8 encoding
    encoded_bytes = text.encode("utf-8")

    # Convert the bytes to a hexadecimal string using binascii.hexlify()
    hex_string = binascii.hexlify(encoded_bytes).decode("ascii")

    return hex_string


def generate_zero_string(num_zeros: int) -> str:
    """
  Generates a string consisting of the specified number of zeros.

  Args:
      num_zeros: The number of zeros to include in the string.

  Returns:
      A string containing the specified number of zeros.

  Raises:
      ValueError: If the number of zeros is negative.
  """

    if num_zeros < 0:
        raise ValueError("Number of zeros cannot be negative.")

    # Method 1: String multiplication (efficient for large numbers)
    zero_string = "0" * num_zeros

    # Method 2: List comprehension with joining (alternative approach)
    # zero_string = ''.join(['0' for _ in range(num_zeros)])

    return zero_string


def encode_and_pad_feed_name(text: str, target_length: int = 42, prefix: str = "01") -> str:
    """
  Encodes a string to hexadecimal, pads it with prefix and zeros, and validates length.

  Args:
      text: The string to encode.
      length: The desired total length of the output string.
      prefix: Optional prefix to add before the encoded string (default: "").

  Returns:
      The padded and validated hexadecimal string.

  Raises:
      ValueError: If the desired length is less than the sum of text length,
                  prefix length, and padding needed.
  """

    try:
        # Encode to bytes and then hex
        encoded_bytes = text.encode("utf-8")
        hex_string = f"{prefix}{binascii.hexlify(encoded_bytes).decode('ascii')}"
        zeros_to_add = target_length - len(hex_string)
        hex_string = f"{hex_string}{generate_zero_string(num_zeros=zeros_to_add)}"

        assert len(hex_string) == target_length

        return f'0x{hex_string}'

    except Exception as e:
        raise ValueError(f"Error encoding and padding string: {e}")


def decode_unpad_feed_name(input: str) -> str:
    decoded_chunk = bytes.fromhex(input[2:42]).decode("ascii").rstrip("\0")
    return decoded_chunk


def decode_feed_names_batch(encoded_feed_names: str) -> dict:
    """
Decodes a hex-encoded string of feed names into a list of strings.

Args:
    encoded_feed_names: The hex-encoded string to decode.

Returns:
    A list of decoded feed names as strings.

Raises:
    ValueError: If the input string is not in valid hex format or has an incorrect length.
"""

    # Check if the string starts with "0x" and remove it if present
    encoded_feed_names_internal = encoded_feed_names[2:] if encoded_feed_names.startswith("0x") else encoded_feed_names

    # Validate hex format using regular expression
    if not re.match(r"^[0-9a-f]+$", encoded_feed_names_internal):
        raise ValueError(f"Invalid format - not hex string: {encoded_feed_names_internal}")

    # Validate length - must be a multiple of 16
    if len(encoded_feed_names_internal) % 42 != 0:
        raise ValueError(f"Invalid format - wrong length: {len(encoded_feed_names_internal)}")

    # Decode each 16-character chunk as hex and remove null bytes
    result: dict = {}
    for i in range(0, len(encoded_feed_names_internal), 42):
        decoded_chunk = bytes.fromhex(encoded_feed_names_internal[i + 2:i + 42]).decode("ascii").rstrip("\0")
        update_chunk = str(decoded_chunk).replace('/', '_')
        result[str(update_chunk)] = f'0x{encoded_feed_names_internal[i:i + 42]}'

    return result
