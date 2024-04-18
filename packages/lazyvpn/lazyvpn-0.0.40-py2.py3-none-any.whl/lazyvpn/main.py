from subprocess import call, run

import keyring

from lazyvpn import errors, ui
from lazyvpn.config import Config, LAZY_VPN_KEYCHAIN_SERVICE_NAME


class LazyVpn(object):

    envvar_list = [
        'OKTA_PASSWORD',
        'OKTA_USERNAME',
    ]

    def _run(self):
        username = self.conf_arg_dict['okta_username']
        password = keyring.get_password(LAZY_VPN_KEYCHAIN_SERVICE_NAME, username)
        if not password:
            password = self.config.get_okta_password(username)
        company_vpn_region = self.conf_arg_dict['company_vpn_region']
        if self.conf_arg_dict['down']:
            call(['bash', '-c', '/opt/cisco/secureclient/bin/vpn -s disconnect'])
        if self.conf_arg_dict['up']:
            already_connected = run(['bash', '-c', '/opt/cisco/secureclient/bin/vpn stats | grep -Ewc "^[ \t]+Connection State.*Connected$"'], capture_output=True, text=True)
            # Running vpn connect if you're already connected disconnects you. This prevents that from happening.
            if already_connected.stdout == '1\n':
                self.ui.notify('You are already connected to the vpn')
            else:
                # If the GUI is open, then the cli will throw an error trying to connect.
                call(['bash', '-c', 'pkill Cisco\ Secure\ Client'])
                call(['bash', '-c', f'printf "{username}\n{password}\n2"  | /opt/cisco/secureclient/bin/vpn -s connect "{company_vpn_region}"'])
        # We can optionally start up the GUI in order to get the status icon in the menu bar
        if self.conf_arg_dict['gui']:
            call(['bash', '-c', 'open /Applications/Cisco/Cisco\ Secure\ Client.app --args -AppCommandLineArg'])

    def __init__(self, ui=ui.cli):
        self.ui = ui
        self.FILE_ROOT = self.ui.HOME
        self._cache = {}

    def run(self):
        try:
            self._run()
        except errors.LazyVpnExitBase as exc:
            exc.handle()

    def generate_config(self):
        """ generates a new configuration and populates
        various config caches
        """
        self._cache['config'] = config = Config(gac_ui=self.ui)
        conf_arg_dict = config.get_config_dict()
        conf_arg_dict.update(config.get_args().__dict__)
        self._cache['conf_arg_dict'] = conf_arg_dict

        for value in self.envvar_list:
            if self.ui.environ.get(value):
                key = value.lower()
                self.conf_arg_dict[key] = self.ui.environ.get(value)

        return config

    @property
    def config(self):
        if 'config' in self._cache:
            return self._cache['config']
        config = self.generate_config()
        return config

    @property
    def conf_arg_dict(self):
        """
        :rtype: dict
        """
        # noinspection PyUnusedLocal
        config = self.config
        return self._cache['conf_arg_dict']


if __name__ == "__main__":
    lazy_vpn = LazyVpn().run()
