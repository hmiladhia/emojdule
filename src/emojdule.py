import sys

from importlib.machinery import (
    SOURCE_SUFFIXES,
    FileFinder,
    EXTENSION_SUFFIXES,
    ExtensionFileLoader,
    SourceFileLoader,
    BYTECODE_SUFFIXES,
    SourcelessFileLoader,
)

__author__ = "Dhia Hmila"
__version__ = "0.0.1"


def install() -> None:
    supported_loaders = [
        (ExtensionFileLoader, [*EXTENSION_SUFFIXES]),
        (SourceFileLoader, [*SOURCE_SUFFIXES]),
        (SourcelessFileLoader, BYTECODE_SUFFIXES),
    ]

    file_finders = [
        i
        for i, x in enumerate(sys.path_hooks)
        if x.__name__ == "path_hook_for_FileFinder"
    ]
    if len(file_finders) != 1:
        sys.path_hooks.insert(
            1, FileFinder.path_hook(*supported_loaders, (SourceFileLoader, [".🐍"]))
        )
        return sys.path_importer_cache.clear()

    loaders = getattr(sys.path_hooks[file_finders[0]], "_loaders", supported_loaders)
    sys.path_hooks[file_finders[0]] = FileFinder.path_hook(
        *loaders, (SourceFileLoader, [".🐍"])
    )

    return sys.path_importer_cache.clear()
