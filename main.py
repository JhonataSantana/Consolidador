import os
import eel
import pandas as pd
import classes.utils as u
from pandas import DataFrame
from datetime import date
from classes.consolidador import Consolidador


def main() -> None:

    main_path: str = os.getcwd()
    
    files_path: str = u.joinPath(u.explodePath('./files'))

    init_date: date = date(2024, 3, 25)
    end_date: date = date.today()
    date_filter = (init_date, end_date, '%Y%m%d')

    consolidated: DataFrame = Consolidador(files_path, substring='test', date_interval=date_filter).run()
    
    final_filename: str = os.path.join(main_path, "consolidado.csv")
    consolidated.to_csv(final_filename, encoding="UTF-8", sep=',', index=False)

    return


@eel.expose
def my_python_function(a, b):
    print(a, b, a + b)
    print('Calling Javascript...')
    eel.my_javascript_function(1, 2, 3, 4)  # This calls the Javascript function
    return 41


def webInterface() -> None:
    eel.init('web')
    eel.start('index.html', size=(600,600))


if __name__ == "__main__":
    # main()
    webInterface()

