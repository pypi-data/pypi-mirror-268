import subprocess 
from mlflow_for_ml_dev.utils.utils import get_root_project

def run_notebook():
    """
    Run the notebook in the notebooks folder
    """
    # get the path to notebook folder within the package
    path = get_root_project()
    path = path / "mlflow_for_ml_dev/notebooks"

    subprocess.run(["jupyter", "notebook", path.as_posix()])