import functools
import pathlib
from typing import IO, Iterable, Union
from .generic import _ArchivePath, Archive
import tarfile
import io


class _TarIO(io.BytesIO):
    """An auxiliary class to handle TAR archive writing."""

    def __init__(self, archive: "TarArchive", member_fn) -> None:
        super().__init__()
        self.archive = archive
        self.member_fn = member_fn

    def close(self) -> None:
        self.seek(0)
        self.archive.write_member(self.member_fn, self)
        super().close()


class TarArchive(Archive):
    """A subclass of Archive for working with TAR archives."""

    _extensions = [
        ".tar",
        ".tar.bz2",
        ".tb2",
        ".tbz",
        ".tbz2",
        ".tz2",
        ".tar.gz",
        ".taz",
        ".tgz",
        ".tar.lzma",
        ".tlz",
    ]

    _pure_path_impl = pathlib.PurePosixPath

    @staticmethod
    def is_readable(archive_fn: Union[str, pathlib.Path]):
        if isinstance(archive_fn, str):
            archive_fn = pathlib.Path(archive_fn)
        return archive_fn.is_file() and tarfile.is_tarfile(archive_fn)

    @functools.cached_property
    def _tarfile(self):
        return tarfile.open(self.archive_fn, self.mode)

    def close(self):
        if "_tarfile" in self.__dict__:
            self._tarfile.close()
            if self.mode in ("ra"):
                # # Remove cached TarFile instance so that it can be transparently reopened
                self.__dict__.pop("_tarfile", None)
                self.__dict__.pop("_members", None)

    def open_member(
        self,
        member_fn: Union[str, pathlib.PurePath],
        mode="r",
        *args,
        compress_hint=True,
        **kwargs,
    ) -> IO:
        # Force str type
        member_fn = str(member_fn)

        # tar does not compress files individually
        del compress_hint

        if mode[0] == "r":
            try:
                tar_info = self._members[member_fn]
                stream = self._tarfile.extractfile(tar_info)
            except KeyError as exc:
                raise FileNotFoundError(member_fn) from exc

            if stream is None:
                raise IOError("There's no data associated with this member")

        elif mode[0] == "w":
            if "r" in self.mode:
                raise ValueError("Can not write to a read-only archive")

            stream = _TarIO(self, member_fn)
        else:
            raise ValueError(f"Unrecognized mode: {mode}")

        if "b" in mode:
            if args or kwargs:
                stream.close()
                raise ValueError("encoding args invalid for binary operation")
            return stream

        # Text mode
        kwargs["encoding"] = io.text_encoding(kwargs.get("encoding"))
        return io.TextIOWrapper(stream, *args, **kwargs)

    @functools.cached_property
    def _members(self):
        # Build a mapping from name to tar_info.
        # Otherwise, the list of members has to be iterated
        # each time a name is searched.
        return {tar_info.name: tar_info for tar_info in self._tarfile.getmembers()}

    def write_member(
        self,
        member_fn: str,
        fileobj_or_bytes: Union[IO, bytes],
        *,
        compress_hint=True,
        mode: str = "w",
    ):
        # tar does not compress files individually
        del compress_hint

        if isinstance(fileobj_or_bytes, bytes):
            fileobj_or_bytes = io.BytesIO(fileobj_or_bytes)

        if isinstance(fileobj_or_bytes, io.BytesIO):
            tar_info = tarfile.TarInfo(member_fn)
            tar_info.size = len(fileobj_or_bytes.getbuffer())
        else:
            tar_info = self._tarfile.gettarinfo(
                arcname=member_fn, fileobj=fileobj_or_bytes
            )

        self._tarfile.addfile(tar_info, fileobj=fileobj_or_bytes)
        self._members[tar_info.name] = tar_info

    def members(self) -> Iterable[_ArchivePath]:
        return (
            _ArchivePath(self, self._pure_path_impl(name))
            for name in self._members.keys()
        )

    def member_is_file(self, member_fn: str | pathlib.PurePath) -> bool:
        # Force str type
        member_fn = str(member_fn)

        return self._members[member_fn].isfile()

    def member_exists(self, member_fn: str | pathlib.PurePath) -> bool:
        # Force str type
        member_fn = str(member_fn)

        return member_fn in self._members
