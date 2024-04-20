import subprocess
import sys
from tqdm import tqdm

def upgrade_medicafe(package):
    try:
        # Use tqdm to create a progress bar
        with tqdm(total=100, desc="Upgrading %s" % package, unit="%") as progress_bar:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', package, '--no-deps', '--disable-pip-version-check'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # Update progress bar to 100% upon completion
            progress_bar.update(100 - progress_bar.n)
        print("Update successful.")
    except subprocess.CalledProcessError:
        print("Update failed. Please check your internet connection and try again later.")
        sys.exit(1)

if __name__ == "__main__":
    medicafe_package = "medicafe"
    upgrade_medicafe(medicafe_package)
