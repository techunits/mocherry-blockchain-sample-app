#!/usr/bin/env python
import os

def main():
    BASEPATH = os.getcwd()
    default_app_name = 'app'
    os.environ.setdefault('MOCHERRY_SETTINGS_PATH', os.path.join(BASEPATH, default_app_name, 'config', 'settings.json'))    
    try:
        import mocherry
    except ImportError as e:
        raise ImportError(
            "Couldn't import MoCherry. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from e
    
    # initialize the application
    mocherry.bootstrap_application()


if __name__ == '__main__':
    main()
