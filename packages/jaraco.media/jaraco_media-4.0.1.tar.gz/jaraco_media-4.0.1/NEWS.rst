v4.0.1
======

Bugfixes
--------

- Utilize helpers in jaraco.packaging.metadata to parse the project's metadata. (#2)


v4.0.0
======

``splice.splice_video`` now expects ``timestamps_include`` to be
a ``starargs`` parameter instead of an explicit tuple.

v3.7.0
======

Added ``splice`` module.

v3.6.0
======

Use accumulate function from jaraco.itertools.

v3.5.0
======

Added concat module, useful for concatenating media files using
ffmpeg, but providing a convenient interface.

Added srt-concat module, for concatenating the srt files associated
with the media files, honoring the offsets as found in those media
files.

Require Python 3.7 or later.

v3.4.0
======

Refreshed package metadata. Fixed a few bugs. Updated dependencies.

v3.3.1
======

Rely on PEP 420 for namespace package.

v3.3.0
======

Allow detection of renamed libmmbd from newer releases of MakeMKV.

v3.2.0
======

Rely on ``jaraco.path`` for hidden file detection.

v3.1.1
======

Fixed error in handbrake path handling.

v3.1.0
======

Packaging refresh and cleanup.

3.0
===

Moved ISAPI script to package. Invoke with
``python -m jaraco.media.isapiapp``.

Switch to `pkgutil namespace technique
<https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages>`_
for the ``jaraco`` namespace.

Drop support for Python 3.5 and earlier.

2.7
===

Moved hosting to Github.

2.5
===

Improved support on OS X.
