import importlib
from textwrap import indent

from flask import g, jsonify, request, render_template_string


def define_routes(app):
    @app.route('/vm/render', methods=['POST'])
    def render_template():
        """
        vm/render: Render a string as a Jinja2 template
        ---
        tags:
          - Rendering
        summary: Render a string as a Jinja2 template
        description: This endpoint allows you to render a string as a Jinja2 template.
        parameters:
          - in: formData
            name: template_string
            type: string
            required: true
            description: The string to render as a Jinja2 template.
        responses:
          200:
            description: The rendered template
            schema:
              type: string
        """
        template_string = request.form.get('template_string', '')
        rendered_template = render_template_string(template_string, _local=g.local, system=g.system)

        return rendered_template

    @app.route('/vm/var', methods=['POST'])
    def set_variable():
        """
        /vm/var: Set a user-defined variable
        ---
        tags:
          - Variables
        summary: Set a user-defined variable
        description: This endpoint allows you to set a user-defined variable.
        parameters:
          - in: formData
            name: key
            type: string
            required: true
            description: The key of the variable.
          - in: formData
            name: value
            type: string
            required: true
            description: The value of the variable.
        responses:
          200:
            description: The variable has been set successfully.
        """
        key = request.form.get('key')
        value = request.form.get('value')

        g.local[key] = value
        return jsonify({'message': 'The variable has been set successfully.'})

    @app.route('/vm/vars', methods=['POST'])
    def set_variables():
        """
        /vm/vars: Set multiple user-defined variables
        ---
        tags:
          - Variables
        summary: Set multiple user-defined variables
        description: This endpoint allows you to set multiple user-defined variables.
        parameters:
          - in: body
            name: variables
            description: The variables to set.
            schema:
              type: object
              additionalProperties:
                type: string
        responses:
          200:
            description: The variables have been set successfully.
        """
        variables = request.get_json()

        for key, value in variables.items():
            g.local[key] = value

        return jsonify({'message': 'The variables have been set successfully.'})

    @app.route('/vm/var', methods=['GET'])
    def get_variables():
        """
        /vm/var: Get all user-defined variables
        ---
        tags:
          - Variables
        summary: Get all user-defined variables
        description: This endpoint allows you to get all user-defined variables.
        responses:
          200:
            description: The variables have been retrieved successfully.
            schema:
              type: object
              properties:
                variables:
                  type: object
                  description: The user-defined variables.
        """
        return jsonify(g.local.to_dict())

    @app.route('/vm/vars', methods=['DELETE'])
    def clear_variables():
        """
        /vm/vars: Clear all user-defined variables
        ---
        tags:
          - Variables
        summary: Clear all user-defined variables
        description: This endpoint allows you to clear all user-defined variables.
        responses:
          200:
            description: All user-defined variables have been cleared.
        """
        g.local.to_dict().clear()
        return jsonify({'message': 'All user-defined variables have been cleared.'})

    @app.route('/vm/var/<key>', methods=['DELETE'])
    def clear_variable(key):
        """
        /vm/var/{key}: Clear a user-defined variable
        ---
        tags:
          - Variables
        summary: Clear a user-defined variable
        description: This endpoint allows you to clear a user-defined variable.
        parameters:
          - in: path
            name: key
            type: string
            required: true
            description: The key of the variable to clear.
        responses:
          200:
            description: The variable has been cleared successfully.
        """
        try:
            del g.local.to_dict()[key]
            return jsonify({'message': 'The variable has been cleared successfully.'})
        except KeyError:
            return jsonify({'message': 'The variable does not exist.'}), 404

    @app.route('/py/runner', methods=['POST'])
    def run_python_code():
        """
        /py/runner: Run Python code and return the result
        ---
        tags:
          - Python
        summary: Run Python code and return the result
        description: This endpoint allows you to run Python code and return the result.
        parameters:
          - in: body
            name: code
            type: string
            required: true
            description: The Python code to run.
        responses:
          200:
            description: The code has been executed successfully and the result is returned.
            schema:
              type: object
              properties:
                result:
                  type: string
                  description: The result of the executed code.
        """
        code = request.get_data(as_text=True)
        wrapped_code = f"def _wrapped():\n{indent(code, '  ')}\nresult = _wrapped()"
        local_vars = g.local.to_dict()
        exec(wrapped_code, local_vars)
        result = local_vars.get('result')
        del local_vars["_wrapped"]
        del local_vars["result"]
        unwanted_keys = [key for key in local_vars if key.startswith('__') and key.endswith('__')]
        for key in unwanted_keys:
            del local_vars[key]
        return jsonify({'result': str(result)})

    @app.route('/py/install', methods=['POST'])
    def install_python_package():
        """
        /py/install: Install a Python package
        ---
        tags:
          - Python
        summary: Install a Python package
        description: This endpoint allows you to install a Python package.
        parameters:
          - in: formData
            name: package_name
            type: string
            required: true
            description: The name of the package to install.
        responses:
          200:
            description: The package has been installed successfully.
        """
        package_name = request.form.get('package_name')
        import subprocess
        for package_name in package_name.split('\n'):
            subprocess.run(['pip', 'install', package_name])
        return jsonify({'message': 'The package has been installed successfully.'})

    @app.route('/py/uninstall', methods=['POST'])
    def uninstall_python_package():
        """
        /py/uninstall: Uninstall a Python package
        ---
        tags:
          - Python
        summary: Uninstall a Python package
        description: This endpoint allows you to uninstall a Python package.
        parameters:
          - in: formData
            name: package_name
            type: string
            required: true
            description: The name of the package to uninstall.
        responses:
          200:
            description: The package has been uninstalled successfully.
        """
        package_name = request.form.get('package_name')
        import subprocess
        for package_name in package_name.split('\n'):
            subprocess.run(['pip', 'uninstall', '-y', package_name])
        return jsonify({'message': 'The package has been uninstalled successfully.'})

    @app.route('/py/packages', methods=['GET'])
    def get_python_packages():
        """
        /py/packages: Get all installed Python packages
        ---
        tags:
          - Python
        summary: Get all installed Python packages
        description: This endpoint allows you to get all installed Python packages.
        responses:
          200:
            description: The installed packages have been retrieved successfully.
            schema:
              type: object
              properties:
                packages:
                  type: array
                  items:
                    type: string
                  description: The installed packages.
        """
        import subprocess
        result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
        packages = result.stdout.decode('utf-8').split('\n')
        return jsonify({'packages': packages})


class VariableManagerExtension:
    def __init__(self, app=None):
        self._local = Local()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.before_request(self.before_request)
        define_routes(app)

    def before_request(self):
        g.system = System()
        g.local = self._local


class System:
    def __init__(self):
        self._modules = {}

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __getitem__(self, name):
        if not isinstance(name, str):
            raise TypeError("Module name must be a string")

        if name in self._modules:
            return self._modules[name]

        try:
            module = importlib.import_module(name)
            self._modules[name] = module
            return module
        except ImportError:
            raise ImportError(f"Module '{name}' not found")


class Local:
    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found")
        return self._data[key]

    def to_dict(self):
        return self._data
