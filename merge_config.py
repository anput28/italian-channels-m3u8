import json
from jsonmerge import merge

# Carica il file config.json originale
with open('../original_config_backup.json', 'r') as original_file:
    original_config = json.load(original_file)

# Carica il file config.json del fork
with open('../fork_config_backup.json', 'r') as fork_file:
    fork_config = json.load(fork_file)

# Unisci i due file, mantenendo le personalizzazioni del fork
updated_config = merge(original_config, fork_config)

# Sovrascrivi il file config.json del fork con il nuovo contenuto
with open('../fork_config_backup.json', 'w') as fork_file:
    json.dump(updated_config, fork_file, indent=4)
