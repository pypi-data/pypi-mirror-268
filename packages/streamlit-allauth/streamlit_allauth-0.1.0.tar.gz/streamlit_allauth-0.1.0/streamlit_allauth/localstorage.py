import streamlit.components.v1 as components

def set_item(key, value):
    """ Stocker une valeur dans LocalStorage """
    js_code = f"""
    window.localStorage.setItem('{key}', `{value}`);
    """
    components.html(js_code, height=0, width=0)

def get_item(key):
    """ Récupérer une valeur de LocalStorage """
    js_code = f"""
    let value = window.localStorage.getItem('{key}');
    Streamlit.setComponentValue(value);
    """
    return components.html(js_code, height=0, width=0)