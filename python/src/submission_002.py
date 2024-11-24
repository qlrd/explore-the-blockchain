"""
submission_002.py

(true / false) Verify the signature by this address over this message:
address: `1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa`
message: `1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa`
signature: `hCsBcgB+Wcm8kOGMH8IpNeg0H4gjCrlqwDf/GlSXphZGBYxm0QkKEPhh9DTJRp2IDNUhVr0FhP9qCqo2W0recNM=`
"""

import hashlib
from bitcoin.signmessage import VerifyMessage


# The question
ADDRESS = "1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa"
MESSAGE = b"1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa"
SIGNATURE = "hCsBcgB+Wcm8kOGMH8IpNeg0H4gjCrlqwDf/GlSXphZGBYxm0QkKEPhh9DTJRp2IDNUhVr0FhP9qCqo2W0recNM="

msg = hashlib.sha256(hashlib.sha256(MESSAGE).digest()).digest()
print(VerifyMessage(ADDRESS, msg, SIGNATURE))
