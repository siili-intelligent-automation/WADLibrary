# Starts up WinAppDriver before the test
import subprocess
import os
import psutil


class Driver:
    def __init__(self, driver_path):
        self.f = open(os.devnull, 'w')
        self.process = None
        self.driver_path = driver_path

    def set_up_driver(self, path=None):
        """Starts the Windows Application Driver as a detached process.

        Arguments detailed:
        | =Argument= | =Input=                                |
        | path       | Location of Windows Application Driver |

        | =Return=   | =Output=                               |  
        | None       | None                                   |
        """
        if path is None:
            path = self.driver_path
        self.process = subprocess.Popen([path], shell=True, stdin=None, stdout=self.f, stderr=None, close_fds=False,
                                        creationflags=8)  # subprocess.DETACHED_PROCESS

    def tear_down_driver(self):
        """Stops the Windows Application Driver."""
        process = psutil.Process(self.process.pid)
        for pro in process.children(recursive=True):
            pro.kill()
        process.kill()
