import os

def walk(top, maxdepth=0, topdown=True, onerror=None, followlinks=False):
    return _walk(os.fspath(top), maxdepth, topdown, onerror, followlinks)

def _walk(top, maxdepth, topdown, onerror, followlinks):
    dirs = []
    nondirs = []
    walk_dirs = []
    try:
        scandir_it = os.scandir(top)
    except OSError as error:
        if onerror is not None:
            onerror(error)
        return

    with scandir_it:
        while True:
            try:
                try:
                    entry = next(scandir_it)
                except StopIteration:
                    break
            except OSError as error:
                if onerror is not None:
                    onerror(error)
                return

            try:
                is_dir = entry.is_dir()
            except OSError:
                is_dir = False

            if is_dir:
                dirs.append(entry.name)
            else:
                nondirs.append(entry.name)

            if not topdown and is_dir:
                if followlinks:
                    walk_into = True
                else:
                    try:
                        is_symlink = entry.is_symlink()
                    except OSError:
                        is_symlink = False
                    walk_into = not is_symlink

                if walk_into:
                    walk_dirs.append(entry.path)

    maxdepth -= 1
    if maxdepth == 0:
        walk_dirs = []

    if topdown:
        yield top, dirs, nondirs
        if maxdepth == 0:
            return
        islink, join = os.path.islink, os.path.join
        for dirname in dirs:
            new_path = join(top, dirname)
            if followlinks or not islink(new_path):
                yield from _walk(new_path, maxdepth, topdown, onerror, followlinks)
    else:
        for new_path in walk_dirs:
            yield from _walk(new_path, maxdepth, topdown, onerror, followlinks)
        yield top, dirs, nondirs
