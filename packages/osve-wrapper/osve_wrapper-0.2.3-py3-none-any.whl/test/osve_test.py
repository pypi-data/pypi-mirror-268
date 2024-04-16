
import os
from osve import osve as osve

sim = osve.osve()
version = sim.get_app_version()
print(version)
scenario_path = os.path.abspath('../TDS/crema_5_0/eps_package')
json_file = os.path.join('../TDS/crema_5_0/eps_package', 'config_osve_template.json')
print(os.path.exists(scenario_path))
print(scenario_path)
sim.execute(scenario_path, json_file)
