from typing import Dict, Any, Union, Optional, List
from pydantic import BaseModel
import json
from tabulate import tabulate
from chat_cli_anything.request import build_client, predict
from chat_cli_anything.util import cache_path
import click
import os

class Provider(BaseModel):
    """
    """
    base_url: str
    api_key: Union[str, None] = ''
    model: Union[str, None] = ''
    proxy: Union[str, None] = ''


class _Config(BaseModel):
    """
    Config
    """
    providers: Dict[str, Provider]
    active: str = ''


class Config(dict):
    """
    Here will set multiple sources, 
    current: 
    other:

    it will save in a json file.
    """
    DEFAULT_PORT = 8789
    CONFIG_PATH = cache_path / '.config.json'

    def __init__(self):
        self.config: Dict[str, Any] = {}

        # Load existing config if available
        if self.CONFIG_PATH.exists():
            with open(self.CONFIG_PATH, 'r') as file:
                self.config = json.load(file)

    def remove(self, name: str, all: bool=False, type: str='llm'):
        """Clean providers in config given name."""
        if all:
            self.config['providers'] = {}
        else:
            key = 'providers' if type == 'llm' else 'embeddings'
            active_key = 'active' if type == 'llm' else 'active_embedding'
            if name in self.config[key]:
                del self.config[key][name]
                if self.config[active_key] == name:
                    self.config[active_key] = None
            else:
                click.secho(f"'{name}' not found in config.", fg='red')
                return
        self._dump_config()
        click.echo(f"'{name}' was removed successfully.")

    def add(self, name: str, base_url: str, 
            api_key: str='Empty', model: str='Empty',
            max_tokens: int=8192, proxy: Optional[str]=None, type: str='llm'):
        """Add provider in local config file. If name already in config files, the original
        configuration will be overrride.
        """
        if name[0] == '*':
            click.secho('Name cannot start with *', fg='red')
            return

        if type == 'llm':
            providers = self.config.get('providers', {})

            providers[name] = {
                'base_url': base_url,
                'api_key': api_key,
                'model': model,
                'max_tokens': max_tokens,
                'proxy': proxy
            }
            self.config['providers'] = providers

            if not self._has_active_provider():
                self.config['active'] = name
        else:
            embedding = self.config.get('embeddings', {})
            embedding[name] = {
                'base_url': base_url,
                'api_key': api_key,
                'model': model
            }
            self.config['embeddings'] = embedding
            if not self._has_active_embedding():
                self.config['active_embedding'] = name

        self._dump_config()

    def list(self, provider_name: str='', api_key: bool=False, config_type: str='llm'):
        """List all llm or embedding providers in a formatted table."""
        # Prepare the data for the table
        click.echo(f'Configuration in {str(self.CONFIG_PATH)}')
        click.echo('Name start with "*" indicating current active provider.')
        if config_type == 'llm':
            keys = ['providers']
        elif config_type == 'embedding':
            keys = ['embeddings']
        else:
            keys = ['providers', 'embeddings']

        for key in keys:
            data = []
            if key not in self.config:
                click.echo(f'No {key[:-1]} has been add.')
                return

            click.echo(f'{key[:-1]} list:')
            if key == 'providers':
                headers=["Name", "Base URL", "API Key", 'Model name', 'max_tokens', 'Proxy']
            else:
                headers = ["Name", "Base URL", "API Key", 'Model name']

            for name, details in self.config[key].items():
                if provider_name and name != provider_name:
                    continue
                api_key_str = details['api_key'] if api_key else "Hidden"
                if key == 'providers' and name == self.config['active']:
                    name = '*' + name
                if key == 'embeddings' and name == self.config['active_embedding']:
                    name = '*' + name

                if key == 'providers':
                    data.append([name, details['base_url'], api_key_str,
                                details['model'], details['max_tokens'],details['proxy']])
                else:
                    data.append([name, details['base_url'], api_key_str,
                                details['model']])

            # Use tabulate to format the data into a table
            table = tabulate(data,
                            headers=headers,
                            tablefmt="simple_outline")
            click.echo(table)

    def switch(self, name: str, type: str='llm'):
        """Switch to provider in local config file and save changes."""
        key = 'providers' if type == 'llm' else 'embeddings'
        active_key = 'active' if type == 'llm' else 'active_embedding'
        if name in self.config[key]:
            self.config[active_key] = name
            # Save the updated configuration back to the file
            self._dump_config()
            click.echo(f"Switched to configuration '{name}'.")
        else:
            click.echo(f"No configuration found with name '{name}'.")

    def dump(self, output_path: str, override: bool=False):
        """Export current config to file."""
        if os.path.exists(output_path) and not override:
            click.echo(f'The file {output_path} already exists. Use `-o` or `--override` to force write.')
            return
        with open(output_path, 'w') as output_file:
            json.dump(self.config, output_file, ensure_ascii=False, indent=4)
            click.echo(f'Configuration dumped {output_path}')

    def load(self, input_path: str, override: bool=False):
        """Load config."""
        if not os.path.exists(input_path):
            click.echo('The file {output_path} is not exists.')
        try:
            config = open(input_path, 'r').read()
            config = _Config.model_validate_json(config)
        except Exception as ex:
            raise ex
            click.echo('The file {output_path} is not a valid configuration JSON file.')
            return

        if override:
            self.config = config
            click.echo('Configuration loaded and override original configuration.')
        else:
            # merge configuration
            for k, v in self.config.get('providers', {}).items():
                self.config[k] = v
            click.echo('Configuration loaded and merged to original configuration.')
        with open(self.CONFIG_PATH, 'w') as file:
            json.dump(self.config, file, indent=4)

    def _has_active_provider(self):
        """Check whether there is a """
        if ('active' not in self.config or
             not self.config['active'] or
             self.config['active'] not in self.config['providers']):
            return False
        return True

    def _has_active_embedding(self):
        """Check whether there is a """
        if ('active_embedding' not in self.config or
             not self.config['active_embedding'] or
             self.config['active_embedding'] not in self.config['embeddings']):
            return False
        return True

    def ping(self, name: str, config_type: str='llm'):
        """Check whether provider is accessible"""
        key = 'providers' if config_type == 'llm' else 'embeddings'
        
        if name not in self.config[key]:
            click.echo(f"{key[:-1]} '{name}' has not been added.")
            return
        if key == 'providers':
            provider = self.config['providers'][name]
            client = build_client(
                provider['base_url'],
                provider['api_key'],
                provider['proxy'],
            )
            try:
                _ = predict(client, provider['model'], 'hi')
                click.secho(f"Provider '{name}' is accessible.", fg='green')
            except Exception as ex:
                click.secho(f"Provider '{name}' is not accessible.", fg='red')
        else:
            import requests
            good = False
            try:
                _ = requests.get(self.config['embeddings'][name]['base_url'] + '/ping', timeout=5)
                # check status code 
                if _.status_code == 200:
                    good = True
            except Exception as ex:
                pass

            if good:
                click.secho(f"Embedding & rerank provider '{name}' is accessible.", fg='green')
            else:
                click.secho(f"Embedding & rerank provider '{name}' is not accessible.", fg='red')

    def set_local_service_setting(self, port: int):
        """Set local service port"""
        self.config['local_service_port'] = port

    def save(self):
        self._dump_config() 

    def _dump_config(self):
        with open(self.CONFIG_PATH, 'w') as file:
            json.dump(self.config, file, indent=4)
    
    def __setitem__(self, __name: str, __value: Any) -> None:
        self.config[__name] = __value

    def __contains__(self, __key: object) -> bool:
        return self.config.__contains__(__key)

    def get(self, __name: str, __default: Optional[Any]=None) -> Any:
        return self.config.get(__name, __default)