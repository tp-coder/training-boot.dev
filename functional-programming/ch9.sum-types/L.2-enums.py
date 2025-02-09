# Create an Enum called Doctype with values:
# - PDF
# - TXT
# - DOCX
# - MD
# - HTML

from enum import Enum

Doctype = Enum('Doctype', [
    'PDF',
    'TXT',
    'DOCX',
    'MD',
    'HTML'
])