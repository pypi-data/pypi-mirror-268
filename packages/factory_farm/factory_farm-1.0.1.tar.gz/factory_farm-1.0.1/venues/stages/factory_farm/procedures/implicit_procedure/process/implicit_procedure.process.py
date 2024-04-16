

print ('implicit procedure :: process')

import rich
import sys
rich.print_json (data = {
	"implicit procedure sys paths": sys.path
})


from clique import start_clique
from factory_farm.procedures.implicit_procedure.process.moves.print_is_done_status_repetively import print_is_done_status_repetively

print_is_done_status_repetively ()

start_clique ()