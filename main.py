from utils import estados, get_filename
from download import download_files
from etl import process_cons, process_det

# for estado in estados:
#     download_files(estado)

for estado in estados:
  for i in range(1, 13):
    # filename = get_filename(estado, i, 'CONS', extension='csv')
    # process_cons(filename)

    filename = get_filename(estado, i, 'DET', extension='csv')
    process_det(filename)
