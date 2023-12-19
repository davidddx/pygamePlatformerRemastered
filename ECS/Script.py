from ECS.Entity import Component
from debug.logger import logger
import os, importlib
class Script(Component):
    def __init__(self, scriptname):
        logger.debug(f"Adding Script Component to Entity. {scriptname=}")
        self.Script = self.ImportScript(script_name= scriptname)
        self.ranReady = false

    def ImportScript(self, script_name : str):
        cwd = os.getcwd()
        script_dir = os.path.abspath(os.path.join(cwd, 'Scripts'))
        logger.info(f"Script: {script_name} | Location: {script_dir}")
        script_module = None
        if script_name.endswith(".py") and not script_name.startswith("__"):
            script_name = script_name[:-3]  # Remove the ".py" extension
            script_path = f'Scripts.{script_name}'
            try:
                script_module = importlib.import_module(script_path)
                logger.debug(f"Loaded Script: {script_path}")
            except Exception as e:
                logger.error(f"Failed to load script {script_path}: {e}")
            return script_module