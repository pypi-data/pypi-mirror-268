import aa_ui.agenta_cli.agenta as agenta
import _app
from mangum import Mangum


handler = Mangum(agenta.app)
