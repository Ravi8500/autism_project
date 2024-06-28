from .Home import app as home
from .Register import app as register
from .Dashboard import app as dashboard
from .Form import app as form
from .Contact import app as contact
from .chat_bot_forlocation import app as chat_bot_forlocation

# Define the order of pages
pages = {
    "Home": home,
    "Register": register,
    "Dashboard": dashboard,
    "Form": form,
    "Contact": contact,
    "Chatbot": chat_bot_forlocation,
}
