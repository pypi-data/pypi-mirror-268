# RHDZMOTA EXT: streamlit_webapps

Package extensions have 2 main purposes:
* Split the dependency sets into several smaller python projects
* Serve as domain-specific packages (i.e., split functionality).

## About the `streamlit_webapps` extension

The streamlit extension contains some common useful abstractions to be used when working on creating streamlit applications.

The starting abstraction is the `PageView` class, which provides an "easy to reason about" pattern to follow when working on creating webapps. To get a sneak-peak of the functionality, consider creating a `webapp.py` script with the following content:

```python
from rhdzmota.ext.streamlit_webapps.page_view import PageView


if __name__ == "__main__":
    with PageView() as page:
        page.view()
```
* Run with: `streamlit run webapp.py

With a single import you can have a fully functional streamlit page with content (in this case, a "non implemented" message.

The `PageView` abstractions allow you to specify the page configuration via class initialization such as:
* `PageView(page_title="Demo", page_layout="wide", favicon_path="path/to/favicon.png")`

You can provide a custom streamlit implementation to a page-view via:
* `Inline` (discouraged) via the `PageView.infline` class constructor.
* `Inheritance` (recommended) by providing an implementation for the `view` instance method.

Code Example: Using inheritance to provide a custom streamlit implementation.

```python
import random
import datetime as dt

import streamlit as st

from rhdzmota.ext.streamlit_webapps.page_view import PageView

class WelcomeView(PageView):
    def view(self, **kwargs):
        st.markdown("# My Custom Webapp")
        with st.form(f"form-{self.refname}"):
            num_input = int(st.number_input("Num. of Options (input)", min_value=2, step=1))
            num_output = int(st.number_input("Num. of Winners", min_value=1, step=1))
            exclusive_select = st.checkbox("Exclusive Select")
            submitted = st.form_submit_button("Submit")

        if not submitted:
            return

        values = [f"Option-{i}" for i in range(num_input)]
        timestamp = dt.datetime.now().isoformat()
        sep = "\n* "
        result_prefix = f"Result (TS: {dt.datetime.now().isoformat()}) "
        if not exclusive_select:
            output = result_prefix + sep + sep.join(random.choices(values, k=num_output))
            return st.markdown(output)
        random.shuffle(values)
        output = result_prefix + sep + sep.join(values[:num_output] if num_output < num_input else values)
        return st.markdown(output)


if __name__ == "__main__":
    with WelcomeView(page_title="Demo", page_layout="wide") as page:
        page.view()

```

## CLI CMD: `run_from_file`

You can use the `cli interface` to execute streamlit applications:

```commandline
$ rhdzmota.ext execute streamlit_webapps --command run_from_file \
    --path {{path/to/file.py}}
```
* Use this command when you have a streamlit entrypoint python file.

```commandline
$ rhdzmota.ext execute streamlit_Webapps --command run_from_refname \
    --function_name {{function-name}} \
    --module_name {{module_name}}
```
* Use this command when you want to execute a function accessible in your current python runtime.

Example:

```commandline
$ rhdzmota.ext execute streamlit_webapps --command run_from_file \
    --path extensions/streamlit_webapps/src/examples/ex1_plain_page_view.py
```

## Linked Installation

Most extensions can be installed indirectly via the main package by providing an extra-dependency tag. Example:

```commandline
$ pip install 'rhdzmota[ext.streamlit_webapps]'
```
* General pattern: `'rhdzmota[ext.<extension-slug>]'`

## Standalone Installations

Package extensions can also be installed independently. For example:

```commandline
$ pip install rhdzmota_extension_streamlit_webapps
```
* General pattern: `rhdzmota_extension_<extension-slug>`

You can also install them locally:

```commandline
$ EXT_BUILD_LOCAL=1 pip install -e extensions/streamlit_webapps
```
* General pattern: `EXT_BUILD_LOCAL=1 pip install -e path/to/extension`

